import math
from PIL import Image
import qrcode

# ascii_characters = ['.',':','-','=','+','*','#','%','@'] # pos full
ascii_characters = [' ','.',':','-','=','*','#','%','@'] # pos with empty best with black background.
# ascii_characters = ['@','%','#','*','+','=','-',':','.'] # neg full
# ascii_characters = ['@','%','#','*','=','-',':','.',' '] # neg with empty

img = Image.open('image.jpg').convert('L')

#---------------------------------------------------------------#
    # Function to run through the conversion.

def convert(img):
    ratio = aspect_ratio(img)
    new_pix = pixel(ratio)
    ascii_img = formating(new_pix)
    return save(ascii_img)


#---------------------------------------------------------------#
    # Creating the aspect ratio to properly size the image.

new_width = 120
def aspect_ratio(img):
    width , height = img.size
    r = math.gcd(width, height)
    x = int(width / r)
    y = int(height / r)
    ratio = x/y
    new_height = ratio * width * .166
    img = img.resize((new_width, int(new_height)))
    return img

#---------------------------------------------------------------#
    # Changing the pixels into ascii characters

def pixel(img):
    pixels = img.getdata()
    pixel =[]
    for p in pixels:
        new_pix = ascii_characters[p//30]
        pixel.append(new_pix)
    new_pix = ''.join(pixel)
    return new_pix

#---------------------------------------------------------------#
    # Code used for how many ascii characters you need and for how they are selected.

pixels = img.getdata()
a= [p//30 for p in pixels]   
# print(a)
a = list(set(a))
print(a)

#---------------------------------------------------------------#
    # Formats the string of new characters to show it as the image.

def formating(new_pix):
    ascii_img=[]
    for i in range(0, len(new_pix), new_width):
        line = new_pix[i:i + new_width]
        ascii_img.append(line)
    ascii_img = '\n'.join(ascii_img)
    return ascii_img

#---------------------------------------------------------------#
    # Saves to a .txt file.

def save(ascii_img):
    with open("image_pos_emp.html", "w") as f:
        f.write(ascii_img)

#---------------------------------------------------------------#
    # Running the program and conversion to a qrcode.
# convert(img)

#---------------------------------------------------------------#
    # Uploading .txt file to web site.




# qr = qrcode.make("image_pos_emp.html")
# qr.save("qrcode.png")
