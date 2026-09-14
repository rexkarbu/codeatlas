// lib/features/topic/topic_screen.dart — F03, F05, F06: Topic detail with
// 8 pedagogical sections, single 'Daftar Isi' navigation, expandable reflection answers,
// status selector, notes editor, prerequisite/related links.

import 'package:flutter/material.dart';

import '../../data/content_repository.dart';
import '../../data/learning_repository.dart';
import '../../data/models.dart';
import '../../state/app_state.dart';
import '../../widgets/code_snippet.dart';

class TopicScreen extends StatefulWidget {
  final String topicId;
  final ContentRepository contentRepo;
  final LearningRepository learningRepo;
  final AppState appState;
  final void Function(String topicId) onOpenTopic;

  const TopicScreen({
    super.key,
    required this.topicId,
    required this.contentRepo,
    required this.learningRepo,
    required this.appState,
    required this.onOpenTopic,
  });

  @override
  State<TopicScreen> createState() => _TopicScreenState();
}

class _TopicScreenState extends State<TopicScreen> {
  Topic? _topic;
  LearningStatus _currentStatus = LearningStatus.notStarted;
  final _notesController = TextEditingController();
  String _savedNotes = '';
  bool _saving = false;
  String? _saveError;
  bool _saveSuccess = false;

  // GlobalKeys for TOC scrolling
  final _keyAnalogy = GlobalKey();
  final _keyProblem = GlobalKey();
  final _keyMechanism = GlobalKey();
  final _keyCode = GlobalKey();
  final _keyMisconceptions = GlobalKey();
  final _keyWhenToUse = GlobalKey();
  final _keyVibecoding = GlobalKey();
  final _keyReflection = GlobalKey();
  final _keyPrereqs = GlobalKey();
  final _keyNotes = GlobalKey();

  bool get _notesDirty => _notesController.text != _savedNotes;

  @override
  void initState() {
    super.initState();
    _load();
  }

  @override
  void dispose() {
    _notesController.dispose();
    super.dispose();
  }

  Future<void> _load() async {
    final topic = await widget.contentRepo.getTopicById(widget.topicId);
    final progress = await widget.learningRepo.getProgress(widget.topicId);

    // Record this topic was opened
    await widget.appState.recordTopicRead(widget.topicId);

    if (mounted) {
      final initialNotes = progress?.notes ?? '';
      setState(() {
        _topic = topic;
        _currentStatus = progress?.status ?? LearningStatus.notStarted;
        _notesController.text = initialNotes;
        _savedNotes = initialNotes;
      });
    }
  }

  Future<bool> _onWillPop() async {
    if (!_notesDirty) return true;

    final result = await showDialog<String>(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Perubahan belum disimpan'),
        content: const Text(
          'Catatan belum disimpan. Apa yang ingin dilakukan?',
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, 'discard'),
            child: const Text('Buang perubahan'),
          ),
          TextButton(
            onPressed: () => Navigator.pop(context, 'stay'),
            child: const Text('Tetap di halaman'),
          ),
          FilledButton(
            onPressed: () => Navigator.pop(context, 'save'),
            child: const Text('Simpan'),
          ),
        ],
      ),
    );

    if (result == 'save') {
      await _saveNotes();
      return !_notesDirty; // Only pop if save succeeded and no further unsaved edits
    }
    if (result == 'discard') return true;
    return false; // stay
  }

  Future<void> _updateStatus(LearningStatus status) async {
    setState(() => _currentStatus = status);
    try {
      await widget.appState.updateTopicStatus(widget.topicId, status);
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(
          context,
        ).showSnackBar(SnackBar(content: Text('Gagal menyimpan status: $e')));
      }
    }
  }

  Future<void> _saveNotes() async {
    final textToSave = _notesController.text;
    setState(() {
      _saving = true;
      _saveError = null;
      _saveSuccess = false;
    });
    try {
      await widget.learningRepo.updateNotes(widget.topicId, textToSave);
      if (mounted) {
        setState(() {
          _saving = false;
          _savedNotes =
              textToSave; // Marked saved only after database confirms write
          _saveSuccess = true;
        });
        // Reset success indicator after 2 seconds
        Future.delayed(const Duration(seconds: 2), () {
          if (mounted) setState(() => _saveSuccess = false);
        });
      }
    } catch (e) {
      if (mounted) {
        setState(() {
          _saving = false;
          _saveError = e.toString();
        });
      }
    }
  }

  void _scrollTo(GlobalKey key) {
    final ctx = key.currentContext;
    if (ctx != null) {
      Scrollable.ensureVisible(
        ctx,
        duration: const Duration(milliseconds: 350),
        curve: Curves.easeInOut,
      );
    }
  }

  void _showTableOfContents() {
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
                        const Icon(Icons.list_alt),
                        const SizedBox(width: 8),
                        Expanded(
                          child: Text(
                            'Daftar Isi Artikel',
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
                  ListTile(
                    leading: const Icon(Icons.lightbulb_outline),
                    title: const Text('1. Apa Konsep Ini?'),
                    onTap: () {
                      Navigator.pop(sheetContext);
                      _scrollTo(_keyAnalogy);
                    },
                  ),
                  if (_topic?.problemContext.isNotEmpty ?? false)
                    ListTile(
                      leading: const Icon(Icons.help_outline),
                      title: const Text('2. Masalah yang Diselesaikan'),
                      onTap: () {
                        Navigator.pop(sheetContext);
                        _scrollTo(_keyProblem);
                      },
                    ),
                  ListTile(
                    leading: const Icon(Icons.psychology_outlined),
                    title: const Text('3. Cara Kerja & Mekanisme'),
                    onTap: () {
                      Navigator.pop(sheetContext);
                      _scrollTo(_keyMechanism);
                    },
                  ),
                  if (_topic?.codeExamples.isNotEmpty ?? false)
                    ListTile(
                      leading: const Icon(Icons.code),
                      title: const Text('4. Contoh Kode & Penelusuran'),
                      onTap: () {
                        Navigator.pop(sheetContext);
                        _scrollTo(_keyCode);
                      },
                    ),
                  if (_topic?.misconceptions.isNotEmpty ?? false)
                    ListTile(
                      leading: const Icon(Icons.warning_amber_outlined),
                      title: const Text('5. Miskonsepsi Umum'),
                      onTap: () {
                        Navigator.pop(sheetContext);
                        _scrollTo(_keyMisconceptions);
                      },
                    ),
                  if (_topic?.whenToUse.isNotEmpty ?? false)
                    ListTile(
                      leading: const Icon(Icons.rule_outlined),
                      title: const Text('6. Kapan Dipakai & Batas'),
                      onTap: () {
                        Navigator.pop(sheetContext);
                        _scrollTo(_keyWhenToUse);
                      },
                    ),
                  ListTile(
                    leading: const Icon(Icons.auto_awesome),
                    title: const Text('7. Relevansi Vibecoding'),
                    onTap: () {
                      Navigator.pop(sheetContext);
                      _scrollTo(_keyVibecoding);
                    },
                  ),
                  if (_topic?.reflectionQuestions.isNotEmpty ?? false)
                    ListTile(
                      leading: const Icon(Icons.quiz_outlined),
                      title: const Text('8. Pertanyaan Refleksi'),
                      onTap: () {
                        Navigator.pop(sheetContext);
                        _scrollTo(_keyReflection);
                      },
                    ),
                  if ((_topic?.prerequisiteIds.isNotEmpty ?? false) ||
                      (_topic?.relatedTopicIds.isNotEmpty ?? false))
                    ListTile(
                      leading: const Icon(Icons.hub_outlined),
                      title: const Text('Prasyarat & Topik Terkait'),
                      onTap: () {
                        Navigator.pop(sheetContext);
                        _scrollTo(_keyPrereqs);
                      },
                    ),
                  ListTile(
                    leading: const Icon(Icons.note_alt_outlined),
                    title: const Text('Catatan Pribadi'),
                    onTap: () {
                      Navigator.pop(sheetContext);
                      _scrollTo(_keyNotes);
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
    if (_topic == null) {
      return Scaffold(
        appBar: AppBar(),
        body: const Center(child: CircularProgressIndicator()),
      );
    }

    final topic = _topic!;
    final theme = Theme.of(context);

    return PopScope(
      canPop: !_notesDirty,
      onPopInvokedWithResult: (didPop, _) async {
        if (!didPop) {
          final canPop = await _onWillPop();
          if (canPop && context.mounted) Navigator.of(context).pop();
        }
      },
      child: Scaffold(
        appBar: AppBar(
          title: Text(topic.title),
          actions: [
            IconButton(
              key: const ValueKey('toc_action_button'),
              icon: const Icon(Icons.list_alt),
              tooltip: 'Daftar Isi',
              onPressed: _showTableOfContents,
            ),
          ],
        ),
        floatingActionButton: FloatingActionButton.extended(
          key: const ValueKey('toc_button'),
          onPressed: _showTableOfContents,
          icon: const Icon(Icons.list_alt),
          label: const Text('Daftar Isi'),
        ),
        body: SingleChildScrollView(
          key: const ValueKey('topic_scrollable'),
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Header: level, time, status
              _buildHeader(topic, theme),
              const SizedBox(height: 16),

              // Summary
              Text(
                topic.summary,
                style: theme.textTheme.bodyLarge?.copyWith(
                  fontStyle: FontStyle.italic,
                  color: theme.colorScheme.onSurfaceVariant,
                ),
              ),
              const SizedBox(height: 24),

              // 1. Explanation Simple / Analogi
              Container(key: _keyAnalogy),
              _SectionTitle(
                title: '1. Apa Konsep Ini?',
                subtitle: 'Analogi Awam & Gambaran Konseptual',
              ),
              const SizedBox(height: 8),
              Text(
                topic.explanationSimple,
                style: theme.textTheme.bodyMedium?.copyWith(height: 1.6),
              ),
              const SizedBox(height: 24),

              // 2. Problem Context
              if (topic.problemContext.isNotEmpty) ...[
                Container(key: _keyProblem),
                _SectionTitle(
                  title: '2. Masalah Apa yang Diselesaikan?',
                  subtitle: 'Konteks Nyata & Mengapa Konsep Ini Dibutuhkan',
                ),
                const SizedBox(height: 8),
                Text(
                  topic.problemContext,
                  style: theme.textTheme.bodyMedium?.copyWith(height: 1.6),
                ),
                const SizedBox(height: 24),
              ],

              // 3. Explanation Technical / Mekanisme
              Container(key: _keyMechanism),
              _SectionTitle(
                title: '3. Bagaimana Cara Kerjanya?',
                subtitle: 'Mekanisme Teknis & Penjelasan Komponen',
              ),
              const SizedBox(height: 8),
              Text(
                topic.explanationTechnical,
                style: theme.textTheme.bodyMedium?.copyWith(height: 1.6),
              ),
              const SizedBox(height: 24),

              // 4. Code Examples & Walkthrough
              if (topic.codeExamples.isNotEmpty) ...[
                Container(key: _keyCode),
                _SectionTitle(
                  title: '4. Bagaimana Membaca Contohnya?',
                  subtitle: 'Contoh Kode & Penelusuran Langkah demi Langkah',
                ),
                const SizedBox(height: 8),
                for (final example in topic.codeExamples) ...[
                  Text(
                    example.label,
                    style: theme.textTheme.labelLarge?.copyWith(
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                  const SizedBox(height: 4),
                  CodeSnippet(
                    code: example.code,
                    language: example.language,
                    expectedOutput: example.expectedOutput,
                  ),
                  if (example.explanation.isNotEmpty) ...[
                    const SizedBox(height: 6),
                    Container(
                      width: double.infinity,
                      padding: const EdgeInsets.all(10),
                      decoration: BoxDecoration(
                        color: theme.colorScheme.surfaceContainerHighest
                            .withValues(alpha: 0.5),
                        borderRadius: BorderRadius.circular(8),
                      ),
                      child: Text(
                        example.explanation,
                        style: theme.textTheme.bodySmall?.copyWith(
                          color: theme.colorScheme.onSurfaceVariant,
                          height: 1.5,
                        ),
                      ),
                    ),
                  ],
                  const SizedBox(height: 16),
                ],
                const SizedBox(height: 8),
              ],

              // 5. Misconceptions
              if (topic.misconceptions.isNotEmpty) ...[
                Container(key: _keyMisconceptions),
                _SectionTitle(
                  title: '5. Apa yang Sering Disalahpahami?',
                  subtitle: 'Miskonsepsi, Penyebab, dan Cara Mengenali',
                ),
                const SizedBox(height: 8),
                for (final misc in topic.misconceptions) ...[
                  Card(
                    elevation: 0,
                    margin: const EdgeInsets.only(bottom: 12),
                    color: theme.colorScheme.errorContainer.withValues(
                      alpha: 0.25,
                    ),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(10),
                      side: BorderSide(
                        color: theme.colorScheme.error.withValues(alpha: 0.4),
                      ),
                    ),
                    child: Padding(
                      padding: const EdgeInsets.all(14),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Row(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Icon(
                                Icons.cancel_outlined,
                                size: 18,
                                color: theme.colorScheme.error,
                              ),
                              const SizedBox(width: 8),
                              Expanded(
                                child: Text(
                                  misc.misconception,
                                  style: theme.textTheme.titleSmall?.copyWith(
                                    fontWeight: FontWeight.bold,
                                    color: theme.colorScheme.error,
                                  ),
                                ),
                              ),
                            ],
                          ),
                          const SizedBox(height: 8),
                          Row(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              const Icon(
                                Icons.check_circle_outline,
                                size: 18,
                                color: Colors.green,
                              ),
                              const SizedBox(width: 8),
                              Expanded(
                                child: Text(
                                  misc.explanation,
                                  style: theme.textTheme.bodyMedium?.copyWith(
                                    height: 1.5,
                                  ),
                                ),
                              ),
                            ],
                          ),
                          if (misc.spotInCode.isNotEmpty) ...[
                            const SizedBox(height: 8),
                            Container(
                              padding: const EdgeInsets.symmetric(
                                horizontal: 10,
                                vertical: 6,
                              ),
                              decoration: BoxDecoration(
                                color: theme.colorScheme.surface,
                                borderRadius: BorderRadius.circular(6),
                              ),
                              child: Row(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Icon(
                                    Icons.search,
                                    size: 16,
                                    color: theme.colorScheme.primary,
                                  ),
                                  const SizedBox(width: 6),
                                  Expanded(
                                    child: Text(
                                      'Di kode: ${misc.spotInCode}',
                                      style: theme.textTheme.bodySmall
                                          ?.copyWith(
                                            fontStyle: FontStyle.italic,
                                          ),
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          ],
                        ],
                      ),
                    ),
                  ),
                ],
                const SizedBox(height: 16),
              ],

              // 6. When to Use & Limits
              if (topic.whenToUse.isNotEmpty) ...[
                Container(key: _keyWhenToUse),
                _SectionTitle(
                  title: '6. Kapan Dipakai & Batas Penerapan?',
                  subtitle: 'Skenario Tepat vs Kapan Sebaiknya Dihindari',
                ),
                const SizedBox(height: 8),
                Text(
                  topic.whenToUse,
                  style: theme.textTheme.bodyMedium?.copyWith(height: 1.6),
                ),
                const SizedBox(height: 24),
              ],

              // 7. Why Vibecoding Matters
              Container(key: _keyVibecoding),
              _SectionTitle(
                title: '7. Mengapa Penting saat Vibecoding?',
                subtitle: 'Jebakan Kode AI & Pertanyaan Kritis untuk AI',
              ),
              const SizedBox(height: 8),
              Container(
                padding: const EdgeInsets.all(14),
                decoration: BoxDecoration(
                  color: theme.colorScheme.primaryContainer.withValues(
                    alpha: 0.35,
                  ),
                  borderRadius: BorderRadius.circular(10),
                  border: Border.all(
                    color: theme.colorScheme.primary.withValues(alpha: 0.3),
                  ),
                ),
                child: Text(
                  topic.whyVibecodingMatters,
                  style: theme.textTheme.bodyMedium?.copyWith(height: 1.6),
                ),
              ),
              const SizedBox(height: 24),

              // 8. Reflection Questions (Expandable answers)
              if (topic.reflectionQuestions.isNotEmpty) ...[
                Container(key: _keyReflection),
                _SectionTitle(
                  title: '8. Bagaimana Memeriksa Pemahaman?',
                  subtitle:
                      'Uji pemahaman mandiri (ketuk untuk melihat jawaban)',
                ),
                const SizedBox(height: 8),
                for (int i = 0; i < topic.reflectionQuestions.length; i++) ...[
                  Card(
                    elevation: 0,
                    margin: const EdgeInsets.only(bottom: 8),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(10),
                      side: BorderSide(
                        color: theme.colorScheme.outlineVariant.withValues(
                          alpha: 0.5,
                        ),
                      ),
                    ),
                    child: ExpansionTile(
                      key: ValueKey('reflection_tile_$i'),
                      leading: CircleAvatar(
                        radius: 14,
                        backgroundColor: theme.colorScheme.primaryContainer,
                        child: Text(
                          '${i + 1}',
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.bold,
                            color: theme.colorScheme.onPrimaryContainer,
                          ),
                        ),
                      ),
                      title: Text(
                        topic.reflectionQuestions[i].question,
                        style: theme.textTheme.bodyMedium?.copyWith(
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                      childrenPadding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
                      expandedCrossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Divider(),
                        const SizedBox(height: 4),
                        Row(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Icon(
                              Icons.check_circle,
                              size: 16,
                              color: theme.colorScheme.primary,
                            ),
                            const SizedBox(width: 8),
                            Expanded(
                              child: Text(
                                topic.reflectionQuestions[i].answer,
                                style: theme.textTheme.bodyMedium?.copyWith(
                                  height: 1.5,
                                ),
                              ),
                            ),
                          ],
                        ),
                      ],
                    ),
                  ),
                ],
                const SizedBox(height: 24),
              ],

              // Prerequisites & Relations
              Container(key: _keyPrereqs),
              if (topic.prerequisiteIds.isNotEmpty) ...[
                _SectionTitle(title: 'Prasyarat'),
                const SizedBox(height: 8),
                _TopicLinks(
                  topicIds: topic.prerequisiteIds,
                  contentRepo: widget.contentRepo,
                  learningRepo: widget.learningRepo,
                  onOpenTopic: widget.onOpenTopic,
                  showPrereqWarning: true,
                ),
                const SizedBox(height: 16),
              ],

              // Related Topics
              if (topic.relatedTopicIds.isNotEmpty) ...[
                _SectionTitle(title: 'Topik Terkait'),
                const SizedBox(height: 8),
                _TopicLinks(
                  topicIds: topic.relatedTopicIds,
                  contentRepo: widget.contentRepo,
                  learningRepo: widget.learningRepo,
                  onOpenTopic: widget.onOpenTopic,
                ),
                const SizedBox(height: 16),
              ],

              // Dependents (topics that require this)
              FutureBuilder<List<String>>(
                future: widget.contentRepo.getDependentTopicIds(widget.topicId),
                builder: (context, snapshot) {
                  final deps = snapshot.data ?? [];
                  if (deps.isEmpty) return const SizedBox.shrink();
                  return Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      _SectionTitle(title: 'Topik yang Membutuhkan Ini'),
                      const SizedBox(height: 8),
                      _TopicLinks(
                        topicIds: deps,
                        contentRepo: widget.contentRepo,
                        learningRepo: widget.learningRepo,
                        onOpenTopic: widget.onOpenTopic,
                      ),
                      const SizedBox(height: 16),
                    ],
                  );
                },
              ),

              const Divider(),
              const SizedBox(height: 8),

              // Notes Section
              Container(key: _keyNotes),
              _SectionTitle(
                title: 'Catatan Pribadi',
                subtitle: 'Simpan pemahaman atau rangkuman pribadimu',
              ),
              const SizedBox(height: 8),
              TextField(
                controller: _notesController,
                maxLines: 6,
                maxLength: 20000,
                decoration: InputDecoration(
                  hintText: 'Tulis pemahamanmu di sini...',
                  border: const OutlineInputBorder(),
                  counterText: '',
                  suffixIcon: _saveSuccess
                      ? const Icon(Icons.check, color: Colors.green)
                      : null,
                ),
                onChanged: (value) => setState(() {}),
              ),
              const SizedBox(height: 8),
              Wrap(
                spacing: 8,
                runSpacing: 8,
                crossAxisAlignment: WrapCrossAlignment.center,
                children: [
                  FilledButton.icon(
                    onPressed: _saving ? null : _saveNotes,
                    icon: _saving
                        ? const SizedBox(
                            width: 16,
                            height: 16,
                            child: CircularProgressIndicator(strokeWidth: 2),
                          )
                        : const Icon(Icons.save),
                    label: Text(
                      _saving
                          ? 'Menyimpan...'
                          : _saveSuccess
                          ? 'Tersimpan'
                          : 'Simpan Catatan',
                    ),
                  ),
                  if (_notesDirty)
                    Text(
                      'Belum disimpan',
                      style: theme.textTheme.bodySmall?.copyWith(
                        color: theme.colorScheme.error,
                      ),
                    ),
                ],
              ),
              if (_saveError != null) ...[
                const SizedBox(height: 4),
                Row(
                  children: [
                    Icon(
                      Icons.error_outline,
                      color: theme.colorScheme.error,
                      size: 16,
                    ),
                    const SizedBox(width: 4),
                    Expanded(
                      child: Text(
                        'Gagal menyimpan: $_saveError',
                        style: theme.textTheme.bodySmall?.copyWith(
                          color: theme.colorScheme.error,
                        ),
                      ),
                    ),
                    TextButton(
                      onPressed: _saveNotes,
                      child: const Text('Coba lagi'),
                    ),
                  ],
                ),
              ],
              const SizedBox(height: 80), // extra padding for FAB
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildHeader(Topic topic, ThemeData theme) {
    return SingleChildScrollView(
      scrollDirection: Axis.horizontal,
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          // Level badge
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
            decoration: BoxDecoration(
              color: theme.colorScheme.secondaryContainer,
              borderRadius: BorderRadius.circular(6),
            ),
            child: Text(
              topic.level.label,
              style: TextStyle(
                fontSize: 12,
                fontWeight: FontWeight.w600,
                color: theme.colorScheme.onSecondaryContainer,
              ),
            ),
          ),
          const SizedBox(width: 8),
          Icon(
            Icons.schedule,
            size: 14,
            color: theme.colorScheme.onSurfaceVariant,
          ),
          const SizedBox(width: 4),
          Text(
            '${topic.estimatedMinutes} menit',
            style: theme.textTheme.bodySmall,
          ),
          const SizedBox(width: 16),
          // Status selector
          Semantics(
            label: 'Status: ${_currentStatus.label}',
            child: SegmentedButton<LearningStatus>(
              showSelectedIcon: false,
              segments: [
                for (final status in LearningStatus.values)
                  ButtonSegment(
                    value: status,
                    label: Text(
                      status.label,
                      style: const TextStyle(fontSize: 11),
                    ),
                  ),
              ],
              selected: {_currentStatus},
              onSelectionChanged: (selected) {
                _updateStatus(selected.first);
              },
            ),
          ),
        ],
      ),
    );
  }
}

class _SectionTitle extends StatelessWidget {
  final String title;
  final String? subtitle;

  const _SectionTitle({required this.title, this.subtitle});

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          title,
          style: theme.textTheme.titleMedium?.copyWith(
            fontWeight: FontWeight.bold,
          ),
        ),
        if (subtitle != null) ...[
          const SizedBox(height: 2),
          Text(
            subtitle!,
            style: theme.textTheme.bodySmall?.copyWith(
              color: theme.colorScheme.onSurfaceVariant,
            ),
          ),
        ],
      ],
    );
  }
}

class _TopicLinks extends StatelessWidget {
  final List<String> topicIds;
  final ContentRepository contentRepo;
  final LearningRepository learningRepo;
  final void Function(String) onOpenTopic;
  final bool showPrereqWarning;

  const _TopicLinks({
    required this.topicIds,
    required this.contentRepo,
    required this.learningRepo,
    required this.onOpenTopic,
    this.showPrereqWarning = false,
  });

  @override
  Widget build(BuildContext context) {
    return Wrap(
      spacing: 6,
      runSpacing: 6,
      children: [
        for (final id in topicIds)
          FutureBuilder<Topic?>(
            future: contentRepo.getTopicById(id),
            builder: (context, topicSnap) {
              final topic = topicSnap.data;
              if (topic == null) {
                return Chip(label: Text(id));
              }
              return FutureBuilder<Progress?>(
                future: learningRepo.getProgress(id),
                builder: (context, progressSnap) {
                  final progress = progressSnap.data;
                  final notUnderstood =
                      showPrereqWarning &&
                      (progress == null ||
                          progress.status != LearningStatus.understood);
                  return ActionChip(
                    avatar: notUnderstood
                        ? Icon(
                            Icons.info_outline,
                            size: 16,
                            color: Theme.of(context).colorScheme.error,
                          )
                        : null,
                    label: Text(topic.title),
                    tooltip: notUnderstood
                        ? 'Disarankan pelajari dahulu'
                        : topic.title,
                    onPressed: () => onOpenTopic(id),
                  );
                },
              );
            },
          ),
      ],
    );
  }
}
