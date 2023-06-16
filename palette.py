from PIL import Image, ImageDraw
import color
import colorsys
import numpy as np
import random

def rand_color(num=1):
    colors = np.random.randint(0, 256, (num, 3)).tolist()
    return tuple(colors[0]) if num == 1 else tuple(colors)

def generate_range_values(start, end, size):
    step = (end - start) / (size - 1)
    values = [start + i * step for i in range(size)]
    return values

def generate_hue_values(start, delta, size):
    values = [(start + i * delta) % 1 for i in range(size)]
    return values

def generate_complimentary_palette(colors=None):
    if colors is None:
        colors = rand_color()
    R, G, B = colors
    cR = 255 - R
    cG = 255 - G
    cB = 255 - B
    palette = (colors, (cR,cG,cB))
    return palette

def generate_monochromatic_palette(base_color=None, size=5, saturation_range=(0.2, 1.0), value_range=(0.2, 1.0)):
    if base_color is None:
        base_color = rand_color()
    if saturation_range is None:
        saturation_range = (0.2, 1.0)
    if value_range is None:
        value_range = (0.2, 1.0)
        
    hue, _, value = colorsys.rgb_to_hsv(*base_color)
    value_min, value_max = value_range
    if random.randint(0, 1) == 0:
        saturation_min, saturation_max = saturation_range
        saturation_values = generate_range_values(saturation_max, saturation_min, size)
    else:
        saturation_min, saturation_max = saturation_range[::-1]
        saturation_values = generate_range_values(saturation_min, saturation_max, size)

    value_values = generate_range_values(value_min, value_max, size)

    palette = [tuple(round(c * 255) for c in colorsys.hsv_to_rgb(hue, s, v)) for s, v in zip(saturation_values, value_values)]
    return [base_color] + palette


def generate_analogous_palette(base_color=None, num_colors=2, hue_delta=0.1):
    if base_color is None:
        base_color = rand_color()
    if hue_delta is None:
        hue_delta = 0.1
    hue, saturation, value = colorsys.rgb_to_hsv(*base_color)
    palette = []
    left = []
    for _ in range(round(num_colors/2)):
        hue = (hue - hue_delta) % 1
        color = tuple(round(c) for c in colorsys.hsv_to_rgb(hue, saturation, value))
        left.append(color)
    left.reverse()
    palette.extend(left)
    palette.append(base_color)

    hue, saturation, value = colorsys.rgb_to_hsv(*base_color)

    for _ in range(round(num_colors/2)):
        hue = (hue + hue_delta) % 1
        color = tuple(round(c) for c in colorsys.hsv_to_rgb(hue, saturation, value))
        palette.append(color)

    return palette

def split_complementary_palette(base_color=None):
    if base_color is None:
         base_color = rand_color()
         
    hue,saturation,value=colorsys.rgb_to_hsv(*base_color)
    
    hue1=(hue-150/360)%1
    hue2=(hue+150/360)%1
    
    rgb1=tuple(round(c) for c in colorsys.hsv_to_rgb(hue,saturation,value))
    
    rgb2=tuple(round(c) for c in colorsys.hsv_to_rgb(hue1,saturation,value))
    
    rgb3=tuple(round(c) for c in colorsys.hsv_to_rgb(hue2,saturation,value))
    
    return [rgb2]+[rgb1]+[rgb3]

def generate_triadic_palette(base_color=None):
    if base_color is None:
        base_color = rand_color()
    r,g,b=base_color
    
    r,g,b=r/255.0,g/255.0,b/255.0
    
    h,s,v=colorsys.rgb_to_hsv(r,g,b)
    
    h1=(h+1/3)%1
    h2=(h+2/3)%1
    
    r1,g1,b1=colorsys.hsv_to_rgb(h1,s,v)
    
    r2,g2,b2=colorsys.hsv_to_rgb(h2,s,v)
    
    return [base_color]+[(int(r*255),int(g*255),int(b*255)) for r,g,b in [(r1,g1,b1),(r2,g2,b2)]]

def generate_tetradic_palette(base_color=None):
    if base_color is None:
        base_color = rand_color()
    r,g,b=base_color
    
    r,g,b=r/255.0,g/255.0,b/255.0
    
    h,s,v=colorsys.rgb_to_hsv(r,g,b)
    
    h1=(h+0.25)%1
    h2=(h+0.5)%1
    h3=(h+0.75)%1
    
    r1,g1,b1=colorsys.hsv_to_rgb(h1,s,v)
    
    r2,g2,b2=colorsys.hsv_to_rgb(h2,s,v)
    
    r3,g3,b3=colorsys.hsv_to_rgb(h3,s,v)
    
    return [base_color]+[(int(r*255),int(g*255),int(b*255)) for r,g,b in [(r1,g1,b1),(r2,g2,b2),(r3,g3,b3)]]


def generate_palette(palette_type, base_color=None, size=2, other_params=None):
    hue_delta = None
    saturation_range = None
    value_range = None
    
    if other_params is not None:
        if len(other_params) > 0 and palette_type == "analogous":
            hue_delta = other_params[0]
        elif len(other_params) > 2 and palette_type == "monochromatic":
            saturation_range, value_range = (other_params[0],other_params[1]),(other_params[2],other_params[3])
        elif len(other_params) > 0 and palette_type == "monochromatic":
            saturation_range = (other_params[0],other_params[1])

    palette_generators = {
        "complementary": (generate_complimentary_palette, [base_color]),
        "analogous": (generate_analogous_palette, [base_color, size, hue_delta]),
        "monochromatic": (generate_monochromatic_palette, [base_color, size, saturation_range, value_range]),
        "split-complementary": (split_complementary_palette, [base_color]),
        "triadic": (generate_triadic_palette, [base_color]),
        "tetradic": (generate_tetradic_palette, [base_color]),
        "random": (rand_color, [size]),
    }

    colors = []
    if palette_type in palette_generators:
        generator_func, params = palette_generators[palette_type]
        colors = generator_func(*params)
    return colors

def generate_palette_image(size, name, colors):
    width = size[0]
    stripe_width = width // len(colors)
    
    image = Image.new("RGBA", size)
    
    for i in range(len(colors)):
        x0 = i * stripe_width
        x1 = (i + 1) * stripe_width
        y0 = 0
        y1 = size[1]
        
        stripe = Image.new("RGBA", (stripe_width, size[1]), colors[i])
        image.paste(stripe, (x0, y0, x1, y1))
    
    image.save(name+'.png')

    return image
