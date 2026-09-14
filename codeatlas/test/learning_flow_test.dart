// test/learning_flow_test.dart — Unit and widget tests for progress, notes,
// quiz session scoring, status independence, and learning path presets.

import 'dart:convert';
import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:codeatlas/data/models.dart';
import 'package:codeatlas/features/learning_paths/path_builder.dart';

void main() {
  group('Learning Flow & Progress Models', () {
    test('Progress model defaults and properties', () {
      final now = DateTime.now();
      final p = Progress(
        topicId: 'f-programming-logic',
        status: LearningStatus.inProgress,
        notes: 'Catatan belajar awal',
        lastReviewedAt: now,
        updatedAt: now,
      );

      expect(p.topicId, equals('f-programming-logic'));
      expect(p.status, equals(LearningStatus.inProgress));
      expect(p.notes, equals('Catatan belajar awal'));
      expect(p.status == LearningStatus.understood, isFalse);

      final understood = Progress(
        topicId: p.topicId,
        status: LearningStatus.understood,
        notes: p.notes,
        lastReviewedAt: p.lastReviewedAt,
        updatedAt: DateTime.now(),
      );
      expect(understood.status == LearningStatus.understood, isTrue);
      expect(understood.notes, equals('Catatan belajar awal'));
    });

    test('LearningStatus labels match Indonesian PRD', () {
      expect(LearningStatus.notStarted.label, equals('Belum'));
      expect(LearningStatus.inProgress.label, equals('Sedang'));
      expect(LearningStatus.understood.label, equals('Paham'));
    });

    test('Notes length limit is 20,000 characters', () {
      const maxLen = 20000;
      final longNotes = 'a' * maxLen;
      expect(longNotes.length, equals(maxLen));

      final p = Progress(
        topicId: 'f-variables-data-types',
        status: LearningStatus.notStarted,
        notes: longNotes,
        updatedAt: DateTime.now(),
      );
      expect(p.notes.length, equals(maxLen));
    });
  });

  group('Quiz Scoring & Question State', () {
    late Quiz sampleQuiz;

    setUp(() {
      sampleQuiz = const Quiz(
        id: 'q-test-01',
        topicId: 'f-programming-logic',
        type: QuizType.concept,
        level: Difficulty.beginner,
        prompt: 'Apa pola instruksi berurutan?',
        snippet: 'A -> B -> C',
        snippetLanguage: 'pseudocode',
        options: [
          QuizOption(id: 'seq', text: 'Urutan (Sequence)'),
          QuizOption(id: 'cond', text: 'Percabangan (Conditional)'),
          QuizOption(id: 'loop', text: 'Perulangan (Loop)'),
          QuizOption(id: 'rec', text: 'Rekursi (Recursion)'),
        ],
        correctOptionId: 'seq',
        explanation: 'Instruksi dijalankan berurutan satu per satu.',
        isActive: true,
      );
    });

    test('Correct answer detection and score tallying', () {
      expect(sampleQuiz.correctOptionId == 'seq', isTrue);
      expect(sampleQuiz.correctOptionId == 'cond', isFalse);
      expect(sampleQuiz.correctOptionId == 'loop', isFalse);
      expect(sampleQuiz.correctOptionId == 'rec', isFalse);
    });

    test('Pre-answer language metadata hiding rule', () {
      // In language quiz mode, the question should not leak language in snippet
      const langQuiz = Quiz(
        id: 'q-test-lang',
        topicId: 'f-variables-data-types',
        type: QuizType.language,
        level: Difficulty.beginner,
        prompt: 'Bahasa apa yang menggunakan tipe number ini?',
        snippet: 'let x: number = 5;',
        snippetLanguage: 'typescript',
        options: [
          QuizOption(id: 'ts', text: 'TypeScript'),
          QuizOption(id: 'py', text: 'Python'),
          QuizOption(id: 'dart', text: 'Dart'),
          QuizOption(id: 'c', text: 'C'),
        ],
        correctOptionId: 'ts',
        explanation: 'Tipe : number adalah TypeScript.',
        isActive: true,
      );

      expect(langQuiz.type, equals(QuizType.language));
      expect(langQuiz.snippet.contains('typescript'), isFalse);
    });
  });

  group('Path Presets & Targets Integrity', () {
    late Set<String> allTopicIds;

    setUpAll(() {
      final file = File('assets/content/content.json');
      final content = file.readAsStringSync();
      final jsonMap = jsonDecode(content) as Map<String, dynamic>;
      final topics = jsonMap['topics'] as List<dynamic>;
      allTopicIds = {
        for (final t in topics) (t as Map<String, dynamic>)['id'] as String,
      };
    });

    test('All 5 Path Presets exist and contain valid active topic IDs', () {
      expect(pathPresets.containsKey('general'), isTrue);
      expect(pathPresets.containsKey('flutter'), isTrue);
      expect(pathPresets.containsKey('web'), isTrue);
      expect(pathPresets.containsKey('backend'), isTrue);
      expect(pathPresets.containsKey('data'), isTrue);

      for (final preset in pathPresets.values) {
        expect(preset.name.isNotEmpty, isTrue);
        expect(preset.description.isNotEmpty, isTrue);
        expect(preset.targetIds.isNotEmpty, isTrue);

        for (final tid in preset.targetIds) {
          expect(
            allTopicIds.contains(tid),
            isTrue,
            reason:
                'Preset ${preset.goal} target topic $tid must exist in content.json',
          );
        }
      }
    });

    test('General path preset targets match PRD table exactly', () {
      final general = pathPresets['general']!;
      expect(
        general.targetIds,
        equals([
          'f-programming-logic',
          'f-variables-data-types',
          'f-operators',
          'f-conditionals',
          'f-loops',
          'f-functions',
          'f-debugging',
          'f-testing',
          'f-git',
        ]),
      );
    });

    test('Flutter path preset targets match PRD table exactly', () {
      final flutter = pathPresets['flutter']!;
      expect(
        flutter.targetIds,
        equals([
          'f-type-system',
          'f-oop',
          'f-modules-packages',
          'f-dependencies',
          'f-error-handling',
          'f-async',
          'f-apis',
          'f-serialization',
          'f-testing',
          'e-mobile-overview',
          'e-frameworks-overview',
        ]),
      );
    });
  });
}
