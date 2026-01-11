# 🔒 HƯỚNG DẪN GIẢI QUYẾT LỖI PRIVACY POLICY

## ❌ Lỗi hiện tại:
```
Your APK or Android App Bundle is using permissions that require a privacy policy: 
(android.permission.CAMERA)
```

## ✅ GIẢI PHÁP - HOST PRIVACY POLICY

Google Play yêu cầu privacy policy phải được **host công khai** trên web (không chấp nhận trong app).

### 🎯 Các cách host miễn phí:

---

## CÁCH 1: GitHub Pages (Khuyến nghị - Miễn phí & Dễ)

### Bước 1: Tạo GitHub Repository
1. Đăng nhập GitHub: https://github.com
2. Click **"New repository"**
3. Tên repo: `qr-scanner-privacy`
4. Chọn **Public**
5. Check **"Add a README file"**
6. Click **Create repository**

### Bước 2: Upload Privacy Policy
1. Click **"Add file"** → **"Create new file"**
2. Tên file: `privacy-policy.html`
3. Copy nội dung từ file `PRIVACY_POLICY.txt` tôi vừa tạo
4. Bọc trong HTML:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Privacy Policy - Quick QR Scanner</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; line-height: 1.6; }
        h1 { color: #333; }
        h2 { color: #555; margin-top: 30px; }
    </style>
</head>
<body>
    <h1>Privacy Policy for Quick QR Scanner</h1>
    <p><strong>Effective Date:</strong> January 11, 2026</p>
    
    <!-- Copy toàn bộ nội dung từ PRIVACY_POLICY.txt vào đây -->
    
</body>
</html>
```
5. Click **"Commit changes"**

### Bước 3: Enable GitHub Pages
1. Vào **Settings** của repo
2. Chọn **Pages** (sidebar bên trái)
3. Source: **Deploy from a branch**
4. Branch: **main** → folder: **/ (root)**
5. Click **Save**
6. Đợi vài phút

### Bước 4: Lấy URL
URL sẽ có dạng:
```
https://YOUR-USERNAME.github.io/qr-scanner-privacy/privacy-policy.html
```

Dùng URL này để điền vào Google Play Console!

---

## CÁCH 2: Google Sites (Miễn phí)

1. Truy cập: https://sites.google.com
2. Click **"Blank"** để tạo site mới
3. Đặt tên: "QR Scanner Privacy Policy"
4. Copy/paste nội dung từ `PRIVACY_POLICY.txt`
5. Click **Publish** → Chọn URL
6. Copy URL và dùng cho Play Store

---

## CÁCH 3: Pastebin / Gist

**GitHub Gist:**
1. https://gist.github.com
2. Tạo gist mới (public)
3. Paste nội dung privacy policy
4. Click **"Create public gist"**
5. Copy URL

**Pastebin:**
1. https://pastebin.com
2. Paste nội dung
3. Exposure: **Public**
4. Click **"Create New Paste"**
5. Copy URL

---

## CÁCH 4: Nếu bạn có website riêng

Upload file HTML lên hosting của bạn:
```
https://your-domain.com/privacy-policy.html
```

---

## 📝 ĐIỀN VÀO GOOGLE PLAY CONSOLE

Sau khi có URL privacy policy:

1. Vào **Google Play Console**
2. **Store presence** → **Store listing**
3. Tìm phần **"Privacy policy"**
4. Nhập URL: `https://...`
5. Click **Save**

---

## ⚠️ LƯU Ý QUAN TRỌNG

Privacy Policy phải:
- ✅ Được host công khai trên web
- ✅ Có thể truy cập không cần đăng nhập
- ✅ Giải thích rõ cách app dùng camera permission
- ✅ Nói rõ không thu thập dữ liệu cá nhân

File `PRIVACY_POLICY.txt` tôi vừa tạo đã bao gồm đầy đủ nội dung cần thiết cho app QR Scanner!

---

## 🎯 KHUYẾN NGHỊ

**GitHub Pages** là cách tốt nhất vì:
- Miễn phí mãi mãi
- Không giới hạn băng thông
- Uy tín cao
- Dễ update sau này

---

## 📧 NHỚ THAY ĐỔI

Trong privacy policy, thay:
```
Email: [YOUR-EMAIL@example.com]
```
Thành email thật của bạn!

---

Sau khi host xong privacy policy và điền URL vào Play Console, upload lại AAB là OK! 🚀
