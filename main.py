from PIL import Image, ImageDraw
from sys import argv
import color
import palette
import gradient
import overlay
import resize

result = ""
command = argv[1].lower()

# Generating a color filled png
if command == "color":
    if len(argv) < 9:
        result = "Error: Not enough arguments for the 'color' command"
    else:
        height, width, R, G, B, A = map(int, argv[2:8])
        name = argv[8]
        result = color.make_color_png((height, width), (R, G, B, A), name)
    #color 200 200 255 0 255 255 color
# Resizing an image keeping the original ratio
elif command == "resize_org_ratio":
    if len(argv) < 6:
        result = "Error: Not enough arguments for the 'resize_org_ratio' command"
    else:
        org_img_path, height, width, new_img_name = argv[2:6]
        height, width = int(height), int(width)
        result = resize.resize_org_ratio(org_img_path, (height, width), new_img_name)
    #resize_org_ratio 0.png 10 15 org.png
# Resizing an image regardless of ratio
elif command == "resize_new_ratio":
    if len(argv) < 6:
        result = "Error: Not enough arguments for the 'resize_new_ratio' command"
    else:
        org_img_path, height, width, new_img_name = argv[2:6]
        height, width = int(height), int(width)
        result = resize.resize_new_ratio(org_img_path, (height, width), new_img_name)
    #resize_new_ratio 0.png 10 15 new.png
# Overlay an image on to all non-transparent pixels of the base image
elif command == "overlayfast_merge":
    if len(argv) < 5:
        result = "Error: Not enough arguments for the 'overlayfast_merge' command"
    else:
        base_img_path, overlay_img_path, new_img_name = argv[2:5]
        result = overlay.overlayfast_merge(base_img_path, overlay_img_path, new_img_name)
    #overlayfast_merge 0.png color.png overlay
# Generata a gradient
elif command == "gradient":
    if len(argv) < 6:
        result = "Error: Not enough arguments for the 'gradient' command"
    else:
        name,height,width,direction=argv[2:6]
        height,width=int(height),int(width)
        arg_num=len(argv)
        colors=[list(map(int ,argv[i:i+4])) for i in range(6,arg_num ,4)]
        result=gradient.gradient(name,(height,width),direction ,colors)
    #gradient vertical 200 200 vertical 255 0 255 255 0 0 255 255
    #gradient horizontal 200 200 horizontal 255 0 255 255 0 0 255 255
    #gradient diagonal_right 200 200 diagonal_right 255 0 255 255 0 0 255 255
    #gradient diagonal_left 200 200 diagonal_left 255 0 255 255 0 0 255 255
# Make a random color palette
elif command == "random_color_palette":
    if len(argv) > 4:
        type_ = argv[2]
        size = int(argv[3])
        params = list(map(float ,argv[4:]))
        result = palette.generate_palette(type_,size = size,other_params=params)
    elif len(argv) > 3:
        type_ = argv[2]
        size = int(argv[3])
        result = palette.generate_palette(type_,size = size)
        #palette.generate_palette_image((200,200),"random_color_paletteTest",result)
    elif len(argv) > 2:
        type_ = argv[2]
        result = palette.generate_palette(type_)
    else:
        result = "Error: Not enough arguments for the 'random_color_palette' command"
    #random_color_palette monochromatic 4 0.1 0.5
    #random_color_palette complementary
    #random_color_palette analogous 5 0.05
    #random_color_palette split-complementary
    #random_color_palette triadic
    #random_color_palette tetradic
    #random_color_palette random 4
    #palette.generate_palette_image((200,200),"random_color_paletteTest_" + type_,result)
# Make a palette based on a given color
elif command == "custom_color_palette":
    if len(argv) > 7:
        type_ = argv[2]
        R, G, B = map(int, argv[3:6])
        size=int(argv[6])
        params = list(map(float ,argv[7:]))
        result = palette.generate_palette(type_,(R, G, B),size,other_params=params)
        #random_color_palette monochromatic 4 0.1 0.5
        #palette.generate_palette_image((200,200),"random_color_paletteTest",result)
    elif len(argv) > 6:
        type_ = argv[2]
        R, G, B = map(int, argv[3:6])
        size=int(argv[6])
        result=palette.generate_palette(type_,(R, G, B),size)
    elif len(argv) > 5:
        type_ = argv[2]
        R, G, B = map(int, argv[3:6])
        result=palette.generate_palette(type_,(R, G, B))
    else:
        result = "Error: Not enough arguments for the 'custom_color_palette' command"
    #custom_color_palette monochromatic 255 0 255 4 0.1 0.5
    #custom_color_palette complementary 255 0 255
    #custom_color_palette analogous 255 0 255 5 0.05
    #custom_color_palette split-complementary 255 0 255
    #custom_color_palette triadic 255 0 255
    #custom_color_palette tetradic 255 0 255
    #custom_color_palette random 255 0 255 4
    #palette.generate_palette_image((200,200),"custom_color_paletteTest_" + type_,result)
# Generate lights and shadows for a given color
elif command == "shadow_light":
    if len(argv) > 8:
        R, G, B, shadow_num, light_num= map(int ,argv[2:7])
        shadow_factor ,light_factor= map(float ,argv[7:9])
        result=color.find_light_shadow((R,G,B),shadow_num ,light_num ,shadow_factor ,light_factor)
    elif len(argv) > 7:
        R, G, B, shadow_num, light_num= map(int ,argv[2:7])
        shadow_factor = float(argv[7])
        result=color.find_light_shadow((R,G,B),shadow_num ,light_num ,shadow_factor)
    elif len(argv) > 6:
        R, G, B, shadow_num, light_num= map(int ,argv[2:7])
        result=color.find_light_shadow((R,G,B), shadow_num, light_num)
    elif len(argv) > 5:
        R,G,B ,shadow_num= map(int ,argv[2:6])
        result=color.find_light_shadow((R,G,B),shadow_num)
    elif len(argv) > 4:
        R,G,B= map(int ,argv[2:5])
        result=color.find_light_shadow((R,G,B))
    else:
        result = "Error: Not enough arguments for the 'shadow_light' command"
    #shadow_light 255 0 255
    #palette.generate_palette_image((200,200),"shadow_light__test_1",result)
# Generate an color palette image
elif command == "palette_image":
    if len(argv) < 9:
        result = "Error: Not enough arguments for the 'palette_image' command"
    else:
        arg_num = len(argv)
        height, width = map(int, argv[2:4])
        name = argv[4]
        colors = [(int(argv[i]), int(argv[i+1]), int(argv[i+2]), int(argv[i+3])) for i in range(5, arg_num, 4)]
        result = palette.generate_palette_image((height, width), name, colors)
    #palette_image 200 200 palette 255 0 255 235 40 225 119 75 119
elif command == "batch_resize":
    for x in range(1, 7):
        result = resize.resize_org_ratio("letter/letter (" + str(x) + ").png", (60, 60), "letter/letter (" + str(x) + ").png")
# Print the result
if result != "":
    print(result)
else:
    print(-1)
