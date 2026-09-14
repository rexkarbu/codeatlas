// test/learning_path_algorithm_test.dart — Algorithm tests for learning path:
// transitive closure, deduplication, topological ordering, and prerequisite violation checks.

import 'dart:convert';
import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:codeatlas/data/content_repository.dart';
import 'package:codeatlas/data/models.dart';
import 'package:codeatlas/features/learning_paths/path_builder.dart';

/// In-memory mock content repository for fast, isolated algorithm testing.
class FakeContentRepository implements ContentRepository {
  final List<Topic> _topics;
  final Map<String, List<String>> _prereqs;

  FakeContentRepository(this._topics, this._prereqs);

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<List<Topic>> getAllActiveTopics() async => _topics;

  @override
  Future<Map<String, List<String>>> getPrerequisiteGraph() async => _prereqs;

  @override
  Future<Set<String>> getTransitivePrerequisites(String topicId) async {
    final result = <String>{};
    final queue = <String>[topicId];
    final visited = <String>{};

    while (queue.isNotEmpty) {
      final curr = queue.removeAt(0);
      if (!visited.add(curr)) continue;

      for (final p in _prereqs[curr] ?? []) {
        result.add(p);
        queue.add(p);
      }
    }
    return result;
  }

  @override
  Future<List<String>> getDependentTopicIds(String topicId) async {
    final dependents = <String>[];
    for (final entry in _prereqs.entries) {
      if (entry.value.contains(topicId)) {
        dependents.add(entry.key);
      }
    }
    return dependents;
  }
}

void main() {
  group('Learning Path Algorithms & Topological Closure', () {
    late FakeContentRepository fakeRepo;
    late List<Topic> mockTopics;
    late Map<String, List<String>> mockPrereqs;

    setUp(() {
      mockTopics = [
        const Topic(
          id: 'T1',
          categoryId: 'cat1',
          title: 'Topic 1 Logic',
          level: Difficulty.beginner,
          summary: 'Sum',
          explanationSimple: 'Simp',
          explanationTechnical: 'Tech',
          whyVibecodingMatters: 'Vibe',
          estimatedMinutes: 5,
          sortOrder: 1,
        ),
        const Topic(
          id: 'T2',
          categoryId: 'cat1',
          title: 'Topic 2 Vars',
          level: Difficulty.beginner,
          summary: 'Sum',
          explanationSimple: 'Simp',
          explanationTechnical: 'Tech',
          whyVibecodingMatters: 'Vibe',
          estimatedMinutes: 5,
          sortOrder: 2,
        ),
        const Topic(
          id: 'T3',
          categoryId: 'cat1',
          title: 'Topic 3 Operators',
          level: Difficulty.beginner,
          summary: 'Sum',
          explanationSimple: 'Simp',
          explanationTechnical: 'Tech',
          whyVibecodingMatters: 'Vibe',
          estimatedMinutes: 5,
          sortOrder: 3,
        ),
        const Topic(
          id: 'T4',
          categoryId: 'cat1',
          title: 'Topic 4 Conditionals',
          level: Difficulty.beginner,
          summary: 'Sum',
          explanationSimple: 'Simp',
          explanationTechnical: 'Tech',
          whyVibecodingMatters: 'Vibe',
          estimatedMinutes: 5,
          sortOrder: 4,
        ),
        const Topic(
          id: 'T5',
          categoryId: 'cat1',
          title: 'Topic 5 Loops',
          level: Difficulty.beginner,
          summary: 'Sum',
          explanationSimple: 'Simp',
          explanationTechnical: 'Tech',
          whyVibecodingMatters: 'Vibe',
          estimatedMinutes: 5,
          sortOrder: 5,
        ),
        const Topic(
          id: 'T6',
          categoryId: 'cat1',
          title: 'Topic 6 Functions',
          level: Difficulty.intermediate,
          summary: 'Sum',
          explanationSimple: 'Simp',
          explanationTechnical: 'Tech',
          whyVibecodingMatters: 'Vibe',
          estimatedMinutes: 5,
          sortOrder: 6,
        ),
        const Topic(
          id: 'T7',
          categoryId: 'cat1',
          title: 'Topic 7 Mini-Project',
          level: Difficulty.intermediate,
          summary: 'Sum',
          explanationSimple: 'Simp',
          explanationTechnical: 'Tech',
          whyVibecodingMatters: 'Vibe',
          estimatedMinutes: 10,
          sortOrder: 7,
        ),
      ];

      mockPrereqs = {
        'T1': [],
        'T2': ['T1'],
        'T3': ['T2'],
        'T4': ['T3'],
        'T5': ['T4'],
        'T6': ['T2'],
        'T7': ['T4', 'T6'],
      };

      fakeRepo = FakeContentRepository(mockTopics, mockPrereqs);
    });

    test(
      'Transitive closure includes all ancestral prerequisites recursively',
      () async {
        final path = await buildPathTopicList(['T5'], fakeRepo);
        expect(path, equals(['T1', 'T2', 'T3', 'T4', 'T5']));
      },
    );

    test(
      'Shared prerequisites across multiple targets are deduplicated',
      () async {
        final path = await buildPathTopicList(['T5', 'T6'], fakeRepo);

        expect(path.toSet().length, equals(path.length));
        expect(path.contains('T1'), isTrue);
        expect(path.contains('T2'), isTrue);

        expect(path.indexOf('T1'), lessThan(path.indexOf('T2')));
        expect(path.indexOf('T2'), lessThan(path.indexOf('T3')));
        expect(path.indexOf('T2'), lessThan(path.indexOf('T6')));
        expect(path.indexOf('T3'), lessThan(path.indexOf('T4')));
        expect(path.indexOf('T4'), lessThan(path.indexOf('T5')));
      },
    );

    test(
      'Targeting an advanced node produces a valid topological sequence',
      () async {
        final path = await buildPathTopicList(['T7'], fakeRepo);

        expect(path.toSet(), equals({'T1', 'T2', 'T3', 'T4', 'T6', 'T7'}));
        expect(path.indexOf('T1'), lessThan(path.indexOf('T2')));
        expect(path.indexOf('T2'), lessThan(path.indexOf('T4')));
        expect(path.indexOf('T2'), lessThan(path.indexOf('T6')));
        expect(path.indexOf('T4'), lessThan(path.indexOf('T7')));
        expect(path.indexOf('T6'), lessThan(path.indexOf('T7')));
      },
    );

    test(
      'Valid path ordering passes validatePathOrder without errors',
      () async {
        final validOrder = ['T1', 'T2', 'T3', 'T4', 'T6', 'T7'];
        final error = await validatePathOrder(validOrder, fakeRepo);
        expect(error, isNull);
      },
    );

    test('Invalid reorder placing topic before prerequisite is rejected with reason', () async {
      final invalidOrder = ['T2', 'T1', 'T3'];
      final error = await validatePathOrder(invalidOrder, fakeRepo);
      expect(error, isNotNull);
      expect(error, contains('Topic 1 Logic'));
      expect(error, contains('harus sebelum'));
      expect(error, contains('Topic 2 Vars'));
    });

    test(
      'Removal dependent check identifies remaining topics that depend on it',
      () async {
        final dependents = await checkRemovalDependents('T2', [
          'T1',
          'T2',
          'T3',
          'T4',
        ], fakeRepo);
        expect(dependents, contains('Topic 3 Operators'));

        final noDependents = await checkRemovalDependents('T2', [
          'T1',
          'T2',
        ], fakeRepo);
        expect(noDependents, isEmpty);
      },
    );

    test(
      'Real production dataset: All 5 presets generate strictly valid paths',
      () async {
        final file = File('assets/content/content.json');
        final content = file.readAsStringSync();
        final jsonMap = jsonDecode(content) as Map<String, dynamic>;

        final topicsRaw = jsonMap['topics'] as List<dynamic>;
        final topics = topicsRaw
            .map((e) => Topic.fromJson(e as Map<String, dynamic>))
            .toList();

        final prereqs = <String, List<String>>{};
        for (final t in topics) {
          prereqs[t.id] = t.prerequisiteIds;
        }

        final prodRepo = FakeContentRepository(topics, prereqs);

        for (final preset in pathPresets.values) {
          final built = await buildPathTopicList(preset.targetIds, prodRepo);
          expect(built.isNotEmpty, isTrue);
          expect(
            built.toSet().length,
            equals(built.length),
            reason: 'No duplicates in ${preset.goal}',
          );

          final error = await validatePathOrder(built, prodRepo);
          expect(
            error,
            isNull,
            reason: 'Preset ${preset.goal} must have 0 ordering errors: $error',
          );
        }
      },
    );
  });
}
