// lib/main.dart — Bootstrap: init JSON codecs, open database, seed content,
// handle errors with retry UI, then launch CodeAtlasApp.

import 'dart:convert';

import 'package:flutter/material.dart';

import 'app.dart';
import 'data/app_database.dart';
import 'data/content_repository.dart';
import 'data/learning_repository.dart';
import 'data/models.dart';
import 'data/seed_loader.dart';
import 'state/app_state.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();

  // Wire JSON codecs for model serialization
  initModelJsonCodecs(
    encode: (value) => jsonEncode(value),
    decode: (source) => jsonDecode(source),
  );

  runApp(const _BootstrapApp());
}

class _BootstrapApp extends StatelessWidget {
  const _BootstrapApp();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'CodeAtlas',
      debugShowCheckedModeBanner: false,
      themeMode: ThemeMode.system,
      theme: ThemeData(
        useMaterial3: true,
        colorSchemeSeed: const Color(0xFF2563EB),
      ),
      darkTheme: ThemeData(
        useMaterial3: true,
        colorSchemeSeed: const Color(0xFF2563EB),
        brightness: Brightness.dark,
      ),
      home: const BootstrapScreen(),
    );
  }
}

class BootstrapScreen extends StatefulWidget {
  final Future<SeedResult> Function()? seedLoaderAction;
  final Future<ContentMeta?> Function()? metaReader;
  final Future<int> Function()? activeTopicsCountReader;
  final ContentRepository? mockContentRepo;
  final LearningRepository? mockLearningRepo;
  final Future<bool> Function()? onRetryUpgrade;

  const BootstrapScreen({
    super.key,
    this.seedLoaderAction,
    this.metaReader,
    this.activeTopicsCountReader,
    this.mockContentRepo,
    this.mockLearningRepo,
    this.onRetryUpgrade,
  });

  @override
  State<BootstrapScreen> createState() => _BootstrapScreenState();
}

class _BootstrapScreenState extends State<BootstrapScreen> {
  String _statusText = 'Mempersiapkan CodeAtlas...';
  String? _errorText;
  bool _loading = true;

  @override
  void initState() {
    super.initState();
    _initialize();
  }

  Future<void> _initialize() async {
    setState(() {
      _loading = true;
      _errorText = null;
      _statusText = 'Membuka database...';
    });

    try {
      final SeedResult result;
      final ContentRepository contentRepo;
      final LearningRepository learningRepo;
      final ContentMeta? existingMeta;
      final int activeTopicsCount;

      if (widget.seedLoaderAction != null) {
        result = await widget.seedLoaderAction!();
        contentRepo = widget.mockContentRepo!;
        learningRepo = widget.mockLearningRepo!;
        existingMeta = widget.metaReader != null
            ? await widget.metaReader!()
            : null;
        activeTopicsCount = widget.activeTopicsCountReader != null
            ? await widget.activeTopicsCountReader!()
            : 0;
      } else {
        final db = await AppDatabase.database;
        setState(() => _statusText = 'Memuat konten...');
        final seedLoader = SeedLoader(db);
        result = await seedLoader.loadFromAsset();
        contentRepo = ContentRepository(db);
        learningRepo = LearningRepository(db);
        existingMeta = await contentRepo.getContentMeta();
        activeTopicsCount = await contentRepo.getActiveTopicCount();
      }

      final hasValidOldData = existingMeta != null && activeTopicsCount > 0;

      if (!result.success) {
        if (hasValidOldData) {
          // Do NOT lock user on error screen: retain access to old valid content!
          final appState = AppState(
            contentRepo: contentRepo,
            learningRepo: learningRepo,
          );
          appState.setContentUpdateNotice(
            'Pembaruan konten gagal: ${result.error}. Menggunakan data versi ${existingMeta.contentVersion}.',
          );
          await appState.refreshCounts();

          if (!mounted) return;
          Navigator.of(context).pushReplacement(
            MaterialPageRoute(
              builder: (context) => CodeAtlasApp(
                appState: appState,
                contentRepo: contentRepo,
                learningRepo: learningRepo,
                onRetryUpgrade: widget.onRetryUpgrade,
              ),
            ),
          );
          return;
        }

        setState(() {
          _loading = false;
          _errorText = result.error ?? 'Gagal memuat konten';
        });
        return;
      }

      setState(() => _statusText = 'Mempersiapkan antarmuka...');

      final appState = AppState(
        contentRepo: contentRepo,
        learningRepo: learningRepo,
      );

      await appState.refreshCounts();

      if (!mounted) return;

      // Replace the bootstrap app with the actual app
      Navigator.of(context).pushReplacement(
        MaterialPageRoute(
          builder: (context) => CodeAtlasApp(
            appState: appState,
            contentRepo: contentRepo,
            learningRepo: learningRepo,
            onRetryUpgrade: widget.onRetryUpgrade,
          ),
        ),
      );
    } catch (e) {
      if (mounted) {
        setState(() {
          _loading = false;
          _errorText = 'Terjadi kesalahan: $e';
        });
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Scaffold(
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(32),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(
                Icons.map_outlined,
                size: 64,
                color: theme.colorScheme.primary,
              ),
              const SizedBox(height: 16),
              Text(
                'CodeAtlas',
                style: theme.textTheme.headlineMedium?.copyWith(
                  fontWeight: FontWeight.bold,
                  color: theme.colorScheme.primary,
                ),
              ),
              const SizedBox(height: 24),
              if (_loading) ...[
                const CircularProgressIndicator(),
                const SizedBox(height: 16),
                Text(
                  _statusText,
                  style: theme.textTheme.bodyMedium?.copyWith(
                    color: theme.colorScheme.onSurfaceVariant,
                  ),
                ),
              ],
              if (_errorText != null) ...[
                Icon(
                  Icons.error_outline,
                  size: 48,
                  color: theme.colorScheme.error,
                ),
                const SizedBox(height: 8),
                Text(
                  _errorText!,
                  textAlign: TextAlign.center,
                  style: theme.textTheme.bodyMedium?.copyWith(
                    color: theme.colorScheme.error,
                  ),
                ),
                const SizedBox(height: 16),
                FilledButton.icon(
                  onPressed: _initialize,
                  icon: const Icon(Icons.refresh),
                  label: const Text('Coba lagi'),
                ),
              ],
            ],
          ),
        ),
      ),
    );
  }
}
