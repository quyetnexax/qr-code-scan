#!/bin/bash

echo "🔧 Uninstalling old app..."
~/Library/Android/sdk/platform-tools/adb uninstall com.qrscanner.utility

echo "🧹 Clearing cache..."
~/Library/Android/sdk/platform-tools/adb shell pm clear com.qrscanner.utility 2>/dev/null

echo "📦 Installing new APK..."
~/Library/Android/sdk/platform-tools/adb install -r app/build/outputs/apk/debug/app-debug.apk

echo "✅ Done! Icon should appear correctly now."
