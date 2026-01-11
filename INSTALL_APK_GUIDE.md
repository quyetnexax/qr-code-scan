# 📱 Cài đặt APK lên máy test

## File APK đã sẵn sàng:
📍 **Location**: `/Users/macs/QR Scan/app/build/outputs/apk/debug/app-debug.apk`
📊 **Size**: 26 MB

---

## 🔧 Cách 1: Cài qua USB (Android Phone)

### Bước 1: Bật Developer Mode
1. Mở **Settings** trên điện thoại
2. Vào **About Phone**
3. Nhấn 7 lần vào **Build Number**
4. Quay lại Settings → **Developer Options**
5. Bật **USB Debugging**

### Bước 2: Kết nối và cài
```bash
# Kết nối điện thoại qua USB
cd "/Users/macs/QR Scan"

# Tìm adb (Android Debug Bridge)
~/Library/Android/sdk/platform-tools/adb devices

# Cài APK
~/Library/Android/sdk/platform-tools/adb install -r app/build/outputs/apk/debug/app-debug.apk
```

---

## 📤 Cách 2: Gửi APK qua Email/AirDrop

### Email:
1. Gửi file `app-debug.apk` cho chính bạn
2. Mở email trên điện thoại Android
3. Tải và cài APK
4. Cho phép "Install from unknown sources"

### AirDrop (nếu có Mac):
1. AirDrop file APK cho chính mình
2. Lưu vào Google Drive/Dropbox
3. Tải về điện thoại Android và cài

---

## ☁️ Cách 3: Qua Google Drive

```bash
# Upload lên Drive (nếu có gdrive CLI)
# Hoặc kéo thả file vào drive.google.com
```

1. Upload `app-debug.apk` lên Google Drive
2. Mở Drive trên điện thoại Android
3. Tải xuống và cài đặt

---

## 📱 Cách 4: Android Emulator (Android Studio)

```bash
# Mở Android Studio
open -a "Android Studio"

# Hoặc dùng command line:
~/Library/Android/sdk/emulator/emulator -list-avds
~/Library/Android/sdk/emulator/emulator -avd Pixel_5_API_34 &

# Sau khi emulator mở:
~/Library/Android/sdk/platform-tools/adb install app/build/outputs/apk/debug/app-debug.apk
```

---

## ✅ Sau khi cài xong:

1. Mở app "QR Scanner" trên điện thoại
2. Cho phép quyền Camera
3. Test quét QR code
4. Chụp screenshots đẹp:
   - Main screen (camera quét)
   - Quét thành công (kết quả)
   - History screen
   - Settings screen

### Chụp screenshot:
- **Samsung**: Volume Down + Power
- **Google Pixel**: Power + Volume Down
- **Xiaomi**: Volume Down + Menu button

---

## 🚀 Quick Test Checklist:

- [ ] App mở được
- [ ] Camera hoạt động
- [ ] Quét QR code thành công
- [ ] Rung khi quét xong
- [ ] Copy to clipboard
- [ ] History mở được
- [ ] Settings mở được
- [ ] Privacy Policy hiển thị
- [ ] UI đẹp, không lỗi
- [ ] Chụp 4-8 screenshots

---

APK file đã mở trong Finder! Chọn cách cài phù hợp nhất với bạn! 📲
