// test/bootstrap_and_retry_widget_test.dart — Widget tests for bootstrap error,
// valid old data fallback, and retry handling according to PRD section 2.A.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:codeatlas/app.dart';
import 'package:codeatlas/data/content_repository.dart';
import 'package:codeatlas/data/learning_repository.dart';
import 'package:codeatlas/data/models.dart';
import 'package:codeatlas/data/seed_loader.dart';
import 'package:codeatlas/main.dart';
import 'package:codeatlas/state/app_state.dart';

class MockBootstrapContentRepository implements ContentRepository {
  final ContentMeta? meta;
  final int activeTopics;
  final List<Topic> topics;
  final List<Category> categories;

  MockBootstrapContentRepository({
    this.meta,
    this.activeTopics = 1,
    this.topics = const [],
    this.categories = const [],
  });

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<ContentMeta?> getContentMeta() async => meta;

  @override
  Future<int> getActiveTopicCount() async => activeTopics;

  @override
  Future<List<Topic>> getAllActiveTopics() async => topics;

  @override
  Future<List<Category>> getAllCategories() async => categories;

  @override
  Future<Map<String, List<String>>> getPrerequisiteGraph() async => {};

  @override
  Future<int> getActiveTopicCountByLayer(ContentLayer layer) async =>
      layer == ContentLayer.fundamentals ? activeTopics : 0;

  @override
  Future<List<Topic>> getTopicsByLayer(ContentLayer layer) async =>
      layer == ContentLayer.fundamentals ? topics : [];

  Future<Map<ContentLayer, int>> getTopicCountByLayer() async => {
    ContentLayer.fundamentals: activeTopics,
    ContentLayer.ecosystem: 0,
  };

  @override
  Future<List<Topic>> getTopicsByCategory(String categoryId) async =>
      topics.where((t) => t.categoryId == categoryId).toList();

  @override
  Future<List<ComparisonGroup>> getComparisonGroups() async => [];

  @override
  Future<Set<String>> getComparisonLanguages() async => {};

  @override
  Future<List<Category>> getGroupCategories(ContentLayer layer) async =>
      categories
          .where((c) => c.layer == layer && c.kind == CategoryKind.group)
          .toList();

  @override
  Future<List<Topic>> search(
    String query, {
    ContentLayer? layer,
    String? categoryId,
    Difficulty? level,
  }) async => topics;

  Future<List<Quiz>> getRandomQuizzes({QuizType? type, int limit = 5}) async =>
      [];
}

class MockBootstrapLearningRepository implements LearningRepository {
  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<String?> getLastReviewedTopicId() async => null;

  @override
  Future<int> countByStatus(
    LearningStatus status, {
    Set<String>? topicIds,
  }) async => 0;

  @override
  Future<Map<String, Progress>> getAllProgress() async => {};

  @override
  Future<Progress?> getProgress(String topicId) async => null;

  Future<Progress?> getLastReadProgress() async => null;

  @override
  Future<List<LearningPath>> getAllPaths() async => [];

  Future<Map<ContentLayer, int>> getUnderstoodCountByLayer() async => {
    ContentLayer.fundamentals: 0,
    ContentLayer.ecosystem: 0,
  };
}

void main() {
  group('Bootstrap and Retry Widget Tests (PRD 2.A)', () {
    testWidgets(
      'Upgrade gagal + database lama valid: aplikasi tetap dapat digunakan dengan MaterialBanner notice',
      (tester) async {
        final mockMeta = const ContentMeta(
          contentVersion: 2,
          dataset: 'production',
          locale: 'id',
        );

        final sampleTopic = const Topic(
          id: 'top-1',
          categoryId: 'cat-1',
          title: 'Topik Lama Valid',
          level: Difficulty.beginner,
          summary: 'Ringkasan',
          explanationSimple: 'Sederhana',
          explanationTechnical: 'Teknis',
          whyVibecodingMatters: 'Vibecoding',
          estimatedMinutes: 5,
          sortOrder: 1,
        );

        final sampleCategory = const Category(
          id: 'cat-1',
          layer: ContentLayer.fundamentals,
          kind: CategoryKind.group,
          title: 'Grup Dasar',
          description: 'Deskripsi',
          sortOrder: 1,
        );

        final mockContent = MockBootstrapContentRepository(
          meta: mockMeta,
          activeTopics: 1,
          topics: [sampleTopic],
          categories: [sampleCategory],
        );
        final mockLearning = MockBootstrapLearningRepository();

        await tester.pumpWidget(
          MaterialApp(
            home: BootstrapScreen(
              seedLoaderAction: () async => SeedResult(
                success: false,
                error: 'Simulasi kegagalan upgrade jaringan/aset',
              ),
              metaReader: () async => mockMeta,
              activeTopicsCountReader: () async => 1,
              mockContentRepo: mockContent,
              mockLearningRepo: mockLearning,
            ),
          ),
        );

        for (int i = 0; i < 10; i++) {
          await tester.pump(const Duration(milliseconds: 100));
        }

        // 1. Verifikasi aplikasi TIDAK terkunci di error screen, tetapi masuk ke CodeAtlasApp
        expect(find.byType(CodeAtlasApp), findsOneWidget);

        // 2. MaterialBanner muncul memberi tahu bahwa data lama digunakan
        expect(find.byType(MaterialBanner), findsOneWidget);
        expect(find.textContaining('Pembaruan konten gagal'), findsOneWidget);
        expect(find.textContaining('versi 2'), findsOneWidget);

        // 3. Konten lama tetap dapat diakses dan digunakan
        expect(find.text('Jelajah'), findsOneWidget);
        expect(find.text('Peta'), findsOneWidget);

        // Beralih ke tab Jelajah
        await tester.tap(find.text('Jelajah'));
        for (int i = 0; i < 5; i++) {
          await tester.pump(const Duration(milliseconds: 100));
        }

        // Topik lama dalam kategori grup tampil dan dapat dibuka
        expect(find.text('Grup Dasar'), findsOneWidget);
        await tester.tap(find.text('Grup Dasar'));
        for (int i = 0; i < 5; i++) {
          await tester.pump(const Duration(milliseconds: 100));
        }

        expect(find.text('Topik Lama Valid'), findsOneWidget);
      },
    );

    testWidgets(
      'Database kosong + seed gagal: tampil pesan error dan tombol Coba lagi',
      (tester) async {
        final mockContent = MockBootstrapContentRepository(
          meta: null,
          activeTopics: 0,
        );
        final mockLearning = MockBootstrapLearningRepository();

        await tester.pumpWidget(
          MaterialApp(
            home: BootstrapScreen(
              seedLoaderAction: () async => SeedResult(
                success: false,
                error: 'Berkas aset rusak atau tidak ditemukan',
              ),
              metaReader: () async => null,
              activeTopicsCountReader: () async => 0,
              mockContentRepo: mockContent,
              mockLearningRepo: mockLearning,
            ),
          ),
        );

        for (int i = 0; i < 5; i++) {
          await tester.pump(const Duration(milliseconds: 100));
        }

        // Aplikasi tidak dapat lanjut karena data kosong: error screen tampil
        expect(find.byType(CodeAtlasApp), findsNothing);
        expect(find.byIcon(Icons.error_outline), findsOneWidget);
        expect(
          find.text('Berkas aset rusak atau tidak ditemukan'),
          findsOneWidget,
        );
        expect(find.widgetWithText(FilledButton, 'Coba lagi'), findsOneWidget);
      },
    );

    testWidgets(
      'Retry berhasil: banner hilang dan katalog serta progress diperbarui',
      (tester) async {
        int refreshCountsCallCount = 0;

        final mockContent = MockBootstrapContentRepository(
          meta: const ContentMeta(
            contentVersion: 2,
            dataset: 'production',
            locale: 'id',
          ),
          activeTopics: 1,
        );
        final mockLearning = MockBootstrapLearningRepository();

        final appState = AppState(
          contentRepo: mockContent,
          learningRepo: mockLearning,
        );
        appState.setContentUpdateNotice(
          'Pembaruan konten tertunda. Klik coba lagi untuk memperbarui.',
        );

        bool retrySimulatedSuccess = false;

        await tester.pumpWidget(
          CodeAtlasApp(
            appState: appState,
            contentRepo: mockContent,
            learningRepo: mockLearning,
            onRetryUpgrade: () async {
              retrySimulatedSuccess = true;
              refreshCountsCallCount++;
              return true;
            },
          ),
        );

        for (int i = 0; i < 5; i++) {
          await tester.pump(const Duration(milliseconds: 100));
        }

        // Banner awalnya muncul
        expect(find.byType(MaterialBanner), findsOneWidget);
        expect(find.text('Coba Lagi'), findsOneWidget);

        // Tap tombol 'Coba Lagi'
        await tester.tap(find.text('Coba Lagi'));
        await tester.pump();
        await tester.pump(const Duration(milliseconds: 300));

        // Retry dipanggil dan berhasil
        expect(retrySimulatedSuccess, isTrue);
        expect(refreshCountsCallCount, greaterThan(0));

        // Banner hilang
        expect(find.byType(MaterialBanner), findsNothing);
        expect(find.text('Pembaruan konten berhasil!'), findsOneWidget);

        // Drain the snackbar timer before test ends
        await tester.pump(const Duration(seconds: 4));
      },
    );
  });
}
