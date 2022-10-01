import tkinter as tk
from tkinter import * #includes messagebox
import time

class Pomodoro:
    def __init__(self, root):
        self.root = root
        
        
    def _time(self, timer):
        #how to display minutes & seconds on GUI
        minutes, seconds = divmod(timer, 60) #divmod(x,y) returns values of x/y as (quotient, remainder) divmod(9,3) // (3,0)
        self.min.set(f"{minutes:02d}")
        self.sec.set(f"{seconds:02d}")
        self.root.update()
        time.sleep(1)
        
    def work_time(self):  
        timer = 25*60 #25 minutes * 60 seconds to get total seconds   
        while timer > 0:
            pomo._time(timer)
            if timer == 0:
                print("Time for your break!")
            timer -=1
    
    

#----------UI-------------------------#
    def main(self):
        self.root = Tk()
        self.root.geometry("365x365")       
        self.root.title("Pomodoro Timer") 
        #self.window = tk.Tk() #Creates window, but if I don't explicitly initialize it, one will be implicitly created when I create widget. But show it anyway.
        
        self.label = tk.Label(                  #Create label
            text="Pomodoro Timer",
            fg="white",
            bg="green",
            width=25,
            height=2,
            
        )
        self.label.pack() #Smacks label on window

        self.start_button = tk.Button(
            text="Start Timer",
            width=25,
            height=5,
            bg="blue",
            fg="white",
            relief="groove",
            command=Pomodoro
        )
        self.start_button.pack()
        
         







        self.root.mainloop() #CALL LAST -- after creating widgets! Keeps window visible on screen until I close it
#Blocks any code that comes after it until 
#Pomodoro timerr
#25 minute work, 5 minute break on loop      
if __name__ == '__main__':
    pomo = Pomodoro(tk.Tk())
    pomo.main()
