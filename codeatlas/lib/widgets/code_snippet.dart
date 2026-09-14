// lib/widgets/code_snippet.dart — Read-only monospace code display.
//
// SelectableText with horizontal scroll, language label, and optional
// "Hasil yang diharapkan" section. No editor, no highlighter, no WebView.

import 'package:flutter/material.dart';

class CodeSnippet extends StatelessWidget {
  final String code;
  final String? language;
  final String? expectedOutput;
  final bool showLanguageLabel;

  const CodeSnippet({
    super.key,
    required this.code,
    this.language,
    this.expectedOutput,
    this.showLanguageLabel = true,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final isDark = theme.brightness == Brightness.dark;
    final bgColor = isDark ? const Color(0xFF1E1E2E) : const Color(0xFFF5F5F5);
    final textColor = isDark
        ? const Color(0xFFCDD6F4)
        : const Color(0xFF1E1E1E);
    final labelColor = isDark
        ? const Color(0xFF89B4FA)
        : const Color(0xFF1E40AF);

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Container(
          decoration: BoxDecoration(
            color: bgColor,
            borderRadius: BorderRadius.circular(8),
            border: Border.all(color: isDark ? Colors.white12 : Colors.black12),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              if (showLanguageLabel && language != null && language!.isNotEmpty)
                Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 12,
                    vertical: 6,
                  ),
                  decoration: BoxDecoration(
                    border: Border(
                      bottom: BorderSide(
                        color: isDark ? Colors.white12 : Colors.black12,
                      ),
                    ),
                  ),
                  child: Text(
                    language!,
                    style: TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.w600,
                      color: labelColor,
                    ),
                    semanticsLabel: showLanguageLabel
                        ? 'Bahasa: $language'
                        : null,
                  ),
                ),
              Padding(
                padding: const EdgeInsets.all(12),
                child: SingleChildScrollView(
                  scrollDirection: Axis.horizontal,
                  child: SelectableText(
                    code,
                    style: TextStyle(
                      fontFamily: 'monospace',
                      fontSize: 13,
                      height: 1.5,
                      color: textColor,
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
        if (expectedOutput != null && expectedOutput!.isNotEmpty)
          Padding(
            padding: const EdgeInsets.only(top: 8),
            child: Container(
              decoration: BoxDecoration(
                color: isDark
                    ? const Color(0xFF1A1A2E)
                    : const Color(0xFFEFF6FF),
                borderRadius: BorderRadius.circular(8),
                border: Border.all(
                  color: isDark ? Colors.white10 : const Color(0xFFBFDBFE),
                ),
              ),
              padding: const EdgeInsets.all(12),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Hasil yang diharapkan:',
                    style: TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.w600,
                      color: labelColor,
                    ),
                  ),
                  const SizedBox(height: 4),
                  SelectableText(
                    expectedOutput!,
                    style: TextStyle(
                      fontFamily: 'monospace',
                      fontSize: 13,
                      height: 1.5,
                      color: textColor,
                    ),
                  ),
                ],
              ),
            ),
          ),
      ],
    );
  }
}
