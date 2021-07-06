from tkinter import *
from time import strftime

clock = Tk()
clock.title("Digital Clock")

lbl = Label(clock, font="arial 160 bold", bg="black",fg="white")
lbl.pack(anchor="center", fill="both", expand="yes")

def time():
    string = strftime(" %H:%M:%S %p")
    lbl.config(text=string)
    lbl.after(100,time)

time()
mainloop()