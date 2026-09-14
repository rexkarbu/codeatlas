// test/topic_notes_widget_test.dart — Widget tests for TopicScreen:
// status independence, notes editing, dirty tracking, in-flight typing protection,
// save error handling, and unsaved changes confirmation dialog.

import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:codeatlas/data/content_repository.dart';
import 'package:codeatlas/data/learning_repository.dart';
import 'package:codeatlas/data/models.dart';
import 'package:codeatlas/features/topic/topic_screen.dart';
import 'package:codeatlas/state/app_state.dart';

class FakeTopicContentRepository implements ContentRepository {
  final Topic topic;

  FakeTopicContentRepository(this.topic);

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<Topic?> getTopicById(String id) async => topic;

  @override
  Future<List<String>> getDependentTopicIds(String topicId) async => [];

  @override
  Future<List<Topic>> getAllActiveTopics() async => [topic];
}

class FakeTopicLearningRepository implements LearningRepository {
  Progress? currentProgress;
  Completer<void>? saveDelayCompleter;
  bool shouldFailSave = false;

  FakeTopicLearningRepository(this.currentProgress);

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<Progress?> getProgress(String topicId) async => currentProgress;

  @override
  Future<void> recordReview(String topicId) async {}

  @override
  Future<void> updateStatus(String topicId, LearningStatus status) async {
    currentProgress = Progress(
      topicId: topicId,
      status: status,
      notes: currentProgress?.notes ?? '',
      updatedAt: DateTime.now(),
    );
  }

  @override
  Future<void> updateNotes(String topicId, String notes) async {
    if (saveDelayCompleter != null) {
      await saveDelayCompleter!.future;
    }
    if (shouldFailSave) {
      throw Exception('Simulasi gagal tulis SQLite');
    }
    currentProgress = Progress(
      topicId: topicId,
      status: currentProgress?.status ?? LearningStatus.notStarted,
      notes: notes,
      updatedAt: DateTime.now(),
    );
  }

  @override
  Future<int> countByStatus(
    LearningStatus status, {
    Set<String>? topicIds,
  }) async => 0;

  @override
  Future<String?> getLastReviewedTopicId() async => null;
}

void main() {
  group('TopicScreen Status & Notes Widget Tests', () {
    late Topic sampleTopic;
    late FakeTopicContentRepository fakeContentRepo;
    late FakeTopicLearningRepository fakeLearningRepo;
    late AppState appState;

    setUp(() {
      sampleTopic = const Topic(
        id: 'f-programming-logic',
        categoryId: 'f-logic-syntax',
        title: 'Programming Logic',
        level: Difficulty.beginner,
        summary: 'Urutan instruksi logis.',
        explanationSimple: 'Analogi resep masakan.',
        explanationTechnical: 'Instruksi sekuensial CPU.',
        whyVibecodingMatters: 'Mencegah halusinasi AI.',
        estimatedMinutes: 8,
        sortOrder: 1,
      );

      fakeContentRepo = FakeTopicContentRepository(sampleTopic);
      fakeLearningRepo = FakeTopicLearningRepository(
        Progress(
          topicId: 'f-programming-logic',
          status: LearningStatus.notStarted,
          notes: 'Catatan awal',
          updatedAt: DateTime.now(),
        ),
      );

      appState = AppState(
        contentRepo: fakeContentRepo,
        learningRepo: fakeLearningRepo,
      );
    });

    testWidgets('Renders topic details, status selector, and initial notes', (
      tester,
    ) async {
      await tester.pumpWidget(
        MaterialApp(
          home: TopicScreen(
            topicId: 'f-programming-logic',
            contentRepo: fakeContentRepo,
            learningRepo: fakeLearningRepo,
            appState: appState,
            onOpenTopic: (_) {},
          ),
        ),
      );
      await tester.pumpAndSettle();

      expect(find.text('Programming Logic'), findsOneWidget);
      expect(find.text('Urutan instruksi logis.'), findsOneWidget);
      expect(find.text('Catatan awal'), findsOneWidget);
      expect(find.text('Belum disimpan'), findsNothing);
    });

    testWidgets('Updating status does not overwrite notes', (tester) async {
      await tester.pumpWidget(
        MaterialApp(
          home: TopicScreen(
            topicId: 'f-programming-logic',
            contentRepo: fakeContentRepo,
            learningRepo: fakeLearningRepo,
            appState: appState,
            onOpenTopic: (_) {},
          ),
        ),
      );
      await tester.pumpAndSettle();

      // Change status to 'Sedang'
      await tester.tap(find.text('Sedang'));
      await tester.pumpAndSettle();

      expect(
        fakeLearningRepo.currentProgress?.status,
        equals(LearningStatus.inProgress),
      );
      expect(fakeLearningRepo.currentProgress?.notes, equals('Catatan awal'));

      // Change status to 'Paham'
      await tester.tap(find.text('Paham'));
      await tester.pumpAndSettle();

      expect(
        fakeLearningRepo.currentProgress?.status,
        equals(LearningStatus.understood),
      );
      expect(fakeLearningRepo.currentProgress?.notes, equals('Catatan awal'));
    });

    testWidgets(
      'Typing in notes shows "Belum disimpan" and saving clears it without changing status',
      (tester) async {
        await tester.pumpWidget(
          MaterialApp(
            home: TopicScreen(
              topicId: 'f-programming-logic',
              contentRepo: fakeContentRepo,
              learningRepo: fakeLearningRepo,
              appState: appState,
              onOpenTopic: (_) {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        // Drag up to reveal notes section
        await tester.drag(find.byType(TopicScreen), const Offset(0, -500));
        await tester.pumpAndSettle();

        // Enter new text into notes
        await tester.enterText(
          find.byType(TextField),
          'Catatan baru telah diperbarui.',
        );
        await tester.pump();

        expect(find.text('Belum disimpan'), findsOneWidget);

        // Press 'Simpan Catatan'
        await tester.tap(find.widgetWithText(FilledButton, 'Simpan Catatan'));
        await tester.pumpAndSettle();

        // "Belum disimpan" indicator disappears
        expect(find.text('Belum disimpan'), findsNothing);
        expect(find.text('Tersimpan'), findsOneWidget);

        // Let the 2-second success timer expire cleanly
        await tester.pump(const Duration(seconds: 2));

        // Verify in repository: notes updated, status untouched
        expect(
          fakeLearningRepo.currentProgress?.notes,
          equals('Catatan baru telah diperbarui.'),
        );
        expect(
          fakeLearningRepo.currentProgress?.status,
          equals(LearningStatus.notStarted),
        );
      },
    );

    testWidgets(
      'In-flight typing protection: typing during delayed save keeps dirty = true',
      (tester) async {
        fakeLearningRepo.saveDelayCompleter = Completer<void>();

        await tester.pumpWidget(
          MaterialApp(
            home: TopicScreen(
              topicId: 'f-programming-logic',
              contentRepo: fakeContentRepo,
              learningRepo: fakeLearningRepo,
              appState: appState,
              onOpenTopic: (_) {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        // 1. Drag up to reveal notes section and enter first draft
        await tester.drag(find.byType(TopicScreen), const Offset(0, -500));
        await tester.pumpAndSettle();
        await tester.enterText(find.byType(TextField), 'Draft 1');
        await tester.pump();
        expect(find.text('Belum disimpan'), findsOneWidget);

        // 2. Click Save (it is now in flight)
        await tester.tap(find.widgetWithText(FilledButton, 'Simpan Catatan'));
        await tester.pump(); // Starts saving, spinner visible
        expect(find.text('Menyimpan...'), findsOneWidget);

        // 3. User types additional text while save is in flight!
        await tester.enterText(
          find.byType(TextField),
          'Draft 1 + tambahan ketikan',
        );
        await tester.pump();

        // 4. Complete the delayed save of Draft 1
        fakeLearningRepo.saveDelayCompleter!.complete();
        await tester.pumpAndSettle();

        // 5. Because the user typed additional text, "Belum disimpan" MUST STILL BE VISIBLE!
        expect(find.text('Belum disimpan'), findsOneWidget);

        // Let the 2-second success timer expire cleanly
        await tester.pump(const Duration(seconds: 2));
      },
    );

    testWidgets(
      'Save failure displays error banner and retains unsaved state',
      (tester) async {
        fakeLearningRepo.shouldFailSave = true;

        await tester.pumpWidget(
          MaterialApp(
            home: TopicScreen(
              topicId: 'f-programming-logic',
              contentRepo: fakeContentRepo,
              learningRepo: fakeLearningRepo,
              appState: appState,
              onOpenTopic: (_) {},
            ),
          ),
        );
        await tester.pumpAndSettle();

        await tester.drag(find.byType(TopicScreen), const Offset(0, -500));
        await tester.pumpAndSettle();
        await tester.enterText(
          find.byType(TextField),
          'Catatan yang gagal disimpan.',
        );
        await tester.pump();

        // Try to save
        await tester.tap(find.widgetWithText(FilledButton, 'Simpan Catatan'));
        await tester.pumpAndSettle();

        // Error message shown
        expect(find.textContaining('Gagal menyimpan'), findsOneWidget);
        expect(find.text('Coba lagi'), findsOneWidget);
        expect(find.text('Belum disimpan'), findsOneWidget);
      },
    );
  });
}
