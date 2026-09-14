// test/explore_filter_widget_test.dart — Widget tests for ExploreScreen:
// tab switching, category filter dropdown, difficulty chips, combined AND filtering,
// and filter reset behavior.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:codeatlas/data/content_repository.dart';
import 'package:codeatlas/data/learning_repository.dart';
import 'package:codeatlas/data/models.dart';
import 'package:codeatlas/features/explore/explore_screen.dart';

class FakeExploreContentRepository implements ContentRepository {
  final List<Category> categories;
  final List<Topic> topics;

  FakeExploreContentRepository({
    required this.categories,
    required this.topics,
  });

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<List<Category>> getAllCategories() async => categories;

  @override
  Future<List<Category>> getCategoriesByLayer(ContentLayer layer) async {
    return categories.where((c) => c.layer == layer).toList();
  }

  @override
  Future<List<Category>> getGroupCategories(ContentLayer layer) async {
    return categories
        .where((c) => c.layer == layer && c.kind == CategoryKind.group)
        .toList();
  }

  @override
  Future<List<Category>> getDomainsByGroup(String groupId) async {
    return categories
        .where((c) => c.kind == CategoryKind.domain && c.parentId == groupId)
        .toList();
  }

  @override
  Future<List<Topic>> getAllActiveTopics() async => topics;

  @override
  Future<List<Topic>> getTopicsByCategory(String categoryId) async {
    return topics.where((t) => t.categoryId == categoryId).toList();
  }

  @override
  Future<List<Topic>> search(
    String query, {
    ContentLayer? layer,
    String? categoryId,
    Difficulty? level,
  }) async {
    final catMap = {for (final c in categories) c.id: c};
    final categoryChildIds = <String, Set<String>>{};
    for (final c in categories) {
      if (c.parentId != null) {
        categoryChildIds.putIfAbsent(c.parentId!, () => {}).add(c.id);
      }
    }

    return topics.where((t) {
      final cat = catMap[t.categoryId];
      if (layer != null && cat?.layer != layer) return false;
      if (categoryId != null) {
        final direct = t.categoryId == categoryId;
        final child =
            categoryChildIds[categoryId]?.contains(t.categoryId) ?? false;
        if (!direct && !child) return false;
      }
      if (level != null && t.level != level) return false;
      if (query.trim().isNotEmpty &&
          !t.title.toLowerCase().contains(query.toLowerCase()) &&
          !t.summary.toLowerCase().contains(query.toLowerCase())) {
        return false;
      }
      return true;
    }).toList();
  }
}

class FakeExploreLearningRepository implements LearningRepository {
  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<Map<String, Progress>> getAllProgress() async => {};
}

void main() {
  group('ExploreScreen Search & Combined Filters Widget Tests', () {
    late FakeExploreContentRepository fakeContentRepo;
    late FakeExploreLearningRepository fakeLearningRepo;

    setUp(() {
      final mockCategories = [
        // Fundamental groups
        const Category(
          id: 'f-logic-syntax',
          layer: ContentLayer.fundamentals,
          kind: CategoryKind.group,
          title: 'Logika & Sintaks',
          description: 'Dasar alur eksekusi',
          sortOrder: 1,
        ),
        const Category(
          id: 'f-data-algo',
          layer: ContentLayer.fundamentals,
          kind: CategoryKind.group,
          title: 'Struktur Data',
          description: 'Penyimpanan data memori',
          sortOrder: 2,
        ),
        // Ecosystem groups & domains
        const Category(
          id: 'e-platforms',
          layer: ContentLayer.ecosystem,
          kind: CategoryKind.group,
          title: 'Platform & Aplikasi',
          description: 'Lingkungan aplikasi',
          sortOrder: 1,
        ),
        const Category(
          id: 'e-frontend',
          parentId: 'e-platforms',
          layer: ContentLayer.ecosystem,
          kind: CategoryKind.domain,
          title: 'Frontend Web',
          description: 'Browser client',
          sortOrder: 1,
        ),
      ];

      final mockTopics = [
        const Topic(
          id: 'f-programming-logic',
          categoryId: 'f-logic-syntax',
          title: 'Programming Logic',
          level: Difficulty.beginner,
          summary: 'Dasar instruksi komputer berurutan',
          explanationSimple: 'Simp',
          explanationTechnical: 'Tech',
          whyVibecodingMatters: 'Vibe',
          estimatedMinutes: 5,
          sortOrder: 1,
        ),
        const Topic(
          id: 'f-data-structures',
          categoryId: 'f-data-algo',
          title: 'Data Structures',
          level: Difficulty.intermediate,
          summary: 'List, map, dan set',
          explanationSimple: 'Simp',
          explanationTechnical: 'Tech',
          whyVibecodingMatters: 'Vibe',
          estimatedMinutes: 8,
          sortOrder: 2,
        ),
        const Topic(
          id: 'e-frontend-overview',
          categoryId: 'e-frontend',
          title: 'Frontend Overview',
          level: Difficulty.beginner,
          summary: 'HTML, CSS, dan DOM',
          explanationSimple: 'Simp',
          explanationTechnical: 'Tech',
          whyVibecodingMatters: 'Vibe',
          estimatedMinutes: 6,
          sortOrder: 1,
        ),
      ];

      fakeContentRepo = FakeExploreContentRepository(
        categories: mockCategories,
        topics: mockTopics,
      );
      fakeLearningRepo = FakeExploreLearningRepository();
    });

    testWidgets(
      'Explore screen switches between Fundamental and Ekosistem tabs',
      (tester) async {
        await tester.pumpWidget(
          MaterialApp(
            home: ExploreScreen(
              contentRepo: fakeContentRepo,
              learningRepo: fakeLearningRepo,
              onOpenTopic: (_) {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        // Initially in Fundamental tab: displays Fundamental groups
        expect(find.text('Logika & Sintaks'), findsOneWidget);
        expect(find.text('Struktur Data'), findsOneWidget);

        // Switch to Ekosistem tab
        await tester.tap(find.text('Ekosistem'));
        await tester.pumpAndSettle();

        // Displays Ecosystem groups
        expect(find.text('Platform & Aplikasi'), findsOneWidget);
      },
    );

    testWidgets(
      'Search mode with Category and Difficulty filters combines with AND logic',
      (tester) async {
        await tester.pumpWidget(
          MaterialApp(
            home: ExploreScreen(
              contentRepo: fakeContentRepo,
              learningRepo: fakeLearningRepo,
              onOpenTopic: (_) {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        // Open Search mode
        await tester.tap(find.byIcon(Icons.search));
        await tester.pumpAndSettle();

        // Verify search input field appears
        expect(find.byType(TextField), findsOneWidget);

        // Both topics visible in Fundamental tab with no filters
        expect(find.text('Programming Logic'), findsOneWidget);
        expect(find.text('Data Structures'), findsOneWidget);

        // 1. Filter by Level: Pemula
        await tester.tap(find.widgetWithText(FilterChip, 'Pemula'));
        await tester.pumpAndSettle();

        // Only Programming Logic (Pemula) matches, Data Structures (Menengah) is filtered out
        expect(find.text('Programming Logic'), findsOneWidget);
        expect(find.text('Data Structures'), findsNothing);

        // 2. Select Category 'Struktur Data' while Pemula is active -> 0 results
        await tester.tap(
          find.byKey(const ValueKey('category_filter_dropdown')),
        );
        await tester.pumpAndSettle();
        await tester.tap(find.text('Struktur Data').last);
        await tester.pumpAndSettle();

        // No topics match Pemula + Struktur Data (AND condition)
        expect(find.text('Tidak ditemukan'), findsOneWidget);

        // 3. Reset filters button resets all filters
        await tester.drag(
          find.byType(SingleChildScrollView).first,
          const Offset(-300, 0),
        );
        await tester.pumpAndSettle();

        expect(find.text('Reset filter'), findsOneWidget);
        await tester.tap(find.text('Reset filter'));
        await tester.pumpAndSettle();

        // Returns to full list
        expect(find.text('Programming Logic'), findsOneWidget);
        expect(find.text('Data Structures'), findsOneWidget);
      },
    );
  });
}
