// lib/features/learning_paths/path_detail_screen.dart — Detail view for curated
// and saved learning paths with prerequisite ordering, topic statuses,
// safe in-memory reading, duplicate-guarded path creation, and auto-refresh.

import 'package:flutter/material.dart';

import '../../data/content_repository.dart';
import '../../data/learning_repository.dart';
import '../../data/models.dart';
import '../../data/reading_time.dart';
import '../../state/app_state.dart';
import '../../theme/atlas_theme.dart';
import 'path_builder.dart';

class PathDetailScreen extends StatefulWidget {
  final String? presetKey;
  final int? pathId;
  final ContentRepository contentRepo;
  final LearningRepository learningRepo;
  final AppState appState;
  final void Function(
    String topicId, {
    String? pathId,
    String? pathName,
    List<String>? pathTopicIds,
    VoidCallback? onBackToPath,
  })
  onOpenTopic;

  const PathDetailScreen({
    super.key,
    this.presetKey,
    this.pathId,
    required this.contentRepo,
    required this.learningRepo,
    required this.appState,
    required this.onOpenTopic,
  });

  @override
  State<PathDetailScreen> createState() => _PathDetailScreenState();
}

class _PathDetailScreenState extends State<PathDetailScreen> {
  bool _loading = true;
  bool _isCreating = false;

  PathPreset? _preset;
  LearningPath? _savedPath;
  String _pathName = '';
  String _pathDescription = '';
  List<String> _topicIds = [];
  List<Topic> _topics = [];
  Map<String, Progress> _progressMap = {};

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    final allTopics = await widget.contentRepo.getAllActiveTopics();
    final topicMap = {for (final t in allTopics) t.id: t};
    final progressMap = await widget.learningRepo.getAllProgress();
    final allSavedPaths = await widget.learningRepo.getAllPaths();

    PathPreset? preset;
    LearningPath? savedPath;
    String name = '';
    String desc = '';
    List<String> topicIds = [];

    if (widget.presetKey != null) {
      preset = pathPresets[widget.presetKey];
      if (preset != null) {
        name = preset.name;
        desc = preset.description;

        // Requirement 1 & 2: Match existing saved path by goal AND name.
        // Multiple paths with the same goal: do not just take the first path by goal,
        // protect custom paths by requiring an exact goal & name match.
        // If duplicates exist, pick the latest updated one.
        final activePreset = preset;
        final matches = allSavedPaths
            .where(
              (p) => p.goal == activePreset.goal && p.name == activePreset.name,
            )
            .toList();
        if (matches.isNotEmpty) {
          matches.sort((a, b) => b.updatedAt.compareTo(a.updatedAt));
          savedPath = matches.first;
        }

        if (savedPath != null) {
          // Use saved topic ordering immediately
          topicIds = savedPath.items.map((i) => i.topicId).toList();
        } else {
          // Fallback to computed topological sort
          topicIds = await buildPathTopicList(
            preset.targetIds,
            widget.contentRepo,
          );
        }
      }
    } else if (widget.pathId != null) {
      for (final p in allSavedPaths) {
        if (p.id == widget.pathId) {
          savedPath = p;
          break;
        }
      }

      if (savedPath != null) {
        name = savedPath.name;
        topicIds = savedPath.items.map((i) => i.topicId).toList();
        if (pathPresets.containsKey(savedPath.goal)) {
          preset = pathPresets[savedPath.goal];
          desc = preset?.description ?? '';
        }
      }
    }

    final validTopics = topicIds
        .map((id) => topicMap[id])
        .whereType<Topic>()
        .toList();

    if (mounted) {
      setState(() {
        _preset = preset;
        _savedPath = savedPath;
        _pathName = name;
        _pathDescription = desc;
        _topicIds = topicIds;
        _topics = validTopics;
        _progressMap = progressMap;
        _loading = false;
      });
    }
  }

  int get _understoodCount {
    return _topics
        .where((t) => _progressMap[t.id]?.status == LearningStatus.understood)
        .length;
  }

  bool get _isAllUnderstood =>
      _topics.isNotEmpty && _understoodCount == _topics.length;

  Future<void> _handleStartOrContinue() async {
    if (_isCreating || _topics.isEmpty) return;
    setState(() => _isCreating = true);

    try {
      // Requirement 2: Prevent duplicate creation with concurrency guard and double-check
      if (_savedPath == null && _preset != null) {
        final existingPaths = await widget.learningRepo.getAllPaths();
        final matches = existingPaths
            .where((p) => p.goal == _preset!.goal && p.name == _preset!.name)
            .toList();

        if (matches.isNotEmpty) {
          matches.sort((a, b) => b.updatedAt.compareTo(a.updatedAt));
          _savedPath = matches.first;
        } else {
          final newId = await widget.learningRepo.createPath(
            name: _preset!.name,
            goal: _preset!.goal,
            topicIds: _topicIds,
          );
          _savedPath = await widget.learningRepo.getPath(newId);
        }
      }

      // Find first topic not yet understood
      String? targetTopicId;
      for (final topic in _topics) {
        final status = _progressMap[topic.id]?.status;
        if (status != LearningStatus.understood) {
          targetTopicId = topic.id;
          break;
        }
      }

      // If all understood, open first topic for review
      targetTopicId ??= _topics.first.id;

      if (mounted) {
        _openTopicWithContext(targetTopicId);
      }
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context)
            .showSnackBar(SnackBar(content: Text('Gagal memulai jalur: $e')));
      }
    } finally {
      if (mounted) {
        setState(() => _isCreating = false);
      }
    }
  }

  void _openTopicWithContext(String topicId) {
    widget.onOpenTopic(
      topicId,
      pathId: _savedPath?.id?.toString(),
      pathName: _pathName,
      pathTopicIds: _topicIds,
      onBackToPath: () {
        if (mounted) _load();
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final brightness = theme.brightness;

    return Scaffold(
      appBar: AppBar(
        title: Text(
          _pathName.isNotEmpty ? _pathName : 'Detail Jalur',
          style: const TextStyle(fontWeight: FontWeight.bold),
        ),
      ),
      body: _loading
          ? const Center(child: CircularProgressIndicator())
          : ListView(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
              children: [
                // Header Card
                _buildHeaderCard(theme, brightness),
                const SizedBox(height: 16),

                // Section Title
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      'Materi Terurut (${_topics.length} Topik)',
                      style: theme.textTheme.titleSmall?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    Text(
                      '$_understoodCount/${_topics.length} Paham',
                      style: theme.textTheme.bodySmall?.copyWith(
                        color: theme.colorScheme.onSurfaceVariant,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 8),

                // Topic List in Prerequisite Order
                for (int i = 0; i < _topics.length; i++) ...[
                  _buildTopicItem(
                    context: context,
                    index: i + 1,
                    topic: _topics[i],
                    theme: theme,
                    brightness: brightness,
                  ),
                  const SizedBox(height: 8),
                ],
                const SizedBox(height: 24),
              ],
            ),
    );
  }

  Widget _buildHeaderCard(ThemeData theme, Brightness brightness) {
    final understood = _understoodCount;
    final total = _topics.length;
    final progressFraction = total > 0
        ? (understood / total).clamp(0.0, 1.0)
        : 0.0;
    final isDone = _isAllUnderstood;

    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(
                    color: AtlasColors.primary(brightness)
                        .withValues(alpha: 0.12),
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: Icon(
                    Icons.route_outlined,
                    size: 22,
                    color: AtlasColors.primary(brightness),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        _pathName,
                        style: theme.textTheme.titleMedium?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      Text(
                        '$total topik sesuai urutan prasyarat',
                        style: theme.textTheme.bodySmall?.copyWith(
                          color: theme.colorScheme.onSurfaceVariant,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
            if (_pathDescription.isNotEmpty) ...[
              const SizedBox(height: 12),
              Text(
                _pathDescription,
                style: theme.textTheme.bodyMedium?.copyWith(
                  color: theme.colorScheme.onSurfaceVariant,
                  height: 1.4,
                ),
              ),
            ],
            const SizedBox(height: 16),
            ClipRRect(
              borderRadius: BorderRadius.circular(4),
              child: LinearProgressIndicator(
                value: progressFraction,
                minHeight: 6,
                backgroundColor: theme.colorScheme.surfaceContainerHighest,
                valueColor: AlwaysStoppedAnimation(
                  isDone
                      ? AtlasColors.mint(brightness)
                      : AtlasColors.primary(brightness),
                ),
              ),
            ),
            const SizedBox(height: 16),
            SizedBox(
              width: double.infinity,
              child: FilledButton.icon(
                onPressed: _isCreating ? null : _handleStartOrContinue,
                style: FilledButton.styleFrom(
                  backgroundColor: isDone
                      ? AtlasColors.mint(brightness)
                      : AtlasColors.primary(brightness),
                  padding: const EdgeInsets.symmetric(vertical: 12),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10),
                  ),
                ),
                icon: _isCreating
                    ? const SizedBox(
                        width: 18,
                        height: 18,
                        child: CircularProgressIndicator(
                          strokeWidth: 2,
                          color: Colors.white,
                        ),
                      )
                    : Icon(
                        isDone ? Icons.replay : Icons.play_arrow_rounded,
                        size: 20,
                      ),
                label: Text(
                  _isCreating
                      ? 'Menyiapkan Jalur...'
                      : isDone
                      ? 'Tinjau Materi'
                      : understood == 0
                      ? 'Mulai Belajar'
                      : 'Lanjutkan Belajar',
                  style: const TextStyle(fontWeight: FontWeight.bold),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildTopicItem({
    required BuildContext context,
    required int index,
    required Topic topic,
    required ThemeData theme,
    required Brightness brightness,
  }) {
    final progress = _progressMap[topic.id];
    final status = progress?.status ?? LearningStatus.notStarted;
    final readingTime = ReadingTimeEstimator.format(topic);

    Color statusBg;
    Color statusFg;
    String statusLabel;
    IconData statusIcon;

    switch (status) {
      case LearningStatus.understood:
        statusBg = AtlasColors.mint(brightness).withValues(alpha: 0.15);
        statusFg = AtlasColors.mint(brightness);
        statusLabel = 'Paham';
        statusIcon = Icons.check_circle;
        break;
      case LearningStatus.inProgress:
        statusBg = AtlasColors.amber(brightness).withValues(alpha: 0.15);
        statusFg = AtlasColors.amber(brightness);
        statusLabel = 'Sedang';
        statusIcon = Icons.timelapse;
        break;
      case LearningStatus.notStarted:
        statusBg = theme.colorScheme.surfaceContainerHighest.withValues(
          alpha: 0.5,
        );
        statusFg = theme.colorScheme.onSurfaceVariant;
        statusLabel = 'Belum';
        statusIcon = Icons.radio_button_unchecked;
        break;
    }

    return Card(
      child: InkWell(
        // Requirement 3: Tapping an article opens in-memory path context without saving to DB
        onTap: () => _openTopicWithContext(topic.id),
        borderRadius: BorderRadius.circular(12),
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
          child: Row(
            children: [
              // Index Circle
              Container(
                width: 28,
                height: 28,
                alignment: Alignment.center,
                decoration: BoxDecoration(
                  color: theme.colorScheme.surfaceContainerHighest,
                  shape: BoxShape.circle,
                ),
                child: Text(
                  '$index',
                  style: theme.textTheme.labelSmall?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              const SizedBox(width: 12),

              // Title and Reading Time
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      topic.title,
                      style: theme.textTheme.bodyMedium?.copyWith(
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                    const SizedBox(height: 2),
                    Text(
                      readingTime,
                      style: theme.textTheme.bodySmall?.copyWith(
                        color: theme.colorScheme.onSurfaceVariant,
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(width: 8),

              // Status Chip
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                decoration: BoxDecoration(
                  color: statusBg,
                  borderRadius: BorderRadius.circular(6),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(statusIcon, size: 13, color: statusFg),
                    const SizedBox(width: 4),
                    Text(
                      statusLabel,
                      style: theme.textTheme.labelSmall?.copyWith(
                        color: statusFg,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
