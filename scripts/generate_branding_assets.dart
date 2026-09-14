// scripts/generate_branding_assets.dart — Generates master icons and Android launcher assets.
import 'dart:io';
import 'dart:math' as math;
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

      final robotoLoader = FontLoader('Roboto');
      robotoLoader.addFont(Future.value(ByteData.view(fontData.buffer)));
      await robotoLoader.load();
    }
  });

  test('Generate branding assets and launcher icons', () async {
    final brandingDir = Directory('assets/branding');
    if (!brandingDir.existsSync()) {
      brandingDir.createSync(recursive: true);
    }

    final rootBrandingDir = Directory('../assets/branding');
    if (!rootBrandingDir.existsSync()) {
      rootBrandingDir.createSync(recursive: true);
    }

    // 1. Master Icon 1024x1024
    print('Generating 1024x1024 master icon...');
    final icon1024Bytes = await renderPainterToPng(
      CodeAtlasLogoPainter(showBackground: true),
      1024,
      1024,
    );
    File('assets/branding/codeatlas_icon_1024.png').writeAsBytesSync(icon1024Bytes);
    File('../assets/branding/codeatlas_icon_1024.png').writeAsBytesSync(icon1024Bytes);

    // 2. High-Res Transparent Logo 1024x1024
    print('Generating 1024x1024 transparent logo...');
    final logoTransBytes = await renderPainterToPng(
      CodeAtlasLogoPainter(showBackground: false),
      1024,
      1024,
    );
    File('assets/branding/codeatlas_logo_transparent.png').writeAsBytesSync(logoTransBytes);
    File('../assets/branding/codeatlas_logo_transparent.png').writeAsBytesSync(logoTransBytes);

    // 3. Monochrome Logo 1024x1024
    print('Generating 1024x1024 monochrome logo...');
    final monoBytes = await renderPainterToPng(
      CodeAtlasLogoPainter(showBackground: false, isMonochrome: true, monochromeColor: Colors.white),
      1024,
      1024,
    );
    File('assets/branding/codeatlas_logo_monochrome.png').writeAsBytesSync(monoBytes);
    File('../assets/branding/codeatlas_logo_monochrome.png').writeAsBytesSync(monoBytes);

    // 4. Android Legacy Launcher Icons (ic_launcher.png)
    final legacySizes = {
      'mipmap-mdpi': 48,
      'mipmap-hdpi': 72,
      'mipmap-xhdpi': 96,
      'mipmap-xxhdpi': 144,
      'mipmap-xxxhdpi': 192,
    };

    for (final entry in legacySizes.entries) {
      final folder = Directory('android/app/src/main/res/${entry.key}');
      if (!folder.existsSync()) folder.createSync(recursive: true);

      final bytes = await renderPainterToPng(
        CodeAtlasLogoPainter(showBackground: true),
        entry.value,
        entry.value,
      );
      File('${folder.path}/ic_launcher.png').writeAsBytesSync(bytes);

      // Round icon (circle clipped)
      final roundBytes = await renderClippedCirclePainterToPng(
        CodeAtlasLogoPainter(showBackground: true),
        entry.value,
        entry.value,
      );
      File('${folder.path}/ic_launcher_round.png').writeAsBytesSync(roundBytes);
    }

    // 5. Android Adaptive Icons (ic_launcher_foreground.png & ic_launcher_monochrome.png)
    // Viewport: 108dp base (mdpi: 108, hdpi: 162, xhdpi: 216, xxhdpi: 324, xxxhdpi: 432)
    // Safe area: symbol scaled to ~64% centered to prevent clipping on circle/squircle masks.
    final adaptiveSizes = {
      'mipmap-mdpi': 108,
      'mipmap-hdpi': 162,
      'mipmap-xhdpi': 216,
      'mipmap-xxhdpi': 324,
      'mipmap-xxxhdpi': 432,
    };

    for (final entry in adaptiveSizes.entries) {
      final folder = Directory('android/app/src/main/res/${entry.key}');
      if (!folder.existsSync()) folder.createSync(recursive: true);

      // Adaptive foreground (transparent background, symbol inside safe area)
      final fgBytes = await renderAdaptiveForegroundToPng(
        isMonochrome: false,
        size: entry.value,
      );
      File('${folder.path}/ic_launcher_foreground.png').writeAsBytesSync(fgBytes);

      // Adaptive monochrome (pure white inside safe area)
      final monoFgBytes = await renderAdaptiveForegroundToPng(
        isMonochrome: true,
        size: entry.value,
      );
      File('${folder.path}/ic_launcher_monochrome.png').writeAsBytesSync(monoFgBytes);
    }

    // 6. Preview Icon Sheet (Matrix across sizes: 16, 24, 32, 48, 64, 128, 256, 512, light, dark, and masks)
    print('Generating icon preview showcase...');
    final previewBytes = await renderShowcaseMatrixToPng();
    File('assets/branding/codeatlas_icon_preview.png').writeAsBytesSync(previewBytes);
    File('../assets/branding/codeatlas_icon_preview.png').writeAsBytesSync(previewBytes);
    File('../hasil/codeatlas_icon_preview.png').writeAsBytesSync(previewBytes);

    print('All branding assets and launcher icons generated successfully!');
  });
}

Future<Uint8List> renderPainterToPng(
  CustomPainter painter,
  int width,
  int height,
) async {
  final recorder = ui.PictureRecorder();
  final canvas = Canvas(recorder, Rect.fromLTWH(0, 0, width.toDouble(), height.toDouble()));
  painter.paint(canvas, Size(width.toDouble(), height.toDouble()));
  final picture = recorder.endRecording();
  final image = await picture.toImage(width, height);
  final byteData = await image.toByteData(format: ui.ImageByteFormat.png);
  return byteData!.buffer.asUint8List();
}

Future<Uint8List> renderClippedCirclePainterToPng(
  CustomPainter painter,
  int width,
  int height,
) async {
  final recorder = ui.PictureRecorder();
  final canvas = Canvas(recorder, Rect.fromLTWH(0, 0, width.toDouble(), height.toDouble()));
  
  final center = Offset(width / 2, height / 2);
  final radius = width / 2;
  final clipPath = Path()..addOval(Rect.fromCircle(center: center, radius: radius));
  canvas.clipPath(clipPath);

  painter.paint(canvas, Size(width.toDouble(), height.toDouble()));
  final picture = recorder.endRecording();
  final image = await picture.toImage(width, height);
  final byteData = await image.toByteData(format: ui.ImageByteFormat.png);
  return byteData!.buffer.asUint8List();
}

Future<Uint8List> renderAdaptiveForegroundToPng({
  required bool isMonochrome,
  required int size,
}) async {
  final recorder = ui.PictureRecorder();
  final canvas = Canvas(recorder, Rect.fromLTWH(0, 0, size.toDouble(), size.toDouble()));

  // In Android adaptive icon (108x108 viewport), the safe zone is the central 66-72dp.
  // We scale the 512x512 vector symbol to 64% of the viewport and center it.
  final targetSymbolSize = size * 0.64;
  final offset = (size - targetSymbolSize) / 2.0;

  canvas.save();
  canvas.translate(offset, offset);
  final scale = targetSymbolSize / 512.0;
  canvas.scale(scale, scale);

  final painter = CodeAtlasLogoPainter(
    showBackground: false,
    isMonochrome: isMonochrome,
    monochromeColor: Colors.white,
  );
  painter.paint(canvas, const Size(512, 512));
  canvas.restore();

  final picture = recorder.endRecording();
  final image = await picture.toImage(size, size);
  final byteData = await image.toByteData(format: ui.ImageByteFormat.png);
  return byteData!.buffer.asUint8List();
}

Future<Uint8List> renderShowcaseMatrixToPng() async {
  const double width = 1200;
  const double height = 800;

  final recorder = ui.PictureRecorder();
  final canvas = Canvas(recorder, const Rect.fromLTWH(0, 0, width, height));

  // Canvas background: Deep Obsidian Indigo
  final bgPaint = Paint()..color = const Color(0xFF0F0D2E);
  canvas.drawRect(const Rect.fromLTWH(0, 0, width, height), bgPaint);

  // Subtle background grid
  final gridPaint = Paint()
    ..color = const Color(0xFF8B5CF6).withValues(alpha: 0.08)
    ..strokeWidth = 1;
  for (double x = 0; x < width; x += 40) {
    canvas.drawLine(Offset(x, 0), Offset(x, height), gridPaint);
  }
  for (double y = 0; y < height; y += 40) {
    canvas.drawLine(Offset(0, y), Offset(width, y), gridPaint);
  }

  // Draw Header Card
  _drawCard(canvas, 40, 40, 1120, 100, const Color(0xFF1E1B4B));
  _drawText(
    canvas,
    'CodeAtlas — Identitas Visual & Matriks Ikon Aplikasi',
    56,
    56,
    fontSize: 26,
    fontWeight: FontWeight.bold,
    color: Colors.white,
  );
  _drawText(
    canvas,
    'Sintesis Peta Pengetahuan (Atlas Grid, Meridian Axis, Constellation Nodes) & Sintaks Kode (< / >)',
    56,
    94,
    fontSize: 14,
    color: const Color(0xFFA78BFA),
  );

  // Column 1: Master Icon 256px + Masks (Circle & Squircle)
  _drawCard(canvas, 40, 160, 360, 590, const Color(0xFF16133B));
  _drawText(canvas, 'Master App Icon (256px)', 60, 180, fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white);
  _drawText(canvas, 'Squircle Standard & Circle Adaptive Mask', 60, 208, fontSize: 12, color: const Color(0xFF94A3B8));

  // 1. Squircle
  canvas.save();
  canvas.translate(92, 240);
  CodeAtlasLogoPainter(showBackground: true).paint(canvas, const Size(256, 256));
  canvas.restore();
  _drawText(canvas, 'Bentuk Squircle (Android Standard / iOS)', 110, 510, fontSize: 12, color: const Color(0xFFCBD5E1));

  // 2. Circle Adaptive
  canvas.save();
  canvas.translate(140, 545);
  final clipPath = Path()..addOval(const Rect.fromLTWH(0, 0, 160, 160));
  canvas.clipPath(clipPath);
  CodeAtlasLogoPainter(showBackground: true).paint(canvas, const Size(160, 160));
  canvas.restore();
  _drawText(canvas, 'Bentuk Mask Lingkaran (Android Adaptive)', 105, 718, fontSize: 12, color: const Color(0xFFCBD5E1));

  // Column 2: Multi-Environment (Dark & Light & Monochrome)
  _drawCard(canvas, 420, 160, 360, 590, const Color(0xFF16133B));
  _drawText(canvas, 'Variasi Lingkungan', 440, 180, fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white);
  _drawText(canvas, 'Dark Mode, Light Theme, & Android Themed Icon', 440, 208, fontSize: 12, color: const Color(0xFF94A3B8));

  // Dark Theme Card
  _drawCard(canvas, 440, 240, 320, 130, const Color(0xFF0C0A27));
  canvas.save();
  canvas.translate(460, 255);
  CodeAtlasLogoPainter(showBackground: true).paint(canvas, const Size(100, 100));
  canvas.restore();
  _drawText(canvas, 'Dark Mode Master', 580, 275, fontSize: 15, fontWeight: FontWeight.bold, color: Colors.white);
  _drawText(canvas, 'Deep Indigo & Electric Violet\nKontras tinggi untuk mode gelap', 580, 305, fontSize: 12, color: const Color(0xFF94A3B8));

  // Light Theme Card
  _drawCard(canvas, 440, 390, 320, 130, const Color(0xFFF5F3FF));
  canvas.save();
  canvas.translate(460, 405);
  // Light squircle
  final lightBgPaint = Paint()..color = const Color(0xFFEDE9FE);
  canvas.drawRRect(RRect.fromRectAndRadius(const Rect.fromLTWH(0, 0, 100, 100), const Radius.circular(22)), lightBgPaint);
  CodeAtlasLogoPainter(showBackground: false).paint(canvas, const Size(100, 100));
  canvas.restore();
  _drawText(canvas, 'Light Theme Variant', 580, 425, fontSize: 15, fontWeight: FontWeight.bold, color: const Color(0xFF1E1B4B));
  _drawText(canvas, 'Lavender Base & Vibrant Vectors\nTerbaca jelas di latar terang', 580, 455, fontSize: 12, color: const Color(0xFF475569));

  // Monochrome Themed Icon Card (Android 13+)
  _drawCard(canvas, 440, 540, 320, 130, const Color(0xFF1E1B4B));
  canvas.save();
  canvas.translate(460, 555);
  final monoBgPaint = Paint()..color = const Color(0xFF312E81);
  canvas.drawRRect(RRect.fromRectAndRadius(const Rect.fromLTWH(0, 0, 100, 100), const Radius.circular(22)), monoBgPaint);
  CodeAtlasLogoPainter(showBackground: false, isMonochrome: true, monochromeColor: Colors.white).paint(canvas, const Size(100, 100));
  canvas.restore();
  _drawText(canvas, 'Monochrome Themed Icon', 580, 575, fontSize: 15, fontWeight: FontWeight.bold, color: Colors.white);
  _drawText(canvas, 'Dynamic System Tint (API 33+)\nSiluet vektor adaptif warna sistem', 580, 605, fontSize: 12, color: const Color(0xFF94A3B8));

  // Column 3: Optical Scale Retention Matrix (16px to 128px)
  _drawCard(canvas, 800, 160, 360, 590, const Color(0xFF16133B));
  _drawText(canvas, 'Uji Keterbacaan Skala Kecil', 820, 180, fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white);
  _drawText(canvas, 'Uji ketajaman siluet pada berbagai ukuran UI', 820, 208, fontSize: 12, color: const Color(0xFF94A3B8));

  final sizes = [
    {'size': 128, 'y': 250, 'label': '128px — App Launcher / Tablet Grid'},
    {'size': 64, 'y': 400, 'label': '64px — Mobile Home Grid'},
    {'size': 48, 'y': 485, 'label': '48px — Notifikasi / Quick Settings'},
    {'size': 32, 'y': 555, 'label': '32px — List View / Settings Item'},
    {'size': 24, 'y': 610, 'label': '24px — AppBar / Bottom Nav Item'},
    {'size': 16, 'y': 655, 'label': '16px — Favicon / Status Bar Glyph'},
  ];

  for (final item in sizes) {
    final s = (item['size'] as num).toDouble();
    final y = (item['y'] as num).toDouble();
    final label = item['label'] as String;

    canvas.save();
    canvas.translate(830, y);
    CodeAtlasLogoPainter(showBackground: true).paint(canvas, Size(s, s));
    canvas.restore();

    _drawText(canvas, label, 830 + s + 16, y + (s > 24 ? (s / 2 - 8) : 0), fontSize: 13, color: Colors.white);
  }

  final picture = recorder.endRecording();
  final image = await picture.toImage(width.toInt(), height.toInt());
  final byteData = await image.toByteData(format: ui.ImageByteFormat.png);
  return byteData!.buffer.asUint8List();
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
