from PIL import Image

def resize_org_ratio(path, size, name):
    img = Image.open(path)
    original_width, original_height = img.size
    new_width, new_height = size

    original_ratio = original_width / original_height
    new_ratio = new_width / new_height

    if original_ratio > new_ratio:
        new_height = int(new_width / original_ratio)
    else:
        new_width = int(new_height * original_ratio)

    img = img.resize((new_width, new_height))
    img.save(name)

def resize_new_ratio(path, size, name):
    img = Image.open(path)
    new_width, new_height = size
    img = img.resize((new_width, new_height))
    img.save(name)
