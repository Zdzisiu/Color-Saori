from PIL import Image, ImageDraw
import numpy as np
import math

def create_gradient(colors, direction, size):
    width, height = size
    gradient = Image.new('RGBA', size)
    if direction == "horizontal":
        gradient = create_horizontal_gradient(colors, size, gradient)
    elif direction == "vertical":
        gradient = create_vertical_gradient(colors, size, gradient)
    elif direction == "diagonal_left":
        gradient = diagonal_gradient(colors, size)
    elif direction == "diagonal_right":
        gradient = diagonal_gradient(list(reversed(colors)), size)
        gradient = gradient.transpose(method=Image.FLIP_TOP_BOTTOM)
    return gradient

def create_horizontal_gradient(colors, size, gradient):
    width, height = size
    num_colors = len(colors)
    segment_width = width / (num_colors - 1)
    draw = ImageDraw.Draw(gradient)

    for i in range(num_colors - 1):
        color_start = colors[i]
        color_end = colors[i + 1]

        r_start, g_start, b_start, a_start = color_start
        r_end, g_end, b_end, a_end = color_end

        for j in range(math.floor(segment_width * i), math.ceil(segment_width * (i + 1))):
            ratio = (j - math.floor(segment_width * i)) / segment_width
            r = int((1 - ratio) * r_start + ratio * r_end)
            g = int((1 - ratio) * g_start + ratio * g_end)
            b = int((1 - ratio) * b_start + ratio * b_end)
            a = int((1 - ratio) * a_start + ratio * a_end)

            draw.line([(j, 0), (j, height)], fill=(r, g, b, a))

    return gradient

def create_vertical_gradient(colors, size, gradient):
    width, height = size
    step_size = math.ceil(height / (len(colors) - 1))
    draw = ImageDraw.Draw(gradient)
    for i in range(len(colors) - 1):
        color_start = colors[i]
        color_end = colors[i + 1]
        for y in range(i * step_size, min((i + 1) * step_size, height)):
            ratio = (y - i * step_size) / step_size
            r = int(color_start[0] * (1 - ratio) + color_end[0] * ratio)
            g = int(color_start[1] * (1 - ratio) + color_end[1] * ratio)
            b = int(color_start[2] * (1 - ratio) + color_end[2] * ratio)
            a = int(color_start[3] * (1 - ratio) + color_end[3] * ratio)
            for x in range(width):
                gradient.putpixel((x, y), (r, g, b, a))
    return gradient

def diagonal_gradient(colors, size):
    width, height = size
    gradient = Image.new('RGBA', size)
    draw = ImageDraw.Draw(gradient)
    num_colors = len(colors)
    steps = max(width, height) * 2
    for i in range(steps):
        # Calculate position and color at current step
        pos = 1.0 * i / steps
        color_idx = int(pos * (num_colors - 1))
        color_left = colors[color_idx]
        color_right = colors[color_idx + 1] if color_idx < num_colors - 1 else color_left
        color = [
            int(color_left[c] + (color_right[c] - color_left[c]) * (pos * (num_colors - 1) - color_idx))
            for c in range(4)
        ]
        x0, y0 = (0, i)
        x1, y1 = (i, 0)
        draw.line((x0, y0, x1, y1), tuple(color))
    return gradient

def gradient(name,size,direction,colors):
    image=create_gradient(colors,direction,size)
    image.save(name+'.png')
    return image

##print(gradient("horizontal",(200, 200),"horizontal",((0, 0, 255,255),(75, 0, 130,150),(238, 130, 238,50),(255, 192, 203,0))))
##print(gradient("vertical",(200, 200),"vertical",((0, 0, 255,255),(75, 0, 130,150),(238, 130, 238,50),(255, 192, 203,0))))
##print(gradient("diagonal_right",(200, 200),"diagonal_right",((0, 0, 255,255),(75, 0, 130,150),(238, 130, 238,50),(255, 192, 203,0))))
##print(gradient("diagonal_left",(200, 200),"diagonal_left",((0, 0, 255,255),(75, 0, 130,150),(238, 130, 238,50),(255, 192, 203,0))))
