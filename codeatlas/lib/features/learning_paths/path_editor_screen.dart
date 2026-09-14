// lib/features/learning_paths/path_editor_screen.dart — F10: Edit path name,
// add/remove topics, reorder with prerequisite validation.

import 'package:flutter/material.dart';

import '../../data/content_repository.dart';
import '../../data/learning_repository.dart';
import '../../data/models.dart';
import 'path_builder.dart';

class PathEditorScreen extends StatefulWidget {
  final ContentRepository contentRepo;
  final LearningRepository learningRepo;
  final LearningPath? existingPath;
  final VoidCallback? onSaved;
  final void Function(String topicId)? onOpenTopic;

  const PathEditorScreen({
    super.key,
    required this.contentRepo,
    required this.learningRepo,
    this.existingPath,
    this.onSaved,
    this.onOpenTopic,
  });

  @override
  State<PathEditorScreen> createState() => _PathEditorScreenState();
}

class _PathEditorScreenState extends State<PathEditorScreen> {
  final _nameController = TextEditingController();
  List<String> _topicIds = [];
  List<Topic> _allTopics = [];
  Map<String, Topic> _topicMap = {};
  Map<String, Progress> _progressMap = {};
  bool _loading = true;
  bool _saving = false;

  bool get _isNew => widget.existingPath == null;

  @override
  void initState() {
    super.initState();
    _load();
  }

  @override
  void dispose() {
    _nameController.dispose();
    super.dispose();
  }

  Future<void> _load() async {
    final allTopics = await widget.contentRepo.getAllActiveTopics();
    final progress = await widget.learningRepo.getAllProgress();

    final topicMap = {for (final t in allTopics) t.id: t};

    if (widget.existingPath != null) {
      _nameController.text = widget.existingPath!.name;
      _topicIds = widget.existingPath!.items.map((i) => i.topicId).toList();
    }

    if (mounted) {
      setState(() {
        _allTopics = allTopics;
        _topicMap = topicMap;
        _progressMap = progress;
        _loading = false;
      });
    }
  }

  Future<void> _addTopic() async {
    final available = _allTopics
        .where((t) => !_topicIds.contains(t.id) && t.isActive)
        .toList();

    final selected = await showDialog<String>(
      context: context,
      builder: (context) =>
          _TopicPickerDialog(topics: available, progressMap: _progressMap),
    );

    if (selected == null) return;

    // Add the topic and its transitive prerequisites
    final prereqs = await widget.contentRepo.getTransitivePrerequisites(
      selected,
    );
    final newIds = <String>[];
    for (final prereq in prereqs) {
      if (!_topicIds.contains(prereq)) {
        newIds.add(prereq);
      }
    }
    newIds.add(selected);

    // Insert new IDs maintaining order
    final combined = [..._topicIds, ...newIds];
    // Validate and reorder
    final validOrder = await buildPathTopicList(combined, widget.contentRepo);

    setState(() => _topicIds = validOrder);
  }

  Future<void> _removeTopic(int index) async {
    final topicId = _topicIds[index];

    // Check if other topics in the path depend on this one
    final dependents = await checkRemovalDependents(
      topicId,
      _topicIds,
      widget.contentRepo,
    );

    if (dependents.isNotEmpty && mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(
            'Tidak bisa menghapus: dibutuhkan oleh ${dependents.join(", ")}. '
            'Hapus topik tersebut terlebih dahulu.',
          ),
          duration: const Duration(seconds: 3),
        ),
      );
      return;
    }

    setState(() => _topicIds.removeAt(index));
  }

  Future<void> _onReorderItem(int oldIndex, int newIndex) async {
    final movedId = _topicIds.removeAt(oldIndex);
    _topicIds.insert(newIndex, movedId);

    // Validate the new order
    final error = await validatePathOrder(_topicIds, widget.contentRepo);
    if (error != null) {
      // Revert
      _topicIds.removeAt(newIndex);
      _topicIds.insert(oldIndex, movedId);
      if (mounted) {
        ScaffoldMessenger.of(
          context,
        ).showSnackBar(SnackBar(content: Text('Urutan tidak valid: $error')));
      }
      return;
    }

    setState(() {});
  }

  Future<void> _save() async {
    final name = _nameController.text.trim();
    if (name.isEmpty || name.length > 100) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Nama jalur harus 1-100 karakter')),
      );
      return;
    }
    if (_topicIds.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Tambahkan minimal satu topik')),
      );
      return;
    }

    setState(() => _saving = true);

    try {
      if (_isNew) {
        await widget.learningRepo.createPath(
          name: name,
          goal: 'custom',
          topicIds: _topicIds,
        );
      } else {
        await widget.learningRepo.updatePath(
          pathId: widget.existingPath!.id!,
          name: name,
          topicIds: _topicIds,
        );
      }

      widget.onSaved?.call();
      if (mounted) Navigator.of(context).pop();
    } catch (e) {
      if (mounted) {
        setState(() => _saving = false);
        ScaffoldMessenger.of(context)
            .showSnackBar(SnackBar(content: Text('Gagal menyimpan: $e')));
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Scaffold(
      appBar: AppBar(
        title: Text(_isNew ? 'Buat Jalur Baru' : 'Edit Jalur'),
        actions: [
          TextButton.icon(
            onPressed: _saving ? null : _save,
            icon: _saving
                ? const SizedBox(
                    width: 16,
                    height: 16,
                    child: CircularProgressIndicator(strokeWidth: 2),
                  )
                : const Icon(Icons.save),
            label: const Text('Simpan'),
          ),
        ],
      ),
      body: _loading
          ? const Center(child: CircularProgressIndicator())
          : Column(
              children: [
                // Name field
                Padding(
                  padding: const EdgeInsets.all(16),
                  child: TextField(
                    controller: _nameController,
                    maxLength: 100,
                    decoration: const InputDecoration(
                      labelText: 'Nama jalur',
                      border: OutlineInputBorder(),
                      counterText: '',
                    ),
                  ),
                ),

                // Add topic button
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        '${_topicIds.length} topik',
                        style: theme.textTheme.labelLarge,
                      ),
                      TextButton.icon(
                        onPressed: _addTopic,
                        icon: const Icon(Icons.add),
                        label: const Text('Tambah topik'),
                      ),
                    ],
                  ),
                ),

                // Topic list with reorder
                Expanded(
                  child: _topicIds.isEmpty
                      ? Center(
                          child: Text(
                            'Belum ada topik. Klik "Tambah topik" untuk memulai.',
                            style: theme.textTheme.bodyMedium?.copyWith(
                              color: theme.colorScheme.onSurfaceVariant,
                            ),
                          ),
                        )
                      : ReorderableListView.builder(
                          padding: const EdgeInsets.only(bottom: 16),
                          itemCount: _topicIds.length,
                          onReorderItem: _onReorderItem,
                          itemBuilder: (context, index) {
                            final topicId = _topicIds[index];
                            final topic = _topicMap[topicId];
                            final progress = _progressMap[topicId];
                            final isUnderstood =
                                progress?.status == LearningStatus.understood;

                            return ListTile(
                              key: ValueKey(topicId),
                              leading: CircleAvatar(
                                radius: 14,
                                backgroundColor: isUnderstood
                                    ? Colors.green
                                    : theme.colorScheme.surfaceContainerHighest,
                                child: Text(
                                  '${index + 1}',
                                  style: TextStyle(
                                    fontSize: 12,
                                    color: isUnderstood
                                        ? Colors.white
                                        : theme.colorScheme.onSurface,
                                  ),
                                ),
                              ),
                              title: Text(
                                topic?.title ?? topicId,
                                style: TextStyle(
                                  decoration: isUnderstood
                                      ? TextDecoration.lineThrough
                                      : null,
                                ),
                              ),
                              subtitle: Text(
                                topic?.level.label ?? '',
                                style: theme.textTheme.bodySmall,
                              ),
                              trailing: Row(
                                mainAxisSize: MainAxisSize.min,
                                children: [
                                  if (widget.onOpenTopic != null)
                                    IconButton(
                                      icon: const Icon(
                                        Icons.open_in_new,
                                        size: 18,
                                      ),
                                      tooltip: 'Buka topik',
                                      onPressed: () =>
                                          widget.onOpenTopic!(topicId),
                                    ),
                                  IconButton(
                                    icon: const Icon(
                                      Icons.remove_circle_outline,
                                      size: 18,
                                    ),
                                    tooltip: 'Hapus dari jalur',
                                    onPressed: () => _removeTopic(index),
                                  ),
                                  const Icon(Icons.drag_handle),
                                ],
                              ),
                            );
                          },
                        ),
                ),
              ],
            ),
    );
  }
}

class _TopicPickerDialog extends StatefulWidget {
  final List<Topic> topics;
  final Map<String, Progress> progressMap;

  const _TopicPickerDialog({required this.topics, required this.progressMap});

  @override
  State<_TopicPickerDialog> createState() => _TopicPickerDialogState();
}

class _TopicPickerDialogState extends State<_TopicPickerDialog> {
  String _query = '';

  List<Topic> get _filtered {
    if (_query.isEmpty) return widget.topics;
    final q = _query.toLowerCase();
    return widget.topics.where((t) {
      return t.title.toLowerCase().contains(q) ||
          t.keywords.any((k) => k.toLowerCase().contains(q));
    }).toList();
  }

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      title: const Text('Pilih Topik'),
      content: SizedBox(
        width: double.maxFinite,
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            TextField(
              decoration: const InputDecoration(
                hintText: 'Cari topik...',
                prefixIcon: Icon(Icons.search),
                border: OutlineInputBorder(),
              ),
              onChanged: (v) => setState(() => _query = v),
            ),
            const SizedBox(height: 8),
            Flexible(
              child: ListView.builder(
                shrinkWrap: true,
                itemCount: _filtered.length,
                itemBuilder: (context, index) {
                  final topic = _filtered[index];
                  return ListTile(
                    title: Text(topic.title),
                    subtitle: Text(topic.level.label),
                    dense: true,
                    onTap: () => Navigator.pop(context, topic.id),
                  );
                },
              ),
            ),
          ],
        ),
      ),
      actions: [
        TextButton(
          onPressed: () => Navigator.pop(context),
          child: const Text('Batal'),
        ),
      ],
    );
  }
}
