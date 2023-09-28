#%%
from PIL import Image
import PIL
# Location of the image
img = Image.open("/home/nwsk/projects/pillow/geek.png")
img = img.rotate(90, PIL.Image.NEAREST, expand = 1) 
# Flip the original image vertically
vertical_img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
vertical_img.save("vertical.png")
 
vertical_img.show()

# size of the image

print(img.size)
 
# format of the image
print(img.format)

img.show()
# %%
im = Image.open(r"/home/nwsk/projects/pillow/geek.png")
 
# Size of the image in pixels
# (size of original image)
# (This is not mandatory)
width, height = im.size
 
# Setting the points for cropped image
left = 4
top = height / 5
right = 154
bottom = 3 * height / 5
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
newsize = (300, 300)
im1 = im1.resize(newsize)
im1.show()
# %%
size = (40, 40)
img = Image.open(r"/home/nwsk/projects/pillow/geek.png")
 
print("Original size of the image")
print(img.size)
 
# resizing the image
r_img = img.resize(size, resample = Image.BILINEAR)
 
# resized_test.png => Destination_path
r_img.save("resized_test.jpg")
 
# Opening the new image
img = Image.open(r"/home/nwsk/projects/pillow/geek.png")
 
 
print("\nNew size of the image")
print(img.size)
img.show()
# importing Image class from PIL package
from PIL import Image
 
# creating a object
image = Image.open(r"/home/nwsk/projects/pillow/geek.png")
image.load()
 
# Splitting the image into individual
# bands
r, g, b, = image.split()
 
# merge function used
im1 = Image.merge('RGB', (g, b, r))
im1.show()# %%

# %%
import os
print(os.curdir)
# %%
print(os.listdir())
#%%
img_01 = Image.open("/home/nwsk/projects/pillow/digitnumberimg0.jpg")
img_02 = Image.open("/home/nwsk/projects/pillow/digitnumberimg1.jpg")
img_03 = Image.open("/home/nwsk/projects/pillow/digitnumberimg2.jpg")
img_04 = Image.open("/home/nwsk/projects/pillow/digitnumberimg3.jpg")
 
img_01_size = img_01.size
img_02_size = img_02.size
img_03_size = img_02.size
img_02_size = img_02.size
 
print('img 1 size: ', img_01_size)
print('img 2 size: ', img_02_size)
print('img 3 size: ', img_03_size)
print('img 4 size: ', img_03_size)
 
new_im = Image.new('RGB', (2*img_01_size[0],2*img_01_size[1]), (250,250,250))
 
new_im.paste(img_01, (0,0))
new_im.paste(img_02, (img_01_size[0],0))
new_im.paste(img_03, (0,img_01_size[1]))
new_im.paste(img_04, (img_01_size[0],img_01_size[1]))
 
new_im.save("merged_images.png", "PNG")
new_im.show()

# %%
# creating a object
image = Image.open(r"./projects/pillow/stopsign.png")
MAX_SIZE = (100, 100)
 
# Creating the thumbnail
image.thumbnail(MAX_SIZE)
 
image.show()
# %%
im = Image.open(r"./projects/pillow/geek.png")
 
# Size of the image in pixels
# (size of original image)
# (This is not mandatory)
width, height = im.size
 
# Setting the points for cropped image
left = 5
top = height / 4
right = 164
bottom = 3 * height / 4
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
 
# Shows the image in image viewer
im1.show()
# %%
from PIL import ImageFilter
# Opens a image in RGB mode
im = Image.open(r"./projects/pillow/geek.png")
 
# Blurring the image
im1 = im.filter(ImageFilter.BLUR)
 
# Shows the image in image viewer
im1.show()
# %%
# Opens a image in RGB mode
im = Image.open(r"./projects/pillow/geek.png")
 
# Blurring the image
im1 = im.filter(ImageFilter.GaussianBlur(4))
 
# Shows the image in image viewer
im1.show()

# %%
# Blurring the image
im = Image.open(r"./projects/pillow/geek.png")

im1 = im.filter(ImageFilter.BoxBlur(4))
 
# Shows the image in image viewer
im1.show()
# %%
# import all the libraries
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
 
# image opening
image = Image.open(r"./projects/pillow/geek.png")

# creating a copy of original image
watermark_image = image.copy()
 
# Image is converted into editable form using
# Draw function and assigned to draw
draw = ImageDraw.Draw(watermark_image)
 
# ("font type",font size)
font = ImageFont.truetype("/usr/share/fonts/truetype/open-sans/OpenSans-Regular.ttf", 12)
 
# Decide the text location, color and font
# (255,255,255)-White color text
draw.text((0, 0), "GeeksforGeeks", (0, 0, 0), font=font)
 
watermark_image.show()
watermark_image.save('./projects/pillow/watermarked.png')
 
# %%
from PIL import Image, ImageFont, ImageDraw
 
# creating a image object
image = Image.open(r'./projects/pillow/stopsign.png')
 
draw = ImageDraw.Draw(image)
 
# specified font size
font = ImageFont.truetype(r"/usr/share/fonts/truetype/open-sans/OpenSans-Regular.ttf", 15)
 
text = u"""\
Stop
for \n tea!"""
 
# drawing text size
draw.text((6, 8), text, fill ="red", font = font, align ="right")
 
image.show()
# %%
# importing image object from PIL
import math
from PIL import Image, ImageDraw
 
w, h = 220, 190
shape = [(40, 40), (w - 10, h - 10)]
 
# creating new Image object
img = Image.new("RGB", (w, h))
 
# create line image
img1 = ImageDraw.Draw(img)
img1.line(shape, fill=None, width=0)
img.show()
# %%
w, h = 220, 190
shape = [(40, 40), (w - 10, h - 10)]
 
# creating new Image object
img = Image.new("RGB", (w, h))
 
# create rectangle image
img1 = ImageDraw.Draw(img)
img1.rectangle(shape, fill="#ffff33", outline="red")
img.show()
# %%
import math
from PIL import Image, ImageDraw
from PIL import ImagePath
 
side = 9
xy = list([
    ((math.cos(th) + 1) * 90,
     (math.sin(th) + 1) * 60)
    for th in [i * (2 * math.pi) / side for i in range(side)]
])
 
image = ImagePath.Path(xy).getbbox()
size = list(map(int, map(math.ceil, image[2:])))
 
img = Image.new("RGB", size, "#f9f9f9")
img1 = ImageDraw.Draw(img)
img1.polygon(xy, fill="#eeeeff", outline="blue")
img.show()
# %%

print(list(xy))
# %%
# This will import Image and ImageEnhance modules
from PIL import Image, ImageEnhance
 
# Opening Image
im = Image.open(r"./projects/pillow/stopsign.png")
 
# Creating object of Color class
im3 = ImageEnhance.Color(im)
 
# showing resultant image
im3.enhance(10.0).show()
# %%
# Opening Image
im = Image.open(r"./projects/pillow/stopsign.png")
 
# Creating object of Contrast class
im3 = ImageEnhance.Contrast(im)
 
# showing resultant image
im3.enhance(5.0).show()
# %%
# Opening Image
im = Image.open(r"./projects/pillow/stopsign.png")
 
# Creating object of Brightness class
im3 = ImageEnhance.Brightness(im)
 
# showing resultant image
im3.enhance(1.5).show()
# %%
# Opening Image
im = Image.open(r"./projects/pillow/stopsign.png")
 
# Creating object of Sharpness class
im3 = ImageEnhance.Sharpness(im)
 
# showing resultant image
im3.enhance(5.0).show()
# %%
# Importing imagechops for using the invert() method
from PIL import Image, ImageChops
 
# Opening the test image, and saving it's object
img = Image.open('./projects/pillow/sample5.jpg')
 
# Passing the image object to invert() 
inv_img = ImageChops.invert(img)
inv_img.save('./projects/pillow/invsample5.jpg')
# Displaying the output image
inv_img.show()
# %%

img = Image.open('./projects/pillow/invsample5.jpg')
 
# Passing the image object to invert() 
inv_img = ImageChops.invert(img)
inv_img.save('./projects/pillow/invinvsample5.jpg')
# Displaying the output image
inv_img.show()
# %%
# numpy for performing batch processing and elementwise
# matrix operations efficiently
import numpy as np
 
 
# Opening an image, and saving open image object
img = Image.open(r"./projects/pillow/sample5.jpg")
 
# Creating an numpy array out of the image object
img_arry = np.array(img)
 
# Maximum intensity value of the color mode
I_max = 255
 
# Subtracting 255 (max value possible in a given image
# channel) from each pixel values and storing the result
img_arry = I_max - img_arry
 
# Creating an image object from the resultant numpy array
inverted_img = Image.fromarray(img_arry)
 
# Saving the image under the name Image_negative.jpg
inverted_img.save(r"./projects/pillow/Image_negative.jpg")
inverted_img.show()
# %%
from PIL import Image
# open the image
Image1 = Image.open('./projects/pillow/cat1.jpg')

# make a copy the image so that the
# original image does not get affected
Image1copy = Image1.copy()
Image2 = Image.open('./projects/pillow/core.jpg')
Image2copy = Image2.copy()
 
# paste image giving dimensions
Image1copy.paste(Image2copy, (0, 0))
 
# save the image

Image1copy.save('./projects/pillow/pasted2.png')
Image1copy.show()
# %%
Image1 = Image.open('./projects/pillow/cat1.jpg')
 
# make a copy the image so that
# the original image does not get affected
Image1copy = Image1.copy()
Image1 = Image.open('./projects/pillow/core.jpg')
Image2copy = Image2.copy()
 
# paste image giving dimensions
Image1copy.paste(Image2copy, (70, 150))
Image1copy.show()
# save the image
Image1copy.save('./projects/pillow/pasted3.jpg')
# Importing the pillow library's
# desired modules
#%%
from PIL import Image, ImageDraw

# Opening the image (R prefixed to
# string in order to deal with '\'
# in paths)
img = Image.open(R"./projects/pillow/input-image1.png")

# Converting the image to RGB mode
img1 = img.convert("RGB")

# Coordinates of the pixel whose value
# would be used as seed
seed = (3, 70)

# Pixel Value which would be used for
# replacement
rep_value = (255, 255, 0)

# Calling the floodfill() function and
# passing it image, seed, value and
# thresh as arguments
ImageDraw.floodfill(img1, seed, rep_value, thresh=50)

# Displaying the image
img1.show()
# %%
# Open the image by specifying the image path.
image_path = "./projects/pillow/300dpi.png"
image_file = Image.open(image_path)
image_file.show()
# the default
image_file.save("./projects/pillow/95.png", quality=95)
  
# Changing the image resolution using quality parameter
# Example-1
image_file.save("./projects/pillow/25.png", quality=25)
  
# Example-2
image_file.save("./projects/pillow/1.png", quality=1)
img1 = Image.open('./projects/pillow/95.png')
img1.show()
img1 = Image.open('./projects/pillow/25.png')
img1.show()
img1 = Image.open('./projects/pillow/1.png')
img1.show()
# %%
