from tkinter import *

import time


root = Tk()
root.title("Digital Clock")
root.geometry("500x200")

clock = Label(
    root,
    text= "Clock",
    font = ("Helevetica", 50),
    pady= 50
    )
clock.pack()


def tick():
    global current_time_previous
    current_time_previous = "0"
    current_time = time.strftime("%H:%M:%S")
    
    if current_time_previous != current_time:
        current_time_previous = current_time
        clock.config(text = current_time)

    clock.after(200, tick)
tick()




root.mainloop()