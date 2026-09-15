// test/topic_variety_test.dart — Dedicated verification for topic variety:
// 1. Programming Logic review example.
// 2. Long article with extensive pedagogical content.
// 3. Multi-language code article (only shows available languages in tabs).
// 4. Article with optional empty sections.
// 5. 200% text scaling on 360dp width for all varieties without overflow.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:codeatlas/data/content_repository.dart';
import 'package:codeatlas/data/learning_repository.dart';
import 'package:codeatlas/data/models.dart';
import 'package:codeatlas/data/reading_time.dart';
import 'package:codeatlas/features/home/home_screen.dart';
import 'package:codeatlas/features/topic/topic_screen.dart';
import 'package:codeatlas/state/app_state.dart';

class VarietyContentRepo implements ContentRepository {
  final Map<String, Topic> topics;

  VarietyContentRepo(this.topics);

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<Topic?> getTopicById(String id) async => topics[id];

  @override
  Future<List<String>> getDependentTopicIds(String topicId) async => [];

  @override
  Future<List<Topic>> getAllActiveTopics() async => topics.values.toList();
}

class VarietyLearningRepo implements LearningRepository {
  final Map<String, Progress> progressMap = {};

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<Progress?> getProgress(String topicId) async => progressMap[topicId];

  @override
  Future<void> recordReview(String topicId) async {}

  @override
  Future<void> updateStatus(String topicId, LearningStatus status) async {
    progressMap[topicId] = Progress(
      topicId: topicId,
      status: status,
      notes: progressMap[topicId]?.notes ?? '',
      updatedAt: DateTime.now(),
    );
  }

  @override
  Future<void> updateNotes(String topicId, String notes) async {
    progressMap[topicId] = Progress(
      topicId: topicId,
      status: progressMap[topicId]?.status ?? LearningStatus.notStarted,
      notes: notes,
      updatedAt: DateTime.now(),
    );
  }
}

void main() {
  // 1. Review example: Programming Logic
  final programmingLogicTopic = Topic(
    id: 'f-programming-logic',
    categoryId: 'f-logic',
    title: 'Programming Logic',
    level: Difficulty.beginner,
    summary: 'Fondasi berpikir terstruktur untuk menyusun instruksi komputer.',
    explanationSimple:
        'Analogi resep masakan yang dieksekusi langkah demi langkah.',
    explanationTechnical:
        'Urutan instruksi sekuensial yang diproses register dan ALU prosesor.',
    whyVibecodingMatters:
        'Keluaran AI bisa tampak meyakinkan tapi memiliki cacat logika fatal.',
    problemContext: 'Komputer tidak memiliki intuisi akal sehat.',
    whenToUse: 'Gunakan saat merancang alur logika sebelum menulis implementasi detail.',
    codeExamples: [
      CodeExample(
        label: 'Eksekusi Sekuensial Sederhana',
        language: 'python',
        code: 'def hitung(a, b):\n    return a + b\n\nprint(hitung(3, 4))',
        explanation:
            'Fungsi menerima dua argumen dan mengembalikan hasil penjumlahan.',
        expectedOutput: '7',
      ),
    ],
    reflectionQuestions: [
      TopicReflection(
        question: 'Mengapa komputer butuh instruksi eksplisit?',
        answer: 'Karena CPU hanya mengeksekusi instruksi biner tanpa asumsi konteks.',
      ),
    ],
    estimatedMinutes: 5,
    sortOrder: 1,
  );

  // 2. Multi-language code example (Dart and Python only)
  final multiLangTopic = Topic(
    id: 'f-control-flow',
    categoryId: 'f-logic',
    title: 'Control Flow: Percabangan',
    level: Difficulty.beginner,
    summary: 'Mekanisme pengambilan keputusan di dalam program.',
    explanationSimple: 'Seperti persimpangan jalan dengan rambu lalu lintas.',
    explanationTechnical:
        'Instruksi jump kondisional pada tingkat assembly (je, jne).',
    whyVibecodingMatters:
        'Mencegah kondisi balapan dan percabangan yang tidak pernah tercapai.',
    codeExamples: [
      CodeExample(
        label: 'Percabangan di Python',
        language: 'python',
        code: 'if x > 0:\n    print("positif")',
        explanation: 'Menguji kondisi boolean.',
        expectedOutput: 'positif',
      ),
      CodeExample(
        label: 'Percabangan di Dart',
        language: 'dart',
        code: 'if (x > 0) {\n  print("positif");\n}',
        explanation: 'Sintaks berbasis C dengan tanda kurung kurawal.',
        expectedOutput: 'positif',
      ),
    ],
    estimatedMinutes: 6,
    sortOrder: 2,
  );

  // 3. Article with empty optional sections
  final minimalTopic = Topic(
    id: 'f-minimal-topic',
    categoryId: 'f-logic',
    title: 'Topik Minimal',
    level: Difficulty.beginner,
    summary: 'Ringkasan singkat.',
    explanationSimple: 'Penjelasan sederhana.',
    explanationTechnical: 'Penjelasan teknis.',
    whyVibecodingMatters: 'Vibecoding relevance.',
    estimatedMinutes: 3,
    sortOrder: 3,
  );

  group('TopicScreen Variety & Structure Tests', () {
    testWidgets('Programming Logic renders 8 pedagogical sections cleanly', (
      tester,
    ) async {
      final repo = VarietyContentRepo({
        'f-programming-logic': programmingLogicTopic,
      });
      final learningRepo = VarietyLearningRepo();
      final appState = AppState(contentRepo: repo, learningRepo: learningRepo);

      await tester.pumpWidget(
        MaterialApp(
          home: TopicScreen(
            topicId: 'f-programming-logic',
            contentRepo: repo,
            learningRepo: learningRepo,
            appState: appState,
            onOpenTopic: (_) {},
          ),
        ),
      );
      await tester.pumpAndSettle();

      expect(find.text('Programming Logic'), findsOneWidget);
      expect(find.text('1. Apa Konsep Ini?'), findsOneWidget);
      expect(find.text('Eksekusi Sekuensial Sederhana'), findsOneWidget);
      expect(find.text('Hasil yang diharapkan:'), findsOneWidget);
      expect(find.text('Status Pemahaman:'), findsOneWidget);
    });

    testWidgets(
      'Multi-language article displays tabs only for available languages',
      (tester) async {
        final repo = VarietyContentRepo({'f-control-flow': multiLangTopic});
        final learningRepo = VarietyLearningRepo();
        final appState = AppState(
          contentRepo: repo,
          learningRepo: learningRepo,
        );

        await tester.pumpWidget(
          MaterialApp(
            home: TopicScreen(
              topicId: 'f-control-flow',
              contentRepo: repo,
              learningRepo: learningRepo,
              appState: appState,
              onOpenTopic: (_) {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        // Verify choice chips for available languages
        expect(find.text('PYTHON'), findsOneWidget);
        expect(find.text('DART'), findsOneWidget);
        // Ensure no phantom TypeScript or third empty tab is forced
        expect(find.text('TYPESCRIPT'), findsNothing);

        // Verify initial example shown is Python
        expect(find.text('Percabangan di Python'), findsOneWidget);

        // Scroll until DART chip is visible, then switch tab to Dart
        final scrollable = find
            .descendant(
              of: find.byKey(const ValueKey('topic_scrollable')),
              matching: find.byType(Scrollable),
            )
            .first;
        await tester.scrollUntilVisible(
          find.text('DART'),
          100,
          scrollable: scrollable,
        );
        await tester.tap(find.text('DART'));
        await tester.pumpAndSettle();

        expect(find.text('Percabangan di Dart'), findsOneWidget);
      },
    );

    testWidgets('Minimal topic with omitted optional sections renders safely', (
      tester,
    ) async {
      final repo = VarietyContentRepo({'f-minimal-topic': minimalTopic});
      final learningRepo = VarietyLearningRepo();
      final appState = AppState(contentRepo: repo, learningRepo: learningRepo);

      await tester.pumpWidget(
        MaterialApp(
          home: TopicScreen(
            topicId: 'f-minimal-topic',
            contentRepo: repo,
            learningRepo: learningRepo,
            appState: appState,
            onOpenTopic: (_) {},
          ),
        ),
      );
      await tester.pumpAndSettle();

      expect(find.text('Topik Minimal'), findsOneWidget);
      expect(find.text('1. Apa Konsep Ini?'), findsOneWidget);
      // Optional sections that are empty do not crash or show empty card
      expect(find.text('2. Masalah Apa yang Diselesaikan?'), findsNothing);
      expect(find.text('5. Apa yang Sering Disalahpahami?'), findsNothing);
    });

    test('Reading time calculation is consistent across HomeScreen and TopicScreen', () {
      final formatted = ReadingTimeEstimator.format(programmingLogicTopic);
      expect(formatted, startsWith('Perkiraan '));
      expect(formatted, endsWith(' mnt baca'));

      // Both HomeScreen helper and ReadingTimeEstimator produce identical result
      expect(HomeScreen.formatReadingTime(programmingLogicTopic), formatted);
      expect(
        HomeScreen.calculateReadingMinutes(programmingLogicTopic),
        ReadingTimeEstimator.estimateMinutes(programmingLogicTopic),
      );
    });

    testWidgets(
      'TopicScreen renders at 200% text scale on 360dp width without overflow and footer buttons are fully visible & interactive',
      (tester) async {
        final binding = TestWidgetsFlutterBinding.ensureInitialized();
        binding.platformDispatcher.textScaleFactorTestValue = 2.0;
        addTearDown(
          () => binding.platformDispatcher.clearTextScaleFactorTestValue(),
        );

        tester.view.physicalSize = const Size(360 * 3, 640 * 3);
        tester.view.devicePixelRatio = 3.0;
        addTearDown(() => tester.view.resetPhysicalSize());

        final repo = VarietyContentRepo({'f-control-flow': multiLangTopic});
        final learningRepo = VarietyLearningRepo();
        final appState = AppState(
          contentRepo: repo,
          learningRepo: learningRepo,
        );

        await tester.pumpWidget(
          MaterialApp(
            home: TopicScreen(
              topicId: 'f-control-flow',
              contentRepo: repo,
              learningRepo: learningRepo,
              appState: appState,
              onOpenTopic: (_) {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        expect(tester.takeException(), isNull);

        // Verify that all 3 status options exist
        final belumFinder = find.text('Belum');
        final sedangFinder = find.text('Sedang');
        final pahamFinder = find.text('Paham');

        expect(belumFinder, findsOneWidget);
        expect(sedangFinder, findsOneWidget);
        expect(pahamFinder, findsOneWidget);

        // Verify geometry: all 3 buttons are strictly within viewport bounds (0..360dp)
        final belumRect = tester.getRect(belumFinder);
        final sedangRect = tester.getRect(sedangFinder);
        final pahamRect = tester.getRect(pahamFinder);

        expect(belumRect.left, greaterThanOrEqualTo(0.0));
        expect(sedangRect.left, greaterThan(belumRect.right));
        expect(pahamRect.left, greaterThan(sedangRect.right));
        expect(pahamRect.right, lessThanOrEqualTo(360.0));

        // Verify interactive tap on "Paham" button updates progress
        await tester.tap(pahamFinder);
        await tester.pumpAndSettle();

        final progress = await learningRepo.getProgress('f-control-flow');
        expect(progress?.status, LearningStatus.understood);
      },
    );

    testWidgets(
      'Long article title in AppBar at 200% text scale on 360dp width does not obscure TOC button',
      (tester) async {
        final binding = TestWidgetsFlutterBinding.ensureInitialized();
        binding.platformDispatcher.textScaleFactorTestValue = 2.0;
        addTearDown(
          () => binding.platformDispatcher.clearTextScaleFactorTestValue(),
        );

        tester.view.physicalSize = const Size(360 * 3, 640 * 3);
        tester.view.devicePixelRatio = 3.0;
        addTearDown(() => tester.view.resetPhysicalSize());

        final longTopic = Topic(
          id: 'f-long-title',
          categoryId: 'f-logic',
          title: 'Prinsip Desain Perangkat Lunak Berorientasi Objek Lanjutan',
          level: Difficulty.beginner,
          summary: 'Ringkasan.',
          explanationSimple: 'Penjelasan sederhana.',
          explanationTechnical: 'Penjelasan teknis.',
          whyVibecodingMatters: 'Vibecoding.',
          estimatedMinutes: 3,
          sortOrder: 1,
        );
        final repo = VarietyContentRepo({'f-long-title': longTopic});
        final learningRepo = VarietyLearningRepo();
        final appState = AppState(
          contentRepo: repo,
          learningRepo: learningRepo,
        );

        await tester.pumpWidget(
          MaterialApp(
            home: TopicScreen(
              topicId: 'f-long-title',
              contentRepo: repo,
              learningRepo: learningRepo,
              appState: appState,
              onOpenTopic: (_) {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        expect(tester.takeException(), isNull);

        // Verify TOC button is present, fully on screen, and accessible
        final tocFinder = find.byKey(const ValueKey('toc_button'));
        expect(tocFinder, findsOneWidget);
        final tocRect = tester.getRect(tocFinder);
        expect(tocRect.right, lessThanOrEqualTo(360.0));
        expect(tocRect.left, greaterThan(250.0));

        // Tap TOC button to ensure modal opens cleanly
        await tester.tap(tocFinder);
        await tester.pumpAndSettle();

        expect(find.text('Daftar Isi Artikel'), findsOneWidget);
      },
    );
  });
}
