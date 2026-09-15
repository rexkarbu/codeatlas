// lib/features/home/home_screen.dart — Redesigned CodeAtlas Home screen.
// Features: Focused Hero "Lanjutkan Belajar", Unified Progress Card,
// New user onboarding with Koda mascot, robust handling of incomplete data,
// dynamic reading time calculation labeled "perkiraan", and 5 learning paths.
// Fully responsive with zero RenderFlex overflow at 200% text scaling on 360dp screens.

import 'package:flutter/material.dart';

import '../../data/content_repository.dart';
import '../../data/models.dart';
import '../../data/reading_time.dart';
import '../../state/app_state.dart';
import '../../theme/atlas_theme.dart';
import '../../widgets/koda_mascot.dart';

class HomeScreen extends StatelessWidget {
  final AppState appState;
  final ContentRepository contentRepo;
  final VoidCallback onNavigateToExplore;
  final VoidCallback onNavigateToPaths;
  final void Function(String topicId) onOpenTopic;
  final VoidCallback onOpenSettings;
  final void Function(String presetKey)? onOpenPathPreset;

  const HomeScreen({
    super.key,
    required this.appState,
    required this.contentRepo,
    required this.onNavigateToExplore,
    required this.onNavigateToPaths,
    required this.onOpenTopic,
    required this.onOpenSettings,
    this.onOpenPathPreset,
  });

  /// Calculates dynamic reading time from actual topic content using shared estimator.
  static int calculateReadingMinutes(Topic topic) =>
      ReadingTimeEstimator.estimateMinutes(topic);

  /// Formats dynamic reading time consistently.
  static String formatReadingTime(Topic topic) =>
      ReadingTimeEstimator.format(topic);

  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: appState,
      builder: (context, _) {
        final hasProgress =
            appState.understoodCount > 0 || appState.inProgressCount > 0;
        final lastReadId = appState.lastReadTopicId;

        return Scaffold(
          appBar: AppBar(
            title: const Text(
              'CodeAtlas',
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
            actions: [
              IconButton(
                icon: const Icon(Icons.settings_outlined),
                tooltip: 'Pengaturan',
                onPressed: onOpenSettings,
              ),
            ],
          ),
          body: ListView(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
            children: [
              // ─── State 1: Active user with a last read topic ───
              if (lastReadId != null) ...[
                _ContinueReadingHero(
                  topicId: lastReadId,
                  contentRepo: contentRepo,
                  onTap: () => onOpenTopic(lastReadId),
                ),
                const SizedBox(height: 16),
              ]
              // ─── State 2: User with progress but no lastReadTopicId (incomplete data) ───
              else if (hasProgress) ...[
                _ResumeProgressCard(
                  onOpenPaths: onNavigateToPaths,
                  onOpenExplore: onNavigateToExplore,
                ),
                const SizedBox(height: 16),
              ]
              // ─── State 3: Brand new user (0 progress) ───
              else ...[
                _NewUserWelcomeCard(
                  onStartFromZero: () {
                    if (onOpenPathPreset != null) {
                      onOpenPathPreset!('general');
                    } else {
                      onOpenTopic('f-programming-logic');
                    }
                  },
                  onChooseGoal: onNavigateToPaths,
                  onExplore: onNavigateToExplore,
                ),
                const SizedBox(height: 16),
              ],

              // ─── Unified Progress Card ───
              _UnifiedProgressCard(appState: appState),
              const SizedBox(height: 20),

              // ─── 5 Learning Paths Quick Access ───
              _LearningPathsSection(
                onNavigateToPaths: onNavigateToPaths,
                onOpenPathPreset: onOpenPathPreset,
              ),
              const SizedBox(height: 24),
            ],
          ),
        );
      },
    );
  }
}

// ─── Hero Card: Lanjutkan Belajar ───

class _ContinueReadingHero extends StatelessWidget {
  final String topicId;
  final ContentRepository contentRepo;
  final VoidCallback onTap;

  const _ContinueReadingHero({
    required this.topicId,
    required this.contentRepo,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final isDark = theme.brightness == Brightness.dark;

    return FutureBuilder<Topic?>(
      future: contentRepo.getTopicById(topicId),
      builder: (context, snapshot) {
        final topic = snapshot.data;
        if (topic == null) return const SizedBox.shrink();

        return Card(
          clipBehavior: Clip.antiAlias,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(14),
            side: BorderSide(
              color: isDark
                  ? AtlasColors.primaryIndigo.withValues(alpha: 0.35)
                  : AtlasColors.primaryIndigoLight.withValues(alpha: 0.25),
              width: 1.5,
            ),
          ),
          child: InkWell(
            onTap: onTap,
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Wrap(
                    spacing: 8,
                    runSpacing: 6,
                    crossAxisAlignment: WrapCrossAlignment.center,
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(
                          horizontal: 8,
                          vertical: 4,
                        ),
                        decoration: BoxDecoration(
                          color: AtlasColors.primaryIndigo.withValues(
                            alpha: 0.15,
                          ),
                          borderRadius: BorderRadius.circular(6),
                        ),
                        child: Wrap(
                          crossAxisAlignment: WrapCrossAlignment.center,
                          spacing: 4,
                          children: [
                            Icon(
                              Icons.bookmark,
                              size: 13,
                              color: AtlasColors.primary(theme.brightness),
                            ),
                            Text(
                              'Lanjutkan membaca',
                              style: TextStyle(
                                fontSize: 11,
                                fontWeight: FontWeight.bold,
                                color: AtlasColors.primary(theme.brightness),
                              ),
                            ),
                          ],
                        ),
                      ),
                      Wrap(
                        crossAxisAlignment: WrapCrossAlignment.center,
                        spacing: 4,
                        children: [
                          Icon(
                            Icons.schedule,
                            size: 14,
                            color: theme.colorScheme.onSurfaceVariant,
                          ),
                          Text(
                            ReadingTimeEstimator.format(topic),
                            style: theme.textTheme.bodySmall?.copyWith(
                              color: theme.colorScheme.onSurfaceVariant,
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                  const SizedBox(height: 10),
                  Text(
                    topic.title,
                    style: theme.textTheme.titleMedium?.copyWith(
                      fontWeight: FontWeight.bold,
                      letterSpacing: -0.2,
                    ),
                  ),
                  if (topic.summary.isNotEmpty) ...[
                    const SizedBox(height: 6),
                    Text(
                      topic.summary,
                      maxLines: 2,
                      overflow: TextOverflow.ellipsis,
                      style: theme.textTheme.bodyMedium?.copyWith(
                        color: theme.colorScheme.onSurfaceVariant,
                        height: 1.4,
                      ),
                    ),
                  ],
                  const SizedBox(height: 14),
                  Wrap(
                    alignment: WrapAlignment.end,
                    children: [
                      FilledButton.icon(
                        onPressed: onTap,
                        icon: const Icon(Icons.arrow_forward_rounded, size: 16),
                        label: const Text('Lanjut Membaca'),
                        style: FilledButton.styleFrom(
                          visualDensity: VisualDensity.compact,
                          padding: const EdgeInsets.symmetric(
                            horizontal: 14,
                            vertical: 8,
                          ),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ),
        );
      },
    );
  }
}

// ─── State 2: Resume Progress when lastReadTopicId is missing ───

class _ResumeProgressCard extends StatelessWidget {
  final VoidCallback onOpenPaths;
  final VoidCallback onOpenExplore;

  const _ResumeProgressCard({
    required this.onOpenPaths,
    required this.onOpenExplore,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Wrap(
              crossAxisAlignment: WrapCrossAlignment.center,
              spacing: 8,
              children: [
                const Icon(
                  Icons.auto_stories,
                  size: 20,
                  color: AtlasColors.accentMint,
                ),
                Text(
                  'Lanjutkan Perjalanan Belajar',
                  style: theme.textTheme.titleMedium?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 8),
            Text(
              'Kamu telah memulai materi di CodeAtlas. '
              'Lanjutkan topik berikutnya melalui jalur belajarmu atau jelajahi ensiklopedia.',
              style: theme.textTheme.bodyMedium?.copyWith(
                color: theme.colorScheme.onSurfaceVariant,
                height: 1.4,
              ),
            ),
            const SizedBox(height: 14),
            Wrap(
              spacing: 8,
              runSpacing: 8,
              children: [
                FilledButton.icon(
                  onPressed: onOpenPaths,
                  icon: const Icon(Icons.route_outlined, size: 16),
                  label: const Text('Buka Jalur Belajar'),
                ),
                OutlinedButton.icon(
                  onPressed: onOpenExplore,
                  icon: const Icon(Icons.explore_outlined, size: 16),
                  label: const Text('Jelajahi Topik'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

// ─── State 3: New User Welcome Card with Koda Mascot ───

class _NewUserWelcomeCard extends StatelessWidget {
  final VoidCallback onStartFromZero;
  final VoidCallback onChooseGoal;
  final VoidCallback onExplore;

  const _NewUserWelcomeCard({
    required this.onStartFromZero,
    required this.onChooseGoal,
    required this.onExplore,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final isDark = theme.brightness == Brightness.dark;

    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                const KodaMascot(size: 64),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        'Halo! Kenalkan, aku Koda',
                        style: TextStyle(
                          fontSize: 12,
                          fontWeight: FontWeight.bold,
                          color: isDark
                              ? AtlasColors.accentLavender
                              : AtlasColors.accentLavenderLight,
                        ),
                      ),
                      const SizedBox(height: 2),
                      Text(
                        'Selamat Datang di CodeAtlas',
                        style: theme.textTheme.titleMedium?.copyWith(
                          fontWeight: FontWeight.bold,
                          letterSpacing: -0.2,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
            const SizedBox(height: 12),
            Text(
              'Ensiklopedia fundamental programming offline. '
              'Mulai dari konsep dasar sekuensial hingga arsitektur modern tanpa distraksi gamifikasi.',
              style: theme.textTheme.bodyMedium?.copyWith(
                color: theme.colorScheme.onSurfaceVariant,
                height: 1.45,
              ),
            ),
            const SizedBox(height: 16),
            Wrap(
              spacing: 8,
              runSpacing: 8,
              children: [
                FilledButton.icon(
                  onPressed: onStartFromZero,
                  icon: const Icon(Icons.play_arrow_rounded, size: 18),
                  label: const Text('Mulai dari nol'),
                ),
                OutlinedButton.icon(
                  onPressed: onChooseGoal,
                  icon: const Icon(Icons.flag_outlined, size: 16),
                  label: const Text('Pilih tujuan'),
                ),
                TextButton.icon(
                  onPressed: onExplore,
                  icon: const Icon(Icons.explore_outlined, size: 16),
                  label: const Text('Jelajahi'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

// ─── Unified Progress Card ───

class _UnifiedProgressCard extends StatelessWidget {
  final AppState appState;

  const _UnifiedProgressCard({required this.appState});

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final total = appState.totalActiveTopics;
    final understood = appState.understoodCount;
    final inProgress = appState.inProgressCount;
    final overallPct = appState.overallProgress;
    final progressValue = total > 0
        ? (understood / total).clamp(0.0, 1.0)
        : 0.0;

    return Card(
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        'Progress Keseluruhan',
                        style: theme.textTheme.titleSmall?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      const SizedBox(height: 2),
                      Text(
                        'Paham: $understood · Sedang: $inProgress · Belum: ${total - understood - inProgress}',
                        style: theme.textTheme.bodySmall?.copyWith(
                          color: theme.colorScheme.onSurfaceVariant,
                        ),
                      ),
                    ],
                  ),
                ),
                Semantics(
                  label: '${overallPct.toStringAsFixed(0)} persen',
                  child: Text(
                    '${overallPct.toStringAsFixed(0)}%',
                    style: theme.textTheme.titleLarge?.copyWith(
                      fontWeight: FontWeight.bold,
                      color: AtlasColors.primary(theme.brightness),
                    ),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 8),
            ClipRRect(
              borderRadius: BorderRadius.circular(3),
              child: LinearProgressIndicator(
                value: progressValue,
                minHeight: 6,
                backgroundColor: theme.colorScheme.surfaceContainerHighest,
                valueColor: AlwaysStoppedAnimation(
                  AtlasColors.primary(theme.brightness),
                ),
              ),
            ),
            const SizedBox(height: 8),
            LayoutBuilder(
              builder: (context, constraints) {
                final isNarrow = constraints.maxWidth < 320;
                final itemWidth = isNarrow
                    ? constraints.maxWidth
                    : (constraints.maxWidth - 16) / 2;

                return Wrap(
                  spacing: 16,
                  runSpacing: 8,
                  children: [
                    SizedBox(
                      width: itemWidth,
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            'Fundamental Programming',
                            style: theme.textTheme.bodySmall?.copyWith(
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                          const SizedBox(height: 2),
                          Text(
                            '${appState.fundamentalUnderstood}/${appState.fundamentalTopicCount} Paham',
                            style: theme.textTheme.bodySmall?.copyWith(
                              color: theme.colorScheme.onSurfaceVariant,
                            ),
                          ),
                        ],
                      ),
                    ),
                    SizedBox(
                      width: itemWidth,
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            'Dunia & Ekosistem Coding',
                            style: theme.textTheme.bodySmall?.copyWith(
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                          const SizedBox(height: 2),
                          Text(
                            '${appState.ecosystemUnderstood}/${appState.ecosystemTopicCount} Paham',
                            style: theme.textTheme.bodySmall?.copyWith(
                              color: theme.colorScheme.onSurfaceVariant,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                );
              },
            ),
          ],
        ),
      ),
    );
  }
}

// ─── 5 Curated Learning Paths Quick Access ───

class _LearningPathsSection extends StatelessWidget {
  final VoidCallback onNavigateToPaths;
  final void Function(String presetKey)? onOpenPathPreset;

  const _LearningPathsSection({
    required this.onNavigateToPaths,
    this.onOpenPathPreset,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    final paths = [
      (
        key: 'general',
        title: 'Umum / Dasar dari Nol',
        desc: 'Konsep dasar: logika, tipe data, percabangan, fungsi, hingga git & testing',
        icon: Icons.lightbulb_outline,
        color: AtlasColors.accentMint,
      ),
      (
        key: 'flutter',
        title: 'Flutter & Mobile',
        desc: 'Pengantar OOP, asynchronous, API, dan arsitektur dasar mobile',
        icon: Icons.phone_android_outlined,
        color: AtlasColors.accentCyan,
      ),
      (
        key: 'web',
        title: 'Web Frontend',
        desc: 'Fondasi HTTP, komunikasi API, serialisasi, keamanan, dan web',
        icon: Icons.language_outlined,
        color: AtlasColors.accentAmber,
      ),
      (
        key: 'backend',
        title: 'Backend & Server',
        desc: 'Pengantar API, database SQL, pemodelan data, autentikasi, dan deployment',
        icon: Icons.dns_outlined,
        color: AtlasColors.accentCoral,
      ),
      (
        key: 'data',
        title: 'Data & Algoritma',
        desc: 'Pengantar struktur data, algoritma, database SQL, dan pemodelan data',
        icon: Icons.analytics_outlined,
        color: AtlasColors.accentLavender,
      ),
    ];

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Wrap(
          alignment: WrapAlignment.spaceBetween,
          crossAxisAlignment: WrapCrossAlignment.center,
          spacing: 8,
          runSpacing: 4,
          children: [
            Text(
              'Jalur Belajar Pilihan',
              style: theme.textTheme.titleSmall?.copyWith(
                fontWeight: FontWeight.bold,
              ),
            ),
            TextButton(
              onPressed: onNavigateToPaths,
              child: const Text('Lihat Semua'),
            ),
          ],
        ),
        const SizedBox(height: 6),
        for (final p in paths) ...[
          Padding(
            padding: const EdgeInsets.only(bottom: 8),
            child: Card(
              child: InkWell(
                onTap: () {
                  if (onOpenPathPreset != null) {
                    onOpenPathPreset!(p.key);
                  } else {
                    onNavigateToPaths();
                  }
                },
                borderRadius: BorderRadius.circular(12),
                child: Padding(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 14,
                    vertical: 12,
                  ),
                  child: Row(
                    children: [
                      Container(
                        padding: const EdgeInsets.all(8),
                        decoration: BoxDecoration(
                          color: p.color.withValues(alpha: 0.12),
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: Icon(p.icon, size: 20, color: p.color),
                      ),
                      const SizedBox(width: 12),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              p.title,
                              style: theme.textTheme.bodyMedium?.copyWith(
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                            const SizedBox(height: 2),
                            Text(
                              p.desc,
                              style: theme.textTheme.bodySmall?.copyWith(
                                color: theme.colorScheme.onSurfaceVariant,
                              ),
                            ),
                          ],
                        ),
                      ),
                      Icon(
                        Icons.chevron_right,
                        size: 18,
                        color: theme.colorScheme.onSurfaceVariant,
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ],
      ],
    );
  }
}
