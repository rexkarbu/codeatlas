plugins {
    id("com.android.application")
    // The Flutter Gradle Plugin must be applied after the Android and Kotlin Gradle plugins.
    id("dev.flutter.flutter-gradle-plugin")
}

android {
    namespace = "com.codeatlas.codeatlas"
    compileSdk = flutter.compileSdkVersion
    ndkVersion = flutter.ndkVersion

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    defaultConfig {
        // TODO: Specify your own unique Application ID (https://developer.android.com/studio/build/application-id.html).
        applicationId = "com.codeatlas.app"
        // You can update the following values to match your application needs.
        // For more information, see: https://flutter.dev/to/review-gradle-config.
        minSdk = flutter.minSdkVersion
        targetSdk = flutter.targetSdkVersion
        // Uses the version code from pubspec.yaml. When using split APKs, 1000 * ABI_VERSION
        // is added automatically by Flutter. (https://developer.android.com/studio/build/configure-apk-splits#configure-APK-versions)
        // You can force using the value of versionCode by specifying the `-P force-version-code-ignoring-abi=true`
        // flag during build.
        versionCode = flutter.versionCode
        versionName = flutter.versionName
    }

    val keystorePath = System.getenv("KEYSTORE_PATH")
    val keystorePassword = System.getenv("KEYSTORE_PASSWORD")
    val keyAliasVal = System.getenv("KEY_ALIAS")
    val keyPasswordVal = System.getenv("KEY_PASSWORD")

    val hasReleaseSigning = !keystorePath.isNullOrEmpty() &&
            file(keystorePath).exists() &&
            !keystorePassword.isNullOrEmpty() &&
            !keyAliasVal.isNullOrEmpty() &&
            !keyPasswordVal.isNullOrEmpty()

    signingConfigs {
        if (hasReleaseSigning) {
            create("release") {
                storeFile = file(keystorePath!!)
                storePassword = keystorePassword
                keyAlias = keyAliasVal
                keyPassword = keyPasswordVal
            }
        }
    }

    buildTypes {
        debug {
            signingConfig = signingConfigs.getByName("debug")
        }
        release {
            if (hasReleaseSigning) {
                signingConfig = signingConfigs.getByName("release")
            } else {
                signingConfig = null
            }
        }
    }
}

gradle.taskGraph.whenReady {
    val isBuildingRelease = allTasks.any { 
        it.name.contains("packageRelease", ignoreCase = true) || 
        it.name.contains("assembleRelease", ignoreCase = true) 
    }
    val hasSigningEnv = !System.getenv("KEYSTORE_PATH").isNullOrEmpty() &&
            file(System.getenv("KEYSTORE_PATH")).exists() &&
            !System.getenv("KEYSTORE_PASSWORD").isNullOrEmpty() &&
            !System.getenv("KEY_ALIAS").isNullOrEmpty() &&
            !System.getenv("KEY_PASSWORD").isNullOrEmpty()

    if (isBuildingRelease && !hasSigningEnv) {
        throw GradleException(
            "FATAL: Release build requested, but release signing credentials are missing or incomplete. " +
            "Environment variables KEYSTORE_PATH, KEYSTORE_PASSWORD, KEY_ALIAS, and KEY_PASSWORD must all be defined, " +
            "and KEYSTORE_PATH must point to an existing keystore file. Release builds must never fall back to debug signing."
        )
    }
}


kotlin {
    compilerOptions {
        jvmTarget = org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_17
    }
}

flutter {
    source = "../.."
}
