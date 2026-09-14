// lib/data/models.dart — Immutable model classes for CodeAtlas.
// Manual JSON parsing with validation. No code generation needed.

// ─── Enums ───

enum ContentLayer {
  fundamentals,
  ecosystem;

  static ContentLayer fromString(String value) {
    return ContentLayer.values.firstWhere(
      (e) => e.name == value,
      orElse: () => throw FormatException('Invalid ContentLayer: $value'),
    );
  }
}

enum CategoryKind {
  group,
  domain;

  static CategoryKind fromString(String value) {
    return CategoryKind.values.firstWhere(
      (e) => e.name == value,
      orElse: () => throw FormatException('Invalid CategoryKind: $value'),
    );
  }
}

enum Difficulty {
  beginner,
  intermediate,
  advanced;

  String get label {
    switch (this) {
      case Difficulty.beginner:
        return 'Pemula';
      case Difficulty.intermediate:
        return 'Menengah';
      case Difficulty.advanced:
        return 'Lanjutan';
    }
  }

  static Difficulty fromString(String value) {
    return Difficulty.values.firstWhere(
      (e) => e.name == value,
      orElse: () => throw FormatException('Invalid Difficulty: $value'),
    );
  }
}

enum LearningStatus {
  notStarted,
  inProgress,
  understood;

  String get dbValue {
    switch (this) {
      case LearningStatus.notStarted:
        return 'not_started';
      case LearningStatus.inProgress:
        return 'in_progress';
      case LearningStatus.understood:
        return 'understood';
    }
  }

  String get label {
    switch (this) {
      case LearningStatus.notStarted:
        return 'Belum';
      case LearningStatus.inProgress:
        return 'Sedang';
      case LearningStatus.understood:
        return 'Paham';
    }
  }

  static LearningStatus fromDbValue(String value) {
    switch (value) {
      case 'not_started':
        return LearningStatus.notStarted;
      case 'in_progress':
        return LearningStatus.inProgress;
      case 'understood':
        return LearningStatus.understood;
      default:
        throw FormatException('Invalid LearningStatus: $value');
    }
  }
}

enum QuizType {
  language,
  concept;

  static QuizType fromString(String value) {
    return QuizType.values.firstWhere(
      (e) => e.name == value,
      orElse: () => throw FormatException('Invalid QuizType: $value'),
    );
  }
}

// ─── Value Objects ───

class CodeExample {
  final String language;
  final String? comparisonKey;
  final String label;
  final String code;
  final String explanation;
  final String? expectedOutput;

  const CodeExample({
    required this.language,
    this.comparisonKey,
    required this.label,
    required this.code,
    required this.explanation,
    this.expectedOutput,
  });

  factory CodeExample.fromJson(Map<String, dynamic> json) {
    final language = json['language'] as String? ?? '';
    final code = json['code'] as String? ?? '';
    final label = json['label'] as String? ?? '';
    final explanation = json['explanation'] as String? ?? '';
    if (language.isEmpty || code.isEmpty || label.isEmpty) {
      throw FormatException(
        'CodeExample missing required fields: language=$language, label=$label',
      );
    }
    return CodeExample(
      language: language,
      comparisonKey: json['comparison_key'] as String?,
      label: label,
      code: code,
      explanation: explanation,
      expectedOutput: json['expected_output'] as String?,
    );
  }

  Map<String, dynamic> toJson() => {
    'language': language,
    'comparison_key': comparisonKey,
    'label': label,
    'code': code,
    'explanation': explanation,
    'expected_output': expectedOutput,
  };
}

class QuizOption {
  final String id;
  final String text;

  const QuizOption({required this.id, required this.text});

  factory QuizOption.fromJson(Map<String, dynamic> json) {
    final id = json['id'] as String? ?? '';
    final text = json['text'] as String? ?? '';
    if (id.isEmpty || text.isEmpty) {
      throw FormatException('QuizOption missing id or text');
    }
    return QuizOption(id: id, text: text);
  }

  Map<String, dynamic> toJson() => {'id': id, 'text': text};
}

class TopicMisconception {
  final String misconception;
  final String explanation;
  final String spotInCode;

  const TopicMisconception({
    required this.misconception,
    required this.explanation,
    this.spotInCode = '',
  });

  factory TopicMisconception.fromJson(Map<String, dynamic> json) {
    return TopicMisconception(
      misconception: json['misconception'] as String? ?? '',
      explanation:
          json['explanation'] as String? ?? json['reality'] as String? ?? '',
      spotInCode:
          json['spot_in_code'] as String? ??
          json['spotInCode'] as String? ??
          '',
    );
  }

  Map<String, dynamic> toJson() => {
    'misconception': misconception,
    'explanation': explanation,
    'spot_in_code': spotInCode,
  };
}

class TopicReflection {
  final String question;
  final String answer;

  const TopicReflection({required this.question, required this.answer});

  factory TopicReflection.fromJson(Map<String, dynamic> json) {
    return TopicReflection(
      question: json['question'] as String? ?? '',
      answer: json['answer'] as String? ?? json['answer_key'] as String? ?? '',
    );
  }

  Map<String, dynamic> toJson() => {'question': question, 'answer': answer};
}

// ─── Models ───

class Category {
  final String id;
  final String? parentId;
  final ContentLayer layer;
  final CategoryKind kind;
  final String title;
  final String description;
  final int sortOrder;

  const Category({
    required this.id,
    this.parentId,
    required this.layer,
    required this.kind,
    required this.title,
    required this.description,
    required this.sortOrder,
  });

  factory Category.fromJson(Map<String, dynamic> json) {
    final id = json['id'] as String? ?? '';
    if (id.isEmpty) throw FormatException('Category id is empty');
    final title = (json['title'] as String? ?? '').trim();
    final description = (json['description'] as String? ?? '').trim();
    if (title.isEmpty) {
      throw FormatException('Category $id: title is empty');
    }
    if (description.isEmpty) {
      throw FormatException('Category $id: description is empty');
    }
    return Category(
      id: id,
      parentId: json['parent_id'] as String?,
      layer: ContentLayer.fromString(json['layer'] as String),
      kind: CategoryKind.fromString(json['kind'] as String),
      title: title,
      description: description,
      sortOrder: json['sort_order'] as int? ?? 0,
    );
  }

  Map<String, dynamic> toDbMap() => {
    'id': id,
    'parent_id': parentId,
    'layer': layer.name,
    'kind': kind.name,
    'title': title,
    'description': description,
    'sort_order': sortOrder,
  };

  factory Category.fromDb(Map<String, dynamic> row) {
    return Category(
      id: row['id'] as String,
      parentId: row['parent_id'] as String?,
      layer: ContentLayer.fromString(row['layer'] as String),
      kind: CategoryKind.fromString(row['kind'] as String),
      title: row['title'] as String,
      description: row['description'] as String,
      sortOrder: row['sort_order'] as int,
    );
  }
}

class Topic {
  final String id;
  final String categoryId;
  final String title;
  final Difficulty level;
  final String summary;
  final String explanationSimple;
  final String explanationTechnical;
  final List<CodeExample> codeExamples;
  final String whyVibecodingMatters;
  final String problemContext;
  final List<TopicMisconception> misconceptions;
  final String whenToUse;
  final List<TopicReflection> reflectionQuestions;
  final List<String> keywords;
  final int estimatedMinutes;
  final int sortOrder;
  final bool isActive;

  // These are populated separately from relation tables
  final List<String> prerequisiteIds;
  final List<String> relatedTopicIds;

  const Topic({
    required this.id,
    required this.categoryId,
    required this.title,
    required this.level,
    required this.summary,
    required this.explanationSimple,
    required this.explanationTechnical,
    this.codeExamples = const [],
    required this.whyVibecodingMatters,
    this.problemContext = '',
    this.misconceptions = const [],
    this.whenToUse = '',
    this.reflectionQuestions = const [],
    this.keywords = const [],
    required this.estimatedMinutes,
    required this.sortOrder,
    this.isActive = true,
    this.prerequisiteIds = const [],
    this.relatedTopicIds = const [],
  });

  factory Topic.fromJson(Map<String, dynamic> json) {
    final id = json['id'] as String? ?? '';
    if (id.isEmpty) throw FormatException('Topic id is empty');

    final title = (json['title'] as String? ?? '').trim();
    final summary = (json['summary'] as String? ?? '').trim();
    final explanationSimple = (json['explanation_simple'] as String? ?? '')
        .trim();
    final explanationTechnical =
        (json['explanation_technical'] as String? ?? '').trim();
    final whyVibecoding = (json['why_vibecoding_matters'] as String? ?? '')
        .trim();

    if (title.isEmpty) throw FormatException('Topic $id: title is empty');
    if (summary.isEmpty) throw FormatException('Topic $id: summary is empty');
    if (explanationSimple.isEmpty) {
      throw FormatException('Topic $id: explanation_simple is empty');
    }
    if (explanationTechnical.isEmpty) {
      throw FormatException('Topic $id: explanation_technical is empty');
    }
    if (whyVibecoding.isEmpty) {
      throw FormatException('Topic $id: why_vibecoding_matters is empty');
    }

    final codeExamplesRaw = json['code_examples'] as List<dynamic>? ?? [];
    if (codeExamplesRaw.isEmpty) {
      throw FormatException('Topic $id: code_examples is empty');
    }
    final codeExamples = codeExamplesRaw
        .map((e) => CodeExample.fromJson(e as Map<String, dynamic>))
        .toList();

    final estimatedMinutes = json['estimated_minutes'] as int? ?? 0;
    if (estimatedMinutes <= 0) {
      throw FormatException('Topic $id: estimated_minutes must be > 0');
    }

    final problemContext = (json['problem_context'] as String? ?? '').trim();
    final misconceptionsRaw = json['misconceptions'] as List<dynamic>? ?? [];
    final misconceptions = misconceptionsRaw
        .map((m) => TopicMisconception.fromJson(m as Map<String, dynamic>))
        .toList();
    final whenToUse = (json['when_to_use'] as String? ?? '').trim();
    final reflectionsRaw = json['reflection_questions'] as List<dynamic>? ?? [];
    final reflections = reflectionsRaw
        .map((r) => TopicReflection.fromJson(r as Map<String, dynamic>))
        .toList();

    return Topic(
      id: id,
      categoryId: json['category_id'] as String? ?? '',
      title: title,
      level: Difficulty.fromString(json['level'] as String),
      summary: summary,
      explanationSimple: explanationSimple,
      explanationTechnical: explanationTechnical,
      codeExamples: codeExamples,
      whyVibecodingMatters: whyVibecoding,
      problemContext: problemContext,
      misconceptions: misconceptions,
      whenToUse: whenToUse,
      reflectionQuestions: reflections,
      keywords: (json['keywords'] as List<dynamic>? ?? [])
          .map((e) => e as String)
          .toList(),
      estimatedMinutes: estimatedMinutes,
      sortOrder: json['sort_order'] as int? ?? 0,
      isActive: json['is_active'] as bool? ?? true,
      prerequisiteIds: (json['prerequisite_ids'] as List<dynamic>? ?? [])
          .map((e) => e as String)
          .toList(),
      relatedTopicIds: (json['related_topic_ids'] as List<dynamic>? ?? [])
          .map((e) => e as String)
          .toList(),
    );
  }

  Map<String, dynamic> toDbMap() {
    return {
      'id': id,
      'category_id': categoryId,
      'title': title,
      'level': level.name,
      'summary': summary,
      'explanation_simple': explanationSimple,
      'explanation_technical': explanationTechnical,
      'code_examples_json': _encodeJson(
        codeExamples.map((e) => e.toJson()).toList(),
      ),
      'why_vibecoding_matters': whyVibecodingMatters,
      'problem_context': problemContext,
      'misconceptions_json': _encodeJson(
        misconceptions.map((m) => m.toJson()).toList(),
      ),
      'when_to_use': whenToUse,
      'reflection_questions_json': _encodeJson(
        reflectionQuestions.map((r) => r.toJson()).toList(),
      ),
      'keywords_json': _encodeJson(keywords),
      'estimated_minutes': estimatedMinutes,
      'sort_order': sortOrder,
      'is_active': isActive ? 1 : 0,
    };
  }

  Topic copyWith({
    String? problemContext,
    List<TopicMisconception>? misconceptions,
    String? whenToUse,
    List<TopicReflection>? reflectionQuestions,
    List<String>? prerequisiteIds,
    List<String>? relatedTopicIds,
  }) {
    return Topic(
      id: id,
      categoryId: categoryId,
      title: title,
      level: level,
      summary: summary,
      explanationSimple: explanationSimple,
      explanationTechnical: explanationTechnical,
      codeExamples: codeExamples,
      whyVibecodingMatters: whyVibecodingMatters,
      problemContext: problemContext ?? this.problemContext,
      misconceptions: misconceptions ?? this.misconceptions,
      whenToUse: whenToUse ?? this.whenToUse,
      reflectionQuestions: reflectionQuestions ?? this.reflectionQuestions,
      keywords: keywords,
      estimatedMinutes: estimatedMinutes,
      sortOrder: sortOrder,
      isActive: isActive,
      prerequisiteIds: prerequisiteIds ?? this.prerequisiteIds,
      relatedTopicIds: relatedTopicIds ?? this.relatedTopicIds,
    );
  }

  factory Topic.fromDb(
    Map<String, dynamic> row, {
    List<String> prerequisiteIds = const [],
    List<String> relatedTopicIds = const [],
  }) {
    final codeExamplesRaw =
        _decodeJson(row['code_examples_json'] as String) as List<dynamic>;
    final keywordsRaw =
        _decodeJson(row['keywords_json'] as String) as List<dynamic>;
    final misconceptionsRaw = row['misconceptions_json'] != null
        ? _decodeJson(row['misconceptions_json'] as String) as List<dynamic>
        : const [];
    final reflectionsRaw = row['reflection_questions_json'] != null
        ? _decodeJson(row['reflection_questions_json'] as String)
              as List<dynamic>
        : const [];

    return Topic(
      id: row['id'] as String,
      categoryId: row['category_id'] as String,
      title: row['title'] as String,
      level: Difficulty.fromString(row['level'] as String),
      summary: row['summary'] as String,
      explanationSimple: row['explanation_simple'] as String,
      explanationTechnical: row['explanation_technical'] as String,
      codeExamples: codeExamplesRaw
          .map((e) => CodeExample.fromJson(e as Map<String, dynamic>))
          .toList(),
      whyVibecodingMatters: row['why_vibecoding_matters'] as String,
      problemContext: row['problem_context'] as String? ?? '',
      misconceptions: misconceptionsRaw
          .map((m) => TopicMisconception.fromJson(m as Map<String, dynamic>))
          .toList(),
      whenToUse: row['when_to_use'] as String? ?? '',
      reflectionQuestions: reflectionsRaw
          .map((r) => TopicReflection.fromJson(r as Map<String, dynamic>))
          .toList(),
      keywords: keywordsRaw.map((e) => e as String).toList(),
      estimatedMinutes: row['estimated_minutes'] as int,
      sortOrder: row['sort_order'] as int,
      isActive: (row['is_active'] as int) == 1,
      prerequisiteIds: prerequisiteIds,
      relatedTopicIds: relatedTopicIds,
    );
  }
}

class Progress {
  final String topicId;
  final LearningStatus status;
  final String notes;
  final DateTime? lastReviewedAt;
  final DateTime updatedAt;

  const Progress({
    required this.topicId,
    required this.status,
    this.notes = '',
    this.lastReviewedAt,
    required this.updatedAt,
  });

  Map<String, dynamic> toDbMap() => {
    'topic_id': topicId,
    'status': status.dbValue,
    'notes': notes,
    'last_reviewed_at': lastReviewedAt?.millisecondsSinceEpoch,
    'updated_at': updatedAt.millisecondsSinceEpoch,
  };

  factory Progress.fromDb(Map<String, dynamic> row) {
    final lastReviewed = row['last_reviewed_at'] as int?;
    return Progress(
      topicId: row['topic_id'] as String,
      status: LearningStatus.fromDbValue(row['status'] as String),
      notes: row['notes'] as String? ?? '',
      lastReviewedAt: lastReviewed != null
          ? DateTime.fromMillisecondsSinceEpoch(lastReviewed, isUtc: true)
          : null,
      updatedAt: DateTime.fromMillisecondsSinceEpoch(
        row['updated_at'] as int,
        isUtc: true,
      ),
    );
  }
}

class Quiz {
  final String id;
  final String topicId;
  final QuizType type;
  final Difficulty level;
  final String prompt;
  final String snippet;
  final String snippetLanguage;
  final List<QuizOption> options;
  final String correctOptionId;
  final String explanation;
  final bool isActive;

  const Quiz({
    required this.id,
    required this.topicId,
    required this.type,
    required this.level,
    required this.prompt,
    required this.snippet,
    required this.snippetLanguage,
    required this.options,
    required this.correctOptionId,
    required this.explanation,
    required this.isActive,
  });

  factory Quiz.fromJson(Map<String, dynamic> json) {
    final id = json['id'] as String? ?? '';
    if (id.isEmpty) throw FormatException('Quiz id is empty');
    final prompt = (json['prompt'] as String? ?? '').trim();
    final snippet = (json['snippet'] as String? ?? '').trim();
    final explanation = (json['explanation'] as String? ?? '').trim();
    if (prompt.isEmpty) throw FormatException('Quiz $id: prompt is empty');
    if (snippet.isEmpty) throw FormatException('Quiz $id: snippet is empty');
    if (explanation.isEmpty) {
      throw FormatException('Quiz $id: explanation is empty');
    }

    final optionsRaw = json['options'] as List<dynamic>? ?? [];
    if (optionsRaw.length != 4) {
      throw FormatException('Quiz $id: must have exactly 4 options');
    }
    final options = optionsRaw
        .map((e) => QuizOption.fromJson(e as Map<String, dynamic>))
        .toList();

    final correctOptionId = json['correct_option_id'] as String? ?? '';
    if (!options.any((o) => o.id == correctOptionId)) {
      throw FormatException(
        'Quiz $id: correct_option_id "$correctOptionId" not in options',
      );
    }

    // Ensure unique option IDs and texts
    final optionIds = options.map((o) => o.id).toSet();
    if (optionIds.length != 4) {
      throw FormatException('Quiz $id: option IDs not unique');
    }
    final optionTexts = options.map((o) => o.text).toSet();
    if (optionTexts.length != 4) {
      throw FormatException('Quiz $id: option texts not unique');
    }

    return Quiz(
      id: id,
      topicId: json['topic_id'] as String? ?? '',
      type: QuizType.fromString(json['type'] as String),
      level: Difficulty.fromString(json['level'] as String),
      prompt: prompt,
      snippet: snippet,
      snippetLanguage: json['snippet_language'] as String? ?? '',
      options: options,
      correctOptionId: correctOptionId,
      explanation: explanation,
      isActive: json['is_active'] as bool? ?? true,
    );
  }

  Map<String, dynamic> toDbMap() => {
    'id': id,
    'topic_id': topicId,
    'type': type.name,
    'level': level.name,
    'prompt': prompt,
    'snippet': snippet,
    'snippet_language': snippetLanguage,
    'options_json': _encodeJson(options.map((o) => o.toJson()).toList()),
    'correct_option_id': correctOptionId,
    'explanation': explanation,
    'is_active': isActive ? 1 : 0,
  };

  factory Quiz.fromDb(Map<String, dynamic> row) {
    final optionsRaw =
        _decodeJson(row['options_json'] as String) as List<dynamic>;
    return Quiz(
      id: row['id'] as String,
      topicId: row['topic_id'] as String,
      type: QuizType.fromString(row['type'] as String),
      level: Difficulty.fromString(row['level'] as String),
      prompt: row['prompt'] as String,
      snippet: row['snippet'] as String,
      snippetLanguage: row['snippet_language'] as String,
      options: optionsRaw
          .map((e) => QuizOption.fromJson(e as Map<String, dynamic>))
          .toList(),
      correctOptionId: row['correct_option_id'] as String,
      explanation: row['explanation'] as String,
      isActive: (row['is_active'] as int) == 1,
    );
  }
}

class LearningPath {
  final int? id;
  final String name;
  final String goal;
  final DateTime createdAt;
  final DateTime updatedAt;
  final List<LearningPathItem> items;

  const LearningPath({
    this.id,
    required this.name,
    required this.goal,
    required this.createdAt,
    required this.updatedAt,
    this.items = const [],
  });

  Map<String, dynamic> toDbMap() => {
    if (id != null) 'id': id,
    'name': name,
    'goal': goal,
    'created_at': createdAt.millisecondsSinceEpoch,
    'updated_at': updatedAt.millisecondsSinceEpoch,
  };

  factory LearningPath.fromDb(
    Map<String, dynamic> row, {
    List<LearningPathItem> items = const [],
  }) {
    return LearningPath(
      id: row['id'] as int,
      name: row['name'] as String,
      goal: row['goal'] as String,
      createdAt: DateTime.fromMillisecondsSinceEpoch(
        row['created_at'] as int,
        isUtc: true,
      ),
      updatedAt: DateTime.fromMillisecondsSinceEpoch(
        row['updated_at'] as int,
        isUtc: true,
      ),
      items: items,
    );
  }

  LearningPath copyWith({
    int? id,
    String? name,
    String? goal,
    DateTime? updatedAt,
    List<LearningPathItem>? items,
  }) {
    return LearningPath(
      id: id ?? this.id,
      name: name ?? this.name,
      goal: goal ?? this.goal,
      createdAt: createdAt,
      updatedAt: updatedAt ?? this.updatedAt,
      items: items ?? this.items,
    );
  }
}

class LearningPathItem {
  final int pathId;
  final String topicId;
  final int position;

  const LearningPathItem({
    required this.pathId,
    required this.topicId,
    required this.position,
  });

  Map<String, dynamic> toDbMap() => {
    'path_id': pathId,
    'topic_id': topicId,
    'position': position,
  };

  factory LearningPathItem.fromDb(Map<String, dynamic> row) {
    return LearningPathItem(
      pathId: row['path_id'] as int,
      topicId: row['topic_id'] as String,
      position: row['position'] as int,
    );
  }
}

class ContentMeta {
  final int contentVersion;
  final String dataset;
  final String locale;

  const ContentMeta({
    required this.contentVersion,
    required this.dataset,
    required this.locale,
  });

  factory ContentMeta.fromDb(Map<String, dynamic> row) {
    return ContentMeta(
      contentVersion: row['content_version'] as int,
      dataset: row['dataset'] as String,
      locale: row['locale'] as String,
    );
  }
}

// ─── JSON helpers ───

String _encodeJson(Object value) {
  // Use dart:convert imported by the files that use models
  // This is a simple helper, actual import is in the calling file
  return _jsonEncode(value);
}

dynamic _decodeJson(String source) {
  return _jsonDecode(source);
}

// These will be wired to dart:convert in the actual app
// We keep them as function references to avoid circular imports
typedef _JsonEncoder = String Function(Object);
typedef _JsonDecoder = dynamic Function(String);

late _JsonEncoder _jsonEncode;
late _JsonDecoder _jsonDecode;

/// Call this once at app startup before using any model serialization.
void initModelJsonCodecs({
  required String Function(Object) encode,
  required dynamic Function(String) decode,
}) {
  _jsonEncode = encode;
  _jsonDecode = decode;
}
