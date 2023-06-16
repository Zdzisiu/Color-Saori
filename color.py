from PIL import Image
import numpy as np
import math

def make_color_png(size, color, name):
    image = Image.new("RGBA", size, color)
    return image.save(name + '.png')

def rand_color(num=1):
    colors = np.random.randint(0, 256, (num, 3)).tolist()
    return tuple(colors[0]) if num == 1 else tuple(colors[::3])

def find_light_shadow(color, num_shadows=1, num_lights=1, shadow_factor=3, light_factor=3):
    shadow_colors = []
    light_colors = []

    max_index = np.argmax(color)
    min_index = np.argmin(color)
    mid_index = 3 - max_index - min_index

    for i in range(1, num_shadows + 1):
        shadow = [0] * 3
        shadow[max_index] = int(color[max_index] - shadow_factor * i * 20)
        shadow[mid_index] = int(color[mid_index] - shadow_factor * i * 30)
        shadow[min_index] = int(color[min_index] - shadow_factor * i * 40)

        shadow = [max(0, component) for component in shadow]
        shadow = [min(255, component) for component in shadow]

        shadow_colors.append(tuple(shadow))

    for i in range(1, num_lights + 1):
        light = [0] * 3
        light[max_index] = int(color[max_index] + light_factor * i * 20)
        light[mid_index] = int(color[mid_index] + light_factor * i * 30)
        light[min_index] = int(color[min_index] + light_factor * i * 40)

        light = [max(0, component) for component in light]
        light = [min(255, component) for component in light]

        light_colors.append(tuple(light))

    return tuple(shadow_colors[::-1] + [color] + light_colors)
