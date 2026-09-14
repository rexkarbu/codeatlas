// test/comparison_widget_test.dart — Widget test for ComparisonScreen:
// 200% text scale, 360/400px widths, concept selector bottom sheet,
// 2 and 3 language selections, and layout toggle button.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:codeatlas/data/content_repository.dart';
import 'package:codeatlas/data/models.dart';
import 'package:codeatlas/features/practice/comparison_screen.dart';

class FakeComparisonContentRepository implements ContentRepository {
  final List<ComparisonGroup> groups;
  final Set<String> languages;

  FakeComparisonContentRepository({
    required this.groups,
    required this.languages,
  });

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<List<ComparisonGroup>> getComparisonGroups() async => groups;

  @override
  Future<Set<String>> getComparisonLanguages() async => languages;
}

void main() {
  group('ComparisonScreen UI & Adaptability Tests', () {
    late FakeComparisonContentRepository fakeRepo;

    setUp(() {
      final mockExamples = [
        const CodeExample(
          language: 'Dart',
          comparisonKey: 'variables',
          label: 'Dart Variables',
          code: 'int age = 25;\nString name = "Atlas";',
          explanation: 'Tipe data statis dengan inferensi kuat.',
          expectedOutput: 'age: 25, name: Atlas',
        ),
        const CodeExample(
          language: 'TypeScript',
          comparisonKey: 'variables',
          label: 'TypeScript Variables',
          code: 'let age: number = 25;\nconst name: string = "Atlas";',
          explanation:
              'Superset JavaScript dengan sistem tipe opsional statis.',
          expectedOutput: 'age: 25, name: Atlas',
        ),
        const CodeExample(
          language: 'Python',
          comparisonKey: 'variables',
          label: 'Python Variables',
          code: 'age: int = 25\nname: str = "Atlas"',
          explanation: 'Pengetikan dinamis dengan dukungan type hint.',
          expectedOutput: 'age: 25, name: Atlas',
        ),
      ];

      final mockGroup1 = ComparisonGroup(
        comparisonKey: 'variables',
        topicId: 'f-variables-data-types',
        topicTitle: 'Variables & Data Types',
        examples: mockExamples,
      );

      final mockGroup2 = ComparisonGroup(
        comparisonKey: 'sequence',
        topicId: 'f-programming-logic',
        topicTitle: 'Programming Logic',
        examples: [
          const CodeExample(
            language: 'Dart',
            comparisonKey: 'sequence',
            label: 'Dart Sequence',
            code: 'print("Langkah 1");\nprint("Langkah 2");',
            explanation: 'Instruksi sekuensial.',
            expectedOutput: 'Langkah 1\nLangkah 2',
          ),
          const CodeExample(
            language: 'TypeScript',
            comparisonKey: 'sequence',
            label: 'TypeScript Sequence',
            code: 'console.log("Langkah 1");\nconsole.log("Langkah 2");',
            explanation: 'Instruksi sekuensial.',
            expectedOutput: 'Langkah 1\nLangkah 2',
          ),
        ],
      );

      fakeRepo = FakeComparisonContentRepository(
        groups: [mockGroup1, mockGroup2],
        languages: {'Dart', 'TypeScript', 'Python'},
      );
    });

    testWidgets(
      '200% text scale on 360px width defaults to vertical layout without overflow',
      (tester) async {
        // Set up 200% text scale factor on 360 logical px width
        await tester.pumpWidget(
          MaterialApp(
            home: MediaQuery(
              data: const MediaQueryData(
                textScaler: TextScaler.linear(2.0),
                size: Size(360, 1600),
              ),
              child: ComparisonScreen(
                contentRepo: fakeRepo,
                onOpenTopic: (_) {},
              ),
            ),
          ),
        );
        await tester.pumpAndSettle();

        // 1. Concept selector button is rendered with Indonesian label
        expect(
          find.byKey(const ValueKey('concept_selector_button')),
          findsOneWidget,
        );
        expect(find.textContaining('Konsep: Variabel'), findsOneWidget);

        // 2. Defaults to vertical stacked list (ListView)
        // Verify Dart card is rendered first
        expect(
          find.descendant(of: find.byType(Card), matching: find.text('Dart')),
          findsOneWidget,
        );
        expect(find.textContaining('int age = 25;'), findsOneWidget);

        // Scroll down to reveal TypeScript card
        await tester.drag(find.byType(ListView).last, const Offset(0, -600));
        await tester.pumpAndSettle();

        expect(
          find.descendant(
            of: find.byType(Card),
            matching: find.text('TypeScript'),
          ),
          findsOneWidget,
        );
        expect(find.textContaining('let age: number = 25;'), findsOneWidget);

        // Scroll down to reveal Python card
        await tester.drag(find.byType(ListView).last, const Offset(0, -600));
        await tester.pumpAndSettle();

        expect(
          find.descendant(of: find.byType(Card), matching: find.text('Python')),
          findsOneWidget,
        );
        expect(find.textContaining('age: int = 25'), findsOneWidget);

        // 3. Verify no RenderFlex overflow exception occurred
        expect(tester.takeException(), isNull);
      },
    );

    testWidgets(
      'Concept selector button opens bottom sheet and changes selected concept',
      (tester) async {
        await tester.pumpWidget(
          MaterialApp(
            home: MediaQuery(
              data: const MediaQueryData(
                textScaler: TextScaler.linear(1.0),
                size: Size(400, 900),
              ),
              child: ComparisonScreen(
                contentRepo: fakeRepo,
                onOpenTopic: (_) {},
              ),
            ),
          ),
        );
        await tester.pumpAndSettle();

        // 1. Initial concept is 'variables' ('Variabel')
        expect(find.textContaining('Konsep: Variabel'), findsOneWidget);

        // 2. Tap concept selector button to open bottom sheet
        await tester.tap(find.byKey(const ValueKey('concept_selector_button')));
        await tester.pumpAndSettle();

        // 3. Bottom sheet displays options with Indonesian labels
        expect(find.text('Pilih Konsep Sintaks'), findsOneWidget);
        final optionSeqFinder = find.byKey(
          const ValueKey('concept_option_f-programming-logic_sequence'),
        );
        expect(optionSeqFinder, findsOneWidget);
        expect(find.text('Urutan Instruksi'), findsOneWidget);

        // 4. Tap 'Urutan Instruksi' option
        await tester.tap(optionSeqFinder);
        await tester.pumpAndSettle();

        // 5. Concept selector button and view are updated
        expect(find.textContaining('Konsep: Urutan Instruksi'), findsOneWidget);
        expect(find.textContaining('Langkah 1'), findsWidgets);
      },
    );

    testWidgets('Language selection filter toggles between 2 and 3 languages', (
      tester,
    ) async {
      await tester.pumpWidget(
        MaterialApp(
          home: MediaQuery(
            data: const MediaQueryData(
              textScaler: TextScaler.linear(1.0),
              size: Size(400, 1600),
            ),
            child: ComparisonScreen(contentRepo: fakeRepo, onOpenTopic: (_) {}),
          ),
        ),
      );
      await tester.pumpAndSettle();

      // Initially all 3 languages (Dart, TypeScript, Python) are selected
      expect(
        find.descendant(of: find.byType(Card), matching: find.text('Dart')),
        findsOneWidget,
      );
      expect(
        find.descendant(
          of: find.byType(Card),
          matching: find.text('TypeScript'),
        ),
        findsOneWidget,
      );

      // Scroll to verify Python card
      await tester.drag(find.byType(ListView).last, const Offset(0, -400));
      await tester.pumpAndSettle();
      expect(
        find.descendant(of: find.byType(Card), matching: find.text('Python')),
        findsOneWidget,
      );

      // Scroll back up to reach filter chips
      await tester.drag(find.byType(ListView).last, const Offset(0, 400));
      await tester.pumpAndSettle();

      // Tap Python FilterChip to deselect it
      final pythonChipFinder = find.widgetWithText(FilterChip, 'Python');
      expect(pythonChipFinder, findsOneWidget);
      await tester.tap(pythonChipFinder);
      await tester.pumpAndSettle();

      // Now only 2 languages are shown (Dart and TypeScript)
      expect(
        find.descendant(of: find.byType(Card), matching: find.text('Dart')),
        findsOneWidget,
      );
      expect(
        find.descendant(
          of: find.byType(Card),
          matching: find.text('TypeScript'),
        ),
        findsOneWidget,
      );
      expect(
        find.descendant(of: find.byType(Card), matching: find.text('Python')),
        findsNothing,
      );

      // Tap Python FilterChip again to re-select it
      await tester.tap(pythonChipFinder);
      await tester.pumpAndSettle();

      // Scroll down to verify Python card is back
      await tester.drag(find.byType(ListView).last, const Offset(0, -400));
      await tester.pumpAndSettle();

      expect(
        find.descendant(of: find.byType(Card), matching: find.text('Python')),
        findsOneWidget,
      );
    });

    testWidgets(
      'Layout toggle button toggles between vertical list and horizontal swipe',
      (tester) async {
        await tester.pumpWidget(
          MaterialApp(
            home: MediaQuery(
              data: const MediaQueryData(
                textScaler: TextScaler.linear(1.0),
                size: Size(400, 900),
              ),
              child: ComparisonScreen(
                contentRepo: fakeRepo,
                onOpenTopic: (_) {},
              ),
            ),
          ),
        );
        await tester.pumpAndSettle();

        // Default layout is vertical (ListView of cards)
        expect(find.byType(ListView), findsWidgets);
        expect(find.byType(PageView), findsNothing);

        // Tap toggle button to switch to horizontal mode
        final toggleBtnFinder = find.widgetWithIcon(
          IconButton,
          Icons.view_carousel_outlined,
        );
        expect(toggleBtnFinder, findsOneWidget);

        await tester.tap(toggleBtnFinder);
        await tester.pumpAndSettle();

        // Now horizontal PageView is active
        expect(find.byType(PageView), findsOneWidget);

        // Tap toggle button again to switch back to vertical mode
        final toggleBackFinder = find.widgetWithIcon(
          IconButton,
          Icons.view_agenda_outlined,
        );
        expect(toggleBackFinder, findsOneWidget);

        await tester.tap(toggleBackFinder);
        await tester.pumpAndSettle();

        expect(find.byType(PageView), findsNothing);
        expect(
          find.descendant(of: find.byType(Card), matching: find.text('Dart')),
          findsOneWidget,
        );
      },
    );
  });
}
