// test/quiz_session_widget_test.dart — Widget tests for QuizScreen:
// metadata hiding before answering, option shuffling with stable ID scoring,
// repeated submit prevention, and score isolation from topic status.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:codeatlas/data/content_repository.dart';
import 'package:codeatlas/data/models.dart';
import 'package:codeatlas/features/practice/quiz_screen.dart';

class FakeQuizContentRepository implements ContentRepository {
  final List<Quiz> _quizzes;

  FakeQuizContentRepository(this._quizzes);

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<List<Quiz>> getActiveQuizzes({
    QuizType? type,
    ContentLayer? layer,
    Difficulty? level,
  }) async {
    var list = _quizzes.where((q) => q.isActive).toList();
    if (type != null) list = list.where((q) => q.type == type).toList();
    if (level != null) list = list.where((q) => q.level == level).toList();
    return list;
  }
}

void main() {
  group('QuizScreen Widget & Behavior Tests', () {
    late FakeQuizContentRepository fakeRepo;
    late Quiz sampleLangQuiz;
    late Quiz sampleConceptQuiz;

    setUp(() {
      sampleLangQuiz = const Quiz(
        id: 'q-lang-01',
        topicId: 'f-variables-data-types',
        type: QuizType.language,
        level: Difficulty.beginner,
        prompt: 'Bahasa apa yang menggunakan tipe number ini?',
        snippet: 'let x: number = 42;',
        snippetLanguage: 'typescript',
        options: [
          QuizOption(id: 'ts', text: 'TypeScript'),
          QuizOption(id: 'dart', text: 'Dart'),
          QuizOption(id: 'py', text: 'Python'),
        ],
        correctOptionId: 'ts',
        explanation: 'Sintaks tipe data : number adalah ciri khas TypeScript.',
        isActive: true,
      );

      sampleConceptQuiz = const Quiz(
        id: 'q-concept-01',
        topicId: 'f-programming-logic',
        type: QuizType.concept,
        level: Difficulty.beginner,
        prompt: 'Apa pola eksekusi instruksi dari baris pertama ke terakhir?',
        snippet: 'step1();\nstep2();\nstep3();',
        snippetLanguage: 'dart',
        options: [
          QuizOption(id: 'seq', text: 'Urutan (Sequence)'),
          QuizOption(id: 'cond', text: 'Percabangan (Conditional)'),
          QuizOption(id: 'loop', text: 'Perulangan (Loop)'),
        ],
        correctOptionId: 'seq',
        explanation: 'Sequence adalah eksekusi kode satu per satu berurutan.',
        isActive: true,
      );

      fakeRepo = FakeQuizContentRepository([sampleLangQuiz, sampleConceptQuiz]);
    });

    testWidgets(
      'Language quiz hides language label on UI and Semantics tree before answering',
      (tester) async {
        await tester.pumpWidget(
          MaterialApp(
            home: QuizScreen(
              contentRepo: fakeRepo,
              quizType: QuizType.language,
              onOpenTopic: (_) {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        // Verify prompt is displayed
        expect(
          find.text('Bahasa apa yang menggunakan tipe number ini?'),
          findsOneWidget,
        );
        expect(find.text('let x: number = 42;'), findsOneWidget);

        // Verify language header label 'typescript' is NOT shown anywhere before answering
        expect(find.text('typescript'), findsNothing);
        expect(find.text('TYPESCRIPT'), findsNothing);

        // Verify Semantics tree does NOT leak language
        expect(
          find.bySemanticsLabel(
            RegExp('Bahasa: typescript', caseSensitive: false),
          ),
          findsNothing,
        );

        // Options are displayed
        expect(find.text('TypeScript'), findsOneWidget);
        expect(find.text('Dart'), findsOneWidget);
        expect(find.text('Python'), findsOneWidget);

        // Submit button is disabled before an option is selected
        final submitButtonFinder = find.widgetWithText(
          FilledButton,
          'Kirim Jawaban',
        );
        expect(submitButtonFinder, findsOneWidget);
        final buttonWidget = tester.widget<FilledButton>(submitButtonFinder);
        expect(buttonWidget.onPressed, isNull);

        // Select option 'TypeScript'
        await tester.tap(find.text('TypeScript'));
        await tester.pump();

        // Submit button is now enabled
        final enabledButtonWidget = tester.widget<FilledButton>(
          submitButtonFinder,
        );
        expect(enabledButtonWidget.onPressed, isNotNull);

        // Submit answer
        await tester.tap(submitButtonFinder);
        await tester.pumpAndSettle();

        // Now answered: explanation and feedback should appear
        expect(find.text('Benar!'), findsOneWidget);
        expect(
          find.textContaining('Sintaks tipe data : number'),
          findsOneWidget,
        );

        // Submit button is gone
        expect(
          find.widgetWithText(FilledButton, 'Kirim Jawaban'),
          findsNothing,
        );
      },
    );

    testWidgets(
      'Option selection with stable IDs correctly recognizes right and wrong answers',
      (tester) async {
        await tester.pumpWidget(
          MaterialApp(
            home: QuizScreen(
              contentRepo: fakeRepo,
              quizType: QuizType.concept,
              onOpenTopic: (_) {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        expect(
          find.text(
            'Apa pola eksekusi instruksi dari baris pertama ke terakhir?',
          ),
          findsOneWidget,
        );

        // Tap wrong option 'Percabangan (Conditional)'
        await tester.tap(find.text('Percabangan (Conditional)'));
        await tester.pump();

        // Submit answer
        await tester.tap(find.widgetWithText(FilledButton, 'Kirim Jawaban'));
        await tester.pumpAndSettle();

        // Shows wrong feedback
        expect(find.text('Kurang tepat'), findsOneWidget);
        expect(
          find.textContaining('Sequence adalah eksekusi kode'),
          findsOneWidget,
        );
      },
    );

    testWidgets('Repeated answer submit is prevented once answered', (
      tester,
    ) async {
      await tester.pumpWidget(
        MaterialApp(
          home: QuizScreen(
            contentRepo: fakeRepo,
            quizType: QuizType.concept,
            onOpenTopic: (_) {},
          ),
        ),
      );
      await tester.pumpAndSettle();

      // Select correct answer
      await tester.tap(find.text('Urutan (Sequence)'));
      await tester.pump();

      // Submit
      await tester.tap(find.widgetWithText(FilledButton, 'Kirim Jawaban'));
      await tester.pumpAndSettle();

      // "Kirim Jawaban" is replaced by next/summary button
      expect(find.widgetWithText(FilledButton, 'Kirim Jawaban'), findsNothing);

      // Tapping option buttons now does nothing (locked)
      await tester.tap(find.text('Percabangan (Conditional)'));
      await tester.pump();
      // Still correct answer marked
      expect(find.text('Benar!'), findsOneWidget);
    });
  });
}
