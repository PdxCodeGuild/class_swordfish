'''Lab 13: Mini Capstone
'''
'''
    -For your final Python project, 
    -Build a program that solves a problem or accomplishes a task. 
    -Your program needs to utilize an external library (not part of the Python standard library 
        - this needs to be something that you pip install).
'''
# external library --> Tkinter --> pip install tk
# Tkinter --> tea-kay-inter
# python -m tkinter --> open a window --> Tk interface
# create an instance of the tk.Tk class --> create application window
# main window = root --> can use any name
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import os
main_window = tk.Tk()  # --> object

greeting = tk.Label(main_window, text="Hello, Sarde!")
greeting.pack()

# --> change window title
main_window.title('Tkinter BMI Calculator')  # --> window title
# --> change the size and position of window
main_window.geometry('600x400+50+50')
'''
ICON PHOTO --> not working
#icon_photo = tk.PhotoImage(file='icons8-bmi-80.png')
#main_window.iconphoto(False, icon_photo)
main_window.iconbitmap(os.path.dirname(
    os.path.abspath(__file__))+'/icons8-bmi-30.ico')
'''

'''
ENTRY WIDGETS
weight_entry = user will enter weight
weight_textbox = tk.Entry(main_window, weight)
height_entry = user will enter height
height_textbox = tk.Entry(main_window, height)
'''
# call mainloop method --> keeps the window visible on the screen, until ypu close it
main_window.mainloop()
