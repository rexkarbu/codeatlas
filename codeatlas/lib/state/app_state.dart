// lib/state/app_state.dart — Shared application state via ChangeNotifier.
//
// Injected with concrete repositories; no DI container needed.
// Caches progress counts and last-read topic for the home screen.

import 'package:flutter/foundation.dart';

import '../data/content_repository.dart';
import '../data/learning_repository.dart';
import '../data/models.dart';

class AppState extends ChangeNotifier {
  final ContentRepository contentRepo;
  final LearningRepository learningRepo;

  AppState({required this.contentRepo, required this.learningRepo});

  // Cached values for home screen
  String? _lastReadTopicId;
  String? _contentUpdateNotice;
  int _totalActiveTopics = 0;
  int _fundamentalTopicCount = 0;
  int _ecosystemTopicCount = 0;
  int _understoodCount = 0;
  int _inProgressCount = 0;
  int _fundamentalUnderstood = 0;
  int _ecosystemUnderstood = 0;
  int _fundamentalInProgress = 0;
  int _ecosystemInProgress = 0;

  String? get lastReadTopicId => _lastReadTopicId;
  String? get contentUpdateNotice => _contentUpdateNotice;
  int get totalActiveTopics => _totalActiveTopics;
  int get fundamentalTopicCount => _fundamentalTopicCount;
  int get ecosystemTopicCount => _ecosystemTopicCount;
  int get understoodCount => _understoodCount;
  int get inProgressCount => _inProgressCount;
  int get fundamentalUnderstood => _fundamentalUnderstood;
  int get ecosystemUnderstood => _ecosystemUnderstood;
  int get fundamentalInProgress => _fundamentalInProgress;
  int get ecosystemInProgress => _ecosystemInProgress;

  double get overallProgress => _totalActiveTopics > 0
      ? (_understoodCount / _totalActiveTopics * 100)
      : 0;

  double get fundamentalProgress => _fundamentalTopicCount > 0
      ? (_fundamentalUnderstood / _fundamentalTopicCount * 100)
      : 0;

  double get ecosystemProgress => _ecosystemTopicCount > 0
      ? (_ecosystemUnderstood / _ecosystemTopicCount * 100)
      : 0;

  /// Refresh all cached counts. Call after seed and after status changes.
  Future<void> refreshCounts() async {
    _lastReadTopicId = await learningRepo.getLastReviewedTopicId();
    _totalActiveTopics = await contentRepo.getActiveTopicCount();
    _fundamentalTopicCount = await contentRepo.getActiveTopicCountByLayer(
      ContentLayer.fundamentals,
    );
    _ecosystemTopicCount = await contentRepo.getActiveTopicCountByLayer(
      ContentLayer.ecosystem,
    );

    // Get topic IDs by layer for status counts
    final fundamentalTopics = await contentRepo.getTopicsByLayer(
      ContentLayer.fundamentals,
    );
    final ecosystemTopics = await contentRepo.getTopicsByLayer(
      ContentLayer.ecosystem,
    );
    final fIds = fundamentalTopics.map((t) => t.id).toSet();
    final eIds = ecosystemTopics.map((t) => t.id).toSet();

    _fundamentalUnderstood = await learningRepo.countByStatus(
      LearningStatus.understood,
      topicIds: fIds,
    );
    _ecosystemUnderstood = await learningRepo.countByStatus(
      LearningStatus.understood,
      topicIds: eIds,
    );
    _fundamentalInProgress = await learningRepo.countByStatus(
      LearningStatus.inProgress,
      topicIds: fIds,
    );
    _ecosystemInProgress = await learningRepo.countByStatus(
      LearningStatus.inProgress,
      topicIds: eIds,
    );
    _understoodCount = _fundamentalUnderstood + _ecosystemUnderstood;
    _inProgressCount = _fundamentalInProgress + _ecosystemInProgress;

    notifyListeners();
  }

  /// Record that user opened a topic.
  Future<void> recordTopicRead(String topicId) async {
    await learningRepo.recordReview(topicId);
    _lastReadTopicId = topicId;
    notifyListeners();
  }

  /// Update topic status and refresh counts.
  Future<void> updateTopicStatus(String topicId, LearningStatus status) async {
    await learningRepo.updateStatus(topicId, status);
    await refreshCounts();
  }

  /// Set a notice for failed content updates (without locking user out).
  void setContentUpdateNotice(String? notice) {
    _contentUpdateNotice = notice;
    notifyListeners();
  }

  /// Dismiss content update notice.
  void dismissContentUpdateNotice() {
    _contentUpdateNotice = null;
    notifyListeners();
  }
}
