import 'dart:io';
import 'dart:ui' as ui;
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  setUpAll(() async {
    final segoeBytes = await File(r'C:\Windows\Fonts\segoeui.ttf').readAsBytes();
    final robotoLoader = FontLoader('Roboto');
    robotoLoader.addFont(Future.value(ByteData.view(segoeBytes.buffer)));
    await robotoLoader.load();

    final iconFile = File(r'D:\development\flutter\flutter\bin\cache\artifacts\material_fonts\materialicons-regular.otf');
    if (iconFile.existsSync()) {
      final iconBytes = await iconFile.readAsBytes();
      final iconLoader = FontLoader('MaterialIcons');
      iconLoader.addFont(Future.value(ByteData.view(iconBytes.buffer)));
      await iconLoader.load();
    }
  });

  testWidgets('Test font rendering', (tester) async {
    final key = GlobalKey();
    await tester.pumpWidget(
      MaterialApp(
        theme: ThemeData(fontFamily: 'Roboto', useMaterial3: true),
        home: Scaffold(
          body: RepaintBoundary(
            key: key,
            child: Container(
              color: Colors.white,
              padding: const EdgeInsets.all(20),
              child: const Row(
                children: [
                  Icon(Icons.menu_book, color: Colors.blue),
                  SizedBox(width: 8),
                  Text('Halo Dunia! Teks Terbaca', style: TextStyle(color: Colors.black, fontSize: 18)),
                ],
              ),
            ),
          ),
        ),
      ),
    );
    await tester.pumpAndSettle();

    await tester.runAsync(() async {
      final boundary = key.currentContext?.findRenderObject() as RenderRepaintBoundary?;
      if (boundary != null) {
        final image = await boundary.toImage();
        final byteData = await image.toByteData(format: ui.ImageByteFormat.png);
        if (byteData != null) {
          final file = File('d:/project/ca/hasil/test_font.png');
          file.writeAsBytesSync(byteData.buffer.asUint8List());
          print('Saved test font image: ${file.lengthSync()} bytes');
        }
      }
    });
  });
}
