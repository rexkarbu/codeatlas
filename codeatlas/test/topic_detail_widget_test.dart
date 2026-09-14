// test/topic_detail_widget_test.dart — Widget tests for long-form article rendering:
// 8 pedagogical sections, single TOC bottom sheet navigation, 200% text scaling (no overflow),
// expandable reflection answers, and persistent notes editing.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:codeatlas/data/content_repository.dart';
import 'package:codeatlas/data/learning_repository.dart';
import 'package:codeatlas/data/models.dart';
import 'package:codeatlas/features/topic/topic_screen.dart';
import 'package:codeatlas/state/app_state.dart';

class FakeDetailContentRepository implements ContentRepository {
  final Topic topic;

  FakeDetailContentRepository(this.topic);

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<Topic?> getTopicById(String id) async => topic;

  @override
  Future<List<String>> getDependentTopicIds(String topicId) async => [];

  @override
  Future<List<Topic>> getAllActiveTopics() async => [topic];
}

class FakeDetailLearningRepository implements LearningRepository {
  Progress? currentProgress;

  FakeDetailLearningRepository(this.currentProgress);

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<Progress?> getProgress(String topicId) async => currentProgress;

  @override
  Future<void> recordReview(String topicId) async {}

  @override
  Future<void> updateStatus(String topicId, LearningStatus status) async {
    currentProgress = Progress(
      topicId: topicId,
      status: status,
      notes: currentProgress?.notes ?? '',
      updatedAt: DateTime.now(),
    );
  }

  @override
  Future<void> updateNotes(String topicId, String notes) async {
    currentProgress = Progress(
      topicId: topicId,
      status: currentProgress?.status ?? LearningStatus.notStarted,
      notes: notes,
      updatedAt: DateTime.now(),
    );
  }

  @override
  Future<int> countByStatus(
    LearningStatus status, {
    Set<String>? topicIds,
  }) async => 0;

  @override
  Future<String?> getLastReviewedTopicId() async => null;
}

void main() {
  final sampleLongTopic = Topic(
    id: 'f-sample-deep',
    categoryId: 'f-logic',
    title: 'Variabel dan Tipe Data',
    level: Difficulty.beginner,
    summary: 'Fondasi penyimpanan dan manipulasi informasi di memori komputer.',
    explanationSimple:
        'Bayangkan variabel seperti toples berlabel di dapur dengan ukuran tertentu. '
        'Toples gula hanya untuk gula, botol sirup hanya untuk cairan. '
        'Label adalah nama variabel, isi toples adalah nilainya, dan bentuk wadahnya adalah tipe data.',
    problemContext:
        'Sebelum ada variabel dan tipe data terstruktur, programmer harus mengingat alamat register '
        'secara manual. Jika sebuah byte angka ditafsirkan sebagai instruksi mesin, program bisa crash seketika.',
    explanationTechnical:
        'Di tingkat arsitektur sistem komputer, deklarasi variabel mengalokasikan ruang memori berukuran tetap atau dinamis. '
        'Tipe data primitif (int, double, bool) disimpan langsung di stack memory, sedangkan objek kompleks disimpan di heap.',
    codeExamples: [
      CodeExample(
        label: 'Penelusuran Langkah demi Langkah',
        language: 'dart',
        code: 'void main() {\n  int age = 25;\n  double price = 19.99;\n  print("Umur: \$age, Harga: \$price");\n}',
        explanation: 'Baris 1: mengalokasikan 64-bit integer di stack. Baris 2: mengalokasikan floating point IEEE-754.',
        expectedOutput: 'Umur: 25, Harga: 19.99',
      ),
    ],
    misconceptions: [
      TopicMisconception(
        misconception:
            'Variabel adalah wadah fisik statis yang menyimpan data selamanya.',
        explanation: 'Variabel adalah penanda simbolik ke blok memori dengan siklus hidup sesuai scope fungsinya.',
        spotInCode:
            'Mengakses variabel lokal di luar blok kurung kurawal fungsi.',
      ),
      TopicMisconception(
        misconception: 'dynamic dan Object? sama persis dalam keamanan tipe.',
        explanation: 'dynamic mematikan static analysis compile-time, sedangkan Object? tetap mewajibkan type checking/casting eksplisit.',
        spotInCode:
            'Menggunakan dynamic saat deserialisasi JSON tanpa validasi skema.',
      ),
    ],
    whenToUse:
        'Gunakan tipe data primitif dan immutable (final/const) sedini mungkin untuk mencegah efek samping. '
        'Hindari tipe dynamic kecuali pada boundary I/O yang belum terverifikasi skemanya.',
    whyVibecodingMatters:
        'AI generator sering kali memilih tipe dynamic atau menebak tipe data yang longgar tanpa null safety yang ketat. '
        'Ajukan pertanyaan ke AI: "Apakah variabel ini aman dari null pointer exception di runtime?"',
    reflectionQuestions: [
      TopicReflection(
        question: 'Apa perbedaan mendasar antara tipe data di stack dan heap?',
        answer:
            'Stack memiliki alokasi memori cepat dan otomatis sesuai siklus stack frame fungsi, '
            'sedangkan heap digunakan untuk struktur data dinamis berukuran fleksibel yang dikelola oleh Garbage Collector.',
      ),
      TopicReflection(
        question:
            'Mengapa mengubah variabel final di Dart memicu error kompilasi?',
        answer: 'Karena kata kunci final menandakan referensi variabel hanya dapat diinisialisasi satu kali seumur hidupnya.',
      ),
    ],
    estimatedMinutes: 7,
    sortOrder: 1,
  );

  group('TopicScreen Deep Article & Accessibility Widget Tests', () {
    late FakeDetailContentRepository fakeContentRepo;
    late FakeDetailLearningRepository fakeLearningRepo;
    late AppState appState;

    setUp(() {
      fakeContentRepo = FakeDetailContentRepository(sampleLongTopic);
      fakeLearningRepo = FakeDetailLearningRepository(null);
      appState = AppState(
        contentRepo: fakeContentRepo,
        learningRepo: fakeLearningRepo,
      );
    });

    testWidgets('All 8 pedagogical sections are rendered and findable', (
      tester,
    ) async {
      await tester.pumpWidget(
        MaterialApp(
          home: TopicScreen(
            topicId: sampleLongTopic.id,
            contentRepo: fakeContentRepo,
            learningRepo: fakeLearningRepo,
            appState: appState,
            onOpenTopic: (_) {},
          ),
        ),
      );
      await tester.pumpAndSettle();

      final scrollable = find
          .descendant(
            of: find.byKey(const ValueKey('topic_scrollable')),
            matching: find.byType(Scrollable),
          )
          .first;

      // 1. Analogi
      expect(find.text('1. Apa Konsep Ini?'), findsOneWidget);
      expect(
        find.textContaining('Bayangkan variabel seperti toples berlabel'),
        findsOneWidget,
      );

      // 2. Masalah yang Diselesaikan
      await tester.scrollUntilVisible(
        find.text('2. Masalah Apa yang Diselesaikan?'),
        150,
        scrollable: scrollable,
      );
      expect(find.text('2. Masalah Apa yang Diselesaikan?'), findsOneWidget);
      expect(
        find.textContaining('Sebelum ada variabel dan tipe data'),
        findsOneWidget,
      );

      // 3. Cara Kerja & Mekanisme
      await tester.scrollUntilVisible(
        find.text('3. Bagaimana Cara Kerjanya?'),
        150,
        scrollable: scrollable,
      );
      expect(find.text('3. Bagaimana Cara Kerjanya?'), findsOneWidget);
      expect(
        find.textContaining('Di tingkat arsitektur sistem komputer'),
        findsOneWidget,
      );

      // 4. Contoh Kode & Penelusuran
      await tester.scrollUntilVisible(
        find.text('4. Bagaimana Membaca Contohnya?'),
        150,
        scrollable: scrollable,
      );
      expect(find.text('4. Bagaimana Membaca Contohnya?'), findsOneWidget);
      expect(find.text('Penelusuran Langkah demi Langkah'), findsOneWidget);

      // 5. Miskonsepsi
      await tester.scrollUntilVisible(
        find.text('5. Apa yang Sering Disalahpahami?'),
        150,
        scrollable: scrollable,
      );
      expect(find.text('5. Apa yang Sering Disalahpahami?'), findsOneWidget);
      expect(
        find.text(
          'Variabel adalah wadah fisik statis yang menyimpan data selamanya.',
        ),
        findsOneWidget,
      );

      // 6. Kapan Dipakai
      await tester.scrollUntilVisible(
        find.text('6. Kapan Dipakai & Batas Penerapan?'),
        150,
        scrollable: scrollable,
      );
      expect(find.text('6. Kapan Dipakai & Batas Penerapan?'), findsOneWidget);
      expect(
        find.textContaining('Gunakan tipe data primitif dan immutable'),
        findsOneWidget,
      );

      // 7. Kenapa Penting saat Vibecoding
      await tester.scrollUntilVisible(
        find.text('7. Mengapa Penting saat Vibecoding?'),
        150,
        scrollable: scrollable,
      );
      expect(find.text('7. Mengapa Penting saat Vibecoding?'), findsOneWidget);
      expect(
        find.textContaining('AI generator sering kali memilih tipe dynamic'),
        findsOneWidget,
      );

      // 8. Pertanyaan Refleksi
      await tester.scrollUntilVisible(
        find.text('8. Bagaimana Memeriksa Pemahaman?'),
        150,
        scrollable: scrollable,
      );
      expect(find.text('8. Bagaimana Memeriksa Pemahaman?'), findsOneWidget);
      expect(
        find.text('Apa perbedaan mendasar antara tipe data di stack dan heap?'),
        findsOneWidget,
      );

      // Catatan Pribadi
      await tester.scrollUntilVisible(
        find.text('Catatan Pribadi'),
        150,
        scrollable: scrollable,
      );
      expect(find.text('Catatan Pribadi'), findsOneWidget);
    });

    testWidgets(
      'Table of contents button opens modal and navigates to section',
      (tester) async {
        await tester.pumpWidget(
          MaterialApp(
            home: TopicScreen(
              topicId: sampleLongTopic.id,
              contentRepo: fakeContentRepo,
              learningRepo: fakeLearningRepo,
              appState: appState,
              onOpenTopic: (_) {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        // Tap Daftar Isi button
        final tocBtn = find.byKey(const ValueKey('toc_button'));
        expect(tocBtn, findsOneWidget);
        await tester.tap(tocBtn);
        await tester.pumpAndSettle();

        // Modal Bottom Sheet appears with TOC list
        expect(find.text('Daftar Isi Artikel'), findsOneWidget);
        expect(find.text('1. Apa Konsep Ini?'), findsWidgets);
        expect(find.text('5. Miskonsepsi Umum'), findsOneWidget);
        expect(find.text('8. Pertanyaan Refleksi'), findsOneWidget);

        // Tap section in TOC
        await tester.tap(find.text('5. Miskonsepsi Umum'));
        await tester.pumpAndSettle();

        // Sheet is closed and section is scrolled into view
        expect(find.text('Daftar Isi Artikel'), findsNothing);
        expect(find.text('5. Apa yang Sering Disalahpahami?'), findsOneWidget);
      },
    );

    testWidgets('Reflection question expansion tile reveals hidden answer', (
      tester,
    ) async {
      await tester.pumpWidget(
        MaterialApp(
          home: TopicScreen(
            topicId: sampleLongTopic.id,
            contentRepo: fakeContentRepo,
            learningRepo: fakeLearningRepo,
            appState: appState,
            onOpenTopic: (_) {},
          ),
        ),
      );
      await tester.pumpAndSettle();

      final scrollable = find
          .descendant(
            of: find.byKey(const ValueKey('topic_scrollable')),
            matching: find.byType(Scrollable),
          )
          .first;
      final tileFinder = find.byKey(const ValueKey('reflection_tile_0'));
      await tester.scrollUntilVisible(tileFinder, 200, scrollable: scrollable);
      expect(tileFinder, findsOneWidget);

      final answerText =
          'Stack memiliki alokasi memori cepat dan otomatis sesuai siklus stack frame fungsi';

      // Tap ExpansionTile to expand
      await tester.tap(tileFinder);
      await tester.pumpAndSettle();

      // Now answer key is visible
      expect(find.textContaining(answerText), findsOneWidget);
    });

    testWidgets('Renders at 200% text scale without overflow error', (
      tester,
    ) async {
      final binding = TestWidgetsFlutterBinding.ensureInitialized();
      binding.platformDispatcher.textScaleFactorTestValue = 2.0;
      addTearDown(
        () => binding.platformDispatcher.clearTextScaleFactorTestValue(),
      );

      await tester.pumpWidget(
        MaterialApp(
          home: MediaQuery(
            data: const MediaQueryData(textScaler: TextScaler.linear(2.0)),
            child: TopicScreen(
              topicId: sampleLongTopic.id,
              contentRepo: fakeContentRepo,
              learningRepo: fakeLearningRepo,
              appState: appState,
              onOpenTopic: (_) {},
            ),
          ),
        ),
      );
      await tester.pumpAndSettle();

      final scrollView = find.byKey(const ValueKey('topic_scrollable'));

      // Scroll down slowly to check every section for render flex overflow
      await tester.drag(scrollView, const Offset(0, -400));
      await tester.pumpAndSettle();
      await tester.drag(scrollView, const Offset(0, -400));
      await tester.pumpAndSettle();
      await tester.drag(scrollView, const Offset(0, -400));
      await tester.pumpAndSettle();

      // No assertion error / overflow occurred
      expect(tester.takeException(), isNull);
    });

    testWidgets('Notes section can be edited and saved', (tester) async {
      await tester.pumpWidget(
        MaterialApp(
          home: TopicScreen(
            topicId: sampleLongTopic.id,
            contentRepo: fakeContentRepo,
            learningRepo: fakeLearningRepo,
            appState: appState,
            onOpenTopic: (_) {},
          ),
        ),
      );
      await tester.pumpAndSettle();

      final scrollable = find
          .descendant(
            of: find.byKey(const ValueKey('topic_scrollable')),
            matching: find.byType(Scrollable),
          )
          .first;
      final notesField = find.byType(TextField);
      await tester.scrollUntilVisible(notesField, 200, scrollable: scrollable);
      expect(notesField, findsOneWidget);

      await tester.enterText(
        notesField,
        'Catatan penting mengenai alokasi memori stack vs heap.',
      );
      await tester.pumpAndSettle();

      expect(find.text('Belum disimpan'), findsOneWidget);

      await tester.tap(find.text('Simpan Catatan'));
      await tester.pumpAndSettle();

      expect(find.text('Tersimpan'), findsOneWidget);
      expect(
        fakeLearningRepo.currentProgress?.notes,
        'Catatan penting mengenai alokasi memori stack vs heap.',
      );
      await tester.pump(const Duration(seconds: 2));
    });
  });
}
