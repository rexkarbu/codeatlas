// test/comparison_widget_test.dart — Widget test for ComparisonScreen:
// 200% text scale, vertical layout alternative, and layout toggle button.

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
  group('ComparisonScreen 200% Text Scale & Layout Toggle Tests (PRD 2.B)', () {
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

      final mockGroup = ComparisonGroup(
        comparisonKey: 'variables',
        topicId: 'f-variables-data-types',
        topicTitle: 'Variabel dan Tipe Data',
        examples: mockExamples,
      );

      fakeRepo = FakeComparisonContentRepository(
        groups: [mockGroup],
        languages: {'Dart', 'TypeScript', 'Python'},
      );
    });

    testWidgets(
      '200% text scale auto-switches to vertical layout and displays all 3 languages without overflow',
      (tester) async {
        // Set up 200% text scale factor (TextScaler.linear(2.0))
        await tester.pumpWidget(
          MaterialApp(
            home: MediaQuery(
              data: const MediaQueryData(
                textScaler: TextScaler.linear(2.0),
                size: Size(500, 1600),
              ),
              child: ComparisonScreen(
                contentRepo: fakeRepo,
                onOpenTopic: (_) {},
              ),
            ),
          ),
        );
        await tester.pumpAndSettle();

        // 1. Initially lists the comparison group chip
        expect(find.widgetWithText(ChoiceChip, 'variables'), findsOneWidget);
        expect(find.textContaining('Variabel dan Tipe Data'), findsOneWidget);

        // Tap group to view comparison
        await tester.tap(find.widgetWithText(ChoiceChip, 'variables'));
        await tester.pumpAndSettle();

        // 2. Under 200% scale, layout defaults to vertical stacked list (ListView)
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
      'Layout toggle button toggles between vertical list and horizontal swipe',
      (tester) async {
        await tester.pumpWidget(
          MaterialApp(
            home: MediaQuery(
              data: const MediaQueryData(
                textScaler: TextScaler.linear(1.0),
                size: Size(500, 900),
              ),
              child: ComparisonScreen(
                contentRepo: fakeRepo,
                onOpenTopic: (_) {},
              ),
            ),
          ),
        );
        await tester.pumpAndSettle();

        // Open comparison
        await tester.tap(find.widgetWithText(ChoiceChip, 'variables'));
        await tester.pumpAndSettle();

        // Default on scale 1.0 is horizontal PageView
        expect(find.byType(PageView), findsOneWidget);

        // Tap toggle button to switch to vertical mode
        final toggleBtnFinder = find.widgetWithIcon(
          IconButton,
          Icons.view_agenda_outlined,
        );
        expect(toggleBtnFinder, findsOneWidget);

        await tester.tap(toggleBtnFinder);
        await tester.pumpAndSettle();

        // Now vertical mode (ListView of cards) is active, PageView is gone
        expect(find.byType(PageView), findsNothing);
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

        // Tap toggle button again to switch back to horizontal PageView
        final toggleBackFinder = find.widgetWithIcon(
          IconButton,
          Icons.view_carousel_outlined,
        );
        expect(toggleBackFinder, findsOneWidget);

        await tester.tap(toggleBackFinder);
        await tester.pumpAndSettle();

        expect(find.byType(PageView), findsOneWidget);
      },
    );
  });
}
