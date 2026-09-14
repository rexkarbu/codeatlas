// lib/widgets/topic_tile.dart — Reusable topic list tile with status, level,
// and layer indicators.

import 'package:flutter/material.dart';

import '../data/models.dart';

class TopicTile extends StatelessWidget {
  final Topic topic;
  final LearningStatus? status;
  final ContentLayer? layer;
  final VoidCallback? onTap;

  const TopicTile({
    super.key,
    required this.topic,
    this.status,
    this.layer,
    this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Semantics(
      label:
          '${topic.title}, ${topic.level.label}, '
          '${status?.label ?? 'Belum'}',
      child: ListTile(
        onTap: onTap,
        contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
        title: Text(
          topic.title,
          style: theme.textTheme.titleSmall?.copyWith(
            fontWeight: FontWeight.w600,
          ),
        ),
        subtitle: Padding(
          padding: const EdgeInsets.only(top: 4),
          child: Row(
            children: [
              _LevelChip(level: topic.level),
              const SizedBox(width: 6),
              Text(
                '${topic.estimatedMinutes} menit',
                style: theme.textTheme.bodySmall?.copyWith(
                  color: theme.colorScheme.onSurfaceVariant,
                ),
              ),
              if (!topic.isActive) ...[
                const SizedBox(width: 6),
                Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 6,
                    vertical: 2,
                  ),
                  decoration: BoxDecoration(
                    color: theme.colorScheme.errorContainer,
                    borderRadius: BorderRadius.circular(4),
                  ),
                  child: Text(
                    'Diarsipkan',
                    style: TextStyle(
                      fontSize: 10,
                      color: theme.colorScheme.onErrorContainer,
                    ),
                  ),
                ),
              ],
            ],
          ),
        ),
        trailing: _StatusIndicator(status: status ?? LearningStatus.notStarted),
      ),
    );
  }
}

class _LevelChip extends StatelessWidget {
  final Difficulty level;

  const _LevelChip({required this.level});

  @override
  Widget build(BuildContext context) {
    final (Color bg, Color fg) = switch (level) {
      Difficulty.beginner => (const Color(0xFFDCFCE7), const Color(0xFF166534)),
      Difficulty.intermediate => (
        const Color(0xFFFEF3C7),
        const Color(0xFF92400E),
      ),
      Difficulty.advanced => (const Color(0xFFFEE2E2), const Color(0xFF991B1B)),
    };

    final isDark = Theme.of(context).brightness == Brightness.dark;
    final actualBg = isDark ? fg.withValues(alpha: 0.2) : bg;
    final actualFg = isDark ? bg : fg;

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
      decoration: BoxDecoration(
        color: actualBg,
        borderRadius: BorderRadius.circular(4),
      ),
      child: Text(
        level.label,
        style: TextStyle(
          fontSize: 10,
          fontWeight: FontWeight.w600,
          color: actualFg,
        ),
      ),
    );
  }
}

class _StatusIndicator extends StatelessWidget {
  final LearningStatus status;

  const _StatusIndicator({required this.status});

  @override
  Widget build(BuildContext context) {
    final (IconData icon, Color color, String label) = switch (status) {
      LearningStatus.notStarted => (
        Icons.circle_outlined,
        Colors.grey,
        'Belum',
      ),
      LearningStatus.inProgress => (Icons.timelapse, Colors.orange, 'Sedang'),
      LearningStatus.understood => (Icons.check_circle, Colors.green, 'Paham'),
    };

    return Semantics(
      label: 'Status: $label',
      excludeSemantics: true,
      child: Tooltip(
        message: label,
        child: Icon(icon, color: color, size: 22),
      ),
    );
  }
}
