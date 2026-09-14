// test/content_and_path_test.dart — Comprehensive validation of content package,
// models, taxonomy, comparison groups, quizzes, DAG acyclicity, and path builder.

import 'dart:convert';
import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:codeatlas/data/models.dart';
import 'package:codeatlas/data/seed_loader.dart';

void main() {
  group('Content Package & JSON Validation', () {
    late Map<String, dynamic> jsonMap;
    late ContentPackage pkg;

    setUpAll(() {
      final file = File('assets/content/content.json');
      expect(
        file.existsSync(),
        isTrue,
        reason: 'content.json asset must exist',
      );
      final content = file.readAsStringSync();
      jsonMap = jsonDecode(content) as Map<String, dynamic>;
      pkg = ContentPackage.fromJson(jsonMap);
    });

    test('Metadata adheres to production specifications', () {
      expect(pkg.formatVersion, equals(1));
      expect(pkg.contentVersion, equals(5));
      expect(pkg.dataset, equals('production'));
      expect(pkg.locale, equals('id-ID'));
    });

    test('Category counts and hierarchy match PRD (76 total)', () {
      expect(pkg.categories.length, equals(76));

      final groups = pkg.categories
          .where((c) => c.kind == CategoryKind.group)
          .toList();
      final domains = pkg.categories
          .where((c) => c.kind == CategoryKind.domain)
          .toList();

      expect(groups.length, equals(24)); // 12 fundamental + 12 ecosystem
      expect(domains.length, equals(52)); // 52 ecosystem domains

      final fundamentalGroups = groups
          .where((g) => g.layer == ContentLayer.fundamentals)
          .toList();
      final ecosystemGroups = groups
          .where((g) => g.layer == ContentLayer.ecosystem)
          .toList();

      expect(fundamentalGroups.length, equals(12));
      expect(ecosystemGroups.length, equals(12));

      final groupIds = groups.map((g) => g.id).toSet();
      for (final d in domains) {
        expect(d.layer, equals(ContentLayer.ecosystem));
        expect(d.parentId, isNotNull);
        expect(
          groupIds.contains(d.parentId),
          isTrue,
          reason: 'Domain parent ${d.parentId} must be a valid group',
        );
      }
    });

    test(
      'Topic counts match PRD (47 fundamental + 52 ecosystem = 99 total)',
      () {
        expect(pkg.topics.length, equals(99));

        final catMap = {for (final c in pkg.categories) c.id: c};
        final topicMap = {for (final t in pkg.topics) t.id: t};

        var fundamentalTopics = 0;
        var ecosystemTopics = 0;

        for (final t in pkg.topics) {
          expect(
            catMap.containsKey(t.categoryId),
            isTrue,
            reason: 'Topic ${t.id} must point to a valid category',
          );
          final cat = catMap[t.categoryId]!;

          if (cat.layer == ContentLayer.fundamentals) {
            fundamentalTopics++;
            expect(cat.kind, equals(CategoryKind.group));
          } else {
            ecosystemTopics++;
            expect(cat.kind, equals(CategoryKind.domain));
          }

          // Validate content quality rules (8 pedagogical dimensions)
          expect(t.title.trim().isNotEmpty, isTrue);
          expect(t.summary.trim().isNotEmpty, isTrue);
          expect(t.explanationSimple.trim().isNotEmpty, isTrue);
          expect(t.problemContext.trim().isNotEmpty, isTrue);
          expect(t.explanationTechnical.trim().isNotEmpty, isTrue);
          expect(t.codeExamples.isNotEmpty, isTrue);
          expect(t.misconceptions.length, greaterThanOrEqualTo(2));
          for (final m in t.misconceptions) {
            expect(m.misconception.trim().isNotEmpty, isTrue);
            expect(m.explanation.trim().isNotEmpty, isTrue);
            expect(m.spotInCode.trim().isNotEmpty, isTrue);
          }
          expect(t.whenToUse.trim().isNotEmpty, isTrue);
          expect(t.whyVibecodingMatters.trim().isNotEmpty, isTrue);
          expect(t.reflectionQuestions.length, greaterThanOrEqualTo(2));
          for (final q in t.reflectionQuestions) {
            expect(q.question.trim().isNotEmpty, isTrue);
            expect(q.answer.trim().isNotEmpty, isTrue);
          }
          expect(t.estimatedMinutes, greaterThan(0));

          // Validate prerequisites and related
          for (final p in t.prerequisiteIds) {
            expect(
              topicMap.containsKey(p),
              isTrue,
              reason: 'Prerequisite $p for topic ${t.id} must exist',
            );
            expect(p, isNot(equals(t.id)));
          }

          expect(
            t.relatedTopicIds.isNotEmpty,
            isTrue,
            reason: 'Topic ${t.id} must have >= 1 related topic',
          );
          for (final r in t.relatedTopicIds) {
            expect(
              topicMap.containsKey(r),
              isTrue,
              reason: 'Related topic $r for topic ${t.id} must exist',
            );
            expect(r, isNot(equals(t.id)));
          }
        }

        expect(fundamentalTopics, equals(47));
        expect(ecosystemTopics, equals(52));
      },
    );

    test('Prerequisite graph is strictly acyclic (DAG check via Kahn)', () {
      final inDegree = <String, int>{for (final t in pkg.topics) t.id: 0};
      final adj = <String, List<String>>{for (final t in pkg.topics) t.id: []};

      for (final t in pkg.topics) {
        for (final p in t.prerequisiteIds) {
          adj[p]!.add(t.id);
          inDegree[t.id] = (inDegree[t.id] ?? 0) + 1;
        }
      }

      final queue = [
        for (final entry in inDegree.entries)
          if (entry.value == 0) entry.key,
      ];

      var count = 0;
      while (queue.isNotEmpty) {
        final curr = queue.removeAt(0);
        count++;
        for (final dep in adj[curr]!) {
          inDegree[dep] = inDegree[dep]! - 1;
          if (inDegree[dep] == 0) {
            queue.add(dep);
          }
        }
      }

      expect(
        count,
        equals(pkg.topics.length),
        reason: 'Cycle detected in prerequisite graph!',
      );
    });

    test(
      'Comparison groups meet minimum 9 requirement across Dart/TS/Python',
      () {
        final compMap = <String, Set<String>>{};
        for (final t in pkg.topics) {
          for (final ex in t.codeExamples) {
            if (ex.comparisonKey != null) {
              compMap
                  .putIfAbsent(ex.comparisonKey!, () => <String>{})
                  .add(ex.language);
            }
          }
        }

        expect(compMap.length, greaterThanOrEqualTo(9));
        for (final entry in compMap.entries) {
          expect(
            entry.value.contains('dart'),
            isTrue,
            reason: 'Comparison group ${entry.key} must contain Dart',
          );
          expect(
            entry.value.contains('typescript'),
            isTrue,
            reason: 'Comparison group ${entry.key} must contain TypeScript',
          );
          expect(
            entry.value.contains('python'),
            isTrue,
            reason: 'Comparison group ${entry.key} must contain Python',
          );
        }
      },
    );

    test('Quizzes meet minimum 30 requirement with proper balance', () {
      expect(pkg.quizzes.length, greaterThanOrEqualTo(30));

      final langQuizzes = pkg.quizzes
          .where((q) => q.type == QuizType.language)
          .toList();
      final conceptQuizzes = pkg.quizzes
          .where((q) => q.type == QuizType.concept)
          .toList();

      expect(langQuizzes.length, greaterThanOrEqualTo(10));
      expect(conceptQuizzes.length, greaterThanOrEqualTo(20));

      final distinctTopics = {for (final q in pkg.quizzes) q.topicId};
      expect(distinctTopics.length, greaterThanOrEqualTo(15));

      final topicIds = {for (final t in pkg.topics) t.id};
      for (final q in pkg.quizzes) {
        expect(topicIds.contains(q.topicId), isTrue);
        expect(q.prompt.trim().isNotEmpty, isTrue);
        expect(q.snippet.trim().isNotEmpty, isTrue);
        expect(q.options.length, equals(4));

        final optionIds = q.options.map((o) => o.id).toSet();
        final optionTexts = q.options.map((o) => o.text).toSet();
        expect(
          optionIds.length,
          equals(4),
          reason: 'Option IDs must be unique',
        );
        expect(
          optionTexts.length,
          equals(4),
          reason: 'Option texts must be unique',
        );
        expect(
          optionIds.contains(q.correctOptionId),
          isTrue,
          reason: 'correctOptionId must point to an option in the list',
        );
        expect(q.explanation.trim().isNotEmpty, isTrue);
      }
    });
  });
}
