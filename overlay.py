from PIL import Image, ImageDraw

def overlayfast_merge(base_path, overlay_path, name):
    base_img = Image.open(base_path).convert("RGBA")
    overlay_img = Image.open(overlay_path).convert("RGBA")
    result_img = Image.new("RGBA", base_img.size)

    base_pixels = base_img.load()
    overlay_pixels = overlay_img.load()
    result_pixels = result_img.load()

    for x in range(base_img.width):
        for y in range(base_img.height):
            base_pixel = base_pixels[x, y]
            if base_pixel[3] == 0:
                result_pixels[x, y] = base_pixel
            else:
                overlay_pixel = overlay_pixels[x, y]
                alpha = overlay_pixel[3] / 255.0
                new_pixel = (
                    int((1 - alpha) * base_pixel[0] + alpha * overlay_pixel[0]),
                    int((1 - alpha) * base_pixel[1] + alpha * overlay_pixel[1]),
                    int((1 - alpha) * base_pixel[2] + alpha * overlay_pixel[2]),
                    base_pixel[3]
                )
                result_pixels[x, y] = new_pixel

    result_img.save(name + ".png")
