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
-Height in inches
    -Example: 5ft 3in = 12in = 1ft, 5*12=60 +3in = 63in
'''
# external library --> Tkinter --> pip install tk
# Tkinter --> tea-kay-inter
# python -m tkinter --> open a window --> Tk interface
# create an instance of the tk.Tk class --> create application window
# main window = root --> can use any name
import os
import tkinter as tk
from tkinter import ttk
from turtle import fillcolor
main_window = tk.Tk()  # --> object
greeting = tk.Label(main_window, text="Hello, Sarde!")
greeting.pack()
# --> change window title
main_window.title('BMI Calculator')  # --> window title
# --> change the size and position of window
# main_window.geometry('300x200')
main_window.geometry('300x200+40+40')

'''
ICON PHOTO --> not working
# icon_photo = tk.PhotoImage(file='icons8-bmi-80.png')
# main_window.iconphoto(False, icon_photo)
main_window.iconbitmap(os.path.dirname(
    os.path.abspath(__file__))+'/icons8-bmi-30.ico')
'''


def calculate_bmi(weight, height):
    # calculate BMi with the weight and heigth entered
    weight = input('Weight: ')
    height = input('Height: ')
    weight = int(weight)
    height = int(height)
    return (weight * 703) / (height * height)


# frame
frame = ttk.Frame(main_window)

# weight label
weight_label = ttk.Label(main_window, text='Weight(lbs)')
weight_label.pack()

# weight entry
weight = tk.StringVar()
weight_entry = ttk.Entry(main_window, textvariable=weight)
weight_entry.pack()

# height label
height_label = ttk.Label(main_window, text='Height(in)')
height_label.pack()

# height_entry
height = tk.StringVar()
height_entry = ttk.Entry(main_window, textvariable=height)
height_entry.pack()

# calculate BMI button


def calculate_bmi_button_clicked():
    # calculate bmi button-click event
    bmi = calculate_bmi(weight, height)
    result = f'Your BMI is {bmi} '
    return result


calculate_bmi_button = ttk.Button(main_window, text='Calculate BMI')
calculate_bmi_button.pack()
calculate_bmi_button.configure(command=calculate_bmi_button_clicked)
# calculate_bmi_button.pack()

# seperator
seperator = ttk.Separator(main_window, orient='horizontal')
seperator.pack(fill='x')

# return calculated BMI to user


# call mainloop method --> keeps the window visible on the screen, until ypu close it
main_window.mainloop()
