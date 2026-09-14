// lib/features/learning_paths/path_builder.dart — Preset targets and
// transitive prerequisite closure with topological sort.
//
// Pure domain logic, no Flutter/UI dependencies.

import '../../data/content_repository.dart';
import '../../data/models.dart';

/// Preset learning path definitions.
const Map<String, PathPreset> pathPresets = {
  'general': PathPreset(
    goal: 'general',
    name: 'Memahami dasar dari nol',
    description:
        'Mulai dari logika dasar sampai bisa testing dan version control.',
    targetIds: [
      'f-programming-logic',
      'f-variables-data-types',
      'f-operators',
      'f-conditionals',
      'f-loops',
      'f-functions',
      'f-debugging',
      'f-testing',
      'f-git',
    ],
  ),
  'flutter': PathPreset(
    goal: 'flutter',
    name: 'Membaca kode Flutter',
    description: 'Pahami konsep yang sering muncul di kode Flutter/Dart.',
    targetIds: [
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
    ],
  ),
  'web': PathPreset(
    goal: 'web',
    name: 'Memahami web',
    description: 'Pelajari dasar-dasar web development.',
    targetIds: [
      'f-http-web',
      'f-apis',
      'f-serialization',
      'f-async',
      'f-security',
      'e-frontend-overview',
      'e-backend-overview',
    ],
  ),
  'backend': PathPreset(
    goal: 'backend',
    name: 'Memahami backend',
    description: 'Pahami bagaimana server dan API bekerja.',
    targetIds: [
      'f-apis',
      'f-databases',
      'f-sql',
      'f-data-modeling',
      'f-auth',
      'f-security',
      'f-testing',
      'f-deployment',
      'e-backend-overview',
    ],
  ),
  'data': PathPreset(
    goal: 'data',
    name: 'Memahami data',
    description: 'Dari struktur data sampai data engineering.',
    targetIds: [
      'f-data-structures',
      'f-algorithms',
      'f-databases',
      'f-sql',
      'f-data-modeling',
      'e-data-engineering-overview',
      'e-data-science-overview',
    ],
  ),
};

class PathPreset {
  final String goal;
  final String name;
  final String description;
  final List<String> targetIds;

  const PathPreset({
    required this.goal,
    required this.name,
    required this.description,
    required this.targetIds,
  });
}

/// Build a complete ordered list of topic IDs from target IDs,
/// including all transitive prerequisites, with topological sort.
Future<List<String>> buildPathTopicList(
  List<String> targetIds,
  ContentRepository contentRepo,
) async {
  // Collect all transitive prerequisites
  final allIds = <String>{...targetIds};
  for (final targetId in targetIds) {
    final prereqs = await contentRepo.getTransitivePrerequisites(targetId);
    allIds.addAll(prereqs);
  }

  // Build adjacency for topological sort
  final prereqGraph = await contentRepo.getPrerequisiteGraph();
  final allTopics = await contentRepo.getAllActiveTopics();
  final topicMap = {for (final t in allTopics) t.id: t};

  // Only consider IDs that exist
  allIds.removeWhere((id) => !topicMap.containsKey(id));

  // Kahn's algorithm with (sort_order, id) as tiebreaker
  final inDegree = <String, int>{};
  final adj = <String, List<String>>{}; // prereq -> [dependent]

  for (final id in allIds) {
    inDegree[id] = 0;
    adj[id] = [];
  }

  for (final id in allIds) {
    for (final prereq in prereqGraph[id] ?? []) {
      if (allIds.contains(prereq)) {
        adj[prereq]!.add(id);
        inDegree[id] = (inDegree[id] ?? 0) + 1;
      }
    }
  }

  // Priority queue using sorted list
  final ready = allIds.where((id) => inDegree[id] == 0).toList()
    ..sort((a, b) => _compareTopics(topicMap[a]!, topicMap[b]!));

  final result = <String>[];
  while (ready.isNotEmpty) {
    final current = ready.removeAt(0);
    result.add(current);

    for (final dep in adj[current] ?? []) {
      inDegree[dep] = (inDegree[dep] ?? 1) - 1;
      if (inDegree[dep] == 0) {
        ready.add(dep);
        ready.sort((a, b) => _compareTopics(topicMap[a]!, topicMap[b]!));
      }
    }
  }

  return result;
}

int _compareTopics(Topic a, Topic b) {
  final sc = a.sortOrder.compareTo(b.sortOrder);
  return sc != 0 ? sc : a.id.compareTo(b.id);
}

/// Validate that a reordered list doesn't violate prerequisites.
/// Returns null if valid, or an error message.
Future<String?> validatePathOrder(
  List<String> topicIds,
  ContentRepository contentRepo,
) async {
  final prereqGraph = await contentRepo.getPrerequisiteGraph();
  final positionOf = <String, int>{};
  for (var i = 0; i < topicIds.length; i++) {
    positionOf[topicIds[i]] = i;
  }

  for (final id in topicIds) {
    for (final prereq in prereqGraph[id] ?? []) {
      if (positionOf.containsKey(prereq)) {
        if (positionOf[prereq]! >= positionOf[id]!) {
          final allTopics = await contentRepo.getAllActiveTopics();
          final prereqTitle =
              allTopics.where((t) => t.id == prereq).firstOrNull?.title ??
              prereq;
          final topicTitle =
              allTopics.where((t) => t.id == id).firstOrNull?.title ?? id;
          return '"$prereqTitle" harus sebelum "$topicTitle"';
        }
      }
    }
  }
  return null;
}

/// Check if removing a topic would break prerequisites for other topics in the path.
/// Returns list of topic titles that depend on it.
Future<List<String>> checkRemovalDependents(
  String topicId,
  List<String> currentTopicIds,
  ContentRepository contentRepo,
) async {
  final dependentIds = await contentRepo.getDependentTopicIds(topicId);
  final remainingIds = currentTopicIds.where((id) => id != topicId).toSet();
  final blocked = dependentIds.where((d) => remainingIds.contains(d)).toList();

  if (blocked.isEmpty) return [];

  final allTopics = await contentRepo.getAllActiveTopics();
  return blocked.map((id) {
    return allTopics.where((t) => t.id == id).firstOrNull?.title ?? id;
  }).toList();
}
