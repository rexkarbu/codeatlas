// test/version_branching_unit_test.dart — Unit tests for Content Version Branching:
// lower version rejection, identical version skipping (no-op), and higher version atomic upgrade.

import 'package:flutter_test/flutter_test.dart';
import 'package:codeatlas/data/seed_loader.dart';

void main() {
  group('Content Version Branching Unit Tests (PRD 2.C & Temuan A.2)', () {
    test('Initial Seed: No existing version in DB triggers initialSeed', () {
      final action = SeedLoader.determineVersionAction(1, null);
      expect(action, equals(VersionAction.initialSeed));

      final actionV2 = SeedLoader.determineVersionAction(2, null);
      expect(actionV2, equals(VersionAction.initialSeed));
    });

    test('Skip Equal: Identical version in package and DB triggers skipEqual (0 writes)', () {
      final actionV1 = SeedLoader.determineVersionAction(1, 1);
      expect(actionV1, equals(VersionAction.skipEqual));

      final actionV2 = SeedLoader.determineVersionAction(2, 2);
      expect(actionV2, equals(VersionAction.skipEqual));

      final actionV100 = SeedLoader.determineVersionAction(100, 100);
      expect(actionV100, equals(VersionAction.skipEqual));
    });

    test('Upgrade Higher: Higher package version triggers upgradeHigher (atomic transaction)', () {
      final action2to3 = SeedLoader.determineVersionAction(3, 2);
      expect(action2to3, equals(VersionAction.upgradeHigher));

      final action1to2 = SeedLoader.determineVersionAction(2, 1);
      expect(action1to2, equals(VersionAction.upgradeHigher));

      final actionMajor = SeedLoader.determineVersionAction(10, 2);
      expect(actionMajor, equals(VersionAction.upgradeHigher));
    });

    test('Real Migration: Version 3 in DB to Version 4 in package triggers upgradeHigher', () {
      final action3to4 = SeedLoader.determineVersionAction(4, 3);
      expect(action3to4, equals(VersionAction.upgradeHigher));
    });

    test('Real Downgrade Rejection: Version 4 in DB to Version 3 in package is strictly rejected', () {
      final action4to3 = SeedLoader.determineVersionAction(3, 4);
      expect(action4to3, equals(VersionAction.rejectDowngrade));
    });

    test('Hypothetical Downgrade Rejection: Version 5 in DB to Version 4 in package is strictly rejected', () {
      final action5to4 = SeedLoader.determineVersionAction(4, 5);
      expect(action5to4, equals(VersionAction.rejectDowngrade));
    });

    test('Validation failure before transaction: malformed package throws FormatException', () {
      expect(
        () => SeedLoader.parseAndValidate({
          'format_version': 999, // unsupported
          'content_version': 4,
          'dataset': 'production',
          'locale': 'id-ID',
          'categories': [],
          'topics': [],
          'quizzes': [],
        }),
        throwsA(isA<FormatException>()),
      );

      expect(
        () => SeedLoader.parseAndValidate({
          'format_version': 1,
          'content_version': 0, // invalid version
          'dataset': 'production',
          'locale': 'id-ID',
          'categories': [],
          'topics': [],
          'quizzes': [],
        }),
        throwsA(isA<FormatException>()),
      );
    });
  });
}
