# Build Instructions

## Prerequisites

- Android Studio Hedgehog (2023.1.1) or later
- JDK 17 or later
- Android SDK 34

## Development Build

1. **Clone/Open Project**
```bash
cd "/Users/macs/QR Scan"
```

2. **Sync Gradle**
```bash
./gradlew clean
```

3. **Build Debug APK**
```bash
./gradlew assembleDebug
```

Output: `app/build/outputs/apk/debug/app-debug.apk`

## Release Build

### Step 1: Create Keystore (First Time Only)

```bash
keytool -genkey -v -keystore qr-scanner-release.jks -keyalg RSA -keysize 2048 -validity 10000 -alias qr-scanner
```

**Save these credentials securely:**
- Keystore password: [YOUR_KEYSTORE_PASSWORD]
- Key alias: qr-scanner
- Key password: [YOUR_KEY_PASSWORD]

### Step 2: Create key.properties

Create `key.properties` in project root:

```properties
storePassword=YOUR_KEYSTORE_PASSWORD
keyPassword=YOUR_KEY_PASSWORD
keyAlias=qr-scanner
storeFile=../qr-scanner-release.jks
```

⚠️ **IMPORTANT**: Add `key.properties` to `.gitignore`

### Step 3: Update app/build.gradle

Add this before `android {` block:

```gradle
def keystorePropertiesFile = rootProject.file("key.properties")
def keystoreProperties = new Properties()
if (keystorePropertiesFile.exists()) {
    keystoreProperties.load(new FileInputStream(keystorePropertiesFile))
}
```

Add this inside `android {` block:

```gradle
signingConfigs {
    release {
        if (keystorePropertiesFile.exists()) {
            keyAlias keystoreProperties['keyAlias']
            keyPassword keystoreProperties['keyPassword']
            storeFile file(keystoreProperties['storeFile'])
            storePassword keystoreProperties['storePassword']
        }
    }
}

buildTypes {
    release {
        signingConfig signingConfigs.release
        minifyEnabled true
        shrinkResources true
        proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
    }
}
```

### Step 4: Build Release AAB (for Google Play)

```bash
./gradlew bundleRelease
```

Output: `app/build/outputs/bundle/release/app-release.aab`

### Step 5: Build Release APK (for testing)

```bash
./gradlew assembleRelease
```

Output: `app/build/outputs/apk/release/app-release.apk`

## Testing Release Build

```bash
adb install app/build/outputs/apk/release/app-release.apk
```

## Verify Signing

```bash
jarsigner -verify -verbose -certs app/build/outputs/apk/release/app-release.apk
```

## Build Variants

- **debug**: Development build with debugging enabled
- **release**: Production build, optimized and signed

## Common Issues

### Issue: "Keystore not found"
**Solution**: Ensure `qr-scanner-release.jks` is in project root

### Issue: "Incorrect password"
**Solution**: Verify passwords in `key.properties`

### Issue: "ProGuard errors"
**Solution**: Check `proguard-rules.pro` for any missing keep rules

## Version Update

Before each release, update in `app/build.gradle`:

```gradle
versionCode 2  // Increment by 1
versionName "1.0.1"  // Update version string
```

## Clean Build

```bash
./gradlew clean
rm -rf .gradle
rm -rf build
rm -rf app/build
./gradlew assembleRelease
```

## Size Optimization

Current optimizations:
- ✅ ProGuard enabled
- ✅ Resource shrinking enabled
- ✅ Using Android App Bundle
- ✅ No unused dependencies

Expected APK size: **8-12 MB**
Expected AAB size: **6-10 MB**

## Next Steps After Build

1. Test on multiple devices
2. Check ProGuard doesn't break functionality
3. Verify all features work in release mode
4. Upload to Play Console Internal Testing
5. Test from Play Store
6. Promote to Production when ready
