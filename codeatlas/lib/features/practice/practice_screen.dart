// lib/features/practice/practice_screen.dart — Entry point for quiz and
// comparison features.

import 'package:flutter/material.dart';

import '../../data/content_repository.dart';
import '../../data/learning_repository.dart';
import '../../data/models.dart';
import 'quiz_screen.dart';
import 'comparison_screen.dart';

class PracticeScreen extends StatelessWidget {
  final ContentRepository contentRepo;
  final LearningRepository learningRepo;
  final void Function(String topicId) onOpenTopic;

  const PracticeScreen({
    super.key,
    required this.contentRepo,
    required this.learningRepo,
    required this.onOpenTopic,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Scaffold(
      appBar: AppBar(title: const Text('Latihan')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          // Quiz Section
          Card(
            child: Padding(
              padding: const EdgeInsets.all(20),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      Icon(Icons.quiz, color: theme.colorScheme.primary),
                      const SizedBox(width: 8),
                      Text(
                        'Kuis Pengenalan Kode',
                        style: theme.textTheme.titleMedium?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 8),
                  Text(
                    'Uji kemampuanmu mengenali bahasa pemrograman dan konsep dari potongan kode.',
                    style: theme.textTheme.bodyMedium?.copyWith(
                      color: theme.colorScheme.onSurfaceVariant,
                    ),
                  ),
                  const SizedBox(height: 16),
                  Wrap(
                    spacing: 8,
                    runSpacing: 8,
                    children: [
                      FilledButton.icon(
                        onPressed: () => _startQuiz(context, QuizType.language),
                        icon: const Icon(Icons.code),
                        label: const Text('Tebak Bahasa'),
                      ),
                      OutlinedButton.icon(
                        onPressed: () => _startQuiz(context, QuizType.concept),
                        icon: const Icon(Icons.lightbulb_outline),
                        label: const Text('Tebak Konsep'),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ),

          const SizedBox(height: 16),

          // Comparison Section
          Card(
            child: Padding(
              padding: const EdgeInsets.all(20),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      Icon(
                        Icons.compare_arrows,
                        color: theme.colorScheme.primary,
                      ),
                      const SizedBox(width: 8),
                      Text(
                        'Perbandingan Sintaks',
                        style: theme.textTheme.titleMedium?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 8),
                  Text(
                    'Bandingkan bagaimana konsep yang sama ditulis dalam beberapa bahasa pemrograman.',
                    style: theme.textTheme.bodyMedium?.copyWith(
                      color: theme.colorScheme.onSurfaceVariant,
                    ),
                  ),
                  const SizedBox(height: 16),
                  FilledButton.tonalIcon(
                    onPressed: () => _openComparison(context),
                    icon: const Icon(Icons.compare),
                    label: const Text('Lihat Perbandingan'),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  void _startQuiz(BuildContext context, QuizType type) {
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) => QuizScreen(
          contentRepo: contentRepo,
          quizType: type,
          onOpenTopic: onOpenTopic,
        ),
      ),
    );
  }

  void _openComparison(BuildContext context) {
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) => ComparisonScreen(
          contentRepo: contentRepo,
          onOpenTopic: onOpenTopic,
        ),
      ),
    );
  }
}
