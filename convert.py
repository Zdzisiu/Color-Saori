import colorsys

def rgb_to_hsv(rgb):
    r, g, b = rgb
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
    return int(h * 360), int(s * 100), int(v * 100)

def hsv_to_rgb(hsv):
    h, s, v = hsv
    r, g, b = colorsys.hsv_to_rgb(h / 360, s / 100, v / 100)
    return int(r * 255), int(g * 255), int(b * 255)

def rgb_to_hex(rgb):
    ''' [255,255,255] -> "#FFFFFF" '''
    return '#' + ''.join(f'{v:02x}' for v in rgb)

def hex_to_rgb(hex):
    ''' "#FFFFFF" -> [255,255,255] '''
    return [int(hex[i:i+2], 16) for i in range(1, 6, 2)]

def hsv_to_hex(hsv):
    ''' [360, 100, 100] -> "#FFFFFF" '''
    rgb = hsv_to_rgb(hsv)
    return rgb_to_hex(rgb)

def hex_to_hsv(hex):
    ''' "#FFFFFF" -> [360, 100, 100] '''
    rgb = hex_to_rgb(hex)
    return rgb_to_hsv(rgb)
