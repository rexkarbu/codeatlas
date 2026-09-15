// test/home_screen_redesign_test.dart — Widget tests for redesigned HomeScreen:
// 1. New user state with Koda mascot and "Mulai dari Nol" CTA.
// 2. Active user state with Hero "Lanjutkan Belajar" and dynamic "Perkiraan X mnt baca".
// 3. Incomplete data state (progress > 0 but lastReadTopicId == null).
// 4. Unified progress card with sub-layer bars.
// 5. 200% text scale on 360dp width screen without overflow error.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:codeatlas/data/content_repository.dart';
import 'package:codeatlas/data/learning_repository.dart';
import 'package:codeatlas/data/models.dart';
import 'package:codeatlas/features/home/home_screen.dart';
import 'package:codeatlas/state/app_state.dart';

class FakeHomeContentRepo implements ContentRepository {
  final Map<String, Topic> topics;

  FakeHomeContentRepo(this.topics);

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<Topic?> getTopicById(String id) async => topics[id];

  @override
  Future<int> getActiveTopicCount() async => topics.length;

  @override
  Future<int> getActiveTopicCountByLayer(ContentLayer layer) async => topics
      .values
      .where(
        (t) => t.categoryId.startsWith('f-')
            ? layer == ContentLayer.fundamentals
            : layer == ContentLayer.ecosystem,
      )
      .length;

  @override
  Future<List<Topic>> getTopicsByLayer(ContentLayer layer) async => topics
      .values
      .where(
        (t) => t.categoryId.startsWith('f-')
            ? layer == ContentLayer.fundamentals
            : layer == ContentLayer.ecosystem,
      )
      .toList();

  @override
  Future<List<Topic>> getAllActiveTopics() async => topics.values.toList();
}

class FakeHomeLearningRepo implements LearningRepository {
  String? lastReviewedId;
  final Map<String, Progress> progressMap = {};

  FakeHomeLearningRepo({this.lastReviewedId});

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<String?> getLastReviewedTopicId() async => lastReviewedId;

  @override
  Future<Progress?> getProgress(String topicId) async => progressMap[topicId];

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

void main() {
  final sampleTopic = Topic(
    id: 'f-programming-logic',
    categoryId: 'f-logic',
    title: 'Programming Logic',
    level: Difficulty.beginner,
    summary: 'Fondasi instruksi terstruktur.',
    explanationSimple: 'Analogi resep dapur yang sekuensial dan jelas.',
    explanationTechnical:
        'Pemrosesan instruksi berurutan CPU dan alur kontrol.',
    whyVibecodingMatters:
        'Memastikan keluaran AI dieksekusi dengan logika benar.',
    estimatedMinutes: 5,
    sortOrder: 1,
  );

  final sampleTopics = {sampleTopic.id: sampleTopic};

  group('HomeScreen Redesign Widget Tests', () {
    testWidgets(
      'New user state shows Koda greeting and "Mulai dari nol" button',
      (tester) async {
        final fakeContentRepo = FakeHomeContentRepo(sampleTopics);
        final fakeLearningRepo = FakeHomeLearningRepo();
        final appState = AppState(
          contentRepo: fakeContentRepo,
          learningRepo: fakeLearningRepo,
        );
        await appState.refreshCounts();

        String? openedTopic;

        await tester.pumpWidget(
          MaterialApp(
            home: HomeScreen(
              appState: appState,
              contentRepo: fakeContentRepo,
              onNavigateToExplore: () {},
              onNavigateToPaths: () {},
              onOpenTopic: (id) => openedTopic = id,
              onOpenSettings: () {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        // Verify Koda mascot greeting
        expect(find.text('Halo! Kenalkan, aku Koda'), findsOneWidget);
        expect(find.text('Selamat Datang di CodeAtlas'), findsOneWidget);

        // Verify 5 learning paths are present
        expect(find.text('Umum / Dasar dari Nol'), findsOneWidget);
        expect(find.text('Flutter & Mobile'), findsOneWidget);
        expect(find.text('Web Frontend'), findsOneWidget);
        expect(find.text('Backend & Server'), findsOneWidget);
        expect(find.text('Data & Algoritma'), findsOneWidget);

        // Tap "Mulai dari nol"
        await tester.tap(find.text('Mulai dari nol'));
        await tester.pumpAndSettle();

        expect(openedTopic, equals('f-programming-logic'));
      },
    );

    testWidgets(
      'Active user state shows Continue Reading Hero with dynamic reading time',
      (tester) async {
        final fakeContentRepo = FakeHomeContentRepo(sampleTopics);
        final fakeLearningRepo = FakeHomeLearningRepo(
          lastReviewedId: 'f-programming-logic',
        );
        final appState = AppState(
          contentRepo: fakeContentRepo,
          learningRepo: fakeLearningRepo,
        );
        await appState.refreshCounts();

        String? openedTopic;

        await tester.pumpWidget(
          MaterialApp(
            home: HomeScreen(
              appState: appState,
              contentRepo: fakeContentRepo,
              onNavigateToExplore: () {},
              onNavigateToPaths: () {},
              onOpenTopic: (id) => openedTopic = id,
              onOpenSettings: () {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        // Verify Continue reading hero
        expect(find.text('Lanjutkan membaca'), findsOneWidget);
        expect(find.text('Programming Logic'), findsOneWidget);
        expect(find.textContaining('Perkiraan'), findsOneWidget);
        expect(find.textContaining('mnt baca'), findsOneWidget);

        // Tap Lanjut Membaca
        await tester.tap(find.text('Lanjut Membaca'));
        await tester.pumpAndSettle();

        expect(openedTopic, equals('f-programming-logic'));
      },
    );

    testWidgets(
      'Incomplete data state (progress > 0 but lastReadTopicId == null) shows Resume card',
      (tester) async {
        final fakeContentRepo = FakeHomeContentRepo(sampleTopics);
        final fakeLearningRepo = FakeHomeLearningRepo();
        fakeLearningRepo.progressMap['f-programming-logic'] = Progress(
          topicId: 'f-programming-logic',
          status: LearningStatus.understood,
          notes: '',
          updatedAt: DateTime.now(),
        );

        final appState = AppState(
          contentRepo: fakeContentRepo,
          learningRepo: fakeLearningRepo,
        );
        await appState.refreshCounts();

        bool pathsOpened = false;

        await tester.pumpWidget(
          MaterialApp(
            home: HomeScreen(
              appState: appState,
              contentRepo: fakeContentRepo,
              onNavigateToExplore: () {},
              onNavigateToPaths: () => pathsOpened = true,
              onOpenTopic: (_) {},
              onOpenSettings: () {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        // Verify Resume progress card is displayed
        expect(find.text('Lanjutkan Perjalanan Belajar'), findsOneWidget);

        // Tap Buka Jalur Belajar
        await tester.tap(find.text('Buka Jalur Belajar'));
        await tester.pumpAndSettle();

        expect(pathsOpened, isTrue);
      },
    );

    testWidgets(
      'Unified progress card displays overall % and both sub-layer bars',
      (tester) async {
        final fakeContentRepo = FakeHomeContentRepo(sampleTopics);
        final fakeLearningRepo = FakeHomeLearningRepo();
        fakeLearningRepo.progressMap['f-programming-logic'] = Progress(
          topicId: 'f-programming-logic',
          status: LearningStatus.understood,
          notes: '',
          updatedAt: DateTime.now(),
        );

        final appState = AppState(
          contentRepo: fakeContentRepo,
          learningRepo: fakeLearningRepo,
        );
        await appState.refreshCounts();

        await tester.pumpWidget(
          MaterialApp(
            home: HomeScreen(
              appState: appState,
              contentRepo: fakeContentRepo,
              onNavigateToExplore: () {},
              onNavigateToPaths: () {},
              onOpenTopic: (_) {},
              onOpenSettings: () {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        expect(find.text('Progress Keseluruhan'), findsOneWidget);
        expect(find.text('Fundamental Programming'), findsOneWidget);
        expect(find.text('Dunia & Ekosistem Coding'), findsOneWidget);
        expect(find.textContaining('Paham: 1'), findsOneWidget);
      },
    );

    testWidgets(
      'HomeScreen renders at 200% text scale on 360dp width without overflow',
      (tester) async {
        final binding = TestWidgetsFlutterBinding.ensureInitialized();
        binding.platformDispatcher.textScaleFactorTestValue = 2.0;
        addTearDown(
          () => binding.platformDispatcher.clearTextScaleFactorTestValue(),
        );

        final fakeContentRepo = FakeHomeContentRepo(sampleTopics);
        final fakeLearningRepo = FakeHomeLearningRepo(
          lastReviewedId: 'f-programming-logic',
        );
        final appState = AppState(
          contentRepo: fakeContentRepo,
          learningRepo: fakeLearningRepo,
        );
        await appState.refreshCounts();

        tester.view.physicalSize = const Size(360 * 3, 640 * 3);
        tester.view.devicePixelRatio = 3.0;
        addTearDown(() => tester.view.resetPhysicalSize());

        await tester.pumpWidget(
          MaterialApp(
            home: HomeScreen(
              appState: appState,
              contentRepo: fakeContentRepo,
              onNavigateToExplore: () {},
              onNavigateToPaths: () {},
              onOpenTopic: (_) {},
              onOpenSettings: () {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        final exception = tester.takeException();
        if (exception is FlutterError) {
          // ignore: avoid_print
          print(
            'EXCEPTION DIAGNOSTICS: ${exception.diagnostics.map((d) => d.toString()).join("\n")}',
          );
        }
        expect(exception, isNull);
      },
    );
  });
}
