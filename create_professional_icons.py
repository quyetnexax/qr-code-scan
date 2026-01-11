#!/usr/bin/env python3
from PIL import Image, ImageDraw
import os

print("🎨 Creating professional QR Scanner icon...")

def create_gradient_bg(size):
    """Create blue gradient background"""
    img = Image.new('RGB', (size, size), '#1976D2')
    draw = ImageDraw.Draw(img)
    
    # Create gradient from light blue to dark blue
    for y in range(size):
        ratio = y / size
        r = int(100 + (25 - 100) * ratio)
        g = int(181 + (118 - 181) * ratio)
        b = int(246 + (210 - 246) * ratio)
        color = (r, g, b)
        draw.line([(0, y), (size, y)], fill=color)
    
    return img

def draw_qr_code(draw, center_x, center_y, qr_size):
    """Draw simplified QR code pattern"""
    cell = qr_size // 10
    offset_x = center_x - qr_size // 2
    offset_y = center_y - qr_size // 2
    
    # Background white square
    draw.rectangle([offset_x, offset_y, offset_x + qr_size, offset_y + qr_size],
                   fill='white', outline='black', width=2)
    
    # Corner patterns (3 corners)
    corner_size = cell * 3
    corners = [
        (offset_x + cell, offset_y + cell),  # Top left
        (offset_x + qr_size - corner_size - cell, offset_y + cell),  # Top right
        (offset_x + cell, offset_y + qr_size - corner_size - cell),  # Bottom left
    ]
    
    for cx, cy in corners:
        # Outer square
        draw.rectangle([cx, cy, cx + corner_size, cy + corner_size],
                      outline='black', width=max(1, cell//4))
        # Inner square
        inner_margin = cell
        draw.rectangle([cx + inner_margin, cy + inner_margin,
                       cx + corner_size - inner_margin, cy + corner_size - inner_margin],
                      fill='black')
    
    # Random QR pattern in center
    pattern_positions = [
        (5, 2), (6, 2), (5, 3), (7, 3),
        (4, 5), (5, 5), (6, 5), (7, 5),
        (5, 6), (6, 6), (7, 6),
        (4, 7), (6, 7), (7, 7),
    ]
    
    for px, py in pattern_positions:
        x = offset_x + px * cell
        y = offset_y + py * cell
        draw.rectangle([x, y, x + cell - 1, y + cell - 1], fill='black')

def draw_scan_frame(draw, center_x, center_y, frame_size, thickness):
    """Draw white scanning frame corners"""
    corner_len = frame_size // 4
    
    # Top left
    draw.line([(center_x - frame_size//2, center_y - frame_size//2),
               (center_x - frame_size//2 + corner_len, center_y - frame_size//2)],
              fill='white', width=thickness)
    draw.line([(center_x - frame_size//2, center_y - frame_size//2),
               (center_x - frame_size//2, center_y - frame_size//2 + corner_len)],
              fill='white', width=thickness)
    
    # Top right
    draw.line([(center_x + frame_size//2, center_y - frame_size//2),
               (center_x + frame_size//2 - corner_len, center_y - frame_size//2)],
              fill='white', width=thickness)
    draw.line([(center_x + frame_size//2, center_y - frame_size//2),
               (center_x + frame_size//2, center_y - frame_size//2 + corner_len)],
              fill='white', width=thickness)
    
    # Bottom left
    draw.line([(center_x - frame_size//2, center_y + frame_size//2),
               (center_x - frame_size//2 + corner_len, center_y + frame_size//2)],
              fill='white', width=thickness)
    draw.line([(center_x - frame_size//2, center_y + frame_size//2),
               (center_x - frame_size//2, center_y + frame_size//2 - corner_len)],
              fill='white', width=thickness)
    
    # Bottom right
    draw.line([(center_x + frame_size//2, center_y + frame_size//2),
               (center_x + frame_size//2 - corner_len, center_y + frame_size//2)],
              fill='white', width=thickness)
    draw.line([(center_x + frame_size//2, center_y + frame_size//2),
               (center_x + frame_size//2, center_y + frame_size//2 - corner_len)],
              fill='white', width=thickness)

def draw_magnifying_glass(draw, x, y, size):
    """Draw magnifying glass"""
    # Glass circle - blue gradient
    circle_radius = size // 2
    
    # Draw glass with gradient effect (light blue)
    for i in range(circle_radius, 0, -1):
        alpha = int(150 + (255 - 150) * (i / circle_radius))
        color = (100 + i//2, 150 + i//3, 200 + i//4)
        draw.ellipse([x + circle_radius - i, y + circle_radius - i,
                     x + circle_radius + i, y + circle_radius + i],
                    outline=color, width=1)
    
    # Glass inner circle (lighter)
    inner_radius = circle_radius - size//8
    draw.ellipse([x + circle_radius - inner_radius, y + circle_radius - inner_radius,
                 x + circle_radius + inner_radius, y + circle_radius + inner_radius],
                outline='white', width=2)
    
    # Glass rim (dark blue/purple)
    draw.ellipse([x, y, x + size, y + size],
                outline=(60, 80, 140), width=max(2, size//20))
    
    # Handle (green)
    handle_width = size // 4
    handle_length = size // 2
    handle_x = x + size - handle_width
    handle_y = y + size - handle_width
    
    # Draw handle with rotation effect
    for i in range(handle_length):
        offset = int(i * 0.7)
        color_val = int(100 + (180 - 100) * (i / handle_length))
        handle_color = (color_val//2, color_val, color_val//2)
        draw.ellipse([handle_x + offset, handle_y + offset,
                     handle_x + offset + handle_width, handle_y + offset + handle_width],
                    fill=handle_color)

def draw_scan_line(draw, center_x, center_y, qr_size):
    """Draw green scanning laser line"""
    line_y = center_y
    line_width = qr_size - 20
    
    # Bright green center
    for i in range(3):
        alpha = 255 - i * 50
        draw.line([(center_x - line_width//2, line_y + i),
                  (center_x + line_width//2, line_y + i)],
                 fill=(0, 255, 0), width=1)
    
    # Glow effect
    for i in range(10):
        alpha = int(100 * (1 - i/10))
        offset = i + 3
        color = (0, 200 - i*10, 0)
        draw.line([(center_x - line_width//2, line_y + offset),
                  (center_x + line_width//2, line_y + offset)],
                 fill=color, width=1)
        draw.line([(center_x - line_width//2, line_y - offset),
                  (center_x + line_width//2, line_y - offset)],
                 fill=color, width=1)

def create_icon(size, with_magnifier=True):
    """Create complete icon"""
    # Create gradient background
    img = create_gradient_bg(size)
    draw = ImageDraw.Draw(img)
    
    center_x, center_y = size // 2, size // 2 - size // 20
    
    # QR code size
    qr_size = int(size * 0.45)
    
    # Draw scanning frame
    frame_size = int(size * 0.7)
    frame_thickness = max(3, size // 60)
    draw_scan_frame(draw, center_x, center_y, frame_size, frame_thickness)
    
    # Draw QR code
    draw_qr_code(draw, center_x, center_y, qr_size)
    
    # Draw scanning laser line
    draw_scan_line(draw, center_x, center_y, qr_size)
    
    # Draw magnifying glass
    if with_magnifier:
        mag_size = int(size * 0.35)
        mag_x = center_x + qr_size // 3
        mag_y = center_y + qr_size // 3
        draw_magnifying_glass(draw, mag_x, mag_y, mag_size)
    
    return img

# Create 512x512 for Play Store
print("📱 Creating 512x512 icon for Play Store...")
os.makedirs('play_store_assets', exist_ok=True)
icon_512 = create_icon(512, with_magnifier=True)
icon_512.save('play_store_assets/ic_launcher_512.png')
print("✅ Created: play_store_assets/ic_launcher_512.png")

# Create feature graphic
print("🖼️ Creating feature graphic 1024x500...")
feature = create_gradient_bg(1024)
feature_temp = feature.crop((0, 0, 1024, 500))
feature = feature_temp

# Add icon on left
icon_for_feature = create_icon(400, with_magnifier=True)
feature.paste(icon_for_feature, (50, 50))

# Add decorative elements on right
draw_feature = ImageDraw.Draw(feature)
for i in range(3):
    y = 120 + i * 80
    width = 400 - i * 60
    draw_feature.rounded_rectangle([550, y, 550 + width, y + 50],
                                   radius=10, fill=(255, 255, 255, 200))

feature.save('play_store_assets/feature_graphic_1024x500.png')
print("✅ Created: play_store_assets/feature_graphic_1024x500.png")

# Create app icons for different densities
print("📲 Creating app icons...")
sizes = {
    'mipmap-mdpi': 48,
    'mipmap-hdpi': 72,
    'mipmap-xhdpi': 96,
    'mipmap-xxhdpi': 144,
    'mipmap-xxxhdpi': 192
}

for folder, icon_size in sizes.items():
    app_icon = create_icon(icon_size, with_magnifier=(icon_size >= 96))
    path = f'app/src/main/res/{folder}'
    os.makedirs(path, exist_ok=True)
    app_icon.save(f'{path}/ic_launcher.png')
    app_icon.save(f'{path}/ic_launcher_round.png')
    print(f"  ✅ {folder} ({icon_size}x{icon_size})")

print("\n🎉 Done! Professional QR Scanner icons created!")
print("📁 Files ready in:")
print("  • play_store_assets/ic_launcher_512.png")
print("  • play_store_assets/feature_graphic_1024x500.png")
print("  • app/src/main/res/mipmap-*/ic_launcher.png")
