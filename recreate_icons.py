#!/usr/bin/env python3
from PIL import Image
import os

# Source image
source_image = "/Users/macs/Downloads/ChatGPT Image Jan 11, 2026, 09_35_30 AM.png"

# Icon sizes for Android
icon_sizes = {
    'mipmap-mdpi': 48,
    'mipmap-hdpi': 72,
    'mipmap-xhdpi': 96,
    'mipmap-xxhdpi': 144,
    'mipmap-xxxhdpi': 192
}

# Open source image
print(f"Opening source image: {source_image}")
img = Image.open(source_image)
print(f"Source image size: {img.size}, mode: {img.mode}")

# Convert to RGBA if not already
if img.mode != 'RGBA':
    img = img.convert('RGBA')

base_path = "/Users/macs/QR Scan/app/src/main/res"

# Create icons for each density
for folder, size in icon_sizes.items():
    folder_path = os.path.join(base_path, folder)
    os.makedirs(folder_path, exist_ok=True)
    
    # Resize image
    resized = img.resize((size, size), Image.LANCZOS)
    
    # Save both regular and round icons
    ic_launcher_path = os.path.join(folder_path, 'ic_launcher.png')
    ic_launcher_round_path = os.path.join(folder_path, 'ic_launcher_round.png')
    
    resized.save(ic_launcher_path, 'PNG', optimize=True)
    resized.save(ic_launcher_round_path, 'PNG', optimize=True)
    
    print(f"Created {size}x{size} icons in {folder}")

# Create 512x512 Play Store icon
play_store_path = "/Users/macs/QR Scan/play_store_assets"
os.makedirs(play_store_path, exist_ok=True)

play_store_icon = img.resize((512, 512), Image.LANCZOS)
play_store_icon.save(os.path.join(play_store_path, 'ic_launcher_512.png'), 'PNG', optimize=True)
print("Created 512x512 Play Store icon")

print("\n✅ All icons created successfully!")
