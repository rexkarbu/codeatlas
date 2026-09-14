// lib/widgets/codeatlas_logo.dart — Reusable vector logo & icon widget for CodeAtlas.
import 'dart:math' as math;

import 'package:flutter/material.dart';

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
    return SizedBox(
      width: size,
      height: size,
      child: CustomPaint(
        size: Size(size, size),
        painter: CodeAtlasLogoPainter(
          showBackground: showBackground,
          isMonochrome: isMonochrome,
          monochromeColor:
              monochromeColor ??
              (Theme.of(context).brightness == Brightness.dark
                  ? Colors.white
                  : const Color(0xFF1E1B4B)),
        ),
      ),
    );
  }
}

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

    // 1. Optional Squircle Background
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

        // Specular highlight
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
            180,
            const Color(0xFF8B5CF6).withValues(alpha: 0.35),
            Colors.transparent,
          );
        canvas.drawCircle(center, 180, glowPaint);
      }
    }

    // 2. Subtle Coordinate Grid & Latitude Circles (if not monochrome)
    if (!isMonochrome) {
      final gridPaint = Paint()
        ..color = const Color(0xFF8B5CF6).withValues(alpha: 0.15)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 1.5;

      canvas.drawCircle(center, 168, gridPaint);
      canvas.drawCircle(center, 108, gridPaint);
      canvas.drawLine(const Offset(256, 80), const Offset(256, 432), gridPaint);
      canvas.drawLine(const Offset(80, 256), const Offset(432, 256), gridPaint);
    }

    // 3. Central Meridian Axis
    final meridianPaint = Paint()
      ..color = isMonochrome ? monochromeColor : const Color(0xFFC4B5FD)
      ..strokeWidth = 10
      ..strokeCap = StrokeCap.round;
    _drawDashedLine(
      canvas,
      const Offset(256, 136),
      const Offset(256, 376),
      10,
      12,
      meridianPaint,
    );

    // 4. Code Brackets '<' and '>'
    final leftPath = Path()
      ..moveTo(230, 148)
      ..lineTo(140, 256)
      ..lineTo(230, 364);

    final rightPath = Path()
      ..moveTo(282, 148)
      ..lineTo(372, 256)
      ..lineTo(282, 364);

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
        ).createShader(const Rect.fromLTWH(140, 148, 90, 216))
        ..style = PaintingStyle.stroke
        ..strokeWidth = 28
        ..strokeCap = StrokeCap.round
        ..strokeJoin = StrokeJoin.round;
      canvas.drawPath(leftPath, leftPaint);

      // Right Bracket: Cyan to Sky Blue Gradient
      final rightPaint = Paint()
        ..shader = const LinearGradient(
          begin: Alignment.bottomLeft,
          end: Alignment.topRight,
          colors: [Color(0xFF06B6D4), Color(0xFF38BDF8)],
        ).createShader(const Rect.fromLTWH(282, 148, 90, 216))
        ..style = PaintingStyle.stroke
        ..strokeWidth = 28
        ..strokeCap = StrokeCap.round
        ..strokeJoin = StrokeJoin.round;
      canvas.drawPath(rightPath, rightPaint);
    }

    // 5. Constellation Knowledge Nodes on Apexes
    if (isMonochrome) {
      final nodePaint = Paint()..color = monochromeColor;
      canvas.drawCircle(const Offset(140, 256), 16, nodePaint);
      canvas.drawCircle(const Offset(372, 256), 16, nodePaint);
      canvas.drawCircle(const Offset(230, 148), 14, nodePaint);
      canvas.drawCircle(const Offset(230, 364), 14, nodePaint);
      canvas.drawCircle(const Offset(282, 148), 14, nodePaint);
      canvas.drawCircle(const Offset(282, 364), 14, nodePaint);
    } else {
      _drawNode(canvas, const Offset(140, 256), 14, const Color(0xFFA78BFA));
      _drawNode(canvas, const Offset(372, 256), 14, const Color(0xFF38BDF8));
      _drawNode(canvas, const Offset(230, 148), 12, const Color(0xFFC4B5FD));
      _drawNode(canvas, const Offset(230, 364), 12, const Color(0xFF8B5CF6));
      _drawNode(canvas, const Offset(282, 148), 12, const Color(0xFF38BDF8));
      _drawNode(canvas, const Offset(282, 364), 12, const Color(0xFF06B6D4));
    }

    // 6. Central Atlas Hub Core
    if (isMonochrome) {
      canvas.drawCircle(center, 26, Paint()..color = monochromeColor);
      canvas.drawCircle(center, 10, Paint()..color = Colors.transparent);
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

      canvas.drawCircle(center, 22, coreOuter);
      canvas.drawCircle(center, 22, coreRing);
      canvas.drawCircle(center, 8, coreNucleus);
    }

    // 7. Cardinal Orientation Marks (North & South Stars)
    final northPath = Path()
      ..moveTo(256, 92)
      ..lineTo(263, 108)
      ..lineTo(256, 120)
      ..lineTo(249, 108)
      ..close();
    final southPath = Path()
      ..moveTo(256, 420)
      ..lineTo(263, 404)
      ..lineTo(256, 392)
      ..lineTo(249, 404)
      ..close();

    final northPaint = Paint()
      ..color = isMonochrome ? monochromeColor : const Color(0xFF38BDF8);
    final southPaint = Paint()
      ..color = isMonochrome ? monochromeColor : const Color(0xFF8B5CF6);
    canvas.drawPath(northPath, northPaint);
    canvas.drawPath(southPath, southPaint);

    canvas.restore();
  }

  void _drawNode(Canvas canvas, Offset offset, double radius, Color color) {
    final borderPaint = Paint()
      ..color = const Color(0xFF1E1B4B)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 4;
    final fillPaint = Paint()..color = color;

    canvas.drawCircle(offset, radius, fillPaint);
    canvas.drawCircle(offset, radius, borderPaint);
  }

  void _drawDashedLine(
    Canvas canvas,
    Offset start,
    Offset end,
    double dashLength,
    double gapLength,
    Paint paint,
  ) {
    final dx = end.dx - start.dx;
    final dy = end.dy - start.dy;
    final totalDist = math.sqrt(dx * dx + dy * dy);
    final ux = dx / totalDist;
    final uy = dy / totalDist;

    double currentDist = 0;
    while (currentDist < totalDist) {
      final p1 = Offset(
        start.dx + ux * currentDist,
        start.dy + uy * currentDist,
      );
      final len = math.min(dashLength, totalDist - currentDist);
      final p2 = Offset(p1.dx + ux * len, p1.dy + uy * len);
      canvas.drawLine(p1, p2, paint);
      currentDist += dashLength + gapLength;
    }
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
