// scripts/capture_v5_deliverables.dart — Generates deliverable screenshots:
// 1. Programming Logic article with new text, distinct walkthrough, no FAB
// 2. Table of Contents bottom sheet opened from AppBar
// 3. Syntax comparison with single concept picker & vertical stack
// 4. Syntax comparison concept picker bottom sheet
// 5. Syntax comparison at 360px width & 200% text scale (zero overflow)
// 6. Roadmap overview

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
import 'package:codeatlas/features/practice/comparison_screen.dart';
import 'package:codeatlas/features/roadmap/roadmap_screen.dart';
import 'package:codeatlas/features/topic/topic_screen.dart';
import 'package:codeatlas/state/app_state.dart';

class ProductionMockContentRepo implements ContentRepository {
  final List<Category> categories;
  final List<Topic> topics;
  final List<ComparisonGroup> comparisonGroups;
  final Set<String> comparisonLanguages;
  final Map<String, List<String>> prereqs;

  ProductionMockContentRepo({
    required this.categories,
    required this.topics,
    required this.comparisonGroups,
    required this.comparisonLanguages,
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

  @override
  Future<List<ComparisonGroup>> getComparisonGroups() async => comparisonGroups;

  @override
  Future<Set<String>> getComparisonLanguages() async => comparisonLanguages;
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
  Future<void> recordReview(String id) async {}

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
        final bytes = byteData.buffer.asUint8List();

        // 1. Save to d:/project/ca/hasil/
        final hasilDir = Directory('d:/project/ca/hasil');
        if (!hasilDir.existsSync()) hasilDir.createSync(recursive: true);
        final file = File('d:/project/ca/hasil/$filename');
        file.writeAsBytesSync(bytes);
        print('Saved to hasil: ${file.path} (${bytes.length} bytes)');

        // 2. Copy to brain artifact directory for display
        final artifactPath =
            'C:/Users/Dimdim/.gemini/antigravity-ide/brain/46ec7035-1b4f-4791-9793-da903bdf6cc0/$filename';
        File(artifactPath).writeAsBytesSync(bytes);
        print('Saved to artifact: $artifactPath');
      }
    }
  });
}

Widget buildAppWrapper({
  required Widget child,
  required GlobalKey boundaryKey,
  required double width,
  required double height,
  double textScale = 1.0,
}) {
  return MaterialApp(
    debugShowCheckedModeBanner: false,
    theme: ThemeData(
      fontFamily: 'Roboto',
      useMaterial3: true,
      colorSchemeSeed: Colors.indigo,
    ),
    builder: (context, materialChild) {
      return MediaQuery(
        data: MediaQueryData(
          size: Size(width, height),
          devicePixelRatio: 2.0,
          textScaler: TextScaler.linear(textScale),
        ),
        child: RepaintBoundary(
          key: boundaryKey,
          child: materialChild!,
        ),
      );
    },
    home: child,
  );
}

void main() {
  late ProductionMockContentRepo contentRepo;
  late ProductionMockLearningRepo learningRepo;
  late AppState appState;

  setUpAll(() async {
    // Load Segoe UI (Regular only as Roboto, avoiding font bold overwrite)
    final segoeBytes =
        await File(r'C:\Windows\Fonts\segoeui.ttf').readAsBytes();
    final robotoLoader = FontLoader('Roboto');
    robotoLoader.addFont(Future.value(ByteData.view(segoeBytes.buffer)));
    await robotoLoader.load();

    // Load MaterialIcons
    final iconFile = File(
      r'D:\development\flutter\flutter\bin\cache\artifacts\material_fonts\materialicons-regular.otf',
    );
    if (iconFile.existsSync()) {
      final iconBytes = await iconFile.readAsBytes();
      final iconLoader = FontLoader('MaterialIcons');
      iconLoader.addFont(Future.value(ByteData.view(iconBytes.buffer)));
      await iconLoader.load();
    }

    // Load production content.json
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

    // Comparison groups
    final compMap = <String, List<CodeExample>>{};
    for (final t in topics) {
      for (final ex in t.codeExamples) {
        if (ex.comparisonKey != null) {
          compMap.putIfAbsent(ex.comparisonKey!, () => []).add(ex);
        }
      }
    }

    final comparisonGroups = <ComparisonGroup>[];
    final comparisonLanguages = <String>{};
    for (final entry in compMap.entries) {
      final topic = topics.firstWhere(
        (t) => t.codeExamples.any((e) => e.comparisonKey == entry.key),
      );
      comparisonGroups.add(
        ComparisonGroup(
          comparisonKey: entry.key,
          topicId: topic.id,
          topicTitle: topic.title,
          examples: entry.value,
        ),
      );
      for (final ex in entry.value) {
        comparisonLanguages.add(ex.language);
      }
    }

    contentRepo = ProductionMockContentRepo(
      categories: categories,
      topics: topics,
      comparisonGroups: comparisonGroups,
      comparisonLanguages: comparisonLanguages,
      prereqs: prereqs,
    );

    learningRepo = ProductionMockLearningRepo({
      'f-programming-logic': Progress(
        topicId: 'f-programming-logic',
        status: LearningStatus.understood,
        notes: 'Catatan penting urutan instruksi.',
        updatedAt: DateTime.now(),
      ),
      'f-variables-data-types': Progress(
        topicId: 'f-variables-data-types',
        status: LearningStatus.inProgress,
        notes: 'Membaca konsep tipe data.',
        updatedAt: DateTime.now(),
      ),
    });

    appState = AppState(
      contentRepo: contentRepo,
      learningRepo: learningRepo,
    );
  });

  testWidgets('Capture 1: Programming Logic Article', (tester) async {
    final boundaryKey = GlobalKey();
    tester.view.physicalSize = const Size(400 * 2.0, 850 * 2.0);
    tester.view.devicePixelRatio = 2.0;

    await tester.pumpWidget(
      buildAppWrapper(
        child: TopicScreen(
          topicId: 'f-programming-logic',
          contentRepo: contentRepo,
          learningRepo: learningRepo,
          appState: appState,
          onOpenTopic: (_) {},
        ),
        boundaryKey: boundaryKey,
        width: 400,
        height: 850,
      ),
    );
    await tester.pumpAndSettle();

    await saveRepaintBoundary(
      tester,
      boundaryKey,
      '01_programming_logic_article.png',
    );
  });

  testWidgets('Capture 2: Table of Contents Modal', (tester) async {
    final boundaryKey = GlobalKey();
    tester.view.physicalSize = const Size(400 * 2.0, 850 * 2.0);
    tester.view.devicePixelRatio = 2.0;

    await tester.pumpWidget(
      buildAppWrapper(
        child: TopicScreen(
          topicId: 'f-programming-logic',
          contentRepo: contentRepo,
          learningRepo: learningRepo,
          appState: appState,
          onOpenTopic: (_) {},
        ),
        boundaryKey: boundaryKey,
        width: 400,
        height: 850,
      ),
    );
    await tester.pumpAndSettle();

    // Tap Daftar Isi button on AppBar
    final tocFinder = find.byKey(const ValueKey('toc_button'));
    expect(tocFinder, findsOneWidget);
    await tester.tap(tocFinder);
    await tester.pumpAndSettle();

    await saveRepaintBoundary(
      tester,
      boundaryKey,
      '02_programming_logic_toc_modal.png',
    );
  });

  testWidgets('Capture 3: Syntax Comparison Vertical Stack', (tester) async {
    final boundaryKey = GlobalKey();
    tester.view.physicalSize = const Size(400 * 2.0, 900 * 2.0);
    tester.view.devicePixelRatio = 2.0;

    await tester.pumpWidget(
      buildAppWrapper(
        child: ComparisonScreen(
          contentRepo: contentRepo,
          onOpenTopic: (_) {},
        ),
        boundaryKey: boundaryKey,
        width: 400,
        height: 900,
      ),
    );
    await tester.pumpAndSettle();

    await saveRepaintBoundary(
      tester,
      boundaryKey,
      '03_comparison_vertical_stack.png',
    );
  });

  testWidgets('Capture 4: Syntax Comparison Concept Picker Modal', (
    tester,
  ) async {
    final boundaryKey = GlobalKey();
    tester.view.physicalSize = const Size(400 * 2.0, 900 * 2.0);
    tester.view.devicePixelRatio = 2.0;

    await tester.pumpWidget(
      buildAppWrapper(
        child: ComparisonScreen(
          contentRepo: contentRepo,
          onOpenTopic: (_) {},
        ),
        boundaryKey: boundaryKey,
        width: 400,
        height: 900,
      ),
    );
    await tester.pumpAndSettle();

    // Tap concept selector button
    final pickerBtn = find.byKey(const ValueKey('concept_selector_button'));
    expect(pickerBtn, findsOneWidget);
    await tester.tap(pickerBtn);
    await tester.pumpAndSettle();

    await saveRepaintBoundary(
      tester,
      boundaryKey,
      '04_comparison_concept_picker_modal.png',
    );
  });

  testWidgets('Capture 5: Syntax Comparison 360px Width Scale 200%', (
    tester,
  ) async {
    final boundaryKey = GlobalKey();
    tester.view.physicalSize = const Size(360 * 2.0, 900 * 2.0);
    tester.view.devicePixelRatio = 2.0;

    await tester.pumpWidget(
      buildAppWrapper(
        child: ComparisonScreen(
          contentRepo: contentRepo,
          onOpenTopic: (_) {},
        ),
        boundaryKey: boundaryKey,
        width: 360,
        height: 900,
        textScale: 2.0,
      ),
    );
    await tester.pumpAndSettle();

    expect(tester.takeException(), isNull);

    await saveRepaintBoundary(
      tester,
      boundaryKey,
      '05_comparison_360_scale200.png',
    );
  });

  testWidgets('Capture 6: Progressive Roadmap Screen', (tester) async {
    final boundaryKey = GlobalKey();
    tester.view.physicalSize = const Size(400 * 2.0, 850 * 2.0);
    tester.view.devicePixelRatio = 2.0;

    await tester.pumpWidget(
      buildAppWrapper(
        child: RoadmapScreen(
          contentRepo: contentRepo,
          learningRepo: learningRepo,
          onOpenTopic: (_) {},
        ),
        boundaryKey: boundaryKey,
        width: 400,
        height: 850,
      ),
    );
    await tester.pumpAndSettle();

    await saveRepaintBoundary(
      tester,
      boundaryKey,
      '06_roadmap_level1_groups.png',
    );
  });
}
