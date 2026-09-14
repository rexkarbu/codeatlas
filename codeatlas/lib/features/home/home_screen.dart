// lib/features/home/home_screen.dart — F01: Home with continue reading,
// start from zero, progress per layer.

import 'package:flutter/material.dart';

import '../../data/content_repository.dart';
import '../../data/models.dart';
import '../../state/app_state.dart';

class HomeScreen extends StatelessWidget {
  final AppState appState;
  final ContentRepository contentRepo;
  final VoidCallback onNavigateToExplore;
  final VoidCallback onNavigateToPaths;
  final void Function(String topicId) onOpenTopic;
  final VoidCallback onOpenSettings;

  const HomeScreen({
    super.key,
    required this.appState,
    required this.contentRepo,
    required this.onNavigateToExplore,
    required this.onNavigateToPaths,
    required this.onOpenTopic,
    required this.onOpenSettings,
  });

  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: appState,
      builder: (context, _) {
        return Scaffold(
          appBar: AppBar(
            title: const Text('CodeAtlas'),
            actions: [
              IconButton(
                icon: const Icon(Icons.settings_outlined),
                tooltip: 'Pengaturan',
                onPressed: onOpenSettings,
              ),
            ],
          ),
          body: ListView(
            padding: const EdgeInsets.all(16),
            children: [
              _WelcomeCard(
                onStartFromZero: () => onOpenTopic('f-programming-logic'),
                onChooseGoal: onNavigateToPaths,
                onExplore: onNavigateToExplore,
              ),
              const SizedBox(height: 16),
              if (appState.lastReadTopicId != null)
                _ContinueReadingCard(
                  topicId: appState.lastReadTopicId!,
                  contentRepo: contentRepo,
                  onTap: () => onOpenTopic(appState.lastReadTopicId!),
                ),
              if (appState.lastReadTopicId != null) const SizedBox(height: 16),
              _ProgressCard(
                title: 'Progress Keseluruhan',
                understood: appState.understoodCount,
                inProgress: appState.inProgressCount,
                total: appState.totalActiveTopics,
                percentage: appState.overallProgress,
              ),
              const SizedBox(height: 12),
              _ProgressCard(
                title: 'Fundamental Programming',
                subtitle: '${appState.fundamentalTopicCount} topik',
                understood: appState.fundamentalUnderstood,
                inProgress: appState.fundamentalInProgress,
                total: appState.fundamentalTopicCount,
                percentage: appState.fundamentalProgress,
              ),
              const SizedBox(height: 12),
              _ProgressCard(
                title: 'Dunia & Ekosistem Coding',
                subtitle: '${appState.ecosystemTopicCount} topik',
                understood: appState.ecosystemUnderstood,
                inProgress: appState.ecosystemInProgress,
                total: appState.ecosystemTopicCount,
                percentage: appState.ecosystemProgress,
              ),
            ],
          ),
        );
      },
    );
  }
}

class _WelcomeCard extends StatelessWidget {
  final VoidCallback onStartFromZero;
  final VoidCallback onChooseGoal;
  final VoidCallback onExplore;

  const _WelcomeCard({
    required this.onStartFromZero,
    required this.onChooseGoal,
    required this.onExplore,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Selamat Datang di CodeAtlas',
              style: theme.textTheme.headlineSmall?.copyWith(
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 8),
            Text(
              'Ensiklopedia interaktif untuk memahami dunia coding. '
              'Dua lapis konten: Fundamental Programming membahas konsep dasar, '
              'dan Dunia & Ekosistem Coding memetakan teknologi yang ada.',
              style: theme.textTheme.bodyMedium?.copyWith(
                color: theme.colorScheme.onSurfaceVariant,
              ),
            ),
            const SizedBox(height: 16),
            Wrap(
              spacing: 8,
              runSpacing: 8,
              children: [
                FilledButton.icon(
                  onPressed: onStartFromZero,
                  icon: const Icon(Icons.play_arrow),
                  label: const Text('Mulai dari nol'),
                ),
                OutlinedButton.icon(
                  onPressed: onChooseGoal,
                  icon: const Icon(Icons.flag_outlined),
                  label: const Text('Pilih tujuan'),
                ),
                TextButton.icon(
                  onPressed: onExplore,
                  icon: const Icon(Icons.explore_outlined),
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

class _ContinueReadingCard extends StatelessWidget {
  final String topicId;
  final ContentRepository contentRepo;
  final VoidCallback onTap;

  const _ContinueReadingCard({
    required this.topicId,
    required this.contentRepo,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    return FutureBuilder<Topic?>(
      future: contentRepo.getTopicById(topicId),
      builder: (context, snapshot) {
        final topic = snapshot.data;
        if (topic == null) return const SizedBox.shrink();
        return Card(
          child: InkWell(
            onTap: onTap,
            borderRadius: BorderRadius.circular(12),
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Row(
                children: [
                  Icon(Icons.bookmark, color: theme.colorScheme.primary),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          'Lanjutkan membaca',
                          style: theme.textTheme.labelMedium?.copyWith(
                            color: theme.colorScheme.primary,
                          ),
                        ),
                        Text(
                          topic.title,
                          style: theme.textTheme.titleSmall?.copyWith(
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ],
                    ),
                  ),
                  Icon(
                    Icons.arrow_forward_ios,
                    size: 16,
                    color: theme.colorScheme.onSurfaceVariant,
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

class _ProgressCard extends StatelessWidget {
  final String title;
  final String? subtitle;
  final int understood;
  final int inProgress;
  final int total;
  final double percentage;

  const _ProgressCard({
    required this.title,
    this.subtitle,
    required this.understood,
    required this.inProgress,
    required this.total,
    required this.percentage,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final progressValue = total > 0 ? understood / total : 0.0;

    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        title,
                        style: theme.textTheme.titleSmall?.copyWith(
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                      if (subtitle != null)
                        Text(
                          subtitle!,
                          style: theme.textTheme.bodySmall?.copyWith(
                            color: theme.colorScheme.onSurfaceVariant,
                          ),
                        ),
                    ],
                  ),
                ),
                Semantics(
                  label: '${percentage.toStringAsFixed(0)} persen',
                  child: Text(
                    '${percentage.toStringAsFixed(0)}%',
                    style: theme.textTheme.headlineSmall?.copyWith(
                      fontWeight: FontWeight.bold,
                      color: theme.colorScheme.primary,
                    ),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 8),
            ClipRRect(
              borderRadius: BorderRadius.circular(4),
              child: LinearProgressIndicator(
                value: progressValue,
                minHeight: 6,
              ),
            ),
            const SizedBox(height: 8),
            Text(
              'Paham: $understood · Sedang: $inProgress · '
              'Belum: ${total - understood - inProgress}',
              style: theme.textTheme.bodySmall?.copyWith(
                color: theme.colorScheme.onSurfaceVariant,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
