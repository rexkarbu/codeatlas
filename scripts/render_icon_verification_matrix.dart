// scripts/render_icon_verification_matrix.dart
import 'dart:io';
import 'dart:typed_data';
import 'dart:ui' as ui;
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:codeatlas/widgets/codeatlas_logo.dart';

void main() {
  setUpAll(() async {
    TestWidgetsFlutterBinding.ensureInitialized();
    final fontFile = File('C:/Windows/Fonts/segoeui.ttf');
    if (fontFile.existsSync()) {
      final fontData = fontFile.readAsBytesSync();
      final fontLoader = FontLoader('Segoe UI');
      fontLoader.addFont(Future.value(ByteData.view(fontData.buffer)));
      await fontLoader.load();
    }
  });

  test('Render 32px, 48px, 64px verification matrix', () async {
    const double width = 860;
    const double height = 480;

    final recorder = ui.PictureRecorder();
    final canvas = Canvas(recorder, const Rect.fromLTWH(0, 0, width, height));

    // Background
    final bgPaint = Paint()..color = const Color(0xFF0F0D2E);
    canvas.drawRect(const Rect.fromLTWH(0, 0, width, height), bgPaint);

    // Title Header
    _drawText(
      canvas,
      'Uji Keterbacaan Logo & Ikon CodeAtlas (32px, 48px, 64px)',
      32,
      28,
      fontSize: 20,
      fontWeight: FontWeight.bold,
      color: Colors.white,
    );
    _drawText(
      canvas,
      'Evaluasi ketajaman siluet pada skala kecil, bentuk mask lingkaran (adaptive), dan mode monokrom',
      32,
      56,
      fontSize: 13,
      color: const Color(0xFFA78BFA),
    );

    // Three Columns:
    // Column 1: 64px
    // Column 2: 48px
    // Column 3: 32px
    final columns = [
      {'size': 64.0, 'x': 32.0, 'w': 250.0, 'title': 'Ukuran 64 × 64 px'},
      {'size': 48.0, 'x': 306.0, 'w': 250.0, 'title': 'Ukuran 48 × 48 px'},
      {'size': 32.0, 'x': 580.0, 'w': 250.0, 'title': 'Ukuran 32 × 32 px'},
    ];

    for (final col in columns) {
      final double s = col['size'] as double;
      final double x = col['x'] as double;
      final double w = col['w'] as double;
      final String title = col['title'] as String;

      // Card Container
      _drawCard(canvas, x, 96, w, 350, const Color(0xFF16133B));
      _drawText(canvas, title, x + 20, 116, fontSize: 16, fontWeight: FontWeight.bold, color: Colors.white);

      // 1. Standard Squircle (Dark)
      final y1 = 155.0;
      canvas.save();
      canvas.translate(x + 24, y1);
      CodeAtlasLogoPainter(showBackground: true).paint(canvas, Size(s, s));
      canvas.restore();
      _drawText(canvas, 'Squircle Standard', x + 24 + s + 16, y1 + (s / 2 - 8), fontSize: 13, color: Colors.white);

      // 2. Circle Mask (Adaptive)
      final y2 = 235.0;
      canvas.save();
      canvas.translate(x + 24, y2);
      final circlePath = Path()..addOval(Rect.fromLTWH(0, 0, s, s));
      canvas.clipPath(circlePath);
      CodeAtlasLogoPainter(showBackground: true).paint(canvas, Size(s, s));
      canvas.restore();
      _drawText(canvas, 'Mask Lingkaran', x + 24 + s + 16, y2 + (s / 2 - 8), fontSize: 13, color: Colors.white);

      // 3. Monochrome (Themed Icon)
      final y3 = 315.0;
      // Container box for contrast
      final monoBox = RRect.fromRectAndRadius(Rect.fromLTWH(x + 24, y3, s, s), Radius.circular(s * 0.22));
      canvas.drawRRect(monoBox, Paint()..color = const Color(0xFF312E81));
      canvas.save();
      canvas.translate(x + 24, y3);
      CodeAtlasLogoPainter(showBackground: false, isMonochrome: true, monochromeColor: Colors.white).paint(canvas, Size(s, s));
      canvas.restore();
      _drawText(canvas, 'Monokrom / Themed', x + 24 + s + 16, y3 + (s / 2 - 8), fontSize: 13, color: Colors.white);
    }

    final picture = recorder.endRecording();
    final image = await picture.toImage(width.toInt(), height.toInt());
    final byteData = await image.toByteData(format: ui.ImageByteFormat.png);
    final bytes = byteData!.buffer.asUint8List();

    const artifactPath = r'C:\Users\Dimdim\.gemini\antigravity-ide\brain\46ec7035-1b4f-4791-9793-da903bdf6cc0\logo_preview_32_48_64.png';
    File(artifactPath).writeAsBytesSync(bytes);
    File('assets/branding/logo_preview_32_48_64.png').writeAsBytesSync(bytes);

    print('Preview rendered successfully to $artifactPath');
  });
}

void _drawCard(Canvas canvas, double x, double y, double w, double h, Color color) {
  final paint = Paint()..color = color;
  final borderPaint = Paint()
    ..color = const Color(0xFF8B5CF6).withValues(alpha: 0.2)
    ..style = PaintingStyle.stroke
    ..strokeWidth = 1.5;
  final rrect = RRect.fromRectAndRadius(Rect.fromLTWH(x, y, w, h), const Radius.circular(16));
  canvas.drawRRect(rrect, paint);
  canvas.drawRRect(rrect, borderPaint);
}

void _drawText(
  Canvas canvas,
  String text,
  double x,
  double y, {
  double fontSize = 14,
  FontWeight fontWeight = FontWeight.normal,
  Color color = Colors.white,
}) {
  final painter = TextPainter(
    text: TextSpan(
      text: text,
      style: TextStyle(
        fontSize: fontSize,
        fontWeight: fontWeight,
        color: color,
        fontFamily: 'Segoe UI',
      ),
    ),
    textDirection: TextDirection.ltr,
  )..layout();
  painter.paint(canvas, Offset(x, y));
}
