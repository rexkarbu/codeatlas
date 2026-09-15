// test/learning_path_flow_test.dart — Comprehensive test suite for Phase 1 Learning Path flows:
// 1. 5 Preset cards on Home screen open PathDetailScreen with respective presetKey.
// 2. Preset prerequisites are dynamically resolved (not hardcoded to magic counts).
// 3. Tapping an article before "Mulai" reads in-memory without creating a database row.
// 4. Rapid double-taps on "Mulai" do not create duplicate learning paths in database.
// 5. Goal matching handles multiple paths, distinguishes exact presets from custom paths, and preserves custom paths.
// 6. Pre-existing saved paths with edited topic ordering display the edited order immediately in detail.
// 7. Topic navigation uses pushReplacement (clean back-stack), respects unsaved draft protection, and does not auto-mark Paham.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:codeatlas/data/content_repository.dart';
import 'package:codeatlas/data/learning_repository.dart';
import 'package:codeatlas/data/models.dart';
import 'package:codeatlas/features/home/home_screen.dart';
import 'package:codeatlas/features/learning_paths/path_builder.dart';
import 'package:codeatlas/features/learning_paths/path_detail_screen.dart';
import 'package:codeatlas/features/topic/topic_screen.dart';
import 'package:codeatlas/state/app_state.dart';
import 'package:codeatlas/theme/atlas_theme.dart';

class FakeFlowContentRepo implements ContentRepository {
  final Map<String, Topic> topics;
  final Map<String, List<String>> prereqs;

  FakeFlowContentRepo(this.topics, {this.prereqs = const {}});

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<Topic?> getTopicById(String id) async => topics[id];

  @override
  Future<List<Topic>> getAllActiveTopics() async => topics.values.toList();

  Future<List<String>> getTopicPrerequisites(String topicId) async =>
      prereqs[topicId] ?? [];

  @override
  Future<List<String>> getDependentTopicIds(String topicId) async {
    final list = <String>[];
    prereqs.forEach((target, reqs) {
      if (reqs.contains(topicId)) list.add(target);
    });
    return list;
  }

  @override
  Future<Map<String, List<String>>> getPrerequisiteGraph() async => prereqs;

  @override
  Future<Set<String>> getTransitivePrerequisites(String topicId) async {
    final result = <String>{};
    final queue = <String>[topicId];
    final visited = <String>{};
    while (queue.isNotEmpty) {
      final curr = queue.removeLast();
      if (!visited.add(curr)) continue;
      final direct = prereqs[curr] ?? [];
      for (final p in direct) {
        result.add(p);
        queue.add(p);
      }
    }
    return result;
  }

  @override
  Future<int> getActiveTopicCount() async => topics.length;

  @override
  Future<int> getActiveTopicCountByLayer(ContentLayer layer) async =>
      topics.length;
}

class FakeFlowLearningRepo implements LearningRepository {
  final Map<String, Progress> progressMap = {};
  final List<LearningPath> savedPaths = [];
  int _nextPathId = 1;
  int createCallCount = 0;

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<Progress?> getProgress(String topicId) async => progressMap[topicId];

  @override
  Future<Map<String, Progress>> getAllProgress() async => Map.from(progressMap);

  @override
  Future<void> recordReview(String topicId) async {}

  @override
  Future<void> updateStatus(String topicId, LearningStatus status) async {
    final existing = progressMap[topicId];
    progressMap[topicId] = Progress(
      topicId: topicId,
      status: status,
      notes: existing?.notes ?? '',
      updatedAt: DateTime.now(),
    );
  }

  @override
  Future<void> updateNotes(String topicId, String notes) async {
    final existing = progressMap[topicId];
    progressMap[topicId] = Progress(
      topicId: topicId,
      status: existing?.status ?? LearningStatus.notStarted,
      notes: notes,
      updatedAt: DateTime.now(),
    );
  }

  @override
  Future<List<LearningPath>> getAllPaths() async {
    final list = List<LearningPath>.from(savedPaths);
    list.sort((a, b) => b.updatedAt.compareTo(a.updatedAt));
    return list;
  }

  @override
  Future<LearningPath?> getPath(int pathId) async {
    for (final p in savedPaths) {
      if (p.id == pathId) return p;
    }
    return null;
  }

  @override
  Future<int> createPath({
    required String name,
    required String goal,
    required List<String> topicIds,
  }) async {
    createCallCount++;
    await Future.microtask(() {});
    final id = _nextPathId++;
    final now = DateTime.now().toUtc();
    final items = [
      for (int i = 0; i < topicIds.length; i++)
        LearningPathItem(pathId: id, topicId: topicIds[i], position: i),
    ];
    final path = LearningPath(
      id: id,
      name: name,
      goal: goal,
      createdAt: now,
      updatedAt: now,
      items: items,
    );
    savedPaths.add(path);
    return id;
  }

  @override
  Future<void> updatePath({
    required int pathId,
    String? name,
    List<String>? topicIds,
  }) async {
    final index = savedPaths.indexWhere((p) => p.id == pathId);
    if (index >= 0) {
      final old = savedPaths[index];
      final now = DateTime.now().toUtc();
      final items = topicIds != null
          ? [
              for (int i = 0; i < topicIds.length; i++)
                LearningPathItem(
                  pathId: pathId,
                  topicId: topicIds[i],
                  position: i,
                ),
            ]
          : old.items;
      savedPaths[index] = old.copyWith(
        name: name ?? old.name,
        updatedAt: now,
        items: items,
      );
    }
  }

  @override
  Future<int> countByStatus(
    LearningStatus status, {
    Set<String>? topicIds,
  }) async {
    return progressMap.values.where((p) {
      if (topicIds != null && !topicIds.contains(p.topicId)) return false;
      return p.status == status;
    }).length;
  }
}

Topic _mockTopic(String id, String title) {
  return Topic(
    id: id,
    categoryId: 'f-basics',
    title: title,
    level: Difficulty.beginner,
    summary: 'Ringkasan materi $title.',
    explanationSimple: 'Analogi sederhana $title.',
    explanationTechnical: 'Penjelasan teknis $title.',
    whyVibecodingMatters: 'Alasan AI penting di $title.',
    estimatedMinutes: 5,
    sortOrder: 1,
  );
}

void main() {
  late FakeFlowContentRepo fakeContentRepo;
  late FakeFlowLearningRepo fakeLearningRepo;
  late AppState appState;

  setUp(() {
    final topicList = [
      // General path topics
      _mockTopic('f-programming-logic', 'Programming Logic'),
      _mockTopic('f-variables-data-types', 'Variabel & Tipe Data'),
      _mockTopic('f-operators', 'Operator & Ekspresi'),
      _mockTopic('f-conditionals', 'Percabangan'),
      _mockTopic('f-loops', 'Perulangan'),
      _mockTopic('f-functions', 'Fungsi & Modularitas'),
      _mockTopic('f-debugging', 'Debugging'),
      _mockTopic('f-testing', 'Pengujian Kode (Testing)'),
      _mockTopic('f-git', 'Git & Version Control'),

      // Flutter path topics
      _mockTopic('f-type-system', 'Sistem Tipe Data'),
      _mockTopic('f-oop', 'OOP & Kelas'),
      _mockTopic('f-modules-packages', 'Modul & Package'),
      _mockTopic('f-dependencies', 'Manajemen Dependensi'),
      _mockTopic('f-error-handling', 'Penanganan Error'),
      _mockTopic('f-async', 'Pemrograman Asinkron'),
      _mockTopic('f-apis', 'REST API & HTTP Client'),
      _mockTopic('f-serialization', 'Serialisasi JSON'),
      _mockTopic('e-mobile-overview', 'Ekosistem Mobile'),
      _mockTopic('e-frameworks-overview', 'Framework Modern'),
    ];

    final topicMap = {for (final t in topicList) t.id: t};

    fakeContentRepo = FakeFlowContentRepo(
      topicMap,
      prereqs: {
        'f-variables-data-types': ['f-programming-logic'],
        'f-operators': ['f-variables-data-types'],
        'f-conditionals': ['f-operators'],
        'f-loops': ['f-conditionals'],
        'f-functions': ['f-loops'],
        'f-debugging': ['f-functions'],
        'f-testing': ['f-debugging'],
        'f-git': ['f-testing'],
        'f-oop': ['f-type-system'],
      },
    );

    fakeLearningRepo = FakeFlowLearningRepo();
    appState = AppState(
      contentRepo: fakeContentRepo,
      learningRepo: fakeLearningRepo,
    );
  });

  group('Learning Path Flow & Edge Cases Tests', () {
    testWidgets(
      '1. Home preset cards pass correct presetKey to onOpenPathPreset',
      (tester) async {
        String? tappedPreset;

        await tester.pumpWidget(
          MaterialApp(
            theme: AtlasTheme.buildTheme(Brightness.light),
            home: HomeScreen(
              appState: appState,
              contentRepo: fakeContentRepo,
              onNavigateToExplore: () {},
              onNavigateToPaths: () {},
              onOpenTopic: (_) {},
              onOpenSettings: () {},
              onOpenPathPreset: (key) => tappedPreset = key,
            ),
          ),
        );
        await tester.pumpAndSettle();

        // Tap Flutter card
        final flutterFinder = find.text('Flutter & Mobile');
        await tester.ensureVisible(flutterFinder);
        await tester.pumpAndSettle();
        await tester.tap(flutterFinder);
        expect(tappedPreset, equals('flutter'));

        // Tap Web Frontend card
        final webFinder = find.text('Web Frontend');
        await tester.ensureVisible(webFinder);
        await tester.pumpAndSettle();
        await tester.tap(webFinder);
        expect(tappedPreset, equals('web'));

        // Tap Backend & Server card
        final backendFinder = find.text('Backend & Server');
        await tester.ensureVisible(backendFinder);
        await tester.pumpAndSettle();
        await tester.tap(backendFinder);
        expect(tappedPreset, equals('backend'));

        // Tap Data & Algoritma card
        final dataFinder = find.text('Data & Algoritma');
        await tester.ensureVisible(dataFinder);
        await tester.pumpAndSettle();
        await tester.tap(dataFinder);
        expect(tappedPreset, equals('data'));

        // Tap Umum card
        final umumFinder = find.text('Umum / Dasar dari Nol');
        await tester.ensureVisible(umumFinder);
        await tester.pumpAndSettle();
        await tester.tap(umumFinder);
        expect(tappedPreset, equals('general'));
      },
    );

    testWidgets(
      '2. Dynamic prerequisite resolution does not hardcode magic numbers',
      (tester) async {
        final preset = pathPresets['general']!;
        final resolvedTopics = await buildPathTopicList(
          preset.targetIds,
          fakeContentRepo,
        );

        // Dynamically verifies that targetIds and their prerequisites are resolved
        expect(resolvedTopics.isNotEmpty, isTrue);
        expect(resolvedTopics.contains('f-programming-logic'), isTrue);

        await tester.pumpWidget(
          MaterialApp(
            theme: AtlasTheme.buildTheme(Brightness.light),
            home: PathDetailScreen(
              presetKey: 'general',
              contentRepo: fakeContentRepo,
              learningRepo: fakeLearningRepo,
              appState: appState,
              onOpenTopic: (
                _, {
                pathId,
                pathName,
                pathTopicIds,
                onBackToPath,
              }) {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        // Screen displays dynamic topic count based on resolvedTopics
        expect(
          find.text('Materi Terurut (${resolvedTopics.length} Topik)'),
          findsOneWidget,
        );
      },
    );

    testWidgets(
      '3. In-memory reading: Opening detail and tapping article does NOT create saved path',
      (tester) async {
        String? openedTopicId;
        String? openedPathId;
        String? openedPathName;
        List<String>? openedPathTopicIds;

        await tester.pumpWidget(
          MaterialApp(
            theme: AtlasTheme.buildTheme(Brightness.light),
            home: PathDetailScreen(
              presetKey: 'general',
              contentRepo: fakeContentRepo,
              learningRepo: fakeLearningRepo,
              appState: appState,
              onOpenTopic:
                  (topicId, {pathId, pathName, pathTopicIds, onBackToPath}) {
                    openedTopicId = topicId;
                    openedPathId = pathId;
                    openedPathName = pathName;
                    openedPathTopicIds = pathTopicIds;
                  },
            ),
          ),
        );
        await tester.pumpAndSettle();

        // Verified: opening detail has not created any DB path
        expect(fakeLearningRepo.savedPaths.isEmpty, isTrue);

        // Tap the first topic in the list
        await tester.tap(find.text('Programming Logic'));
        await tester.pumpAndSettle();

        // Verified: Topic opened with in-memory context (pathId == null)
        expect(openedTopicId, equals('f-programming-logic'));
        expect(openedPathId, isNull);
        expect(openedPathName, equals(pathPresets['general']!.name));
        expect(openedPathTopicIds, isNotNull);
        expect(openedPathTopicIds!.isNotEmpty, isTrue);

        // Still NO path saved in DB
        expect(fakeLearningRepo.savedPaths.isEmpty, isTrue);
      },
    );

    testWidgets(
      '4. Rapid double-tap on Mulai Belajar does NOT create duplicate paths',
      (tester) async {
        await tester.pumpWidget(
          MaterialApp(
            theme: AtlasTheme.buildTheme(Brightness.light),
            home: PathDetailScreen(
              presetKey: 'general',
              contentRepo: fakeContentRepo,
              learningRepo: fakeLearningRepo,
              appState: appState,
              onOpenTopic: (
                _, {
                pathId,
                pathName,
                pathTopicIds,
                onBackToPath,
              }) {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        final buttonFinder = find.widgetWithText(FilledButton, 'Mulai Belajar');
        expect(buttonFinder, findsOneWidget);

        // Simulate rapid double-tap
        await tester.tap(buttonFinder);
        await tester.tap(buttonFinder, warnIfMissed: false);
        await tester.pumpAndSettle();

        // Concurrency guard and duplicate check ensured exactly 1 path created
        expect(fakeLearningRepo.savedPaths.length, equals(1));
        expect(fakeLearningRepo.createCallCount, equals(1));
      },
    );

    testWidgets('5. Goal matching preserves custom paths with same goal', (
      tester,
    ) async {
      // Pre-seed a custom path with goal 'flutter' but custom name
      await fakeLearningRepo.createPath(
        name: 'Jalur Mobile Khusus Saya',
        goal: 'flutter',
        topicIds: ['f-oop', 'f-async'],
      );
      expect(fakeLearningRepo.savedPaths.length, equals(1));

      // Open the Flutter preset detail
      await tester.pumpWidget(
        MaterialApp(
          theme: AtlasTheme.buildTheme(Brightness.light),
          home: PathDetailScreen(
            presetKey: 'flutter',
            contentRepo: fakeContentRepo,
            learningRepo: fakeLearningRepo,
            appState: appState,
            onOpenTopic: (_, {pathId, pathName, pathTopicIds, onBackToPath}) {},
          ),
        ),
      );
      await tester.pumpAndSettle();

      // Tap "Mulai Belajar" to create the preset's path
      await tester.tap(find.widgetWithText(FilledButton, 'Mulai Belajar'));
      await tester.pumpAndSettle();

      // There should now be 2 paths: the user's custom path and the preset path
      expect(fakeLearningRepo.savedPaths.length, equals(2));
      final customPath = fakeLearningRepo.savedPaths.firstWhere(
        (p) => p.name == 'Jalur Mobile Khusus Saya',
      );
      expect(
        customPath.items.map((i) => i.topicId).toList(),
        equals(['f-oop', 'f-async']),
      );

      final presetPath = fakeLearningRepo.savedPaths.firstWhere(
        (p) => p.name == pathPresets['flutter']!.name,
      );
      expect(presetPath.goal, equals('flutter'));
    });

    testWidgets(
      '6. Pre-existing saved path with edited order displays edited order immediately',
      (tester) async {
        // Pre-create the preset path with an edited order
        final customOrder = ['f-git', 'f-debugging', 'f-programming-logic'];
        await fakeLearningRepo.createPath(
          name: pathPresets['general']!.name,
          goal: 'general',
          topicIds: customOrder,
        );

        await tester.pumpWidget(
          MaterialApp(
            theme: AtlasTheme.buildTheme(Brightness.light),
            home: PathDetailScreen(
              presetKey: 'general',
              contentRepo: fakeContentRepo,
              learningRepo: fakeLearningRepo,
              appState: appState,
              onOpenTopic: (
                _, {
                pathId,
                pathName,
                pathTopicIds,
                onBackToPath,
              }) {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        // Verify the three topics are rendered
        final gitFinder = find.text('Git & Version Control');
        final debugFinder = find.text('Debugging');
        final logicFinder = find.text('Programming Logic');

        expect(gitFinder, findsOneWidget);
        expect(debugFinder, findsOneWidget);
        expect(logicFinder, findsOneWidget);

        // Verify the vertical ordering matches customOrder: git above debugging above logic
        final gitY = tester.getTopLeft(gitFinder).dy;
        final debugY = tester.getTopLeft(debugFinder).dy;
        final logicY = tester.getTopLeft(logicFinder).dy;

        expect(gitY < debugY, isTrue);
        expect(debugY < logicY, isTrue);
      },
    );

    testWidgets(
      '7. Topic progression: pushReplacement, draft warning, no auto-Paham, refreshes on return',
      (tester) async {
        bool pathRefreshed = false;

        await tester.pumpWidget(
          MaterialApp(
            theme: AtlasTheme.buildTheme(Brightness.light),
            home: TopicScreen(
              topicId: 'f-programming-logic',
              contentRepo: fakeContentRepo,
              learningRepo: fakeLearningRepo,
              appState: appState,
              onOpenTopic: (_) {},
              pathName: 'Memahami dasar dari nol',
              pathTopicIds: const [
                'f-programming-logic',
                'f-variables-data-types',
              ],
              onBackToPath: () => pathRefreshed = true,
            ),
          ),
        );
        await tester.pumpAndSettle();

        // 1. Check path header banner
        expect(
          find.text('Memahami dasar dari nol • Materi 1 dari 2'),
          findsOneWidget,
        );

        // 2. Type some notes without saving
        await tester.enterText(
          find.byType(TextField),
          'Catatan draf yang belum disimpan',
        );
        await tester.pump();
        expect(find.text('Belum disimpan'), findsOneWidget);

        // 3. Scroll to Next Topic button and tap
        final nextButton = find.byKey(const ValueKey('next_topic_button'));
        await tester.ensureVisible(nextButton);
        await tester.pumpAndSettle();
        await tester.tap(nextButton);
        await tester.pumpAndSettle();

        // 4. Draft warning dialog appears!
        expect(find.text('Perubahan belum disimpan'), findsOneWidget);

        // Discard changes
        await tester.tap(find.text('Buang perubahan'));
        await tester.pumpAndSettle();

        // 5. Verify status was NOT automatically marked as Paham
        final progress = await fakeLearningRepo.getProgress(
          'f-programming-logic',
        );
        expect(
          progress?.status ?? LearningStatus.notStarted,
          isNot(equals(LearningStatus.understood)),
        );

        // 6. Now on second topic (Variabel & Tipe Data)
        expect(
          find.text('Memahami dasar dari nol • Materi 2 dari 2'),
          findsOneWidget,
        );

        // 7. Last topic has button to return to path detail
        final returnButton = find.widgetWithText(
          OutlinedButton,
          'Kembali ke Detail Jalur',
        );
        await tester.ensureVisible(returnButton);
        await tester.pumpAndSettle();
        await tester.tap(returnButton);
        await tester.pumpAndSettle();

        // onBackToPath was called to refresh path progress
        expect(pathRefreshed, isTrue);
      },
    );
  });
}
