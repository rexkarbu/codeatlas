// lib/features/practice/comparison_screen.dart — F08: Side-by-side syntax
// comparison with horizontal swipe cards on mobile.

import 'package:flutter/material.dart';

import '../../data/content_repository.dart';
import '../../widgets/code_snippet.dart';

class ComparisonScreen extends StatefulWidget {
  final ContentRepository contentRepo;
  final void Function(String topicId) onOpenTopic;

  const ComparisonScreen({
    super.key,
    required this.contentRepo,
    required this.onOpenTopic,
  });

  @override
  State<ComparisonScreen> createState() => _ComparisonScreenState();
}

class _ComparisonScreenState extends State<ComparisonScreen> {
  List<ComparisonGroup> _groups = [];
  Set<String> _allLanguages = {};
  Set<String> _selectedLanguages = {};
  ComparisonGroup? _selectedGroup;
  bool _loading = true;
  bool? _userVerticalPreference;

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    final groups = await widget.contentRepo.getComparisonGroups();
    final languages = await widget.contentRepo.getComparisonLanguages();

    if (mounted) {
      setState(() {
        _groups = groups;
        _allLanguages = languages;
        _selectedLanguages = Set.from(languages); // Select all by default
        _loading = false;
      });
    }
  }

  List<ComparisonGroup> get _filteredGroups {
    if (_selectedLanguages.length < 2) return [];
    return _groups.where((g) {
      final groupLangs = g.examples.map((e) => e.language).toSet();
      return groupLangs.intersection(_selectedLanguages).length >= 2;
    }).toList();
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Scaffold(
      appBar: AppBar(title: const Text('Perbandingan Sintaks')),
      body: _loading
          ? const Center(child: CircularProgressIndicator())
          : _groups.isEmpty
          ? _buildEmpty()
          : Column(
              children: [
                // Language filter
                Padding(
                  padding: const EdgeInsets.all(12),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        'Pilih 2-3 bahasa:',
                        style: theme.textTheme.labelLarge,
                      ),
                      const SizedBox(height: 8),
                      Wrap(
                        spacing: 6,
                        runSpacing: 6,
                        children: [
                          for (final lang in _allLanguages.toList()..sort())
                            FilterChip(
                              label: Text(lang),
                              selected: _selectedLanguages.contains(lang),
                              onSelected: (sel) {
                                setState(() {
                                  if (sel) {
                                    if (_selectedLanguages.length < 3) {
                                      _selectedLanguages.add(lang);
                                    }
                                  } else {
                                    _selectedLanguages.remove(lang);
                                  }
                                  _selectedGroup = null;
                                });
                              },
                            ),
                        ],
                      ),
                    ],
                  ),
                ),
                const Divider(height: 1),

                // Group selector
                if (_filteredGroups.isNotEmpty)
                  SizedBox(
                    height: 48,
                    child: ListView(
                      scrollDirection: Axis.horizontal,
                      padding: const EdgeInsets.symmetric(horizontal: 12),
                      children: [
                        for (final group in _filteredGroups)
                          Padding(
                            padding: const EdgeInsets.only(right: 6),
                            child: ChoiceChip(
                              label: Text(group.comparisonKey),
                              selected: _selectedGroup == group,
                              onSelected: (sel) {
                                setState(() {
                                  _selectedGroup = sel ? group : null;
                                });
                              },
                            ),
                          ),
                      ],
                    ),
                  ),

                // Comparison display
                Expanded(
                  child: _selectedGroup == null
                      ? _buildGroupList()
                      : _buildComparison(_selectedGroup!),
                ),
              ],
            ),
    );
  }

  Widget _buildEmpty() {
    return const Center(
      child: Text('Belum ada kelompok perbandingan tersedia.'),
    );
  }

  Widget _buildGroupList() {
    final groups = _filteredGroups;
    if (groups.isEmpty) {
      return Center(
        child: Text(
          _selectedLanguages.length < 2
              ? 'Pilih minimal 2 bahasa'
              : 'Tidak ada perbandingan untuk bahasa terpilih',
        ),
      );
    }

    return ListView.builder(
      padding: const EdgeInsets.all(12),
      itemCount: groups.length,
      itemBuilder: (context, index) {
        final group = groups[index];
        final langs = group.examples.map((e) => e.language).toSet().join(', ');
        return Card(
          child: ListTile(
            title: Text(group.comparisonKey),
            subtitle: Text('${group.topicTitle} • $langs'),
            trailing: const Icon(Icons.compare_arrows),
            onTap: () {
              setState(() => _selectedGroup = group);
            },
          ),
        );
      },
    );
  }

  Widget _buildComparison(ComparisonGroup group) {
    final theme = Theme.of(context);
    final filteredExamples = group.examples
        .where((e) => _selectedLanguages.contains(e.language))
        .toList();

    final isLargeText = MediaQuery.textScalerOf(context).scale(1) > 1.3;
    final useVertical = _userVerticalPreference ?? isLargeText;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Topic link & layout toggle
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
          child: Row(
            children: [
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      group.comparisonKey,
                      style: theme.textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    GestureDetector(
                      onTap: () => widget.onOpenTopic(group.topicId),
                      child: Text(
                        '→ ${group.topicTitle}',
                        style: theme.textTheme.bodySmall?.copyWith(
                          color: theme.colorScheme.primary,
                          decoration: TextDecoration.underline,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
              IconButton.filledTonal(
                icon: Icon(
                  useVertical
                      ? Icons.view_carousel_outlined
                      : Icons.view_agenda_outlined,
                  size: 20,
                ),
                tooltip: useVertical
                    ? 'Beralih ke geser horizontal'
                    : 'Beralih ke daftar vertikal',
                onPressed: () {
                  setState(() => _userVerticalPreference = !useVertical);
                },
              ),
            ],
          ),
        ),
        // Layout view: vertical stack or horizontal swipe
        Expanded(
          child: useVertical
              ? ListView.builder(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 12,
                    vertical: 4,
                  ),
                  itemCount: filteredExamples.length,
                  itemBuilder: (context, index) {
                    final example = filteredExamples[index];
                    return Padding(
                      padding: const EdgeInsets.only(bottom: 12),
                      child: Card(
                        child: Padding(
                          padding: const EdgeInsets.all(16),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                example.language.toUpperCase(),
                                style: theme.textTheme.titleSmall?.copyWith(
                                  fontWeight: FontWeight.bold,
                                  color: theme.colorScheme.primary,
                                ),
                              ),
                              const SizedBox(height: 4),
                              Text(
                                example.label,
                                style: theme.textTheme.bodySmall,
                              ),
                              const SizedBox(height: 8),
                              CodeSnippet(
                                code: example.code,
                                language: example.language,
                                expectedOutput: example.expectedOutput,
                              ),
                              if (example.explanation.isNotEmpty) ...[
                                const SizedBox(height: 8),
                                Text(
                                  example.explanation,
                                  style: theme.textTheme.bodySmall?.copyWith(
                                    color: theme.colorScheme.onSurfaceVariant,
                                  ),
                                ),
                              ],
                            ],
                          ),
                        ),
                      ),
                    );
                  },
                )
              : PageView.builder(
                  itemCount: filteredExamples.length,
                  controller: PageController(viewportFraction: 0.9),
                  itemBuilder: (context, index) {
                    final example = filteredExamples[index];
                    return Padding(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 4,
                        vertical: 8,
                      ),
                      child: Card(
                        child: Padding(
                          padding: const EdgeInsets.all(16),
                          child: SingleChildScrollView(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  example.language.toUpperCase(),
                                  style: theme.textTheme.titleSmall?.copyWith(
                                    fontWeight: FontWeight.bold,
                                    color: theme.colorScheme.primary,
                                  ),
                                ),
                                const SizedBox(height: 4),
                                Text(
                                  example.label,
                                  style: theme.textTheme.bodySmall,
                                ),
                                const SizedBox(height: 8),
                                CodeSnippet(
                                  code: example.code,
                                  language: example.language,
                                  expectedOutput: example.expectedOutput,
                                ),
                                if (example.explanation.isNotEmpty) ...[
                                  const SizedBox(height: 8),
                                  Text(
                                    example.explanation,
                                    style: theme.textTheme.bodySmall?.copyWith(
                                      color: theme.colorScheme.onSurfaceVariant,
                                    ),
                                  ),
                                ],
                              ],
                            ),
                          ),
                        ),
                      ),
                    );
                  },
                ),
        ),
        // Page indicator (only when horizontal)
        if (!useVertical)
          Padding(
            padding: const EdgeInsets.only(bottom: 8),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                for (var i = 0; i < filteredExamples.length; i++)
                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 3),
                    child: Text(
                      filteredExamples[i].language,
                      style: theme.textTheme.bodySmall?.copyWith(
                        color: theme.colorScheme.onSurfaceVariant,
                      ),
                    ),
                  ),
              ],
            ),
          ),
      ],
    );
  }
}
