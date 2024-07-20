import tkinter as Tk
from tkinter import *
from tkinter import messagebox
import label
from label import lab
def lose():
    loseW=Tk()
    loseW.configure(bg='#ff3131')
    loseW.geometry("500x500")
    lose_image=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/youLOSE.png",master=loseW)
    lab(loseW,lose_image)
    loseW.mainloop()
