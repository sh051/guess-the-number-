import tkinter as Tk
from tkinter import *
import label
from label import lab
import winMusic
def win_win():
    win_window=Tk()
    win_window.configure(bg='#ff3131')
    win_window.geometry("500x500")
    win_image=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/youWIN.png",master=win_window)
    lab(win_window,win_image)
    winMusic.winSound(win_window)
    win_window.mainloop()




