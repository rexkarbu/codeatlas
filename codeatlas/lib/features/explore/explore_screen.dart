// lib/features/explore/explore_screen.dart — F02, F09: Browse categories,
// search, and filter by layer/category/level.

import 'package:flutter/material.dart';

import '../../data/content_repository.dart';
import '../../data/learning_repository.dart';
import '../../data/models.dart';
import '../../widgets/topic_tile.dart';

class ExploreScreen extends StatefulWidget {
  final ContentRepository contentRepo;
  final LearningRepository learningRepo;
  final void Function(String topicId) onOpenTopic;

  const ExploreScreen({
    super.key,
    required this.contentRepo,
    required this.learningRepo,
    required this.onOpenTopic,
  });

  @override
  State<ExploreScreen> createState() => _ExploreScreenState();
}

class _ExploreScreenState extends State<ExploreScreen>
    with SingleTickerProviderStateMixin {
  late TabController _tabController;
  final _searchController = TextEditingController();
  Difficulty? _levelFilter;
  String? _categoryFilter;
  bool _isSearching = false;

  List<Topic> _searchResults = [];
  Map<String, Progress> _progressMap = {};
  List<Category> _activeCategories = [];

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
    _tabController.addListener(() {
      if (!_tabController.indexIsChanging) {
        _categoryFilter = null;
        _loadCategories();
        if (_isSearching) _performSearch();
        setState(() {});
      }
    });
    _loadProgress();
    _loadCategories();
  }

  @override
  void dispose() {
    _tabController.dispose();
    _searchController.dispose();
    super.dispose();
  }

  Future<void> _loadProgress() async {
    final progress = await widget.learningRepo.getAllProgress();
    if (mounted) setState(() => _progressMap = progress);
  }

  Future<void> _loadCategories() async {
    final layer = _tabController.index == 0
        ? ContentLayer.fundamentals
        : ContentLayer.ecosystem;
    final groups = await widget.contentRepo.getGroupCategories(layer);
    if (mounted) setState(() => _activeCategories = groups);
  }

  Future<void> _performSearch() async {
    final query = _searchController.text;
    final layer = _tabController.index == 0
        ? ContentLayer.fundamentals
        : ContentLayer.ecosystem;

    final results = await widget.contentRepo.search(
      query,
      layer: layer,
      categoryId: _categoryFilter,
      level: _levelFilter,
    );
    if (mounted) setState(() => _searchResults = results);
  }

  void _resetFilters() {
    setState(() {
      _searchController.clear();
      _levelFilter = null;
      _categoryFilter = null;
      _searchResults = [];
      _isSearching = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: _isSearching ? _buildSearchField() : const Text('Jelajah'),
        actions: [
          if (!_isSearching)
            IconButton(
              icon: const Icon(Icons.search),
              tooltip: 'Cari',
              onPressed: () {
                setState(() => _isSearching = true);
                _performSearch();
              },
            ),
          if (_isSearching)
            IconButton(
              icon: const Icon(Icons.close),
              tooltip: 'Tutup pencarian',
              onPressed: _resetFilters,
            ),
        ],
        bottom: TabBar(
          controller: _tabController,
          onTap: (_) {
            _categoryFilter = null;
            if (_isSearching) _performSearch();
            setState(() {});
          },
          tabs: const [
            Tab(text: 'Fundamental'),
            Tab(text: 'Ekosistem'),
          ],
        ),
      ),
      body: Column(
        children: [
          if (_isSearching) _buildFilterRow(),
          Expanded(
            child: _isSearching
                ? _buildSearchResults()
                : TabBarView(
                    controller: _tabController,
                    children: [
                      _CategoryListView(
                        contentRepo: widget.contentRepo,
                        learningRepo: widget.learningRepo,
                        layer: ContentLayer.fundamentals,
                        progressMap: _progressMap,
                        onOpenTopic: widget.onOpenTopic,
                      ),
                      _CategoryListView(
                        contentRepo: widget.contentRepo,
                        learningRepo: widget.learningRepo,
                        layer: ContentLayer.ecosystem,
                        progressMap: _progressMap,
                        onOpenTopic: widget.onOpenTopic,
                      ),
                    ],
                  ),
          ),
        ],
      ),
    );
  }

  Widget _buildSearchField() {
    return TextField(
      controller: _searchController,
      autofocus: true,
      decoration: const InputDecoration(
        hintText: 'Cari topik...',
        border: InputBorder.none,
      ),
      onChanged: (_) => _performSearch(),
    );
  }

  Widget _buildFilterRow() {
    final theme = Theme.of(context);
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
      child: SingleChildScrollView(
        scrollDirection: Axis.horizontal,
        child: Row(
          children: [
            // Category filter control
            Padding(
              padding: const EdgeInsets.only(right: 8),
              child: Container(
                padding: const EdgeInsets.symmetric(
                  horizontal: 10,
                  vertical: 2,
                ),
                decoration: BoxDecoration(
                  border: Border.all(
                    color: _categoryFilter != null
                        ? theme.colorScheme.primary
                        : theme.colorScheme.outlineVariant,
                  ),
                  borderRadius: BorderRadius.circular(8),
                  color: _categoryFilter != null
                      ? theme.colorScheme.primaryContainer.withValues(
                          alpha: 0.3,
                        )
                      : null,
                ),
                child: DropdownButtonHideUnderline(
                  child: DropdownButton<String?>(
                    key: const ValueKey('category_filter_dropdown'),
                    value: _categoryFilter,
                    isDense: true,
                    icon: const Icon(Icons.arrow_drop_down, size: 20),
                    hint: const Text(
                      'Semua Kategori',
                      style: TextStyle(fontSize: 12),
                    ),
                    items: [
                      const DropdownMenuItem<String?>(
                        value: null,
                        child: Text(
                          'Semua Kategori',
                          style: TextStyle(fontSize: 12),
                        ),
                      ),
                      for (final cat in _activeCategories)
                        DropdownMenuItem<String?>(
                          value: cat.id,
                          child: Text(
                            cat.title,
                            style: const TextStyle(fontSize: 12),
                          ),
                        ),
                    ],
                    onChanged: (catId) {
                      setState(() => _categoryFilter = catId);
                      _performSearch();
                    },
                  ),
                ),
              ),
            ),
            for (final level in Difficulty.values)
              Padding(
                padding: const EdgeInsets.only(right: 6),
                child: FilterChip(
                  label: Text(level.label),
                  selected: _levelFilter == level,
                  onSelected: (selected) {
                    setState(() {
                      _levelFilter = selected ? level : null;
                    });
                    _performSearch();
                  },
                ),
              ),
            if (_levelFilter != null || _categoryFilter != null)
              TextButton.icon(
                onPressed: () {
                  setState(() {
                    _levelFilter = null;
                    _categoryFilter = null;
                  });
                  _performSearch();
                },
                icon: const Icon(Icons.clear, size: 16),
                label: const Text('Reset filter'),
              ),
          ],
        ),
      ),
    );
  }

  Widget _buildSearchResults() {
    if (_searchResults.isEmpty) {
      return Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              Icons.search_off,
              size: 48,
              color: Theme.of(context).colorScheme.onSurfaceVariant,
            ),
            const SizedBox(height: 8),
            Text(
              _searchController.text.isEmpty &&
                      _levelFilter == null &&
                      _categoryFilter == null
                  ? 'Masukkan kata kunci untuk mencari'
                  : 'Tidak ditemukan',
              style: Theme.of(context).textTheme.bodyLarge,
            ),
          ],
        ),
      );
    }

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
          child: Text(
            '${_searchResults.length} hasil',
            style: Theme.of(context).textTheme.bodySmall,
          ),
        ),
        Expanded(
          child: ListView.builder(
            itemCount: _searchResults.length,
            itemBuilder: (context, index) {
              final topic = _searchResults[index];
              return TopicTile(
                topic: topic,
                status: _progressMap[topic.id]?.status,
                onTap: () => widget.onOpenTopic(topic.id),
              );
            },
          ),
        ),
      ],
    );
  }
}

class _CategoryListView extends StatefulWidget {
  final ContentRepository contentRepo;
  final LearningRepository learningRepo;
  final ContentLayer layer;
  final Map<String, Progress> progressMap;
  final void Function(String) onOpenTopic;

  const _CategoryListView({
    required this.contentRepo,
    required this.learningRepo,
    required this.layer,
    required this.progressMap,
    required this.onOpenTopic,
  });

  @override
  State<_CategoryListView> createState() => _CategoryListViewState();
}

class _CategoryListViewState extends State<_CategoryListView>
    with AutomaticKeepAliveClientMixin {
  List<Category>? _groups;
  Map<String, List<Category>>? _domainsByGroup;
  Map<String, List<Topic>>? _topicsByCategory;

  @override
  bool get wantKeepAlive => true;

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    final groups = await widget.contentRepo.getGroupCategories(widget.layer);
    final domainsByGroup = <String, List<Category>>{};
    final topicsByCategory = <String, List<Topic>>{};

    for (final group in groups) {
      if (widget.layer == ContentLayer.ecosystem) {
        final domains = await widget.contentRepo.getDomainsByGroup(group.id);
        domainsByGroup[group.id] = domains;
        for (final domain in domains) {
          topicsByCategory[domain.id] = await widget.contentRepo
              .getTopicsByCategory(domain.id);
        }
      } else {
        topicsByCategory[group.id] = await widget.contentRepo
            .getTopicsByCategory(group.id);
      }
    }

    if (mounted) {
      setState(() {
        _groups = groups;
        _domainsByGroup = domainsByGroup;
        _topicsByCategory = topicsByCategory;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    super.build(context);
    if (_groups == null) {
      return const Center(child: CircularProgressIndicator());
    }

    final theme = Theme.of(context);

    return ListView.builder(
      padding: const EdgeInsets.only(bottom: 16),
      itemCount: _groups!.length,
      itemBuilder: (context, index) {
        final group = _groups![index];

        if (widget.layer == ContentLayer.ecosystem) {
          final domains = _domainsByGroup?[group.id] ?? [];
          return _GroupSection(
            group: group,
            child: Column(
              children: [
                for (final domain in domains) ...[
                  Padding(
                    padding: const EdgeInsets.only(left: 16, right: 16, top: 4),
                    child: Text(
                      domain.title,
                      style: theme.textTheme.labelLarge?.copyWith(
                        color: theme.colorScheme.primary,
                      ),
                    ),
                  ),
                  for (final topic
                      in _topicsByCategory?[domain.id] ?? <Topic>[])
                    TopicTile(
                      topic: topic,
                      status: widget.progressMap[topic.id]?.status,
                      onTap: () => widget.onOpenTopic(topic.id),
                    ),
                ],
              ],
            ),
          );
        } else {
          final topics = _topicsByCategory?[group.id] ?? [];
          return _GroupSection(
            group: group,
            child: Column(
              children: [
                for (final topic in topics)
                  TopicTile(
                    topic: topic,
                    status: widget.progressMap[topic.id]?.status,
                    onTap: () => widget.onOpenTopic(topic.id),
                  ),
              ],
            ),
          );
        }
      },
    );
  }
}

class _GroupSection extends StatelessWidget {
  final Category group;
  final Widget child;

  const _GroupSection({required this.group, required this.child});

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    return Card(
      margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
      child: ExpansionTile(
        initiallyExpanded: false,
        title: Text(
          group.title,
          style: theme.textTheme.titleMedium?.copyWith(
            fontWeight: FontWeight.w600,
          ),
        ),
        subtitle: Text(
          group.description,
          maxLines: 2,
          overflow: TextOverflow.ellipsis,
          style: theme.textTheme.bodySmall?.copyWith(
            color: theme.colorScheme.onSurfaceVariant,
          ),
        ),
        children: [child],
      ),
    );
  }
}
