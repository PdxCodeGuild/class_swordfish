# from cgi import test
# from turtle import width
from PIL import Image

ascii_characters = ['.',':','-','=','+','*','#','%','@']
img = Image.open('test_image4.jpg').convert('L')

        # Creating the aspect ratio to properly size the image.
# def aspect_ratio(img):
#     height, width = img.size
#     asp_rat = height/width
#     width = 120
#     height = asp_rat * width * 0.55
#     img = img.resize((width, int(height)))
width, height = img.size
asp_rat = height/width
n_width = 120
n_height = asp_rat * n_width * 0.55
img = img.resize((n_width, int(n_height)))

        # Changing the pixels into ascii characters
def pixel():
    pixels = img.getdata()
    pixel =[]
    for p in pixels:
        new_pix = ascii_characters[p//30]
        pixel.append(new_pix)
    new_pix = ''.join(pixel)
# pixels = img.getdata()
# pixel =[]
# for p in pixels:
#     new_pix = ascii_characters[p//30]
#     pixel.append(new_pix)
# new_pix = ''.join(pixel)

# a= [p//25 for p in pixels]    Code used for how many ascii characters you need and for how they are selected.
# a = list(set(a))
# print(a)

def formating():
    for i in range(0, len(pixel()), n_width):

   


# print(new_pix)

# print(ascii_characters)
