// lib/features/learning_paths/paths_screen.dart — F10: List, create, and
// manage learning paths.

import 'package:flutter/material.dart';

import '../../data/content_repository.dart';
import '../../data/learning_repository.dart';
import '../../data/models.dart';
import '../../state/app_state.dart';
import 'path_builder.dart';
import 'path_editor_screen.dart';

class PathsScreen extends StatefulWidget {
  final ContentRepository contentRepo;
  final LearningRepository learningRepo;
  final AppState appState;
  final void Function(String topicId) onOpenTopic;

  const PathsScreen({
    super.key,
    required this.contentRepo,
    required this.learningRepo,
    required this.appState,
    required this.onOpenTopic,
  });

  @override
  State<PathsScreen> createState() => _PathsScreenState();
}

class _PathsScreenState extends State<PathsScreen> {
  List<LearningPath>? _paths;

  @override
  void initState() {
    super.initState();
    _loadPaths();
  }

  Future<void> _loadPaths() async {
    final paths = await widget.learningRepo.getAllPaths();
    if (mounted) setState(() => _paths = paths);
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Scaffold(
      appBar: AppBar(title: const Text('Jalur Belajar')),
      body: _paths == null
          ? const Center(child: CircularProgressIndicator())
          : _paths!.isEmpty
          ? _buildEmpty(theme)
          : _buildList(theme),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () => _showCreateDialog(context),
        icon: const Icon(Icons.add),
        label: const Text('Buat Jalur'),
      ),
    );
  }

  Widget _buildEmpty(ThemeData theme) {
    return Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(
            Icons.route_outlined,
            size: 64,
            color: theme.colorScheme.onSurfaceVariant,
          ),
          const SizedBox(height: 12),
          Text('Belum ada jalur belajar', style: theme.textTheme.titleMedium),
          const SizedBox(height: 8),
          Text(
            'Buat jalur sesuai tujuanmu atau gunakan preset.',
            style: theme.textTheme.bodyMedium?.copyWith(
              color: theme.colorScheme.onSurfaceVariant,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildList(ThemeData theme) {
    return ListView.builder(
      padding: const EdgeInsets.only(bottom: 80, top: 8, left: 12, right: 12),
      itemCount: _paths!.length,
      itemBuilder: (context, index) {
        final path = _paths![index];
        return _PathCard(
          path: path,
          learningRepo: widget.learningRepo,
          onTap: () => _openPathDetail(path),
          onDelete: () => _deletePath(path),
          onContinue: () => _continuePath(path),
        );
      },
    );
  }

  Future<void> _showCreateDialog(BuildContext context) async {
    final theme = Theme.of(context);

    final result = await showModalBottomSheet<String>(
      context: context,
      isScrollControlled: true,
      builder: (context) {
        return DraggableScrollableSheet(
          initialChildSize: 0.7,
          maxChildSize: 0.9,
          minChildSize: 0.3,
          expand: false,
          builder: (context, scrollController) {
            return Padding(
              padding: const EdgeInsets.all(16),
              child: ListView(
                controller: scrollController,
                children: [
                  Text(
                    'Pilih Tujuan',
                    style: theme.textTheme.titleLarge?.copyWith(
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 16),
                  for (final entry in pathPresets.entries) ...[
                    Card(
                      child: ListTile(
                        title: Text(entry.value.name),
                        subtitle: Text(entry.value.description),
                        trailing: const Icon(Icons.arrow_forward_ios, size: 16),
                        onTap: () => Navigator.pop(context, entry.key),
                      ),
                    ),
                    const SizedBox(height: 4),
                  ],
                  const Divider(),
                  Card(
                    child: ListTile(
                      leading: const Icon(Icons.edit),
                      title: const Text('Buat sendiri'),
                      subtitle: const Text(
                        'Pilih topik yang ingin dipelajari secara manual.',
                      ),
                      onTap: () => Navigator.pop(context, 'custom'),
                    ),
                  ),
                ],
              ),
            );
          },
        );
      },
    );

    if (result == null || !mounted) return;

    if (result == 'custom') {
      _openCustomEditor();
    } else {
      await _createFromPreset(result);
    }
  }

  Future<void> _createFromPreset(String presetKey) async {
    final preset = pathPresets[presetKey];
    if (preset == null) return;

    try {
      final topicIds = await buildPathTopicList(
        preset.targetIds,
        widget.contentRepo,
      );

      if (topicIds.isEmpty) {
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Tidak ada topik yang tersedia')),
          );
        }
        return;
      }

      await widget.learningRepo.createPath(
        name: preset.name,
        goal: preset.goal,
        topicIds: topicIds,
      );

      _loadPaths();
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context)
            .showSnackBar(SnackBar(content: Text('Gagal membuat jalur: $e')));
      }
    }
  }

  void _openCustomEditor() {
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) => PathEditorScreen(
          contentRepo: widget.contentRepo,
          learningRepo: widget.learningRepo,
          onSaved: _loadPaths,
        ),
      ),
    );
  }

  void _openPathDetail(LearningPath path) {
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) => PathEditorScreen(
          contentRepo: widget.contentRepo,
          learningRepo: widget.learningRepo,
          existingPath: path,
          onSaved: _loadPaths,
          onOpenTopic: widget.onOpenTopic,
        ),
      ),
    );
  }

  Future<void> _deletePath(LearningPath path) async {
    final confirmed = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Hapus jalur?'),
        content: Text(
          'Jalur "${path.name}" akan dihapus. '
          'Progress dan catatan topik tetap tersimpan.',
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: const Text('Batal'),
          ),
          FilledButton(
            onPressed: () => Navigator.pop(context, true),
            style: FilledButton.styleFrom(
              backgroundColor: Theme.of(context).colorScheme.error,
            ),
            child: const Text('Hapus'),
          ),
        ],
      ),
    );

    if (confirmed == true && path.id != null) {
      await widget.learningRepo.deletePath(path.id!);
      _loadPaths();
    }
  }

  Future<void> _continuePath(LearningPath path) async {
    if (path.id == null) return;
    final nextTopic = await widget.learningRepo.getNextUnfinishedTopic(
      path.id!,
    );
    if (nextTopic != null) {
      widget.onOpenTopic(nextTopic);
    } else {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('Semua topik di jalur sudah Paham!')),
        );
      }
    }
  }
}

class _PathCard extends StatelessWidget {
  final LearningPath path;
  final LearningRepository learningRepo;
  final VoidCallback onTap;
  final VoidCallback onDelete;
  final VoidCallback onContinue;

  const _PathCard({
    required this.path,
    required this.learningRepo,
    required this.onTap,
    required this.onDelete,
    required this.onContinue,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Card(
      margin: const EdgeInsets.only(bottom: 8),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(12),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Expanded(
                    child: Text(
                      path.name,
                      style: theme.textTheme.titleSmall?.copyWith(
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ),
                  IconButton(
                    icon: const Icon(Icons.delete_outline, size: 20),
                    tooltip: 'Hapus jalur',
                    onPressed: onDelete,
                  ),
                ],
              ),
              Text(
                '${path.items.length} topik',
                style: theme.textTheme.bodySmall?.copyWith(
                  color: theme.colorScheme.onSurfaceVariant,
                ),
              ),
              const SizedBox(height: 8),
              FutureBuilder<int>(
                future: _countUnderstood(),
                builder: (context, snap) {
                  final understood = snap.data ?? 0;
                  final total = path.items.length;
                  final pct = total > 0 ? understood / total : 0.0;
                  return Column(
                    children: [
                      ClipRRect(
                        borderRadius: BorderRadius.circular(4),
                        child: LinearProgressIndicator(
                          value: pct,
                          minHeight: 4,
                        ),
                      ),
                      const SizedBox(height: 4),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Text(
                            '$understood/$total Paham',
                            style: theme.textTheme.bodySmall,
                          ),
                          if (understood < total)
                            TextButton.icon(
                              onPressed: onContinue,
                              icon: const Icon(Icons.play_arrow, size: 16),
                              label: const Text('Lanjutkan'),
                            ),
                        ],
                      ),
                    ],
                  );
                },
              ),
            ],
          ),
        ),
      ),
    );
  }

  Future<int> _countUnderstood() async {
    int count = 0;
    for (final item in path.items) {
      final progress = await learningRepo.getProgress(item.topicId);
      if (progress?.status == LearningStatus.understood) count++;
    }
    return count;
  }
}
