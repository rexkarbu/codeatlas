import 'dart:convert';
import 'dart:io';
import 'dart:ui' as ui;
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:codeatlas/data/content_repository.dart';
import 'package:codeatlas/data/learning_repository.dart';
import 'package:codeatlas/data/models.dart';
import 'package:codeatlas/features/roadmap/roadmap_screen.dart';

class ProductionMockContentRepo implements ContentRepository {
  final List<Category> categories;
  final List<Topic> topics;
  final Map<String, List<String>> prereqs;

  ProductionMockContentRepo({
    required this.categories,
    required this.topics,
    required this.prereqs,
  });

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<List<Category>> getAllCategories() async => categories;

  @override
  Future<List<Topic>> getAllActiveTopics() async =>
      topics.where((t) => t.isActive).toList();

  @override
  Future<Map<String, List<String>>> getPrerequisiteGraph() async => prereqs;

  @override
  Future<Topic?> getTopicById(String id) async {
    return topics.where((t) => t.id == id).firstOrNull;
  }

  @override
  Future<List<String>> getDependentTopicIds(String id) async {
    final dependents = <String>[];
    for (final entry in prereqs.entries) {
      if (entry.value.contains(id)) {
        dependents.add(entry.key);
      }
    }
    return dependents;
  }
}

class ProductionMockLearningRepo implements LearningRepository {
  final Map<String, Progress> progressMap;

  ProductionMockLearningRepo(this.progressMap);

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<Map<String, Progress>> getAllProgress() async => progressMap;

  @override
  Future<Progress?> getProgress(String id) async => progressMap[id];

  @override
  Future<void> updateNotes(String id, String text) async {
    final existing = progressMap[id];
    progressMap[id] = Progress(
      topicId: id,
      status: existing?.status ?? LearningStatus.notStarted,
      notes: text,
      lastReviewedAt: existing?.lastReviewedAt,
      updatedAt: DateTime.now(),
    );
  }

  @override
  Future<void> updateStatus(String id, LearningStatus status) async {
    final existing = progressMap[id];
    progressMap[id] = Progress(
      topicId: id,
      status: status,
      notes: existing?.notes ?? '',
      lastReviewedAt: existing?.lastReviewedAt,
      updatedAt: DateTime.now(),
    );
  }
}

Future<void> saveRepaintBoundary(
  WidgetTester tester,
  GlobalKey key,
  String filename,
) async {
  await tester.runAsync(() async {
    final boundary =
        key.currentContext?.findRenderObject() as RenderRepaintBoundary?;
    if (boundary != null) {
      final image = await boundary.toImage(pixelRatio: 2.0);
      final byteData = await image.toByteData(format: ui.ImageByteFormat.png);
      if (byteData != null) {
        final file = File('d:/project/ca/hasil/$filename');
        file.writeAsBytesSync(byteData.buffer.asUint8List());
        print('BERHASIL DISIMPAN: ${file.path} (${file.lengthSync()} bytes)');
      }
    }
  });
}

void main() {
  late ProductionMockContentRepo contentRepo;
  late ProductionMockLearningRepo learningRepo;

  setUpAll(() async {
    // 1. Load Segoe UI (Regular and Bold) as Roboto and sans-serif
    final segoeBytes =
        await File(r'C:\Windows\Fonts\segoeui.ttf').readAsBytes();
    final robotoLoader = FontLoader('Roboto');
    robotoLoader.addFont(Future.value(ByteData.view(segoeBytes.buffer)));
    await robotoLoader.load();

    final segoeBoldBytes =
        await File(r'C:\Windows\Fonts\segoeuib.ttf').readAsBytes();
    final robotoBoldLoader = FontLoader('Roboto');
    robotoBoldLoader.addFont(
      Future.value(ByteData.view(segoeBoldBytes.buffer)),
    );
    await robotoBoldLoader.load();

    // 2. Load MaterialIcons
    final iconFile = File(
      r'D:\development\flutter\flutter\bin\cache\artifacts\material_fonts\materialicons-regular.otf',
    );
    if (iconFile.existsSync()) {
      final iconBytes = await iconFile.readAsBytes();
      final iconLoader = FontLoader('MaterialIcons');
      iconLoader.addFont(Future.value(ByteData.view(iconBytes.buffer)));
      await iconLoader.load();
    }

    // 3. Load actual production dataset from assets/content/content.json
    final jsonFile = File('assets/content/content.json');
    final jsonStr = await jsonFile.readAsString();
    final pkg = jsonDecode(jsonStr) as Map<String, dynamic>;

    final categories = (pkg['categories'] as List<dynamic>)
        .map((c) => Category.fromJson(c as Map<String, dynamic>))
        .toList();

    final topics = (pkg['topics'] as List<dynamic>)
        .map((t) => Topic.fromJson(t as Map<String, dynamic>))
        .toList();

    final prereqs = <String, List<String>>{};
    for (final t in topics) {
      prereqs[t.id] = t.prerequisiteIds;
    }

    contentRepo = ProductionMockContentRepo(
      categories: categories,
      topics: topics,
      prereqs: prereqs,
    );

    learningRepo = ProductionMockLearningRepo({
      'f-programming-logic': Progress(
        topicId: 'f-programming-logic',
        status: LearningStatus.understood,
        notes: 'Catatan penting.',
        updatedAt: DateTime.now(),
      ),
      'f-variables-data-types': Progress(
        topicId: 'f-variables-data-types',
        status: LearningStatus.inProgress,
        notes: 'Sedang membaca perbandingan stack vs heap.',
        updatedAt: DateTime.now(),
      ),
    });
  });

  Widget buildTestableRoadmap({
    required GlobalKey key,
    required double logicalWidth,
    required double textScale,
  }) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        fontFamily: 'Roboto',
        useMaterial3: true,
        colorSchemeSeed: Colors.indigo,
      ),
      home: MediaQuery(
        data: MediaQueryData(
          size: Size(logicalWidth, 800),
          devicePixelRatio: 2.0,
          textScaler: TextScaler.linear(textScale),
        ),
        child: SizedBox(
          width: logicalWidth,
          height: 800,
          child: RepaintBoundary(
            key: key,
            child: RoadmapScreen(
              contentRepo: contentRepo,
              learningRepo: learningRepo,
              onOpenTopic: (_) {},
            ),
          ),
        ),
      ),
    );
  }

  // ─────────────────────────────────────────────────────────
  // TEST SUITE: Menangkap Screenshot & Memverifikasi Bebas Overflow
  // ─────────────────────────────────────────────────────────
  testWidgets(
    'Ambil Screenshot Peta Terbaca & Verifikasi Bebas Overflow (360px & 400px, 100% & 200%)',
    (tester) async {
      // ═══════════════════════════════════════════════════════
      // 1. VIEWPORT 400px (Skala Normal 1.0) - Tiga Tangkapan Layar Utama
      // ═══════════════════════════════════════════════════════
      tester.view.physicalSize = const Size(800, 1600);
      tester.view.devicePixelRatio = 2.0; // 400 x 800 logical px

      final key400 = GlobalKey();
      await tester.pumpWidget(
        buildTestableRoadmap(key: key400, logicalWidth: 400, textScale: 1.0),
      );
      await tester.pumpAndSettle();

      // SCREEN 1: Peta awal dengan kelompok materi
      await saveRepaintBoundary(tester, key400, '01_peta_awal_kelompok.png');

      // SCREEN 2: Buka kelompok 'Logika & Sintaks Dasar'
      await tester.tap(find.text('Logika & Sintaks Dasar'));
      await tester.pumpAndSettle();
      await saveRepaintBoundary(tester, key400, '02_peta_kelompok_topik.png');

      // SCREEN 3: Pilih topik 'Variables & Data Types' untuk membuka panel fokus
      await tester.tap(find.text('Variables & Data Types').first);
      await tester.pumpAndSettle();
      print('RoadmapScreen rect: ${tester.getRect(find.byType(RoadmapScreen))}');
      print('View size: ${tester.view.physicalSize} / ${tester.view.devicePixelRatio}');
      print('Focus panel rect: ${tester.getRect(find.text("Buka Artikel"))}');
      await saveRepaintBoundary(tester, key400, '03_peta_panel_fokus.png');

      // ═══════════════════════════════════════════════════════
      // 2. VIEWPORT 360px (Skala Ekstrem 200% / 2.0) - Bukti Bebas Overflow
      // ═══════════════════════════════════════════════════════
      tester.view.physicalSize = const Size(720, 1600);
      tester.view.devicePixelRatio = 2.0; // 360 x 800 logical px

      final key360Scale200 = GlobalKey();
      await tester.pumpWidget(
        buildTestableRoadmap(key: key360Scale200, logicalWidth: 360, textScale: 2.0),
      );
      await tester.pumpAndSettle();

      // SCREEN 4: Peta awal pada lebar 360px dan skala teks 200%
      await saveRepaintBoundary(
        tester,
        key360Scale200,
        '04_peta_awal_360_scale200.png',
      );

      // SCREEN 5: Buka kelompok pada 360px skala 200%
      await tester.tap(find.text('Logika & Sintaks Dasar'));
      await tester.pumpAndSettle();
      await saveRepaintBoundary(
        tester,
        key360Scale200,
        '05_peta_kelompok_topik_360_scale200.png',
      );

      // SCREEN 6: Buka panel fokus pada 360px skala 200%
      await tester.tap(find.text('Variables & Data Types').first);
      await tester.pumpAndSettle();
      await saveRepaintBoundary(
        tester,
        key360Scale200,
        '06_peta_panel_fokus_360_scale200.png',
      );

      // ═══════════════════════════════════════════════════════
      // 3. PENGUJIAN KOMBINASI LEBAR & SKALA LAINNYA
      // ═══════════════════════════════════════════════════════
      // A. Lebar 360px, Skala 1.0 (Normal)
      final key360Normal = GlobalKey();
      await tester.pumpWidget(
        buildTestableRoadmap(key: key360Normal, logicalWidth: 360, textScale: 1.0),
      );
      await tester.pumpAndSettle();

      // B. Lebar 400px, Skala 2.0 (200%)
      tester.view.physicalSize = const Size(800, 1600);
      final key400Scale200 = GlobalKey();
      await tester.pumpWidget(
        buildTestableRoadmap(key: key400Scale200, logicalWidth: 400, textScale: 2.0),
      );
      await tester.pumpAndSettle();

      // Restore view parameters
      addTearDown(() {
        tester.view.resetPhysicalSize();
        tester.view.resetDevicePixelRatio();
      });
    },
  );
}
