from tkinter import *
from tkcalendar import *

root = Tk()
root.title("Calendar")
root.geometry("600x400")

cal = Calendar(root, year=2021, month=1 , day=5)
cal.pack(pady=60)

root.mainloop()