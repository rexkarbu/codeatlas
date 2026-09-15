// test/render_snapshots_test.dart — Render and export actual Flutter UI screenshots
// for Beranda and TopicScreen across Light, Dark, 100%, and 200% text scale on 360dp width.
// Uses real production content dataset (47 Fundamental, 52 Ecosystem, 99 Total)
// and loads offline MaterialIcons + Segoe UI fonts.

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
import 'package:codeatlas/features/home/home_screen.dart';
import 'package:codeatlas/features/learning_paths/path_detail_screen.dart';
import 'package:codeatlas/features/topic/topic_screen.dart';
import 'package:codeatlas/state/app_state.dart';
import 'package:codeatlas/theme/atlas_theme.dart';
import 'package:codeatlas/widgets/codeatlas_logo.dart';

class SnapshotContentRepo implements ContentRepository {
  final List<Topic> allTopics;
  final Map<String, Topic> topicMap;

  SnapshotContentRepo(this.allTopics)
    : topicMap = {for (final t in allTopics) t.id: t};

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<Topic?> getTopicById(String id) async => topicMap[id];

  @override
  Future<int> getActiveTopicCount() async => allTopics.length;

  @override
  Future<int> getActiveTopicCountByLayer(ContentLayer layer) async {
    final prefix = layer == ContentLayer.fundamentals ? 'f-' : 'e-';
    return allTopics.where((t) => t.categoryId.startsWith(prefix)).length;
  }

  @override
  Future<List<Topic>> getTopicsByLayer(ContentLayer layer) async {
    final prefix = layer == ContentLayer.fundamentals ? 'f-' : 'e-';
    return allTopics.where((t) => t.categoryId.startsWith(prefix)).toList();
  }

  @override
  Future<List<Topic>> getAllActiveTopics() async => allTopics;

  @override
  Future<List<String>> getDependentTopicIds(String topicId) async => [];

  @override
  Future<Set<String>> getTransitivePrerequisites(String topicId) async => {};

  @override
  Future<Map<String, List<String>>> getPrerequisiteGraph() async => {};
}

class SnapshotLearningRepo implements LearningRepository {
  final Set<String> understoodTopics;
  final Set<String> inProgressTopics;

  SnapshotLearningRepo({
    required this.understoodTopics,
    required this.inProgressTopics,
  });

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<String?> getLastReviewedTopicId() async => 'f-programming-logic';

  @override
  Future<Progress?> getProgress(String topicId) async => Progress(
    topicId: topicId,
    status: understoodTopics.contains(topicId)
        ? LearningStatus.understood
        : inProgressTopics.contains(topicId)
        ? LearningStatus.inProgress
        : LearningStatus.notStarted,
    notes: topicId == 'f-programming-logic'
        ? 'Catatan pribadi: 3 fondasi logika (sekuensial, percabangan, perulangan) harus dipahami sebelum membuat loop bertingkat.'
        : '',
    updatedAt: DateTime.now(),
  );

  @override
  Future<void> recordReview(String topicId) async {}

  @override
  Future<void> updateStatus(String topicId, LearningStatus status) async {}

  @override
  Future<void> updateNotes(String topicId, String notes) async {}

  @override
  Future<Map<String, Progress>> getAllProgress() async {
    final map = <String, Progress>{};
    for (final id in understoodTopics) {
      map[id] = Progress(
        topicId: id,
        status: LearningStatus.understood,
        notes: '',
        updatedAt: DateTime.now(),
      );
    }
    for (final id in inProgressTopics) {
      map[id] = Progress(
        topicId: id,
        status: LearningStatus.inProgress,
        notes: '',
        updatedAt: DateTime.now(),
      );
    }
    return map;
  }

  @override
  Future<List<LearningPath>> getAllPaths() async => [];

  @override
  Future<LearningPath?> getPath(int pathId) async => null;

  @override
  Future<int> createPath({
    required String name,
    required String goal,
    required List<String> topicIds,
  }) async => 1;

  @override
  Future<int> countByStatus(
    LearningStatus status, {
    Set<String>? topicIds,
  }) async {
    if (status == LearningStatus.understood) {
      if (topicIds == null) return understoodTopics.length;
      return understoodTopics.intersection(topicIds).length;
    }
    if (status == LearningStatus.inProgress) {
      if (topicIds == null) return inProgressTopics.length;
      return inProgressTopics.intersection(topicIds).length;
    }
    return 0;
  }
}

File _resolveContentJson() {
  const candidates = [
    'assets/content/content.json',
    'codeatlas/assets/content/content.json',
    '../assets/content/content.json',
  ];
  for (final c in candidates) {
    final f = File(c);
    if (f.existsSync()) return f;
  }
  return File('assets/content/content.json');
}

Directory _resolveSnapshotDir() {
  const artifactDirPath =
      'C:/Users/Dimdim/.gemini/antigravity-ide/brain/46ec7035-1b4f-4791-9793-da903bdf6cc0';
  final primaryDir = Directory(artifactDirPath);
  if (primaryDir.existsSync()) {
    return primaryDir;
  }
  // Cross-platform fallback for GitHub Actions Ubuntu or another environment
  final fallbackDir = Directory('build/test_snapshots');
  if (!fallbackDir.existsSync()) {
    fallbackDir.createSync(recursive: true);
  }
  return fallbackDir;
}

File? _findMaterialIconsFont() {
  // 1. Check FLUTTER_ROOT environment variable (commonly set on CI / local setups)
  final flutterRoot = Platform.environment['FLUTTER_ROOT'];
  if (flutterRoot != null && flutterRoot.isNotEmpty) {
    final candidate = File(
      '$flutterRoot/bin/cache/artifacts/material_fonts/MaterialIcons-Regular.otf',
    );
    if (candidate.existsSync()) return candidate;
  }

  // 2. Discover by traversing upwards from the active Dart VM executable
  try {
    var dir = File(Platform.resolvedExecutable).parent;
    for (int i = 0; i < 7; i++) {
      final c1 = File(
        '${dir.path}/bin/cache/artifacts/material_fonts/MaterialIcons-Regular.otf',
      );
      if (c1.existsSync()) return c1;
      final c2 = File(
        '${dir.path}/cache/artifacts/material_fonts/MaterialIcons-Regular.otf',
      );
      if (c2.existsSync()) return c2;
      if (dir.parent.path == dir.path) break;
      dir = dir.parent;
    }
  } catch (_) {}

  // 3. Fallback known standard locations
  final common = [
    'D:/development/Flutter/flutter/bin/cache/artifacts/material_fonts/MaterialIcons-Regular.otf',
    'C:/flutter/bin/cache/artifacts/material_fonts/MaterialIcons-Regular.otf',
    '/opt/hostedtoolcache/flutter/bin/cache/artifacts/material_fonts/MaterialIcons-Regular.otf',
  ];
  for (final p in common) {
    final f = File(p);
    if (f.existsSync()) return f;
  }
  return null;
}

File? _findSystemTextFont() {
  final candidates = [
    // Windows
    'C:/Windows/Fonts/segoeui.ttf',
    'C:/Windows/Fonts/arial.ttf',
    // Linux (Ubuntu / Debian / GitHub Actions ubuntu-latest)
    '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
    '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Regular.ttf',
    '/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf',
    // macOS
    '/System/Library/Fonts/SFNSText.ttf',
    '/Library/Fonts/Arial.ttf',
  ];
  for (final p in candidates) {
    final f = File(p);
    if (f.existsSync()) return f;
  }
  return null;
}

void main() {
  // 1. Load real production dataset
  final contentJsonFile = _resolveContentJson();
  final jsonStr = contentJsonFile.readAsStringSync();
  final jsonData = jsonDecode(jsonStr) as Map<String, dynamic>;
  final rawTopics = jsonData['topics'] as List<dynamic>;
  final allTopics = rawTopics
      .map((t) => Topic.fromJson(t as Map<String, dynamic>))
      .where((t) => t.isActive)
      .toList();

  final fundamentalTopics = allTopics
      .where((t) => t.categoryId.startsWith('f-'))
      .toList();
  final ecosystemTopics = allTopics
      .where((t) => t.categoryId.startsWith('e-'))
      .toList();

  // Consistent simulation based on real 47 & 52 counts
  final understoodFundamental = fundamentalTopics
      .take(24)
      .map((t) => t.id)
      .toSet();
  final inProgressFundamental = fundamentalTopics
      .skip(24)
      .take(4)
      .map((t) => t.id)
      .toSet();

  final understoodEcosystem = ecosystemTopics.take(15).map((t) => t.id).toSet();
  final inProgressEcosystem = ecosystemTopics
      .skip(15)
      .take(3)
      .map((t) => t.id)
      .toSet();

  final contentRepo = SnapshotContentRepo(allTopics);
  final learningRepo = SnapshotLearningRepo(
    understoodTopics: {...understoodFundamental, ...understoodEcosystem},
    inProgressTopics: {...inProgressFundamental, ...inProgressEcosystem},
  );

  setUpAll(() async {
    // 1. Load text font dynamically if available
    final fontFile = _findSystemTextFont();
    if (fontFile != null && fontFile.existsSync()) {
      try {
        final fontData = fontFile.readAsBytesSync();
        for (final family in [
          'Roboto',
          '.SF UI Text',
          'Segoe UI',
          'Sans-Serif',
        ]) {
          final loader = FontLoader(family);
          loader.addFont(Future.value(ByteData.view(fontData.buffer)));
          await loader.load();
        }
      } catch (_) {}
    }

    // 2. Load MaterialIcons font offline if available
    final iconFontFile = _findMaterialIconsFont();
    if (iconFontFile != null && iconFontFile.existsSync()) {
      try {
        final iconFontData = iconFontFile.readAsBytesSync();
        final iconLoader = FontLoader('MaterialIcons');
        iconLoader.addFont(Future.value(ByteData.view(iconFontData.buffer)));
        await iconLoader.load();
      } catch (_) {}
    }
  });

  Future<void> captureWidget({
    required WidgetTester tester,
    required Widget widget,
    required String filename,
    Size size = const Size(360, 780),
    double textScale = 1.0,
    Future<void> Function(WidgetTester tester)? onBeforeCapture,
  }) async {
    final repaintKey = GlobalKey();

    tester.view.physicalSize = Size(size.width * 2, size.height * 2);
    tester.view.devicePixelRatio = 2.0;
    addTearDown(() => tester.view.resetPhysicalSize());

    final binding = TestWidgetsFlutterBinding.ensureInitialized();
    binding.platformDispatcher.textScaleFactorTestValue = textScale;
    addTearDown(
      () => binding.platformDispatcher.clearTextScaleFactorTestValue(),
    );

    await tester.pumpWidget(
      RepaintBoundary(
        key: repaintKey,
        child: SizedBox(width: size.width, height: size.height, child: widget),
      ),
    );
    await tester.pumpAndSettle();

    if (onBeforeCapture != null) {
      await onBeforeCapture(tester);
      await tester.pumpAndSettle();
    }

    await tester.runAsync(() async {
      final boundary =
          repaintKey.currentContext!.findRenderObject()!
              as RenderRepaintBoundary;
      final image = await boundary.toImage(pixelRatio: 2.0);
      final byteData = await image.toByteData(format: ui.ImageByteFormat.png);
      final bytes = byteData!.buffer.asUint8List();

      final outDir = _resolveSnapshotDir();
      final file = File('${outDir.path}/$filename');
      if (!file.parent.existsSync()) {
        file.parent.createSync(recursive: true);
      }
      await file.writeAsBytes(bytes);
    });
  }

  testWidgets(
    'Export visual snapshots for Beranda & TopicScreen on 360dp width',
    (tester) async {
      final appState = AppState(
        contentRepo: contentRepo,
        learningRepo: learningRepo,
      );
      await appState.refreshCounts();

      // 1. Beranda Dark Horizon (360dp, 100%)
      await captureWidget(
        tester: tester,
        widget: MaterialApp(
          debugShowCheckedModeBanner: false,
          theme: AtlasTheme.buildTheme(Brightness.dark),
          home: HomeScreen(
            appState: appState,
            contentRepo: contentRepo,
            onNavigateToExplore: () {},
            onNavigateToPaths: () {},
            onOpenTopic: (_) {},
            onOpenSettings: () {},
          ),
        ),
        size: const Size(360, 780),
        textScale: 1.0,
        filename: 'actual_beranda_dark.png',
      );

      // 2. Beranda Light Atlas (360dp, 100%)
      await captureWidget(
        tester: tester,
        widget: MaterialApp(
          debugShowCheckedModeBanner: false,
          theme: AtlasTheme.buildTheme(Brightness.light),
          home: HomeScreen(
            appState: appState,
            contentRepo: contentRepo,
            onNavigateToExplore: () {},
            onNavigateToPaths: () {},
            onOpenTopic: (_) {},
            onOpenSettings: () {},
          ),
        ),
        size: const Size(360, 780),
        textScale: 1.0,
        filename: 'actual_beranda_light.png',
      );

      // 3. Beranda 200% Text Scale (360dp, 200%)
      await captureWidget(
        tester: tester,
        widget: MaterialApp(
          debugShowCheckedModeBanner: false,
          theme: AtlasTheme.buildTheme(Brightness.dark),
          home: HomeScreen(
            appState: appState,
            contentRepo: contentRepo,
            onNavigateToExplore: () {},
            onNavigateToPaths: () {},
            onOpenTopic: (_) {},
            onOpenSettings: () {},
          ),
        ),
        size: const Size(360, 780),
        textScale: 2.0,
        filename: 'actual_beranda_scale200.png',
      );

      // 4. TopicScreen Dark Horizon (360dp, 100%, Top)
      await captureWidget(
        tester: tester,
        widget: MaterialApp(
          debugShowCheckedModeBanner: false,
          theme: AtlasTheme.buildTheme(Brightness.dark),
          home: TopicScreen(
            topicId: 'f-programming-logic',
            contentRepo: contentRepo,
            learningRepo: learningRepo,
            appState: appState,
            onOpenTopic: (_) {},
          ),
        ),
        size: const Size(360, 780),
        textScale: 1.0,
        filename: 'actual_artikel_dark.png',
      );

      // 5. TopicScreen Light Atlas (360dp, 100%, Top)
      await captureWidget(
        tester: tester,
        widget: MaterialApp(
          debugShowCheckedModeBanner: false,
          theme: AtlasTheme.buildTheme(Brightness.light),
          home: TopicScreen(
            topicId: 'f-programming-logic',
            contentRepo: contentRepo,
            learningRepo: learningRepo,
            appState: appState,
            onOpenTopic: (_) {},
          ),
        ),
        size: const Size(360, 780),
        textScale: 1.0,
        filename: 'actual_artikel_light.png',
      );

      // 6. TopicScreen 200% Text Scale (360dp, 200%, Top)
      await captureWidget(
        tester: tester,
        widget: MaterialApp(
          debugShowCheckedModeBanner: false,
          theme: AtlasTheme.buildTheme(Brightness.dark),
          home: TopicScreen(
            topicId: 'f-programming-logic',
            contentRepo: contentRepo,
            learningRepo: learningRepo,
            appState: appState,
            onOpenTopic: (_) {},
          ),
        ),
        size: const Size(360, 780),
        textScale: 2.0,
        filename: 'actual_artikel_scale200.png',
      );

      // 7. TopicScreen Bottom Dark (360dp, 100%, Notes + Save Button + Footer)
      await captureWidget(
        tester: tester,
        widget: MaterialApp(
          debugShowCheckedModeBanner: false,
          theme: AtlasTheme.buildTheme(Brightness.dark),
          home: TopicScreen(
            topicId: 'f-programming-logic',
            contentRepo: contentRepo,
            learningRepo: learningRepo,
            appState: appState,
            onOpenTopic: (_) {},
          ),
        ),
        size: const Size(360, 780),
        textScale: 1.0,
        onBeforeCapture: (tester) async {
          final scrollable = find
              .descendant(
                of: find.byKey(const ValueKey('topic_scrollable')),
                matching: find.byType(Scrollable),
              )
              .first;
          await tester.scrollUntilVisible(
            find.text('Simpan Catatan'),
            400,
            scrollable: scrollable,
          );
          await tester.pumpAndSettle();
        },
        filename: 'actual_artikel_bottom_dark.png',
      );

      // 8. TopicScreen Bottom 200% Text Scale (360dp, 200%, Notes + Save Button + Footer)
      await captureWidget(
        tester: tester,
        widget: MaterialApp(
          debugShowCheckedModeBanner: false,
          theme: AtlasTheme.buildTheme(Brightness.dark),
          home: TopicScreen(
            topicId: 'f-programming-logic',
            contentRepo: contentRepo,
            learningRepo: learningRepo,
            appState: appState,
            onOpenTopic: (_) {},
          ),
        ),
        size: const Size(360, 780),
        textScale: 2.0,
        onBeforeCapture: (tester) async {
          final scrollable = find
              .descendant(
                of: find.byKey(const ValueKey('topic_scrollable')),
                matching: find.byType(Scrollable),
              )
              .first;
          await tester.scrollUntilVisible(
            find.text('Simpan Catatan'),
            400,
            scrollable: scrollable,
          );
          await tester.pumpAndSettle();
        },
        filename: 'actual_artikel_bottom_scale200.png',
      );

      // 9. PathDetailScreen Jalur Umum Dark (360dp, 100%)
      await captureWidget(
        tester: tester,
        widget: MaterialApp(
          debugShowCheckedModeBanner: false,
          theme: AtlasTheme.buildTheme(Brightness.dark),
          home: PathDetailScreen(
            presetKey: 'general',
            contentRepo: contentRepo,
            learningRepo: learningRepo,
            appState: appState,
            onOpenTopic: (_, {pathId, pathName, pathTopicIds, onBackToPath}) {},
          ),
        ),
        size: const Size(360, 780),
        textScale: 1.0,
        filename: 'actual_detail_jalur_umum_dark.png',
      );

      // 10. PathDetailScreen Jalur Flutter Light (360dp, 100%)
      await captureWidget(
        tester: tester,
        widget: MaterialApp(
          debugShowCheckedModeBanner: false,
          theme: AtlasTheme.buildTheme(Brightness.light),
          home: PathDetailScreen(
            presetKey: 'flutter',
            contentRepo: contentRepo,
            learningRepo: learningRepo,
            appState: appState,
            onOpenTopic: (_, {pathId, pathName, pathTopicIds, onBackToPath}) {},
          ),
        ),
        size: const Size(360, 780),
        textScale: 1.0,
        filename: 'actual_detail_jalur_flutter_light.png',
      );

      // 11. Pengaturan Dialog Dark (360dp, 100%)
      await captureWidget(
        tester: tester,
        widget: MaterialApp(
          debugShowCheckedModeBanner: false,
          theme: AtlasTheme.buildTheme(Brightness.dark),
          home: Scaffold(
            body: Center(
              child: AlertDialog(
                title: const Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    CodeAtlasLogo(size: 32, showBackground: true),
                    SizedBox(width: 12),
                    Expanded(child: Text('Tentang CodeAtlas')),
                  ],
                ),
                content: const SingleChildScrollView(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text(
                        'CodeAtlas v1.0.1',
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                      SizedBox(height: 8),
                      Text(
                        'Ensiklopedia interaktif fundamental coding berbahasa Indonesia. '
                        'Semua konten tersedia offline.',
                      ),
                      SizedBox(height: 12),
                      Text(
                        'Tema',
                        style: TextStyle(fontWeight: FontWeight.w600),
                      ),
                      Text('Mengikuti pengaturan sistem (light/dark).'),
                      SizedBox(height: 12),
                      Text(
                        'Penyimpanan Data',
                        style: TextStyle(fontWeight: FontWeight.w600),
                      ),
                      Text('Semua data disimpan di perangkat ini.'),
                    ],
                  ),
                ),
                actions: [
                  TextButton(onPressed: () {}, child: const Text('Tutup')),
                ],
              ),
            ),
          ),
        ),
        size: const Size(360, 780),
        textScale: 1.0,
        filename: 'actual_pengaturan_dialog_dark.png',
      );
    },
  );
}
