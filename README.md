# Color-Saori
Color Saori Basic made by Teacup/Zdzisiu

requires proxy_ex.dll to run

FUNCTIONS:
- Generating a color image file using RGB:
	argument 1: "color"
	argument 2: height
	argument 3: width
	argument 4: R/Red value
	argument 5: G/Green value
	argument 6: B/Blue value
	argument 7: Alpha value (0-255)
	argument 8: file name (without the file extension)

- Resizing an image:
	argument 1: 
		"resize_org_ratio" - resize keeping the original aspect ratio
		"resize_new_ratio" - resize ignoring the original aspect ratio
	argument 2: file name and path of the file to resize
	argument 3: height
	argument 4: width
	argument 5: file name after resizing (include the file extension ex. .png, .jpg)

- Overlaying image on non-transparent pixels of the base image	
	argument 1: "overlayfast_merge"
	argument 2: base image file name/path
	argument 3: overlay image file name/path
	argument 4: output image name (without the file extension)



examples of usage:

COLOR:
	FUNCTIONEX("proxy_ex.dll", "color.exe", "color", height, width, R, G, B, Alpha (0-255), file name)	

	Generating a color, with size 400x640 and no transparency, the output file is named "yellow.png":
		FUNCTIONEX("proxy_ex.dll","color.exe","color","400","640","255","255","0","255","yellow")

RESIZE:
	FUNCTIONEX("proxy_ex.dll","color.exe","resize_org_ratio"/"resize_new_ratio", file name (and path) to resize, height, height, file name after resize)

	Resizing an image as closely as possible while keeping its aspect ratio and saving it as "cpbra.png":
		FUNCTIONEX("proxy_ex.dll","color.exe","resize_org_ratio","cobra.jpg","400","640","cobra.png")

	Resizing an image ignoring its original aspect ratio and saving it as "cpbra.png" (will most likely result in a distorted image):
		
OVERLAY:
	FUNCTIONEX("proxy_ex.dll","color.exe","overlayfast_merge",base file name/path,overlay file name/path,output file name)

	overlaying heart.png with red.png
		FUNCTIONEX("proxy_ex.dll","color.exe","overlayfast_merge","heart.png","red.png","red_heart")



