import tkinter as tk
from tkinter import *
from pygame import mixer
def winSound(window):
    mixer.init()
    sound = mixer.Sound("/home/shraddha/Downloads/mixkit-ethereal-fairy-win-sound-2019.wav")
    tk.Button(window, text="click me!", fg='white', font = 'ultra',bg='blue',command=sound.play).place(x=0,y=0)
