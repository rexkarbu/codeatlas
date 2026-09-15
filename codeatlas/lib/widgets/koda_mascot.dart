// lib/widgets/koda_mascot.dart — Static vector mascot for CodeAtlas onboarding.
// Crisp, lightweight, 100% offline, zero asset overhead.

import 'package:flutter/material.dart';

/// Static vector illustration of Koda, the CodeAtlas explorer guide.
class KodaMascot extends StatelessWidget {
  final double size;

  const KodaMascot({super.key, this.size = 80.0});

  @override
  Widget build(BuildContext context) {
    return Semantics(
      label: 'Maskot Koda - Pemandu Belajar CodeAtlas',
      child: SizedBox(
        width: size,
        height: size,
        child: CustomPaint(
          size: Size(size, size),
          painter: _KodaMascotPainter(
            isDark: Theme.of(context).brightness == Brightness.dark,
          ),
        ),
      ),
    );
  }
}

class _KodaMascotPainter extends CustomPainter {
  final bool isDark;

  _KodaMascotPainter({required this.isDark});

  @override
  void paint(Canvas canvas, Size size) {
    final w = size.width;
    final h = size.height;
    final center = Offset(w / 2, h / 2);

    // 1. Soft Background Aura / Glow
    final auraPaint = Paint()
      ..shader = RadialGradient(
        colors: [
          const Color(0xFF6366F1).withValues(alpha: isDark ? 0.35 : 0.2),
          const Color(0xFF10B981).withValues(alpha: 0.0),
        ],
      ).createShader(Rect.fromCircle(center: center, radius: w * 0.48));
    canvas.drawCircle(center, w * 0.48, auraPaint);

    // 2. Head / Helmet Base (Rounded Hexagon / Squircle)
    final headRect = RRect.fromRectAndRadius(
      Rect.fromCenter(
        center: Offset(center.dx, center.dy + h * 0.02),
        width: w * 0.72,
        height: h * 0.68,
      ),
      Radius.circular(w * 0.26),
    );

    final headPaint = Paint()
      ..shader = LinearGradient(
        begin: Alignment.topLeft,
        end: Alignment.bottomRight,
        colors: isDark
            ? [const Color(0xFF2E3456), const Color(0xFF1E2238)]
            : [const Color(0xFFE2E8F0), const Color(0xFFCBD5E1)],
      ).createShader(headRect.outerRect);

    final headBorder = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = w * 0.035
      ..shader = const LinearGradient(
        colors: [Color(0xFF6366F1), Color(0xFFA78BFA)],
      ).createShader(headRect.outerRect);

    canvas.drawRRect(headRect, headPaint);
    canvas.drawRRect(headRect, headBorder);

    // 3. Explorer Compass Ears / Antennas
    final earPaint = Paint()
      ..style = PaintingStyle.fill
      ..color = const Color(0xFF6366F1);

    // Left Ear
    final leftEar = Path()
      ..moveTo(w * 0.22, h * 0.28)
      ..lineTo(w * 0.14, h * 0.14)
      ..lineTo(w * 0.34, h * 0.20)
      ..close();
    canvas.drawPath(leftEar, earPaint);

    // Right Ear
    final rightEar = Path()
      ..moveTo(w * 0.78, h * 0.28)
      ..lineTo(w * 0.86, h * 0.14)
      ..lineTo(w * 0.66, h * 0.20)
      ..close();
    canvas.drawPath(rightEar, earPaint);

    // 4. Visor / Face Screen
    final visorRect = RRect.fromRectAndRadius(
      Rect.fromCenter(
        center: Offset(center.dx, center.dy + h * 0.02),
        width: w * 0.54,
        height: h * 0.36,
      ),
      Radius.circular(w * 0.14),
    );

    final visorPaint = Paint()
      ..color = isDark ? const Color(0xFF0F111E) : const Color(0xFF1E293B);
    canvas.drawRRect(visorRect, visorPaint);

    // 5. Friendly Luminous Eyes (Twin glowing pill / circles)
    final eyePaint = Paint()
      ..style = PaintingStyle.fill
      ..color = const Color(0xFF10B981); // Friendly Mint glow

    final leftEye = RRect.fromRectAndRadius(
      Rect.fromCenter(
        center: Offset(w * 0.40, center.dy + h * 0.01),
        width: w * 0.11,
        height: h * 0.16,
      ),
      Radius.circular(w * 0.05),
    );
    final rightEye = RRect.fromRectAndRadius(
      Rect.fromCenter(
        center: Offset(w * 0.60, center.dy + h * 0.01),
        width: w * 0.11,
        height: h * 0.16,
      ),
      Radius.circular(w * 0.05),
    );

    canvas.drawRRect(leftEye, eyePaint);
    canvas.drawRRect(rightEye, eyePaint);

    // Eye Sparkles
    final sparklePaint = Paint()..color = Colors.white;
    canvas.drawCircle(
      Offset(w * 0.42, center.dy - h * 0.03),
      w * 0.025,
      sparklePaint,
    );
    canvas.drawCircle(
      Offset(w * 0.62, center.dy - h * 0.03),
      w * 0.025,
      sparklePaint,
    );

    // 6. Cute Smile / Compass Needle Accent
    final smilePath = Path()
      ..moveTo(w * 0.45, center.dy + h * 0.11)
      ..quadraticBezierTo(
        center.dx,
        center.dy + h * 0.14,
        w * 0.55,
        center.dy + h * 0.11,
      );

    final smilePaint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = w * 0.025
      ..strokeCap = StrokeCap.round
      ..color = const Color(0xFFA78BFA);
    canvas.drawPath(smilePath, smilePaint);
  }

  @override
  bool shouldRepaint(covariant _KodaMascotPainter oldDelegate) =>
      oldDelegate.isDark != isDark;
}
