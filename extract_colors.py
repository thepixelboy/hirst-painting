import colorgram

# Extract 6 colors from an image.
rgb_colors = []
colors = colorgram.extract('image.jpg', 36)
for color in colors:
  r = color.rgb.r
  g = color.rgb.g
  b = color.rgb.b

  rgb_colors.append((r, g, b))

print(rgb_colors)