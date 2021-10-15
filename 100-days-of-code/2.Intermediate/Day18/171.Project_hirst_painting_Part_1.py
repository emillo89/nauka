import colorgram

# Create some colors
colors = colorgram.extract("image.jpg", 30)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    # tuple with rgb values
    rgb_colors.append(new_color)

print(rgb_colors)

# It's copy a list rgb_colors without white colors (white colors we can deleted)
color_list = [ (246, 243, 237), (224, 234, 242), (243, 225, 74), (179, 78, 29), (49, 36, 26), (219, 151, 76), (146, 28, 41), (22, 25, 69), (44, 43, 120), (243, 236, 239), (170, 21, 16), (48, 87, 158), (210, 85, 128), (156, 50, 86), (120, 160, 224), (27, 43, 28), (215, 79, 62), (139, 183, 140), (115, 106, 202), (75, 120, 57), (65, 30, 35), (157, 179, 231), (150, 211, 191), (204, 135, 43), (86, 87, 33), (87, 155, 109), (202, 121, 162), (61, 148, 170), (55, 100, 18)]

