#!/usr/bin/env python3
from PIL import Image, ImageDraw
import os

print("🎨 Creating Play Store assets...")

# Create 512x512 icon for Google Play Store
size = 512
img = Image.new('RGB', (size, size), color='#1976D2')
draw = ImageDraw.Draw(img)

# Draw QR-like grid pattern
cell_size = size // 8
padding = cell_size

# Draw outer border
draw.rectangle([padding, padding, size-padding, size-padding], 
               outline='white', width=12)

# Draw corner squares (like QR code)
corner_size = cell_size * 2
for x, y in [(padding+20, padding+20), 
             (size-padding-corner_size-20, padding+20),
             (padding+20, size-padding-corner_size-20)]:
    draw.rectangle([x, y, x+corner_size, y+corner_size], 
                   outline='white', width=10)
    draw.rectangle([x+20, y+20, x+corner_size-20, y+corner_size-20], 
                   fill='white')

# Draw center pattern
center = size // 2
center_size = 80
draw.rectangle([center-center_size, center-center_size, 
                center+center_size, center+center_size],
               outline='white', width=8)
draw.rectangle([center-center_size+20, center-center_size+20,
                center+center_size-20, center+center_size-20],
               fill='white')

# Save 512x512 for Play Store
os.makedirs('play_store_assets', exist_ok=True)
img.save('play_store_assets/ic_launcher_512.png')
print('✅ Created: play_store_assets/ic_launcher_512.png')

# Create feature graphic 1024x500
feature = Image.new('RGB', (1024, 500), color='#1976D2')
draw_feature = ImageDraw.Draw(feature)

# Add QR icon on left
icon_small = img.resize((300, 300))
feature.paste(icon_small, (80, 100))

# Add text-like rectangles on right (placeholder for text)
for i in range(3):
    y_pos = 150 + i * 60
    width = 400 - i * 50
    draw_feature.rectangle([500, y_pos, 500+width, y_pos+40],
                          fill='white')

feature.save('play_store_assets/feature_graphic_1024x500.png')
print('✅ Created: play_store_assets/feature_graphic_1024x500.png')

# Update existing icons with better design
print("🔄 Updating app icons...")
sizes = {
    'mipmap-mdpi': 48,
    'mipmap-hdpi': 72,
    'mipmap-xhdpi': 96,
    'mipmap-xxhdpi': 144,
    'mipmap-xxxhdpi': 192
}

for folder, icon_size in sizes.items():
    icon = Image.new('RGB', (icon_size, icon_size), color='#1976D2')
    draw_icon = ImageDraw.Draw(icon)
    
    # Scale pattern to icon size
    cell = icon_size // 8
    pad = cell
    
    # Outer border
    draw_icon.rectangle([pad, pad, icon_size-pad, icon_size-pad],
                       outline='white', width=max(2, icon_size//40))
    
    # Corner squares
    corner = cell * 2
    line_width = max(2, icon_size//50)
    for x, y in [(pad+3, pad+3),
                 (icon_size-pad-corner-3, pad+3),
                 (pad+3, icon_size-pad-corner-3)]:
        draw_icon.rectangle([x, y, x+corner, y+corner],
                          outline='white', width=line_width)
        inner_pad = max(3, icon_size//25)
        draw_icon.rectangle([x+inner_pad, y+inner_pad,
                           x+corner-inner_pad, y+corner-inner_pad],
                          fill='white')
    
    # Center
    center = icon_size // 2
    center_size = icon_size // 6
    draw_icon.rectangle([center-center_size, center-center_size,
                        center+center_size, center+center_size],
                       outline='white', width=line_width)
    inner_pad = max(3, icon_size//30)
    draw_icon.rectangle([center-center_size+inner_pad,
                        center-center_size+inner_pad,
                        center+center_size-inner_pad,
                        center+center_size-inner_pad],
                       fill='white')
    
    path = f'app/src/main/res/{folder}'
    icon.save(f'{path}/ic_launcher.png')
    icon.save(f'{path}/ic_launcher_round.png')
    print(f'  ✅ {folder}')

print('\n🎉 Done! Files created:')
print('📁 play_store_assets/')
print('  • ic_launcher_512.png (512x512) - Upload to Play Console')
print('  • feature_graphic_1024x500.png (1024x500) - Feature graphic')
