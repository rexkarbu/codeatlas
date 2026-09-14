// lib/features/roadmap/roadmap_screen.dart — Progressive Multi-Level Roadmap:
// Level 1: Layer & Group Cards overview with progress and descriptions.
// Level 2: Vertical group topic flow with true prerequisite connectors.
// Level 3: Topic focus panel with cross-group jump chips & navigation history.
// Level 4: Accessible relational list alternative.

import 'package:flutter/material.dart';

import '../../data/content_repository.dart';
import '../../data/learning_repository.dart';
import '../../data/models.dart';

class RoadmapScreen extends StatefulWidget {
  final ContentRepository contentRepo;
  final LearningRepository learningRepo;
  final void Function(String topicId) onOpenTopic;

  const RoadmapScreen({
    super.key,
    required this.contentRepo,
    required this.learningRepo,
    required this.onOpenTopic,
  });

  @override
  State<RoadmapScreen> createState() => _RoadmapScreenState();
}

class _RoadmapScreenState extends State<RoadmapScreen> {
  bool _showListView = false;
  ContentLayer _layerFilter = ContentLayer.fundamentals;
  Category? _selectedGroup;
  String? _selectedTopicId;

  // Navigation history for cross-group jumps
  final List<Category> _groupHistory = [];

  List<Topic> _topics = [];
  List<Category> _groups = [];
  Map<String, Category> _categoryMap = {};
  Map<String, Set<String>> _groupDomainIds = {};
  Map<String, List<String>> _prerequisiteGraph = {};
  Map<String, Progress> _progressMap = {};
  bool _loading = true;

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    final allTopics = await widget.contentRepo.getAllActiveTopics();
    final allCategories = await widget.contentRepo.getAllCategories();
    final prereqGraph = await widget.contentRepo.getPrerequisiteGraph();
    final progress = await widget.learningRepo.getAllProgress();

    final categoryMap = <String, Category>{};
    final groupDomainIds = <String, Set<String>>{};
    for (final c in allCategories) {
      categoryMap[c.id] = c;
      if (c.parentId != null) {
        groupDomainIds.putIfAbsent(c.parentId!, () => {}).add(c.id);
      }
    }

    final groups =
        allCategories.where((c) => c.kind == CategoryKind.group).toList()
          ..sort((a, b) => a.sortOrder.compareTo(b.sortOrder));

    if (mounted) {
      setState(() {
        _topics = allTopics;
        _groups = groups;
        _categoryMap = categoryMap;
        _groupDomainIds = groupDomainIds;
        _prerequisiteGraph = prereqGraph;
        _progressMap = progress;
        _loading = false;
      });
    }
  }

  @override
  void didUpdateWidget(covariant RoadmapScreen oldWidget) {
    super.didUpdateWidget(oldWidget);
    _load();
  }

  // Helper to find parent group of any topic
  Category? _getGroupForTopic(Topic topic) {
    final cat = _categoryMap[topic.categoryId];
    if (cat == null) return null;
    if (cat.kind == CategoryKind.group) return cat;
    if (cat.parentId != null) return _categoryMap[cat.parentId];
    return null;
  }

  // Get topics belonging to a specific group (direct or via domain children)
  List<Topic> _getTopicsInGroup(Category group) {
    final domainIds = _groupDomainIds[group.id] ?? <String>{};
    final groupTopics = _topics.where((t) {
      return t.categoryId == group.id || domainIds.contains(t.categoryId);
    }).toList();

    // Sort topologically using prerequisites within group + sortOrder
    groupTopics.sort((a, b) {
      final aPrereqs = _prerequisiteGraph[a.id] ?? [];
      final bPrereqs = _prerequisiteGraph[b.id] ?? [];
      if (aPrereqs.contains(b.id)) return 1;
      if (bPrereqs.contains(a.id)) return -1;
      final sc = a.sortOrder.compareTo(b.sortOrder);
      return sc != 0 ? sc : a.title.compareTo(b.title);
    });

    return groupTopics;
  }

  // Calculate group progress stats
  _GroupStats _getGroupStats(Category group) {
    final topics = _getTopicsInGroup(group);
    var understood = 0;
    var inProgress = 0;
    for (final t in topics) {
      final status = _progressMap[t.id]?.status ?? LearningStatus.notStarted;
      if (status == LearningStatus.understood) understood++;
      if (status == LearningStatus.inProgress) inProgress++;
    }
    return _GroupStats(
      totalTopics: topics.length,
      understoodTopics: understood,
      inProgressTopics: inProgress,
    );
  }

  // Cross-group jump action
  void _jumpToTopic(String topicId) {
    final targetTopic = _topics.where((t) => t.id == topicId).firstOrNull;
    if (targetTopic == null) return;
    final targetGroup = _getGroupForTopic(targetTopic);
    if (targetGroup == null) return;

    setState(() {
      if (_selectedGroup != null && _selectedGroup!.id != targetGroup.id) {
        _groupHistory.add(_selectedGroup!);
      }
      _layerFilter = targetGroup.layer;
      _selectedGroup = targetGroup;
      _selectedTopicId = topicId;
    });
  }

  // Back button handling in Group View
  void _goBack() {
    setState(() {
      if (_groupHistory.isNotEmpty) {
        _selectedGroup = _groupHistory.removeLast();
        _layerFilter = _selectedGroup!.layer;
        _selectedTopicId = null;
      } else {
        _selectedGroup = null;
        _selectedTopicId = null;
      }
    });
  }

  void _showGroupPickerBottomSheet() {
    final groupsInLayer = _groups
        .where((g) => g.layer == _layerFilter)
        .toList();
    showModalBottomSheet<void>(
      context: context,
      isScrollControlled: true,
      builder: (context) {
        return SafeArea(
          child: Padding(
            padding: const EdgeInsets.symmetric(vertical: 16),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Padding(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 20,
                    vertical: 8,
                  ),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        'Pilih Kelompok Materi',
                        style: Theme.of(context).textTheme.titleMedium
                            ?.copyWith(fontWeight: FontWeight.bold),
                      ),
                      IconButton(
                        icon: const Icon(Icons.close),
                        onPressed: () => Navigator.pop(context),
                      ),
                    ],
                  ),
                ),
                const Divider(),
                Flexible(
                  child: ListView.builder(
                    shrinkWrap: true,
                    itemCount: groupsInLayer.length,
                    itemBuilder: (context, index) {
                      final g = groupsInLayer[index];
                      final isCurrent = _selectedGroup?.id == g.id;
                      final stats = _getGroupStats(g);
                      return ListTile(
                        leading: Icon(
                          isCurrent
                              ? Icons.check_circle
                              : Icons.folder_outlined,
                          color: isCurrent
                              ? Theme.of(context).colorScheme.primary
                              : null,
                        ),
                        title: Text(
                          g.title,
                          style: TextStyle(
                            fontWeight: isCurrent
                                ? FontWeight.bold
                                : FontWeight.normal,
                          ),
                        ),
                        subtitle: Text(
                          '${stats.totalTopics} topik • ${stats.understoodTopics} dipahami',
                        ),
                        selected: isCurrent,
                        onTap: () {
                          Navigator.pop(context);
                          setState(() {
                            if (_selectedGroup?.id != g.id) {
                              _groupHistory.clear();
                              _selectedGroup = g;
                              _selectedTopicId = null;
                            }
                          });
                        },
                      );
                    },
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    if (_loading) {
      return Scaffold(
        appBar: AppBar(title: const Text('Peta Topik')),
        body: const Center(child: CircularProgressIndicator()),
      );
    }

    return Scaffold(
      appBar: AppBar(
        title: Text(
          _selectedGroup == null ? 'Peta Pembelajaran' : _selectedGroup!.title,
        ),
        leading: _selectedGroup != null
            ? IconButton(
                icon: const Icon(Icons.arrow_back),
                tooltip: 'Kembali ke Semua Kelompok',
                onPressed: _goBack,
              )
            : null,
        actions: [
          IconButton(
            icon: Icon(_showListView ? Icons.account_tree : Icons.list),
            tooltip: _showListView
                ? 'Tampilan grafik kelompok'
                : 'Tampilan daftar relasi',
            onPressed: () {
              setState(() => _showListView = !_showListView);
            },
          ),
        ],
      ),
      body: _showListView
          ? _buildAccessibleListView(theme)
          : (_selectedGroup == null
                ? _buildInitialOverview(theme)
                : _buildGroupDetailView(theme)),
    );
  }

  // ─────────────────────────────────────────────────────────
  // 1. TAMPILAN AWAL: Daftar Kartu Kelompok
  // ─────────────────────────────────────────────────────────
  Widget _buildInitialOverview(ThemeData theme) {
    final groupsInLayer = _groups
        .where((g) => g.layer == _layerFilter)
        .toList();

    return Column(
      children: [
        // Layer Selector (Wrap ensures no overflow on 360px width or 200% text scale)
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
          decoration: BoxDecoration(
            color: theme.colorScheme.surfaceContainerHighest.withValues(
              alpha: 0.3,
            ),
            border: Border(
              bottom: BorderSide(
                color: theme.dividerColor.withValues(alpha: 0.2),
              ),
            ),
          ),
          child: Wrap(
            spacing: 8,
            runSpacing: 8,
            crossAxisAlignment: WrapCrossAlignment.center,
            alignment: WrapAlignment.spaceBetween,
            children: [
              Wrap(
                spacing: 8,
                runSpacing: 8,
                crossAxisAlignment: WrapCrossAlignment.center,
                children: [
                  FilterChip(
                    label: const Text('Fundamental'),
                    selected: _layerFilter == ContentLayer.fundamentals,
                    avatar: Icon(
                      Icons.menu_book,
                      size: 16,
                      color: _layerFilter == ContentLayer.fundamentals
                          ? theme.colorScheme.onSecondaryContainer
                          : null,
                    ),
                    onSelected: (selected) {
                      if (selected) {
                        setState(() {
                          _layerFilter = ContentLayer.fundamentals;
                          _selectedTopicId = null;
                        });
                      }
                    },
                  ),
                  FilterChip(
                    label: const Text('Ekosistem'),
                    selected: _layerFilter == ContentLayer.ecosystem,
                    avatar: Icon(
                      Icons.hub,
                      size: 16,
                      color: _layerFilter == ContentLayer.ecosystem
                          ? theme.colorScheme.onSecondaryContainer
                          : null,
                    ),
                    onSelected: (selected) {
                      if (selected) {
                        setState(() {
                          _layerFilter = ContentLayer.ecosystem;
                          _selectedTopicId = null;
                        });
                      }
                    },
                  ),
                ],
              ),
              Padding(
                padding: const EdgeInsets.symmetric(vertical: 4),
                child: Text(
                  '${groupsInLayer.length} Kelompok',
                  style: theme.textTheme.labelMedium?.copyWith(
                    color: theme.colorScheme.onSurfaceVariant,
                  ),
                ),
              ),
            ],
          ),
        ),

        // List of Group Cards
        Expanded(
          child: ListView.builder(
            padding: const EdgeInsets.all(16),
            itemCount: groupsInLayer.length,
            itemBuilder: (context, index) {
              final group = groupsInLayer[index];
              final stats = _getGroupStats(group);
              final progressFraction = stats.totalTopics > 0
                  ? stats.understoodTopics / stats.totalTopics
                  : 0.0;

              return Card(
                elevation: 1,
                margin: const EdgeInsets.only(bottom: 12),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(12),
                  side: BorderSide(
                    color: theme.colorScheme.outlineVariant.withValues(
                      alpha: 0.4,
                    ),
                  ),
                ),
                child: InkWell(
                  borderRadius: BorderRadius.circular(12),
                  onTap: () {
                    setState(() {
                      _selectedGroup = group;
                      _selectedTopicId = null;
                    });
                  },
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
                                color: theme.colorScheme.primaryContainer
                                    .withValues(alpha: 0.6),
                                borderRadius: BorderRadius.circular(8),
                              ),
                              child: Icon(
                                _layerFilter == ContentLayer.fundamentals
                                    ? Icons.terminal
                                    : Icons.layers,
                                size: 20,
                                color: theme.colorScheme.primary,
                              ),
                            ),
                            const SizedBox(width: 12),
                            Expanded(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(
                                    group.title,
                                    style: theme.textTheme.titleMedium
                                        ?.copyWith(fontWeight: FontWeight.bold),
                                  ),
                                  const SizedBox(height: 2),
                                  Text(
                                    '${stats.totalTopics} Topik',
                                    style: theme.textTheme.bodySmall?.copyWith(
                                      color: theme.colorScheme.onSurfaceVariant,
                                    ),
                                  ),
                                ],
                              ),
                            ),
                            const Icon(Icons.arrow_forward_ios, size: 16),
                          ],
                        ),
                        if (group.description.isNotEmpty) ...[
                          const SizedBox(height: 10),
                          Text(
                            group.description,
                            style: theme.textTheme.bodyMedium?.copyWith(
                              color: theme.colorScheme.onSurfaceVariant,
                            ),
                            maxLines: 2,
                            overflow: TextOverflow.ellipsis,
                          ),
                        ],
                        const SizedBox(height: 12),
                        Row(
                          children: [
                            Expanded(
                              child: ClipRRect(
                                borderRadius: BorderRadius.circular(4),
                                child: LinearProgressIndicator(
                                  value: progressFraction,
                                  minHeight: 6,
                                  backgroundColor:
                                      theme.colorScheme.surfaceContainerHighest,
                                ),
                              ),
                            ),
                            const SizedBox(width: 12),
                            Text(
                              '${stats.understoodTopics}/${stats.totalTopics} Dipahami',
                              style: theme.textTheme.labelSmall?.copyWith(
                                fontWeight: FontWeight.w600,
                                color: stats.understoodTopics > 0
                                    ? Colors.green.shade700
                                    : theme.colorScheme.onSurfaceVariant,
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
          ),
        ),
      ],
    );
  }

  // ─────────────────────────────────────────────────────────
  // 2. TAMPILAN KELOMPOK: Alur Vertikal Topik & Hubungan Prasyarat
  // ─────────────────────────────────────────────────────────
  Widget _buildGroupDetailView(ThemeData theme) {
    final group = _selectedGroup!;
    final groupTopics = _getTopicsInGroup(group);

    return Column(
      children: [
        // Navigation bar within group
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
          decoration: BoxDecoration(
            color: theme.colorScheme.surfaceContainerHighest.withValues(
              alpha: 0.3,
            ),
            border: Border(
              bottom: BorderSide(
                color: theme.dividerColor.withValues(alpha: 0.2),
              ),
            ),
          ),
          child: Wrap(
            spacing: 8,
            runSpacing: 8,
            alignment: WrapAlignment.spaceBetween,
            crossAxisAlignment: WrapCrossAlignment.center,
            children: [
              Text(
                '${_layerFilter == ContentLayer.fundamentals ? "Fundamental" : "Ekosistem"} • ${groupTopics.length} Topik',
                style: theme.textTheme.bodySmall?.copyWith(
                  color: theme.colorScheme.onSurfaceVariant,
                  fontWeight: FontWeight.w500,
                ),
              ),
              OutlinedButton.icon(
                icon: const Icon(Icons.swap_vert, size: 16),
                label: const Text('Ganti Kelompok'),
                style: OutlinedButton.styleFrom(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 12,
                    vertical: 6,
                  ),
                  visualDensity: VisualDensity.compact,
                ),
                onPressed: _showGroupPickerBottomSheet,
              ),
            ],
          ),
        ),

        // Vertical list of topics with true prerequisite connectors
        Expanded(
          child: ListView.builder(
            padding: const EdgeInsets.fromLTRB(16, 16, 16, 120),
            itemCount: groupTopics.length,
            itemBuilder: (context, index) {
              final topic = groupTopics[index];
              final isSelected = _selectedTopicId == topic.id;
              final progress = _progressMap[topic.id];
              final status = progress?.status ?? LearningStatus.notStarted;

              // Find prerequisites
              final allPrereqIds = _prerequisiteGraph[topic.id] ?? <String>[];
              final internalPrereqIds = allPrereqIds.where((pid) {
                return groupTopics.any((t) => t.id == pid);
              }).toList();
              final externalPrereqIds = allPrereqIds.where((pid) {
                return !groupTopics.any((t) => t.id == pid);
              }).toList();

              return Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Draw incoming connector only if it has internal prerequisites
                  if (internalPrereqIds.isNotEmpty)
                    Padding(
                      padding: const EdgeInsets.only(left: 32, bottom: 4),
                      child: Row(
                        children: [
                          Icon(
                            Icons.arrow_downward,
                            size: 16,
                            color: theme.colorScheme.primary,
                          ),
                          const SizedBox(width: 8),
                          Expanded(
                            child: Text(
                              'Prasyarat: ${internalPrereqIds.map((id) => _topics.where((t) => t.id == id).firstOrNull?.title ?? id).join(", ")}',
                              maxLines: 1,
                              overflow: TextOverflow.ellipsis,
                              style: theme.textTheme.labelSmall?.copyWith(
                                color: theme.colorScheme.primary,
                                fontStyle: FontStyle.italic,
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),

                  // Topic Card
                  Card(
                    elevation: isSelected ? 3 : 1,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(12),
                      side: BorderSide(
                        color: isSelected
                            ? theme.colorScheme.primary
                            : theme.colorScheme.outlineVariant.withValues(
                                alpha: 0.5,
                              ),
                        width: isSelected ? 2 : 1,
                      ),
                    ),
                    color: isSelected
                        ? theme.colorScheme.primaryContainer.withValues(
                            alpha: 0.2,
                          )
                        : null,
                    child: InkWell(
                      borderRadius: BorderRadius.circular(12),
                      onTap: () {
                        setState(() {
                          _selectedTopicId = topic.id;
                        });
                      },
                      child: Padding(
                        padding: const EdgeInsets.all(14),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Row(
                              children: [
                                _buildStatusIcon(status),
                                const SizedBox(width: 10),
                                Expanded(
                                  child: Text(
                                    topic.title,
                                    style: theme.textTheme.titleMedium
                                        ?.copyWith(
                                          fontWeight: FontWeight.bold,
                                          color: isSelected
                                              ? theme.colorScheme.primary
                                              : null,
                                        ),
                                  ),
                                ),
                                _buildDifficultyBadge(topic.level, theme),
                              ],
                            ),
                            if (topic.summary.isNotEmpty) ...[
                              const SizedBox(height: 6),
                              Text(
                                topic.summary,
                                style: theme.textTheme.bodySmall?.copyWith(
                                  color: theme.colorScheme.onSurfaceVariant,
                                ),
                                maxLines: 2,
                                overflow: TextOverflow.ellipsis,
                              ),
                            ],

                            // External Prerequisite Chips (Cross-group jumps)
                            if (externalPrereqIds.isNotEmpty) ...[
                              const SizedBox(height: 10),
                              Wrap(
                                spacing: 6,
                                runSpacing: 4,
                                children: [
                                  for (final extPid in externalPrereqIds) ...[
                                    Builder(
                                      builder: (context) {
                                        final extTopic = _topics
                                            .where((t) => t.id == extPid)
                                            .firstOrNull;
                                        final extGroup = extTopic != null
                                            ? _getGroupForTopic(extTopic)
                                            : null;
                                        final groupName =
                                            extGroup?.title ?? 'Lain';
                                        final topicName =
                                            extTopic?.title ?? extPid;
                                        return ActionChip(
                                          avatar: const Icon(
                                            Icons.call_made,
                                            size: 14,
                                          ),
                                          label: Text(
                                            'Dari $groupName: $topicName',
                                            style: const TextStyle(
                                              fontSize: 11,
                                            ),
                                          ),
                                          onPressed: () => _jumpToTopic(extPid),
                                        );
                                      },
                                    ),
                                  ],
                                ],
                              ),
                            ],
                          ],
                        ),
                      ),
                    ),
                  ),

                  const SizedBox(height: 12),
                ],
              );
            },
          ),
        ),

        // Bottom Detail Focus Panel (Active when a topic is selected)
        if (_selectedTopicId != null) _buildFocusPanel(theme),
      ],
    );
  }

  // ─────────────────────────────────────────────────────────
  // 3. FOKUS SATU TOPIK: Detail Panel & Action
  // ─────────────────────────────────────────────────────────
  Widget _buildFocusPanel(ThemeData theme) {
    final topic = _topics.where((t) => t.id == _selectedTopicId).firstOrNull;
    if (topic == null) return const SizedBox.shrink();

    final status = _progressMap[topic.id]?.status ?? LearningStatus.notStarted;
    final prereqs = _prerequisiteGraph[topic.id] ?? <String>[];
    final dependents = <String>[];
    for (final entry in _prerequisiteGraph.entries) {
      if (entry.value.contains(topic.id)) {
        dependents.add(entry.key);
      }
    }

    final screenHeight = MediaQuery.maybeSizeOf(context)?.height ?? 0;
    final maxPanelHeight = screenHeight > 100 ? screenHeight * 0.7 : 500.0;

    return Container(
      width: double.infinity,
      constraints: BoxConstraints(
        maxHeight: maxPanelHeight,
      ),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: theme.colorScheme.surface,
        borderRadius: const BorderRadius.vertical(top: Radius.circular(20)),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.15),
            blurRadius: 10,
            offset: const Offset(0, -2),
          ),
        ],
      ),
      child: SafeArea(
        child: SingleChildScrollView(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
            Row(
              children: [
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        topic.title,
                        style: theme.textTheme.titleMedium?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      const SizedBox(height: 2),
                      Row(
                        children: [
                          _buildStatusIcon(status),
                          const SizedBox(width: 6),
                          Text(
                            status.label,
                            style: theme.textTheme.bodySmall?.copyWith(
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
                IconButton(
                  icon: const Icon(Icons.close),
                  tooltip: 'Tutup panel',
                  onPressed: () => setState(() => _selectedTopicId = null),
                ),
              ],
            ),
            const SizedBox(height: 8),
            Text(
              topic.summary,
              style: theme.textTheme.bodySmall?.copyWith(
                color: theme.colorScheme.onSurfaceVariant,
              ),
            ),
            const SizedBox(height: 10),

            // Prerequisites row
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Prasyarat: ',
                  style: theme.textTheme.labelSmall?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
                ),
                Expanded(
                  child: prereqs.isEmpty
                      ? Text(
                          'Tidak ada (langsung dipelajari)',
                          style: theme.textTheme.labelSmall,
                        )
                      : Wrap(
                          spacing: 4,
                          runSpacing: 4,
                          children: [
                            for (final pid in prereqs)
                              ActionChip(
                                label: Text(
                                  _topics
                                          .where((t) => t.id == pid)
                                          .firstOrNull
                                          ?.title ??
                                      pid,
                                  style: const TextStyle(fontSize: 10),
                                ),
                                onPressed: () => _jumpToTopic(pid),
                              ),
                          ],
                        ),
                ),
              ],
            ),
            const SizedBox(height: 6),

            // Dependents row
            if (dependents.isNotEmpty)
              Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Dibutuhkan oleh: ',
                    style: theme.textTheme.labelSmall?.copyWith(
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  Expanded(
                    child: Wrap(
                      spacing: 4,
                      runSpacing: 4,
                      children: [
                        for (final did in dependents)
                          ActionChip(
                            label: Text(
                              _topics
                                      .where((t) => t.id == did)
                                      .firstOrNull
                                      ?.title ??
                                  did,
                              style: const TextStyle(fontSize: 10),
                            ),
                            onPressed: () => _jumpToTopic(did),
                          ),
                      ],
                    ),
                  ),
                ],
              ),

            const SizedBox(height: 14),
            SizedBox(
              width: double.infinity,
              child: FilledButton.icon(
                icon: const Icon(Icons.menu_book),
                label: const Text('Buka Artikel'),
                onPressed: () => widget.onOpenTopic(topic.id),
              ),
            ),
          ],
        ),
      ),
    ),
  );
}

  // ─────────────────────────────────────────────────────────
  // 4. AKSESIBILITAS: Daftar Teks Bertingkat Alternatif
  // ─────────────────────────────────────────────────────────
  Widget _buildAccessibleListView(ThemeData theme) {
    final topicsInLayer = _topics.where((t) {
      final cat = _categoryMap[t.categoryId];
      return cat?.layer == _layerFilter;
    }).toList();

    return Column(
      children: [
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
          color: theme.colorScheme.surfaceContainerHighest.withValues(
            alpha: 0.4,
          ),
          child: Row(
            children: [
              Expanded(
                child: Text(
                  'Daftar Relasi Lengkap (${_layerFilter == ContentLayer.fundamentals ? "Fundamental" : "Ekosistem"})',
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: theme.textTheme.titleSmall?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              const SizedBox(width: 8),
              Text(
                '${topicsInLayer.length} topik',
                style: theme.textTheme.bodySmall,
              ),
            ],
          ),
        ),
        Expanded(
          child: ListView.builder(
            padding: const EdgeInsets.all(16),
            itemCount: topicsInLayer.length,
            itemBuilder: (context, index) {
              final topic = topicsInLayer[index];
              final prereqs = _prerequisiteGraph[topic.id] ?? [];
              final status =
                  _progressMap[topic.id]?.status ?? LearningStatus.notStarted;

              return Card(
                margin: const EdgeInsets.only(bottom: 8),
                child: ListTile(
                  leading: _buildStatusIcon(status),
                  title: Text(
                    topic.title,
                    style: const TextStyle(fontWeight: FontWeight.bold),
                  ),
                  subtitle: Text(
                    prereqs.isEmpty
                        ? 'Prasyarat: Tidak ada'
                        : 'Prasyarat: ${prereqs.map((pid) => _topics.where((t) => t.id == pid).firstOrNull?.title ?? pid).join(", ")}',
                  ),
                  trailing: const Icon(Icons.chevron_right),
                  onTap: () => widget.onOpenTopic(topic.id),
                ),
              );
            },
          ),
        ),
      ],
    );
  }

  // ─────────────────────────────────────────────────────────
  // WIDGET HELPERS
  // ─────────────────────────────────────────────────────────
  Widget _buildStatusIcon(LearningStatus status) {
    switch (status) {
      case LearningStatus.understood:
        return const Icon(Icons.check_circle, color: Colors.green, size: 20);
      case LearningStatus.inProgress:
        return const Icon(Icons.timelapse, color: Colors.orange, size: 20);
      case LearningStatus.notStarted:
        return const Icon(
          Icons.radio_button_unchecked,
          color: Colors.grey,
          size: 20,
        );
    }
  }

  Widget _buildDifficultyBadge(Difficulty level, ThemeData theme) {
    final (label, color) = switch (level) {
      Difficulty.beginner => ('Pemula', Colors.teal),
      Difficulty.intermediate => ('Menengah', Colors.indigo),
      Difficulty.advanced => ('Mahir', Colors.deepPurple),
    };

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
      decoration: BoxDecoration(
        color: color.withValues(alpha: 0.15),
        borderRadius: BorderRadius.circular(6),
      ),
      child: Text(
        label,
        style: TextStyle(
          fontSize: 11,
          fontWeight: FontWeight.bold,
          color: color,
        ),
      ),
    );
  }
}

class _GroupStats {
  final int totalTopics;
  final int understoodTopics;
  final int inProgressTopics;

  _GroupStats({
    required this.totalTopics,
    required this.understoodTopics,
    required this.inProgressTopics,
  });
}
