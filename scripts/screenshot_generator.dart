import 'dart:io';
import 'dart:ui' as ui;
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:codeatlas/data/content_repository.dart';
import 'package:codeatlas/data/learning_repository.dart';
import 'package:codeatlas/data/models.dart';
import 'package:codeatlas/features/roadmap/roadmap_screen.dart';
import 'package:codeatlas/features/topic/topic_screen.dart';
import 'package:codeatlas/state/app_state.dart';

class FakeRoadmapContentRepo implements ContentRepository {
  final List<Category> categories;
  final List<Topic> topics;
  final Map<String, List<String>> prereqs;

  FakeRoadmapContentRepo({
    required this.categories,
    required this.topics,
    required this.prereqs,
  });

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<List<Category>> getAllCategories() async => categories;

  @override
  Future<List<Topic>> getAllActiveTopics() async => topics;

  @override
  Future<Map<String, List<String>>> getPrerequisiteGraph() async => prereqs;

  @override
  Future<Topic?> getTopicById(String id) async {
    try {
      return topics.firstWhere((t) => t.id == id);
    } catch (_) {
      return null;
    }
  }

  @override
  Future<List<String>> getDependentTopicIds(String id) async => [];
}

class FakeRoadmapLearningRepo implements LearningRepository {
  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<Map<String, Progress>> getAllProgress() async => {
        'f-programming-logic': Progress(
          topicId: 'f-programming-logic',
          status: LearningStatus.understood,
          notes: 'Catatan penting.',
          updatedAt: DateTime.now(),
        ),
      };

  @override
  Future<Progress?> getProgress(String id) async => null;

  @override
  Future<void> updateNotes(String id, String text) async {}

  @override
  Future<void> updateStatus(String id, LearningStatus s) async {}

  @override
  Future<void> recordReview(String id) async {}
}

Future<void> saveScreenshot(WidgetTester tester, GlobalKey key, String filename) async {
  await tester.runAsync(() async {
    final boundary = key.currentContext?.findRenderObject() as RenderRepaintBoundary?;
    if (boundary != null) {
      final image = await boundary.toImage(pixelRatio: 2.0);
      final byteData = await image.toByteData(format: ui.ImageByteFormat.png);
      if (byteData != null) {
        final file = File('d:/project/ca/hasil/$filename');
        file.writeAsBytesSync(byteData.buffer.asUint8List());
        print('Saved screenshot: ${file.path} (${file.lengthSync()} bytes)');
      }
    }
  });
}

void main() {
  testWidgets('Generate UI screenshots for review', (tester) async {
    tester.view.physicalSize = const Size(800, 1600);
    tester.view.devicePixelRatio = 2.0;

    final categories = [
      const Category(
        id: 'f-logic',
        layer: ContentLayer.fundamentals,
        kind: CategoryKind.group,
        title: 'Logika & Alur Kontrol',
        description: 'Dasar penalaran komputasi dan instruksi berurutan',
        sortOrder: 1,
      ),
      const Category(
        id: 'f-data-structures',
        layer: ContentLayer.fundamentals,
        kind: CategoryKind.group,
        title: 'Struktur Data & Algoritma',
        description: 'Penyimpanan terorganisir dan pemrosesan efisien',
        sortOrder: 2,
      ),
    ];

    final topics = [
      const Topic(
        id: 'f-programming-logic',
        categoryId: 'f-logic',
        title: 'Programming Logic',
        level: Difficulty.beginner,
        summary: 'Menyusun langkah berurutan yang logis.',
        explanationSimple: 'Analogi toples dapur berlabel.',
        problemContext: 'Memori biner mentah tanpa makna.',
        explanationTechnical: 'Penalaran sekuensial dan algoritma.',
        whyVibecodingMatters: 'Verifikasi urutan eksekusi kode AI.',
        whenToUse: 'Terapkan pada setiap modul program.',
        codeExamples: [],
        prerequisiteIds: [],
        relatedTopicIds: ['f-variables-data-types'],
        misconceptions: [
          TopicMisconception(
            misconception: 'Komputer paham maksud programmer',
            explanation: 'Komputer hanya mengeksekusi instruksi',
            spotInCode: 'Urutan terbalik',
          ),
        ],
        reflectionQuestions: [
          TopicReflection(
            question: 'Apa itu logic error?',
            answer: 'Kesalahan urutan atau perhitungan yang tidak memicu syntax error.',
          ),
        ],
        keywords: ['logic', 'sequence'],
        estimatedMinutes: 10,
        sortOrder: 1,
      ),
      const Topic(
        id: 'f-variables-data-types',
        categoryId: 'f-logic',
        title: 'Variables & Data Types',
        level: Difficulty.beginner,
        summary: 'Memberi nama simbolik pada data.',
        explanationSimple: 'Analogi toples kaca berlabel.',
        problemContext: 'Memori komputer hanya angka biner.',
        explanationTechnical: 'Binding simbolik ke alamat memori.',
        whyVibecodingMatters: 'Mencegah konversi implisit salah.',
        whenToUse: 'Definisikan tipe statis untuk integritas data.',
        codeExamples: [],
        prerequisiteIds: ['f-programming-logic'],
        relatedTopicIds: ['f-programming-logic'],
        misconceptions: [
          TopicMisconception(
            misconception: '== sama di semua bahasa',
            explanation: 'Perilaku == berbeda antar bahasa',
            spotInCode: 'obj1 == obj2 di JS',
          ),
        ],
        reflectionQuestions: [
          TopicReflection(
            question: 'Mengapa primitif tidak selalu di stack?',
            answer: 'Di Python semua adalah objek heap, di Dart field kelas ada di heap.',
          ),
        ],
        keywords: ['variables', 'types'],
        estimatedMinutes: 15,
        sortOrder: 2,
      ),
    ];

    final contentRepo = FakeRoadmapContentRepo(
      categories: categories,
      topics: topics,
      prereqs: {
        'f-variables-data-types': ['f-programming-logic'],
      },
    );
    final learningRepo = FakeRoadmapLearningRepo();
    final appState = AppState(contentRepo: contentRepo, learningRepo: learningRepo);

    final keyRoadmap = GlobalKey();

    // Screen 1: Roadmap Level 1
    await tester.pumpWidget(
      MaterialApp(
        theme: ThemeData(useMaterial3: true, colorSchemeSeed: Colors.indigo),
        home: Scaffold(
          body: RepaintBoundary(
            key: keyRoadmap,
            child: RoadmapScreen(
              contentRepo: contentRepo,
              learningRepo: learningRepo,
              onOpenTopic: (_) {},
            ),
          ),
        ),
      ),
    );
    await tester.pumpAndSettle();
    await saveScreenshot(tester, keyRoadmap, '01_roadmap_level1_overview.png');

    // Screen 2: Tap group card to open Level 2 (Vertical topics)
    await tester.tap(find.text('Logika & Alur Kontrol'));
    await tester.pumpAndSettle();
    await saveScreenshot(tester, keyRoadmap, '02_roadmap_level2_vertical_topics.png');

    // Screen 3: Tap topic to open Level 3 (Focus panel)
    await tester.tap(find.text('Variables & Data Types'));
    await tester.pumpAndSettle();
    await saveScreenshot(tester, keyRoadmap, '03_roadmap_level3_focus_panel.png');

    // Screen 4: TopicScreen
    final keyTopic = GlobalKey();
    await tester.pumpWidget(
      MaterialApp(
        theme: ThemeData(useMaterial3: true, colorSchemeSeed: Colors.indigo),
        home: Scaffold(
          body: RepaintBoundary(
            key: keyTopic,
            child: TopicScreen(
              topicId: 'f-variables-data-types',
              contentRepo: contentRepo,
              learningRepo: learningRepo,
              appState: appState,
              onOpenTopic: (_) {},
            ),
          ),
        ),
      ),
    );
    await tester.pumpAndSettle();
    await saveScreenshot(tester, keyTopic, '04_topic_article_8_sections.png');

    // Screen 5: Tap Table of Contents FAB to open modal
    await tester.tap(find.byKey(const ValueKey('toc_button')));
    await tester.pumpAndSettle();
    await saveScreenshot(tester, keyTopic, '05_topic_table_of_contents_modal.png');
  });
}
