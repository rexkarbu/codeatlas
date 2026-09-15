// lib/data/reading_time.dart — Consistent reading time calculation
// shared between HomeScreen and TopicScreen.

import 'models.dart';

class ReadingTimeEstimator {
  /// Consistently calculates estimated reading minutes from actual topic content.
  static int estimateMinutes(Topic topic) {
    final buffer = StringBuffer();
    buffer.write(topic.summary);
    buffer.write(' ');
    buffer.write(topic.explanationSimple);
    buffer.write(' ');
    buffer.write(topic.problemContext);
    buffer.write(' ');
    buffer.write(topic.explanationTechnical);
    buffer.write(' ');
    buffer.write(topic.whyVibecodingMatters);
    buffer.write(' ');
    buffer.write(topic.whenToUse);
    for (final ex in topic.codeExamples) {
      buffer.write(' ');
      buffer.write(ex.explanation);
    }
    for (final m in topic.misconceptions) {
      buffer.write(' ');
      buffer.write(m.misconception);
      buffer.write(' ');
      buffer.write(m.explanation);
    }
    for (final r in topic.reflectionQuestions) {
      buffer.write(' ');
      buffer.write(r.question);
      buffer.write(' ');
      buffer.write(r.answer);
    }
    final words = buffer
        .toString()
        .trim()
        .split(RegExp(r'\s+'))
        .where((w) => w.isNotEmpty)
        .length;

    // Average reading speed for technical learning: ~150 words per minute.
    final calculated = (words / 150).ceil();
    return calculated > 0 ? calculated : topic.estimatedMinutes;
  }

  /// Formats the estimated reading time with standard Indonesian label.
  static String format(Topic topic) {
    final mins = estimateMinutes(topic);
    return 'Perkiraan $mins mnt baca';
  }
}
