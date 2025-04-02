#Write a Python program to convert a color image to a black-and-white image.

from PIL import Image
image = Image.open("color_image.jpg")  
bw_image = image.convert("L")  
bw_image.save("bw_image.jpg")  
bw_image.show()  