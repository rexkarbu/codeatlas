// lib/app.dart — MaterialApp shell with Material 3 theming and bottom navigation.
// System theme follow (light/dark). Indonesian labels.

import 'package:flutter/material.dart';

import 'data/app_database.dart';
import 'data/content_repository.dart';
import 'data/learning_repository.dart';
import 'data/seed_loader.dart';
import 'features/explore/explore_screen.dart';
import 'features/home/home_screen.dart';
import 'features/learning_paths/path_detail_screen.dart';
import 'features/learning_paths/paths_screen.dart';
import 'features/practice/practice_screen.dart';
import 'features/roadmap/roadmap_screen.dart';
import 'features/topic/topic_screen.dart';
import 'state/app_state.dart';
import 'theme/atlas_theme.dart';
import 'widgets/codeatlas_logo.dart';

class CodeAtlasApp extends StatefulWidget {
  final AppState appState;
  final ContentRepository contentRepo;
  final LearningRepository learningRepo;
  final Future<bool> Function()? onRetryUpgrade;

  const CodeAtlasApp({
    super.key,
    required this.appState,
    required this.contentRepo,
    required this.learningRepo,
    this.onRetryUpgrade,
  });

  @override
  State<CodeAtlasApp> createState() => _CodeAtlasAppState();
}

class _CodeAtlasAppState extends State<CodeAtlasApp> {
  int _currentIndex = 0;

  void _openTopic(
    String topicId, {
    String? pathId,
    String? pathName,
    List<String>? pathTopicIds,
    VoidCallback? onBackToPath,
  }) {
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) => TopicScreen(
          topicId: topicId,
          contentRepo: widget.contentRepo,
          learningRepo: widget.learningRepo,
          appState: widget.appState,
          onOpenTopic: _openTopic,
          pathId: pathId,
          pathName: pathName,
          pathTopicIds: pathTopicIds,
          onBackToPath: onBackToPath,
        ),
      ),
    );
  }

  void _openPathDetail(String presetKey) {
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) => PathDetailScreen(
          presetKey: presetKey,
          contentRepo: widget.contentRepo,
          learningRepo: widget.learningRepo,
          appState: widget.appState,
          onOpenTopic:
              (topicId, {pathId, pathName, pathTopicIds, onBackToPath}) {
                _openTopic(
                  topicId,
                  pathId: pathId,
                  pathName: pathName,
                  pathTopicIds: pathTopicIds,
                  onBackToPath: onBackToPath,
                );
              },
        ),
      ),
    );
  }

  void _switchTab(int index) {
    setState(() => _currentIndex = index);
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'CodeAtlas',
      debugShowCheckedModeBanner: false,
      themeMode: ThemeMode.system,
      theme: AtlasTheme.buildTheme(Brightness.light),
      darkTheme: AtlasTheme.buildTheme(Brightness.dark),
      home: _buildScaffold(),
    );
  }

  Widget _buildScaffold() {
    return ListenableBuilder(
      listenable: widget.appState,
      builder: (context, child) {
        final notice = widget.appState.contentUpdateNotice;
        return Scaffold(
          body: SafeArea(
            child: Column(
              children: [
                if (notice != null)
                  MaterialBanner(
                    leading: const Icon(
                      Icons.warning_amber_rounded,
                      color: Colors.orange,
                    ),
                    content: Text(notice, style: const TextStyle(fontSize: 13)),
                    backgroundColor: Colors.orange.shade50,
                    actions: [
                      TextButton(
                        onPressed: () async {
                          bool success = false;
                          String? errorMsg;
                          if (widget.onRetryUpgrade != null) {
                            success = await widget.onRetryUpgrade!();
                            if (!success) errorMsg = 'Gagal memperbarui data';
                          } else {
                            final db = await AppDatabase.database;
                            final seedLoader = SeedLoader(db);
                            final res = await seedLoader.loadFromAsset();
                            success = res.success;
                            errorMsg = res.error;
                          }

                          if (success) {
                            widget.appState.dismissContentUpdateNotice();
                            await widget.appState.refreshCounts();
                            if (context.mounted) {
                              ScaffoldMessenger.of(context).showSnackBar(
                                const SnackBar(
                                  content: Text('Pembaruan konten berhasil!'),
                                ),
                              );
                            }
                          } else {
                            if (context.mounted) {
                              ScaffoldMessenger.of(context).showSnackBar(
                                SnackBar(
                                  content: Text(
                                    'Coba lagi gagal: ${errorMsg ?? "Kesalahan tidak diketahui"}',
                                  ),
                                ),
                              );
                            }
                          }
                        },
                        child: const Text('Coba Lagi'),
                      ),
                      TextButton(
                        onPressed: () =>
                            widget.appState.dismissContentUpdateNotice(),
                        child: const Text('Tutup'),
                      ),
                    ],
                  ),
                Expanded(
                  child: IndexedStack(
                    index: _currentIndex,
                    children: [
                      HomeScreen(
                        appState: widget.appState,
                        contentRepo: widget.contentRepo,
                        onNavigateToExplore: () => _switchTab(1),
                        onNavigateToPaths: () => _switchTab(4),
                        onOpenTopic: _openTopic,
                        onOpenSettings: _showSettings,
                        onOpenPathPreset: _openPathDetail,
                      ),
                      ExploreScreen(
                        contentRepo: widget.contentRepo,
                        learningRepo: widget.learningRepo,
                        onOpenTopic: _openTopic,
                      ),
                      RoadmapScreen(
                        contentRepo: widget.contentRepo,
                        learningRepo: widget.learningRepo,
                        onOpenTopic: _openTopic,
                      ),
                      PracticeScreen(
                        contentRepo: widget.contentRepo,
                        learningRepo: widget.learningRepo,
                        onOpenTopic: _openTopic,
                      ),
                      PathsScreen(
                        contentRepo: widget.contentRepo,
                        learningRepo: widget.learningRepo,
                        appState: widget.appState,
                        onOpenTopic: _openTopic,
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
          bottomNavigationBar: NavigationBar(
            selectedIndex: _currentIndex,
            onDestinationSelected: _switchTab,
            destinations: const [
              NavigationDestination(
                icon: Icon(Icons.home_outlined),
                selectedIcon: Icon(Icons.home),
                label: 'Beranda',
              ),
              NavigationDestination(
                icon: Icon(Icons.explore_outlined),
                selectedIcon: Icon(Icons.explore),
                label: 'Jelajah',
              ),
              NavigationDestination(
                icon: Icon(Icons.account_tree_outlined),
                selectedIcon: Icon(Icons.account_tree),
                label: 'Peta',
              ),
              NavigationDestination(
                icon: Icon(Icons.school_outlined),
                selectedIcon: Icon(Icons.school),
                label: 'Latihan',
              ),
              NavigationDestination(
                icon: Icon(Icons.route_outlined),
                selectedIcon: Icon(Icons.route),
                label: 'Jalurku',
              ),
            ],
          ),
        );
      },
    );
  }

  void _showSettings() {
    showDialog(
      context: context,
      builder: (dialogContext) {
        return AlertDialog(
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
                Text('Tema', style: TextStyle(fontWeight: FontWeight.w600)),
                Text('Mengikuti pengaturan sistem (light/dark).'),
                SizedBox(height: 12),
                Text(
                  'Penyimpanan Data',
                  style: TextStyle(fontWeight: FontWeight.w600),
                ),
                Text(
                  'Semua data disimpan di perangkat ini. '
                  'Uninstall atau penghapusan data aplikasi akan '
                  'menghilangkan progress, catatan, dan jalur belajar. '
                  'Backup dan sinkronisasi belum tersedia pada versi ini.',
                ),
                SizedBox(height: 12),
                Text(
                  'Penilaian Diri',
                  style: TextStyle(fontWeight: FontWeight.w600),
                ),
                Text(
                  'Status "Paham" adalah penilaian diri Anda sendiri, '
                  'bukan sertifikasi kompetensi.',
                ),
              ],
            ),
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context),
              child: const Text('Tutup'),
            ),
          ],
        );
      },
    );
  }
}
