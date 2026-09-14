// lib/features/practice/quiz_screen.dart — F07: Quiz with two modes,
// randomized options, locked answers, session summary.

import 'dart:math';

import 'package:flutter/material.dart';

import '../../data/content_repository.dart';
import '../../data/models.dart';
import '../../widgets/code_snippet.dart';

class QuizScreen extends StatefulWidget {
  final ContentRepository contentRepo;
  final QuizType quizType;
  final void Function(String topicId) onOpenTopic;

  const QuizScreen({
    super.key,
    required this.contentRepo,
    required this.quizType,
    required this.onOpenTopic,
  });

  @override
  State<QuizScreen> createState() => _QuizScreenState();
}

class _QuizScreenState extends State<QuizScreen> {
  List<_QuizItem> _items = [];
  int _currentIndex = 0;
  int _correctCount = 0;
  bool _sessionDone = false;
  bool _loading = true;

  @override
  void initState() {
    super.initState();
    _loadQuizzes();
  }

  Future<void> _loadQuizzes() async {
    final quizzes = await widget.contentRepo.getActiveQuizzes(
      type: widget.quizType,
    );

    if (quizzes.isEmpty) {
      if (mounted) setState(() => _loading = false);
      return;
    }

    // Shuffle and take min(5, available)
    final rng = Random();
    final shuffled = List<Quiz>.from(quizzes)..shuffle(rng);
    final selected = shuffled.take(min(5, shuffled.length)).toList();

    // Shuffle options for each quiz, but keep IDs stable
    final items = selected.map((quiz) {
      final shuffledOptions = List<QuizOption>.from(quiz.options)..shuffle(rng);
      return _QuizItem(quiz: quiz, shuffledOptions: shuffledOptions);
    }).toList();

    if (mounted) {
      setState(() {
        _items = items;
        _loading = false;
      });
    }
  }

  Future<bool> _onWillPop() async {
    if (_sessionDone || _items.isEmpty) return true;

    final result = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Keluar dari kuis?'),
        content: const Text(
          'Sesi kuis belum selesai. Progress sesi ini akan hilang.',
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: const Text('Lanjutkan kuis'),
          ),
          FilledButton(
            onPressed: () => Navigator.pop(context, true),
            child: const Text('Keluar'),
          ),
        ],
      ),
    );
    return result ?? false;
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return PopScope(
      canPop: _sessionDone || _items.isEmpty,
      onPopInvokedWithResult: (didPop, _) async {
        if (!didPop) {
          final canPop = await _onWillPop();
          if (canPop && context.mounted) Navigator.of(context).pop();
        }
      },
      child: Scaffold(
        appBar: AppBar(
          title: Text(
            widget.quizType == QuizType.language
                ? 'Tebak Bahasa'
                : 'Tebak Konsep',
          ),
          actions: [
            if (_items.isNotEmpty && !_sessionDone)
              Center(
                child: Padding(
                  padding: const EdgeInsets.only(right: 16),
                  child: Text(
                    '${_currentIndex + 1}/${_items.length}',
                    style: theme.textTheme.labelLarge,
                  ),
                ),
              ),
          ],
        ),
        body: _loading
            ? const Center(child: CircularProgressIndicator())
            : _items.isEmpty
            ? _buildEmpty()
            : _sessionDone
            ? _buildSummary()
            : _buildQuestion(),
      ),
    );
  }

  Widget _buildEmpty() {
    return Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(
            Icons.quiz_outlined,
            size: 48,
            color: Theme.of(context).colorScheme.onSurfaceVariant,
          ),
          const SizedBox(height: 8),
          const Text('Belum ada soal tersedia untuk mode ini.'),
        ],
      ),
    );
  }

  Widget _buildQuestion() {
    final item = _items[_currentIndex];
    final quiz = item.quiz;
    final theme = Theme.of(context);
    final isLanguageQuiz = quiz.type == QuizType.language;

    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        // Prompt
        Text(
          quiz.prompt,
          style: theme.textTheme.titleMedium?.copyWith(
            fontWeight: FontWeight.w600,
          ),
        ),
        const SizedBox(height: 12),

        // Snippet — hide language label for language quiz before answering
        CodeSnippet(
          code: quiz.snippet,
          language: item.isAnswered || !isLanguageQuiz
              ? quiz.snippetLanguage
              : null,
          showLanguageLabel: item.isAnswered || !isLanguageQuiz,
        ),
        const SizedBox(height: 16),

        // Options
        for (final option in item.shuffledOptions) ...[
          _OptionButton(
            option: option,
            isSelected: item.selectedOptionId == option.id,
            isCorrect: item.isAnswered
                ? option.id == quiz.correctOptionId
                : null,
            isLocked: item.isAnswered,
            onTap: item.isAnswered
                ? null
                : () {
                    setState(() {
                      item.selectedOptionId = option.id;
                    });
                  },
          ),
          const SizedBox(height: 8),
        ],

        const SizedBox(height: 16),

        // Submit / Next button
        if (!item.isAnswered)
          FilledButton(
            onPressed: item.selectedOptionId == null
                ? null
                : () {
                    setState(() {
                      item.isAnswered = true;
                      if (item.selectedOptionId == quiz.correctOptionId) {
                        _correctCount++;
                      }
                    });
                  },
            child: const Text('Kirim Jawaban'),
          ),

        if (item.isAnswered) ...[
          // Feedback
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: item.selectedOptionId == quiz.correctOptionId
                  ? Colors.green.withValues(alpha: 0.1)
                  : Colors.red.withValues(alpha: 0.1),
              borderRadius: BorderRadius.circular(8),
              border: Border.all(
                color: item.selectedOptionId == quiz.correctOptionId
                    ? Colors.green
                    : Colors.red,
              ),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Icon(
                      item.selectedOptionId == quiz.correctOptionId
                          ? Icons.check_circle
                          : Icons.cancel,
                      color: item.selectedOptionId == quiz.correctOptionId
                          ? Colors.green
                          : Colors.red,
                    ),
                    const SizedBox(width: 8),
                    Text(
                      item.selectedOptionId == quiz.correctOptionId
                          ? 'Benar!'
                          : 'Kurang tepat',
                      style: theme.textTheme.titleSmall?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 8),
                Text(quiz.explanation, style: theme.textTheme.bodyMedium),
              ],
            ),
          ),
          const SizedBox(height: 12),
          FilledButton(
            onPressed: () {
              if (_currentIndex < _items.length - 1) {
                setState(() => _currentIndex++);
              } else {
                setState(() => _sessionDone = true);
              }
            },
            child: Text(
              _currentIndex < _items.length - 1
                  ? 'Soal Berikutnya'
                  : 'Lihat Hasil',
            ),
          ),
        ],
      ],
    );
  }

  Widget _buildSummary() {
    final theme = Theme.of(context);
    final wrongItems = _items
        .where((item) => item.selectedOptionId != item.quiz.correctOptionId)
        .toList();

    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        Card(
          child: Padding(
            padding: const EdgeInsets.all(20),
            child: Column(
              children: [
                Icon(
                  _correctCount == _items.length
                      ? Icons.celebration
                      : Icons.assessment,
                  size: 48,
                  color: theme.colorScheme.primary,
                ),
                const SizedBox(height: 12),
                Text(
                  'Hasil Kuis',
                  style: theme.textTheme.headlineSmall?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 8),
                Text(
                  '$_correctCount / ${_items.length} benar',
                  style: theme.textTheme.titleLarge?.copyWith(
                    color: theme.colorScheme.primary,
                  ),
                ),
              ],
            ),
          ),
        ),
        if (wrongItems.isNotEmpty) ...[
          const SizedBox(height: 16),
          Text(
            'Pelajari lebih lanjut:',
            style: theme.textTheme.titleSmall?.copyWith(
              fontWeight: FontWeight.w600,
            ),
          ),
          const SizedBox(height: 8),
          for (final item in wrongItems)
            Card(
              child: ListTile(
                title: Text(item.quiz.prompt, maxLines: 2),
                trailing: const Icon(Icons.arrow_forward_ios, size: 16),
                onTap: () => widget.onOpenTopic(item.quiz.topicId),
              ),
            ),
        ],
        const SizedBox(height: 16),
        OutlinedButton(
          onPressed: () => Navigator.of(context).pop(),
          child: const Text('Kembali'),
        ),
      ],
    );
  }
}

class _QuizItem {
  final Quiz quiz;
  final List<QuizOption> shuffledOptions;
  String? selectedOptionId;
  bool isAnswered = false;

  _QuizItem({required this.quiz, required this.shuffledOptions});
}

class _OptionButton extends StatelessWidget {
  final QuizOption option;
  final bool isSelected;
  final bool? isCorrect; // null before answer
  final bool isLocked;
  final VoidCallback? onTap;

  const _OptionButton({
    required this.option,
    required this.isSelected,
    required this.isCorrect,
    required this.isLocked,
    this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    Color? borderColor;
    Color? bgColor;
    if (isCorrect == true) {
      borderColor = Colors.green;
      bgColor = Colors.green.withValues(alpha: 0.1);
    } else if (isCorrect == false && isSelected) {
      borderColor = Colors.red;
      bgColor = Colors.red.withValues(alpha: 0.1);
    } else if (isSelected) {
      borderColor = theme.colorScheme.primary;
      bgColor = theme.colorScheme.primaryContainer.withValues(alpha: 0.3);
    }

    return Semantics(
      label:
          '${option.text}${isCorrect == true ? ', benar' : ''}${isCorrect == false && isSelected ? ', salah' : ''}',
      selected: isSelected,
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(8),
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
          decoration: BoxDecoration(
            color: bgColor,
            border: Border.all(
              color: borderColor ?? theme.colorScheme.outlineVariant,
              width: isSelected ? 2 : 1,
            ),
            borderRadius: BorderRadius.circular(8),
          ),
          child: Row(
            children: [
              Expanded(
                child: Text(option.text, style: theme.textTheme.bodyMedium),
              ),
              if (isCorrect == true)
                const Icon(Icons.check_circle, color: Colors.green, size: 20),
              if (isCorrect == false && isSelected)
                const Icon(Icons.cancel, color: Colors.red, size: 20),
            ],
          ),
        ),
      ),
    );
  }
}
