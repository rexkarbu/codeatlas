// lib/features/practice/comparison_screen.dart — F08: Side-by-side syntax
// comparison with single concept selector bottom sheet, default vertical stack,
// Indonesian concept labels, and consistent language casing.

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

  static const Map<String, String> _conceptLabels = {
    'sequence': 'Urutan Instruksi',
    'variables': 'Variabel',
    'operators': 'Operator',
    'conditionals': 'Percabangan',
    'loops': 'Perulangan',
    'functions': 'Fungsi',
    'lists': 'List / Array',
    'classes': 'Class dan Objek',
    'error-handling': 'Penanganan Kesalahan',
    'async': 'Pemrograman Asinkron',
  };

  static String _getConceptLabel(String key) {
    return _conceptLabels[key] ?? key;
  }

  static String _formatLanguageName(String lang) {
    switch (lang.toLowerCase()) {
      case 'dart':
        return 'Dart';
      case 'python':
        return 'Python';
      case 'typescript':
        return 'TypeScript';
      default:
        return lang.isNotEmpty
            ? '${lang[0].toUpperCase()}${lang.substring(1)}'
            : lang;
    }
  }

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
        if (groups.isNotEmpty) {
          _selectedGroup = groups.first;
        }
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

  void _showConceptPicker(List<ComparisonGroup> groups) {
    showModalBottomSheet<void>(
      context: context,
      isScrollControlled: true,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(16)),
      ),
      builder: (sheetContext) {
        return SafeArea(
          child: Padding(
            padding: const EdgeInsets.symmetric(vertical: 8),
            child: SingleChildScrollView(
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Padding(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 16,
                      vertical: 8,
                    ),
                    child: Row(
                      children: [
                        const Icon(Icons.compare_arrows),
                        const SizedBox(width: 8),
                        Expanded(
                          child: Text(
                            'Pilih Konsep Sintaks',
                            style: Theme.of(sheetContext).textTheme.titleMedium
                                ?.copyWith(fontWeight: FontWeight.bold),
                          ),
                        ),
                        IconButton(
                          icon: const Icon(Icons.close),
                          onPressed: () => Navigator.pop(sheetContext),
                        ),
                      ],
                    ),
                  ),
                  const Divider(height: 1),
                  for (final group in groups)
                    ListTile(
                      key: ValueKey(
                        'concept_option_${group.topicId}_${group.comparisonKey}',
                      ),
                      title: Text(_getConceptLabel(group.comparisonKey)),
                      subtitle: Text(group.topicTitle),
                      selected:
                          _selectedGroup?.topicId == group.topicId &&
                          _selectedGroup?.comparisonKey == group.comparisonKey,
                      trailing:
                          (_selectedGroup?.topicId == group.topicId &&
                              _selectedGroup?.comparisonKey ==
                                  group.comparisonKey)
                          ? const Icon(Icons.check, color: Colors.green)
                          : null,
                      onTap: () {
                        setState(() => _selectedGroup = group);
                        Navigator.pop(sheetContext);
                      },
                    ),
                ],
              ),
            ),
          ),
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final filtered = _filteredGroups;

    // Ensure active group is valid
    ComparisonGroup? activeGroup = _selectedGroup;
    if (activeGroup != null && !filtered.contains(activeGroup)) {
      activeGroup = filtered.isNotEmpty ? filtered.first : null;
    } else if (activeGroup == null && filtered.isNotEmpty) {
      activeGroup = filtered.first;
    }

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
                              label: Text(_formatLanguageName(lang)),
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
                                });
                              },
                            ),
                        ],
                      ),
                    ],
                  ),
                ),
                const Divider(height: 1),

                // Single Concept Selector Button
                Padding(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 12,
                    vertical: 8,
                  ),
                  child: OutlinedButton.icon(
                    key: const ValueKey('concept_selector_button'),
                    onPressed: filtered.isEmpty
                        ? null
                        : () => _showConceptPicker(filtered),
                    icon: const Icon(Icons.menu_book),
                    label: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Expanded(
                          child: Text(
                            activeGroup != null
                                ? 'Konsep: ${_getConceptLabel(activeGroup.comparisonKey)}'
                                : 'Pilih Konsep...',
                            overflow: TextOverflow.ellipsis,
                            style: const TextStyle(fontWeight: FontWeight.bold),
                          ),
                        ),
                        const Icon(Icons.arrow_drop_down),
                      ],
                    ),
                    style: OutlinedButton.styleFrom(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 16,
                        vertical: 12,
                      ),
                    ),
                  ),
                ),

                // Comparison display
                Expanded(
                  child: filtered.isEmpty
                      ? Center(
                          child: Text(
                            _selectedLanguages.length < 2
                                ? 'Pilih minimal 2 bahasa untuk melihat perbandingan'
                                : 'Tidak ada perbandingan untuk bahasa terpilih',
                            style: theme.textTheme.bodyMedium?.copyWith(
                              color: theme.colorScheme.onSurfaceVariant,
                            ),
                          ),
                        )
                      : activeGroup == null
                      ? const SizedBox.shrink()
                      : _buildComparison(activeGroup),
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

  Widget _buildComparison(ComparisonGroup group) {
    final theme = Theme.of(context);
    final filteredExamples = group.examples
        .where((e) => _selectedLanguages.contains(e.language))
        .toList();

    // Default to vertical stack on mobile; can be toggled by user
    final useVertical = _userVerticalPreference ?? true;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Topic link & layout toggle
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
          child: Row(
            children: [
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      _getConceptLabel(group.comparisonKey),
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
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Text(
                                _formatLanguageName(example.language),
                                style: theme.textTheme.titleSmall?.copyWith(
                                  fontWeight: FontWeight.bold,
                                  color: theme.colorScheme.primary,
                                ),
                              ),
                              const SizedBox(height: 4),
                              Text(
                                example.label,
                                style: theme.textTheme.bodySmall?.copyWith(
                                  fontWeight: FontWeight.normal,
                                ),
                              ),
                              const SizedBox(height: 8),
                              CodeSnippet(
                                code: example.code,
                                language: _formatLanguageName(example.language),
                                expectedOutput: example.expectedOutput,
                                showLanguageLabel: false,
                              ),
                              if (example.explanation.isNotEmpty) ...[
                                const SizedBox(height: 8),
                                Text(
                                  example.explanation,
                                  style: theme.textTheme.bodySmall?.copyWith(
                                    color: theme.colorScheme.onSurfaceVariant,
                                    fontWeight: FontWeight.normal,
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
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                Text(
                                  _formatLanguageName(example.language),
                                  style: theme.textTheme.titleSmall?.copyWith(
                                    fontWeight: FontWeight.bold,
                                    color: theme.colorScheme.primary,
                                  ),
                                ),
                                const SizedBox(height: 4),
                                Text(
                                  example.label,
                                  style: theme.textTheme.bodySmall?.copyWith(
                                    fontWeight: FontWeight.normal,
                                  ),
                                ),
                                const SizedBox(height: 8),
                                CodeSnippet(
                                  code: example.code,
                                  language: _formatLanguageName(
                                    example.language,
                                  ),
                                  expectedOutput: example.expectedOutput,
                                  showLanguageLabel: false,
                                ),
                                if (example.explanation.isNotEmpty) ...[
                                  const SizedBox(height: 8),
                                  Text(
                                    example.explanation,
                                    style: theme.textTheme.bodySmall?.copyWith(
                                      color: theme.colorScheme.onSurfaceVariant,
                                      fontWeight: FontWeight.normal,
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
                      _formatLanguageName(filteredExamples[i].language),
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
