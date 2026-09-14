import 'package:flutter/material.dart';

/// Application logo widget utilizing pre-rendered assets via [Image.asset].
///
/// Streamlined visual identity: bold 32px syntax brackets, central atlas hub,
/// and clear constellation apex nodes for maximum legibility at small sizes (32px).
class CodeAtlasLogo extends StatelessWidget {
  final double size;
  final bool showBackground;
  final bool isMonochrome;
  final Color? monochromeColor;

  const CodeAtlasLogo({
    super.key,
    this.size = 48.0,
    this.showBackground = false,
    this.isMonochrome = false,
    this.monochromeColor,
  });

  @override
  Widget build(BuildContext context) {
    final String assetPath;
    if (isMonochrome) {
      assetPath = 'assets/branding/codeatlas_logo_monochrome.png';
    } else if (showBackground) {
      assetPath = 'assets/branding/codeatlas_icon_1024.png';
    } else {
      assetPath = 'assets/branding/codeatlas_logo_transparent.png';
    }

    Widget image = Image.asset(
      assetPath,
      width: size,
      height: size,
      fit: BoxFit.contain,
      filterQuality: FilterQuality.medium,
    );

    if (isMonochrome) {
      final color =
          monochromeColor ??
          (Theme.of(context).brightness == Brightness.dark
              ? Colors.white
              : const Color(0xFF1E1B4B));
      image = ColorFiltered(
        colorFilter: ColorFilter.mode(color, BlendMode.srcIn),
        child: image,
      );
    }

    return SizedBox(
      width: size,
      height: size,
      child: image,
    );
  }
}

/// Streamlined vector painter used for asset generation and precision scaling.
class CodeAtlasLogoPainter extends CustomPainter {
  final bool showBackground;
  final bool isMonochrome;
  final Color monochromeColor;

  CodeAtlasLogoPainter({
    this.showBackground = false,
    this.isMonochrome = false,
    this.monochromeColor = Colors.white,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final scale = size.width / 512.0;
    canvas.save();
    canvas.scale(scale, scale);

    final center = const Offset(256, 256);

    // 1. Squircle Background
    if (showBackground) {
      final bgRect = const Rect.fromLTWH(0, 0, 512, 512);
      final bgRRect = RRect.fromRectAndRadius(
        bgRect,
        const Radius.circular(116),
      );

      if (isMonochrome) {
        final bgPaint = Paint()
          ..color = monochromeColor.withValues(alpha: 0.15);
        canvas.drawRRect(bgRRect, bgPaint);
      } else {
        final bgPaint = Paint()
          ..shader = const LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [Color(0xFF1E1B4B), Color(0xFF15123F), Color(0xFF0C0A27)],
          ).createShader(bgRect);
        canvas.drawRRect(bgRRect, bgPaint);

        // Specular border highlight
        final borderPaint = Paint()
          ..color = const Color(0xFF8B5CF6).withValues(alpha: 0.22)
          ..style = PaintingStyle.stroke
          ..strokeWidth = 3;
        canvas.drawRRect(
          RRect.fromRectAndRadius(
            const Rect.fromLTWH(2, 2, 508, 508),
            const Radius.circular(114),
          ),
          borderPaint,
        );

        // Center ambient radial glow
        final glowPaint = Paint()
          ..shader = uiGradient(
            center,
            160,
            const Color(0xFF8B5CF6).withValues(alpha: 0.32),
            Colors.transparent,
          );
        canvas.drawCircle(center, 160, glowPaint);
      }
    }

    // 2. Streamlined Central Meridian Axis
    final meridianPaint = Paint()
      ..color = isMonochrome
          ? monochromeColor.withValues(alpha: 0.4)
          : const Color(0xFF8B5CF6).withValues(alpha: 0.35)
      ..strokeWidth = 8
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(const Offset(256, 110), const Offset(256, 402), meridianPaint);

    // 3. Primary Geometry: Code Syntax Brackets '<' and '>' (Bold 32px stroke)
    final leftPath = Path()
      ..moveTo(236, 156)
      ..lineTo(140, 256)
      ..lineTo(236, 356);

    final rightPath = Path()
      ..moveTo(276, 156)
      ..lineTo(372, 256)
      ..lineTo(276, 356);

    if (isMonochrome) {
      final bracketPaint = Paint()
        ..color = monochromeColor
        ..style = PaintingStyle.stroke
        ..strokeWidth = 32
        ..strokeCap = StrokeCap.round
        ..strokeJoin = StrokeJoin.round;
      canvas.drawPath(leftPath, bracketPaint);
      canvas.drawPath(rightPath, bracketPaint);
    } else {
      // Left Bracket: Violet to Cyan Gradient
      final leftPaint = Paint()
        ..shader = const LinearGradient(
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
          colors: [Color(0xFFA78BFA), Color(0xFF8B5CF6), Color(0xFF06B6D4)],
        ).createShader(const Rect.fromLTWH(140, 156, 96, 200))
        ..style = PaintingStyle.stroke
        ..strokeWidth = 32
        ..strokeCap = StrokeCap.round
        ..strokeJoin = StrokeJoin.round;
      canvas.drawPath(leftPath, leftPaint);

      // Right Bracket: Cyan to Sky Blue Gradient
      final rightPaint = Paint()
        ..shader = const LinearGradient(
          begin: Alignment.bottomLeft,
          end: Alignment.topRight,
          colors: [Color(0xFF06B6D4), Color(0xFF38BDF8)],
        ).createShader(const Rect.fromLTWH(276, 156, 96, 200))
        ..style = PaintingStyle.stroke
        ..strokeWidth = 32
        ..strokeCap = StrokeCap.round
        ..strokeJoin = StrokeJoin.round;
      canvas.drawPath(rightPath, rightPaint);
    }

    // 4. Constellation Nodes on Apexes (2 vertex nodes only)
    if (isMonochrome) {
      final nodePaint = Paint()..color = monochromeColor;
      canvas.drawCircle(const Offset(140, 256), 16, nodePaint);
      canvas.drawCircle(const Offset(372, 256), 16, nodePaint);
    } else {
      _drawNode(canvas, const Offset(140, 256), 16, const Color(0xFFA78BFA));
      _drawNode(canvas, const Offset(372, 256), 16, const Color(0xFF38BDF8));
    }

    // 5. Central Atlas Hub Core (Clear visual anchor across all scales)
    if (isMonochrome) {
      canvas.drawCircle(center, 26, Paint()..color = monochromeColor);
      canvas.drawCircle(center, 10, Paint()..color = Colors.black);
    } else {
      final coreOuter = Paint()
        ..color = const Color(0xFF0F0D2E)
        ..style = PaintingStyle.fill;
      final coreRing = Paint()
        ..color = const Color(0xFF22D3EE)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 8;
      final coreNucleus = Paint()
        ..color = Colors.white
        ..style = PaintingStyle.fill;

      canvas.drawCircle(center, 26, coreOuter);
      canvas.drawCircle(center, 26, coreRing);
      canvas.drawCircle(center, 10, coreNucleus);
    }

    canvas.restore();
  }

  void _drawNode(Canvas canvas, Offset offset, double radius, Color color) {
    final borderPaint = Paint()
      ..color = const Color(0xFF1E1B4B)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 5;
    final fillPaint = Paint()..color = color;

    canvas.drawCircle(offset, radius, fillPaint);
    canvas.drawCircle(offset, radius, borderPaint);
  }

  Shader uiGradient(Offset center, double radius, Color start, Color end) {
    return RadialGradient(
      colors: [start, end],
      stops: const [0.0, 1.0],
    ).createShader(Rect.fromCircle(center: center, radius: radius));
  }

  @override
  bool shouldRepaint(covariant CodeAtlasLogoPainter oldDelegate) {
    return oldDelegate.showBackground != showBackground ||
        oldDelegate.isMonochrome != isMonochrome ||
        oldDelegate.monochromeColor != monochromeColor;
  }
}
