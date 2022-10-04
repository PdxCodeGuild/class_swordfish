'''Lab 13: Mini Capstone
'''
'''
    -For your final Python project,
    -Build a program that solves a problem or accomplishes a task.
    -Your program needs to utilize an external library (not part of the Python standard library
        - this needs to be something that you pip install).
'''
'''
-Create an application, where the user would enter weight and height
-and BMI would be calculated from the values entered
-BMI = Body Mass Index
-BMI = (weight in pounds * 703) / (height in inches * height in inches)
-Height-entered in inches
'''
# --> TKINTER
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
main_window = Tk()  # GUI --> an object

# --> change the size and position of window
main_window.geometry("350x350+40+40")
# window-title
main_window.title('BMI Calculator')

# --> icon photo
main_window.iconbitmap("tk-0.1.0/icons8-heart-health-50.png")


# image
image = Image.open("tk-0.1.0/balloon_bmi.jpg")
img = image.resize((275, 175))  # --> resized image
photo = ImageTk.PhotoImage(img)
img_label = Label(image=photo,)
img_label.pack()


def calculate_bmi():
    # calculate BMI with the weight and heigth entered
    weight = int(w.get())  # --> gets the output of an entry widget
    height = int(h.get())
    bmi = round((weight * 703) / (height * height), 1)
    label.config(text=bmi)


# weigth widget- user will enter weight
w_label = Label(main_window, text='Weight(lbs)', font=('Calibri 13')).pack()
w = Entry(main_window, width=30)
w.pack()  # --> arranges widgets around the edges of their container(root window, frame)

# heigth widget-user will enter height
h_label = Label(main_window, text='Height(in)', font=('Calibri 13')).pack()
h = Entry(main_window, width=30)
h.pack()

label = Label(main_window, text="Your BMI is: ",
              fg='magenta', font=('Calibri 15'))
label.pack(pady=10)


Button(main_window, text="Calculate BMI",
       bg="magenta", command=calculate_bmi).pack()
main_window.mainloop()
