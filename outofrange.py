import tkinter as Tk
from tkinter import *
from tkinter import messagebox
import label
from label import lab
def outofRange_win():
    outofRange_win=Tk()
    outofRange_win.configure(bg='#ff3131')
    outofRange_win.geometry("500x500")
    outofRange_image=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/outofRange.png",master=outofRange_win)
    lab(outofRange_win,outofRange_image)
    outofRange_win.mainloop()

