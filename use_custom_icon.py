#!/usr/bin/env python3
from PIL import Image
import os

# Load the source image
source_path = "/Users/macs/Downloads/ChatGPT Image Jan 11, 2026, 09_35_30 AM.png"
print(f"📥 Loading image: {source_path}")

img = Image.open(source_path)
print(f"✅ Loaded: {img.size[0]}x{img.size[1]}")

# Convert to RGB if needed (remove alpha channel)
if img.mode == 'RGBA':
    background = Image.new('RGB', img.size, (255, 255, 255))
    background.paste(img, mask=img.split()[3])
    img = background

# Create 512x512 for Play Store
print("\n📱 Creating Play Store assets...")
os.makedirs('play_store_assets', exist_ok=True)

icon_512 = img.resize((512, 512), Image.LANCZOS)
icon_512.save('play_store_assets/ic_launcher_512.png', 'PNG', quality=95)
print("  ✅ ic_launcher_512.png (512x512)")

# Create feature graphic (1024x500)
feature_width = 1024
feature_height = 500
feature_img = Image.new('RGB', (feature_width, feature_height), '#1976D2')

# Paste icon on left side
icon_for_feature = img.resize((400, 400), Image.LANCZOS)
feature_img.paste(icon_for_feature, (50, 50))

feature_img.save('play_store_assets/feature_graphic_1024x500.png', 'PNG', quality=95)
print("  ✅ feature_graphic_1024x500.png (1024x500)")

# Create app icons for different densities
print("\n📲 Creating app icons...")
sizes = {
    'mipmap-mdpi': 48,
    'mipmap-hdpi': 72,
    'mipmap-xhdpi': 96,
    'mipmap-xxhdpi': 144,
    'mipmap-xxxhdpi': 192
}

for folder, size in sizes.items():
    icon = img.resize((size, size), Image.LANCZOS)
    path = f'app/src/main/res/{folder}'
    os.makedirs(path, exist_ok=True)
    
    icon.save(f'{path}/ic_launcher.png', 'PNG', quality=95)
    icon.save(f'{path}/ic_launcher_round.png', 'PNG', quality=95)
    print(f"  ✅ {folder} ({size}x{size})")

print("\n🎉 Done! Your custom icon is now used for:")
print("  • App launcher (all screen densities)")
print("  • Play Store listing (512x512)")
print("  • Feature graphic (1024x500)")
