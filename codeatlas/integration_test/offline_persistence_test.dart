// integration_test/offline_persistence_test.dart — Integration test for
// SQLite persistence, idempotent seed, upgrade without data loss, and error rollback.

import 'dart:convert';

import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:path/path.dart' as p;
import 'package:sqflite/sqflite.dart';

import 'package:codeatlas/data/app_database.dart';
import 'package:codeatlas/data/content_repository.dart';
import 'package:codeatlas/data/learning_repository.dart';
import 'package:codeatlas/data/models.dart';
import 'package:codeatlas/data/seed_loader.dart';

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  late Database db;
  late ContentRepository contentRepo;
  late LearningRepository learningRepo;
  late SeedLoader seedLoader;
  late String testDbPath;

  setUp(() async {
    await AppDatabase.close();
    final dbPath = await getDatabasesPath();
    testDbPath = p.join(dbPath, 'test_offline_persistence.db');
    await deleteDatabase(testDbPath);

    db = await AppDatabase.openWithPath(testDbPath);

    contentRepo = ContentRepository(db);
    learningRepo = LearningRepository(db);
    seedLoader = SeedLoader(db);
  });

  tearDown(() async {
    await AppDatabase.close();
    await deleteDatabase(testDbPath);
  });

  testWidgets(
    'Offline persistence: seed, save progress, upgrade, and verify data retention',
    (tester) async {
      // 1. Load bundled asset (which is version 5)
      final jsonStr = await rootBundle.loadString(
        'assets/content/content.json',
      );
      final data = jsonDecode(jsonStr) as Map<String, dynamic>;

      // Initial seed with version 4 content package
      final v4Data = Map<String, dynamic>.from(data);
      v4Data['content_version'] = 4;

      final result1 = await seedLoader.seedFromMap(v4Data);
      expect(result1.success, isTrue);
      expect(result1.topicsCount, equals(99));

      // 1b. Repeated seed with identical version 4 is idempotent (0 writes)
      final resultRepeat = await seedLoader.seedFromMap(v4Data);
      expect(resultRepeat.success, isTrue);
      expect(
        resultRepeat.topicsCount,
        equals(0),
        reason: 'Identical version should not rewrite topics',
      );

      // 2. User sets status and writes notes in version 4
      await learningRepo.updateStatus(
        'f-programming-logic',
        LearningStatus.understood,
      );
      await learningRepo.updateNotes(
        'f-programming-logic',
        'Catatan penting urutan instruksi.',
      );

      // Create a custom learning path
      final pathId = await learningRepo.createPath(
        name: 'Jalur Kustom Saya',
        goal: 'custom',
        topicIds: ['f-programming-logic', 'f-variables-data-types'],
      );
      expect(pathId, greaterThan(0));

      // Verify progress saved
      final progBefore = await learningRepo.getProgress('f-programming-logic');
      expect(progBefore?.status, equals(LearningStatus.understood));
      expect(progBefore?.notes, equals('Catatan penting urutan instruksi.'));

      // 3. Real content upgrade from version 4 to version 5
      final result2 = await seedLoader.seedFromMap(data);
      expect(result2.success, isTrue);
      expect(result2.topicsCount, equals(99));

      // 4. Verify user data is 100% retained after v4 -> v5 upgrade
      final progAfter = await learningRepo.getProgress('f-programming-logic');
      expect(
        progAfter?.status,
        equals(LearningStatus.understood),
        reason: 'User progress status must not be lost after content upgrade',
      );
      expect(
        progAfter?.notes,
        equals('Catatan penting urutan instruksi.'),
        reason: 'User notes must not be overwritten after content upgrade',
      );

      final userPaths = await learningRepo.getAllPaths();
      expect(
        userPaths.any((p) => p.name == 'Jalur Kustom Saya'),
        isTrue,
        reason:
            'User custom learning path must be preserved after content upgrade',
      );

      // 4b. Tutup dan buka kembali koneksi database untuk memeriksa persistensi (restart simulasi)
      await AppDatabase.close();
      db = await AppDatabase.openWithPath(testDbPath);
      contentRepo = ContentRepository(db);
      learningRepo = LearningRepository(db);
      seedLoader = SeedLoader(db);

      final reloadedProg = await learningRepo.getProgress(
        'f-programming-logic',
      );
      expect(reloadedProg?.status, equals(LearningStatus.understood));
      expect(reloadedProg?.notes, equals('Catatan penting urutan instruksi.'));
      final reloadedPaths = await learningRepo.getAllPaths();
      expect(reloadedPaths.any((p) => p.name == 'Jalur Kustom Saya'), isTrue);

      // 5. Downgrade attempt (version 4 < version 5) must be rejected
      final downgradeData = Map<String, dynamic>.from(data);
      downgradeData['content_version'] = 4;
      final resultDowngrade = await seedLoader.seedFromMap(downgradeData);
      expect(
        resultDowngrade.success,
        isFalse,
        reason: 'Downgrade to lower content_version must be rejected',
      );
      expect(resultDowngrade.error, contains('Downgrade versi konten ditolak'));

      // 6. Corrupted package is safely rejected and rolled back
      final corruptedData = Map<String, dynamic>.from(data);
      corruptedData['content_version'] = 6;
      // Introduce broken prerequisite reference
      final corruptedTopics = List<dynamic>.from(
        corruptedData['topics'] as List,
      );
      final firstTopic = Map<String, dynamic>.from(
        corruptedTopics[0] as Map<String, dynamic>,
      );
      firstTopic['prerequisite_ids'] = ['non_existent_topic_id'];
      corruptedTopics[0] = firstTopic;
      corruptedData['topics'] = corruptedTopics;

      final resultCorrupted = await seedLoader.seedFromMap(corruptedData);
      expect(
        resultCorrupted.success,
        isFalse,
        reason: 'Corrupted package with broken reference must be rejected',
      );

      // 6b. Uji rollback dengan kegagalan setelah sebagian penulisan berlangsung di dalam transaksi
      bool midTxnExceptionCaught = false;
      try {
        await db.transaction((txn) async {
          // Penulisan pertama berhasil dijalankan
          await txn.insert('categories', {
            'id': 'temp-cat-rollback',
            'layer': 'fundamentals',
            'kind': 'group',
            'title': 'Kategori Sementara',
            'description': 'Akan di rollback',
            'sort_order': 999,
          });
          // Kegagalan terjadi di tengah-tengah transaksi setelah baris pertama tertulis
          throw Exception(
            'Simulasi kegagalan I/O saat transaksi separuh berjalan',
          );
        });
      } catch (e) {
        midTxnExceptionCaught = true;
      }
      expect(midTxnExceptionCaught, isTrue);

      // Verifikasi bahwa penulisan sebagian dibatalkan sepenuhnya (tidak ada data bocor)
      final rolledBackCat = await db.query(
        'categories',
        where: 'id = ?',
        whereArgs: ['temp-cat-rollback'],
      );
      expect(
        rolledBackCat.isEmpty,
        isTrue,
        reason: 'Kategori sementara wajib di-rollback penuh saat terjadi kegagalan di tengah penulisan',
      );

      // Meta content_version remains at 5
      final meta = await contentRepo.getContentMeta();
      expect(
        meta!.contentVersion,
        equals(5),
        reason: 'Failed upgrade must rollback and preserve valid version 5',
      );

      // 7. Verify all user data remains intact after rejection and rollback
      final progFinal = await learningRepo.getProgress('f-programming-logic');
      expect(progFinal?.status, equals(LearningStatus.understood));
      expect(progFinal?.notes, equals('Catatan penting urutan instruksi.'));

      // 8. Artikel yang diarsipkan (is_active = 0) tetap memiliki akses ke catatan lama
      await db.update(
        'topics',
        {'is_active': 0},
        where: 'id = ?',
        whereArgs: ['f-programming-logic'],
      );

      // Pastikan topik tidak lagi masuk ke daftar topik aktif
      final activeTopics = await contentRepo.getAllActiveTopics();
      expect(activeTopics.any((t) => t.id == 'f-programming-logic'), isFalse);

      // Namun progress dan catatan pribadi pengguna tetap dapat diakses
      final archivedProg = await learningRepo.getProgress(
        'f-programming-logic',
      );
      expect(archivedProg?.status, equals(LearningStatus.understood));
      expect(archivedProg?.notes, equals('Catatan penting urutan instruksi.'));
    },
  );
}
