import tkinter as tk

import time

total_time = 0 #input("How many seconds? ")
def countdown(total_time):
    while total_time > 0:
        mins = total_time // 60
        secs = total_time % 60
        total_timer = '{:02d}:{:02d}'.format(mins, secs)
        print(total_timer, end="\r") # basically overwrites current line-- makes next line begin at current line
        time.sleep(1)
        total_time -= 1
    print("Done!")
#countdown(int(total_time))

def pomodoro():    
    for i in range(4):
        print("Time to Work!")
        total_time = 5 #25 minutes * 60 seconds to get total seconds
        while total_time > 0:
            mins = total_time // 60
            secs = total_time % 60
            total_timer = '{:02d}:{:02d}'.format(mins, secs)
            print(total_timer, end="\r") # basically overwrites current line-- makes next line begin at current line
            time.sleep(1)
            total_time -= 1
        print("Time for a Break!")

        total_time = 5
        while total_time > 0:
            mins = total_time // 60
            secs = total_time % 60
            total_timer = '{:02d}:{:02d}'.format(mins, secs)
            print(total_timer, end="\r") # basically overwrites current line-- makes next line begin at current line
            time.sleep(1)
            total_time -= 1
        print("Break's Over!")
#pomodoro() 

""" def start_pause():
    if start_button['text'] == 'Start':
        pomodoro()
        start_button['text'] = 'Pause'
    else:
        start_button["text"]= "Start" """
    

#----------UI-------------------------#

window = tk.Tk() #Creates window
frame = tk.Frame(master=window, borderwidth=5)
frame.pack()
label = tk.Label(                  #Create label
    text="Pomodoro Timer",
    fg="white",
    bg="green",
    width=25,
    height=2
)
label.pack() #Smacks label on window



start_button = tk.Button(
    text="Start Timer",
    width=25,
    height=5,
    bg="blue",
    fg="white",
    relief="groove",
    command=pomodoro
)
start_button.pack()





window.mainloop() #CALL LAST -- after creating widgets! Keeps window visible on screen until I close it
#Blocks any code that comes after it until 
#Pomodoro total_timer
#25 minute work, 5 minute break on loop      
