import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 26)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
color_list =  [(199, 176, 117), (124, 37, 24), (208, 221, 212), (166, 106, 57), (6, 57, 83), (185, 158, 54), (220, 224, 228), (108, 68, 84), (113, 161, 175), (40, 37, 35), (23, 122, 173), (64, 153, 139), (77, 40, 48), (90, 142, 53), (9, 67, 47), (180, 97, 80), (131, 39, 41), (211, 202, 152), (140, 172, 157), (176, 152, 158), (178, 201, 186), (218, 181, 171), (169, 200, 209), (205, 183, 188)]
