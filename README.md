# QR Scanner - Android App

A simple, fast, and privacy-focused QR code scanner for Android.

## Features

✅ **Fast QR Code Scanning** - Instantly scan QR codes and barcodes using ML Kit
✅ **Simple & Clean UI** - Material Design 3 with intuitive interface
✅ **Privacy First** - No ads, no tracking, all data stored locally
✅ **History Management** - Keep track of your scanned codes
✅ **Vibration Feedback** - Haptic response on successful scans
✅ **Clipboard Support** - Easily copy scan results

## Technical Specifications

- **Minimum SDK**: 24 (Android 7.0)
- **Target SDK**: 34 (Android 14)
- **Language**: Kotlin
- **Architecture**: MVVM (ready for expansion)
- **Scanning Engine**: Google ML Kit Barcode Scanning
- **Camera**: CameraX

## Supported Formats

- QR Code
- Data Matrix
- Aztec
- EAN-13
- EAN-8
- UPC-A
- UPC-E
- Code-39
- Code-93
- Code-128
- ITF
- Codabar
- PDF417

## Build Instructions

1. Clone the repository
2. Open in Android Studio (Hedgehog or later)
3. Sync Gradle files
4. Run on device or emulator

```bash
./gradlew assembleRelease
```

## Permissions

- **CAMERA** - Required for scanning QR codes
- **VIBRATE** - Provides haptic feedback on scan
- **INTERNET** - For opening web links from scanned codes (optional)

## Privacy Policy

This app:
- ✅ Stores all data locally on device
- ✅ Does not collect user information
- ✅ Does not use analytics or tracking
- ✅ Does not display ads
- ✅ Does not require login

Full privacy policy available in app settings.

## Google Play Compliance

This app is designed to meet Google Play requirements:
- ✅ Target API 34
- ✅ Privacy Policy included
- ✅ Proper permissions declared
- ✅ Data safety declarations ready
- ✅ No dangerous permissions
- ✅ No ad networks (for initial version)
- ✅ User-facing functionality (genuine utility)

## License

This project is provided as-is for educational and commercial purposes.

## Support

For issues or questions, please use the GitHub issues section.

---

**Version**: 1.0.0
**Last Updated**: January 2026
