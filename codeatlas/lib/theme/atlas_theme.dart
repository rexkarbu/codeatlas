// lib/theme/atlas_theme.dart — Curated visual tokens and local theme builder
// for CodeAtlas UI/UX redesign (Dark Horizon & Light Atlas).

import 'package:flutter/material.dart';

class AtlasColors {
  // ─── Dark Mode Palette (Dark Horizon) ───
  static const darkCanvas = Color(0xFF0F111E);
  static const darkSurface = Color(0xFF1A1D2E);
  static const darkSurfaceElevated = Color(0xFF22263C);
  static const darkBorder = Color(0xFF2D324E);
  static const darkBorderSubtle = Color(0x1AFFFFFF);
  static const darkTextPrimary = Color(0xFFF8FAFC);
  static const darkTextSecondary = Color(0xFF94A3B8);
  static const darkTextMuted = Color(0xFF64748B);

  // ─── Light Mode Palette (Light Atlas) ───
  static const lightCanvas = Color(0xFFF8FAFC);
  static const lightSurface = Color(0xFFFFFFFF);
  static const lightSurfaceElevated = Color(0xFFF1F5F9);
  static const lightBorder = Color(0xFFE2E8F0);
  static const lightBorderSubtle = Color(0x1F0F172A);
  static const lightTextPrimary = Color(0xFF0F172A);
  static const lightTextSecondary = Color(0xFF475569);
  static const lightTextMuted = Color(0xFF94A3B8);

  // ─── Semantic Accents ───
  static const primaryIndigo = Color(0xFF6366F1);
  static const primaryIndigoLight = Color(0xFF4F46E5);

  static const accentMint = Color(0xFF10B981);
  static const accentMintLight = Color(0xFF059669);

  static const accentAmber = Color(0xFFF59E0B);
  static const accentAmberLight = Color(0xFFD97706);

  static const accentLavender = Color(0xFFA78BFA);
  static const accentLavenderLight = Color(0xFF7C3AED);

  static const accentCoral = Color(0xFFF43F5E);
  static const accentCoralLight = Color(0xFFE11D48);

  static const accentCyan = Color(0xFF06B6D4);
  static const accentCyanLight = Color(0xFF0284C7);

  // Helper getters based on brightness
  static Color canvas(Brightness brightness) =>
      brightness == Brightness.dark ? darkCanvas : lightCanvas;

  static Color surface(Brightness brightness) =>
      brightness == Brightness.dark ? darkSurface : lightSurface;

  static Color surfaceElevated(Brightness brightness) =>
      brightness == Brightness.dark
      ? darkSurfaceElevated
      : lightSurfaceElevated;

  static Color border(Brightness brightness) =>
      brightness == Brightness.dark ? darkBorder : lightBorder;

  static Color textPrimary(Brightness brightness) =>
      brightness == Brightness.dark ? darkTextPrimary : lightTextPrimary;

  static Color textSecondary(Brightness brightness) =>
      brightness == Brightness.dark ? darkTextSecondary : lightTextSecondary;

  static Color primary(Brightness brightness) =>
      brightness == Brightness.dark ? primaryIndigo : primaryIndigoLight;

  static Color mint(Brightness brightness) =>
      brightness == Brightness.dark ? accentMint : accentMintLight;

  static Color amber(Brightness brightness) =>
      brightness == Brightness.dark ? accentAmber : accentAmberLight;

  static Color lavender(Brightness brightness) =>
      brightness == Brightness.dark ? accentLavender : accentLavenderLight;
}

class AtlasTheme {
  /// Builds a localized ThemeData for the pilot screens.
  static ThemeData buildTheme(Brightness brightness) {
    final isDark = brightness == Brightness.dark;
    final primary = AtlasColors.primary(brightness);
    final canvas = AtlasColors.canvas(brightness);
    final surface = AtlasColors.surface(brightness);
    final border = AtlasColors.border(brightness);
    final textPrimary = AtlasColors.textPrimary(brightness);

    final base = isDark
        ? ThemeData.dark(useMaterial3: true)
        : ThemeData.light(useMaterial3: true);

    return base.copyWith(
      scaffoldBackgroundColor: canvas,
      colorScheme: ColorScheme.fromSeed(
        seedColor: primary,
        brightness: brightness,
        surface: surface,
      ),
      appBarTheme: AppBarTheme(
        backgroundColor: canvas,
        foregroundColor: textPrimary,
        elevation: 0,
        scrolledUnderElevation: 1,
        surfaceTintColor: Colors.transparent,
      ),
      cardTheme: CardThemeData(
        color: surface,
        elevation: 0,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
          side: BorderSide(color: border, width: 1),
        ),
        margin: EdgeInsets.zero,
      ),
      dividerTheme: DividerThemeData(color: border, thickness: 1, space: 1),
      dialogTheme: DialogThemeData(
        backgroundColor: surface,
        surfaceTintColor: Colors.transparent,
        titleTextStyle: TextStyle(
          color: textPrimary,
          fontSize: 18,
          fontWeight: FontWeight.bold,
        ),
        contentTextStyle: TextStyle(
          color: AtlasColors.textSecondary(brightness),
          fontSize: 14,
        ),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(16),
          side: BorderSide(color: border, width: 1),
        ),
      ),
      bottomSheetTheme: BottomSheetThemeData(
        backgroundColor: surface,
        surfaceTintColor: Colors.transparent,
        shape: const RoundedRectangleBorder(
          borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
        ),
      ),
      snackBarTheme: SnackBarThemeData(
        backgroundColor: AtlasColors.surfaceElevated(brightness),
        contentTextStyle: TextStyle(color: textPrimary),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(8),
          side: BorderSide(color: border, width: 1),
        ),
      ),
      textTheme: base.textTheme.apply(
        bodyColor: textPrimary,
        displayColor: textPrimary,
      ),
    );
  }
}
