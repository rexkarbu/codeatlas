// test/roadmap_filter_widget_test.dart — Widget test for Progressive RoadmapScreen:
// 3-level progressive flow (layer/group list -> group view -> focus panel),
// cross-group prerequisite jumping, back navigation, and topic opening.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:codeatlas/data/content_repository.dart';
import 'package:codeatlas/data/learning_repository.dart';
import 'package:codeatlas/data/models.dart';
import 'package:codeatlas/features/roadmap/roadmap_screen.dart';

class FakeRoadmapContentRepository implements ContentRepository {
  final List<Category> categories;
  final List<Topic> topics;
  final Map<String, List<String>> prereqs;

  FakeRoadmapContentRepository({
    required this.categories,
    required this.topics,
    required this.prereqs,
  });

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<List<Category>> getAllCategories() async => categories;

  @override
  Future<List<Topic>> getAllActiveTopics() async => topics;

  @override
  Future<Map<String, List<String>>> getPrerequisiteGraph() async => prereqs;
}

class FakeRoadmapLearningRepository implements LearningRepository {
  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<Map<String, Progress>> getAllProgress() async => {};
}

void main() {
  group('Progressive RoadmapScreen Tests', () {
    late FakeRoadmapContentRepository fakeContentRepo;
    late FakeRoadmapLearningRepository fakeLearningRepo;

    setUp(() {
      final mockCategories = [
        const Category(
          id: 'f-logic',
          layer: ContentLayer.fundamentals,
          kind: CategoryKind.group,
          title: 'Logika Dasar',
          description: 'Kelompok fundamental logika',
          sortOrder: 1,
        ),
        const Category(
          id: 'e-platforms',
          layer: ContentLayer.ecosystem,
          kind: CategoryKind.group,
          title: 'Platform & Apps',
          description: 'Kelompok ekosistem aplikasi',
          sortOrder: 1,
        ),
        const Category(
          id: 'e-frontend',
          parentId: 'e-platforms',
          layer: ContentLayer.ecosystem,
          kind: CategoryKind.domain,
          title: 'Frontend Domain',
          description: 'Desc',
          sortOrder: 1,
        ),
        const Category(
          id: 'e-backend',
          parentId: 'e-platforms',
          layer: ContentLayer.ecosystem,
          kind: CategoryKind.domain,
          title: 'Backend Domain',
          description: 'Desc',
          sortOrder: 2,
        ),
      ];

      final mockTopics = [
        const Topic(
          id: 'f-logic-top',
          categoryId: 'f-logic',
          title: 'Logic Topic',
          level: Difficulty.beginner,
          summary: 'Sum',
          explanationSimple: 'Simp',
          explanationTechnical: 'Tech',
          whyVibecodingMatters: 'Vibe',
          estimatedMinutes: 5,
          sortOrder: 1,
        ),
        const Topic(
          id: 'e-fe-topic',
          categoryId: 'e-frontend',
          title: 'Frontend Topic',
          level: Difficulty.beginner,
          summary: 'Sum',
          explanationSimple: 'Simp',
          explanationTechnical: 'Tech',
          whyVibecodingMatters: 'Vibe',
          estimatedMinutes: 5,
          sortOrder: 1,
        ),
        const Topic(
          id: 'e-be-topic',
          categoryId: 'e-backend',
          title: 'Backend Topic',
          level: Difficulty.beginner,
          summary: 'Sum',
          explanationSimple: 'Simp',
          explanationTechnical: 'Tech',
          whyVibecodingMatters: 'Vibe',
          estimatedMinutes: 5,
          sortOrder: 2,
        ),
      ];

      final mockPrereqs = {
        'f-logic-top': <String>[],
        'e-fe-topic': ['f-logic-top'],
        'e-be-topic': ['f-logic-top'],
      };

      fakeContentRepo = FakeRoadmapContentRepository(
        categories: mockCategories,
        topics: mockTopics,
        prereqs: mockPrereqs,
      );
      fakeLearningRepo = FakeRoadmapLearningRepository();
    });

    testWidgets(
      'Progressive flow: Level 1 groups -> Level 2 topics -> Level 3 focus panel',
      (tester) async {
        String? openedTopicId;

        await tester.pumpWidget(
          MaterialApp(
            home: RoadmapScreen(
              contentRepo: fakeContentRepo,
              learningRepo: fakeLearningRepo,
              onOpenTopic: (id) => openedTopicId = id,
            ),
          ),
        );
        await tester.pumpAndSettle();

        // Level 1: Shows Fundamental group card
        expect(find.text('Logika Dasar'), findsOneWidget);
        expect(find.text('Platform & Apps'), findsNothing);

        // Switch to Ekosistem layer
        await tester.tap(find.widgetWithText(FilterChip, 'Ekosistem'));
        await tester.pumpAndSettle();

        // Now Level 1 shows Platform & Apps group card
        expect(find.text('Platform & Apps'), findsOneWidget);
        expect(find.text('Logika Dasar'), findsNothing);

        // Tap group card to enter Level 2
        await tester.tap(find.text('Platform & Apps'));
        await tester.pumpAndSettle();

        // Inside Level 2: group topics are visible
        expect(find.text('Frontend Topic'), findsOneWidget);
        expect(find.text('Backend Topic'), findsOneWidget);

        // Tap topic to enter Level 3 focus panel
        await tester.tap(find.text('Frontend Topic'));
        await tester.pumpAndSettle();

        // Focus panel displayed
        expect(find.text('Buka Artikel'), findsOneWidget);
        expect(find.textContaining('Prasyarat:'), findsOneWidget);

        // Open article
        await tester.tap(find.text('Buka Artikel'));
        await tester.pumpAndSettle();

        expect(openedTopicId, equals('e-fe-topic'));
      },
    );

    testWidgets(
      'Cross-group prerequisite jump updates layer, group, and focused topic',
      (tester) async {
        await tester.pumpWidget(
          MaterialApp(
            home: RoadmapScreen(
              contentRepo: fakeContentRepo,
              learningRepo: fakeLearningRepo,
              onOpenTopic: (_) {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        // Switch to Ekosistem and open Platform & Apps
        await tester.tap(find.widgetWithText(FilterChip, 'Ekosistem'));
        await tester.pumpAndSettle();
        await tester.tap(find.text('Platform & Apps'));
        await tester.pumpAndSettle();

        // Focus Frontend Topic
        await tester.tap(find.text('Frontend Topic'));
        await tester.pumpAndSettle();

        // Prerequisite chip links to cross-group topic 'Logic Topic' from 'Logika Dasar'
        expect(find.text('Logic Topic'), findsWidgets);

        // Tap the prerequisite chip inside focus panel or topic card
        final jumpChip = find.widgetWithText(ActionChip, 'Logic Topic');
        expect(jumpChip, findsWidgets);
        await tester.tap(jumpChip.first);
        await tester.pumpAndSettle();

        // We should now be in Logika Dasar group (Fundamental layer) focusing Logic Topic!
        expect(find.text('Logika Dasar'), findsWidgets);
        expect(find.text('Buka Artikel'), findsOneWidget);

        // Tap back button (top bar in group view)
        await tester.tap(find.byIcon(Icons.arrow_back));
        await tester.pumpAndSettle();

        // Back returns to previous context (Ekosistem / Platform & Apps)
        expect(find.text('Platform & Apps'), findsWidgets);
      },
    );
  });
}
