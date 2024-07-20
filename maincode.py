import tkinter as tk
from tkinter import *
import random
from pygame import mixer
import time
from time import strftime
import win
from win import win_win
import losing
from losing import lose
import outofrange
from outofrange import outofRange_win
import SPLASHSCREEN
from SPLASHSCREEN import splashScreen
import datetime


root1=Tk()
width= root1.winfo_screenwidth() 
height= root1.winfo_screenheight()
root1.geometry("%dx%d" % (width, height))
root1.configure(bg='#ff3131')


img=PhotoImage(file=r"/home/shraddha/Downloads/guessTheNumber1.png",master=root1)
img_label=Label(root1,image=img)
img_label.place(x=-35,y=0)

text=''
n=1

#sound
mixer.init()
sound = mixer.Sound("/home/shraddha/Downloads/on-the-road-to-the-eighties_59sec-177566.mp3")
tk.Button(root1, text="sound", fg='white', font = 'ultra',bg='blue',command=sound.play).place(x=1770,y=0)


def check(t):
    global n
    if n==5:
        lose()
    elif int(t)==answer:
        win_win()
    elif int(t)>int(range_entry.get()):
        n+=1

        outofRange_win()
    else:
        n+=1
    
    if int(t)<answer:
        textbox1.insert(tk.END,t+'\n')
    if int(t)>answer:
        textbox2.insert(tk.END,t+'\n')
            
def main_win():
    root=Tk()
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    root.geometry("%dx%d" % (width,height))
    root.configure(bg='#ff3131')

    global textbox1
    global textbox2

    textbox1 = Text(root, height = 5, 
                      width = 5, 
                      bg = "blue",
                      font = ("ultra",50),
                      fg = "white")
    textbox2 = Text(root, height = 5, 
                      width = 5, 
                      bg = "blue",
                      font = ("ultra",50),
                      fg = "white")
    textbox1.pack()
    textbox1.place(x = 1000, y = 350)
    textbox2.pack()
    textbox2.place(x = 1460, y = 350)

    lessLabel=Label(root,text="GUESS HIGHER",fg='white',bg='#ff3131',font=('Courier New',20)).place(x=1000,y=250)
    moreLabel=Label(root,text="GUESS LOWER",fg='white',bg='#ff3131',font=('Courier New',20)).place(x=1450,y=250)

   #time
    def time():
        time_str = strftime('%H:%M:%S %p')
        time_label.config(text="Time-"+time_str)
        time_label.after(1000, time)

    time_label=Label(root,fg='white',bg='blue',font=('Courier New',20))
    time_label.place(x=700,y=0)
    time()
        

    def button_press(num):
        global text
        text = text + str(num)
        equation_label.set(text)
        print(text)
        
        
    def clear():
        global text
        equation_label.set("")
        text = ""
    def enter():
        global text
        try:
            total = str(eval(text))
            equation_label.set(total)
            text = total
            check(text)
        except SyntaxError:
            equation_label.set("syntax error")
            text = ""
        except ZeroDivisionError:
            equation_label.set("arithmetic error")
            text = ""
        clear()
    text =""

    equation_label = StringVar()
    label = Label(root, textvariable=equation_label, font=('C059',20), bg="blue", width=24, height=2)
    label.place(x=130,y=100)
   
    canvas = Canvas(root, width = 500, height = 150,bg='red')
    canvas.pack()
    hint_img = PhotoImage(file="/home/shraddha/Pictures/Screenshots/hint1.png")
    canvas.create_image(-10,0, anchor=NW, image=hint_img)
    canvas.place(x=1100,y=20)


    btn1img=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/1-.png")
    btn1=Button(root, image=btn1img,bg="red",activebackground="red",command=lambda: button_press(1))
    btn1.place(x=50,y=250)


    btn2img=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/2-.png")
    btn2=Button(root, image=btn2img,bg="red",activebackground="red",command=lambda: button_press(2))
    btn2.place(x=250,y=250)


    btn3img=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/3-.png")
    btn3=Button(root, image=btn3img,bg="red",activebackground="red",command=lambda: button_press(3))
    btn3.place(x=450,y=250)


    btn4img=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/4-.png")
    btn4=Button(root, image=btn4img,bg="red",activebackground="red",command=lambda: button_press(4))
    btn4.place(x=50,y=400)


    btn5img=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/5-.png")
    btn5=Button(root, image=btn5img,bg="red",activebackground="red",command=lambda: button_press(5))
    btn5.place(x=250,y=400)


    btn6img=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/6-.png")
    btn6=Button(root, image=btn6img,bg="red",activebackground="red",command=lambda: button_press(6))
    btn6.place(x=450,y=400)


    btn7img=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/7-.png")
    btn7=Button(root, image=btn7img,bg="red",activebackground="red",command=lambda: button_press(7))
    btn7.place(x=50,y=550)


    btn8img=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/8-.png")
    btn8=Button(root, image=btn8img,bg="red",activebackground="red",command=lambda: button_press(8))
    btn8.place(x=250,y=550)

    btn9img=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/9-.png")
    btn9=Button(root, image=btn9img,bg="red",activebackground="red",command=lambda: button_press(9))
    btn9.place(x=450,y=550)


    btn10img=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/0-.png")
    btn10=Button(root, image=btn10img,bg="red",activebackground="red",command=lambda: button_press(0))
    btn10.place(x=250,y=700)

    btnclrimg=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/clear.png")
    btnclr=Button(root,image=btnclrimg,bg="red",activebackground="red",command=lambda: clear())
    btnclr.place(x=50,y=700)

    btnenterimg=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/enter.png")
    btnenter=Button(root, image=btnenterimg,bg="red",activebackground="red",command=lambda: enter())
    btnenter.place(x=450,y=700)

    global answer
    answer=random.randint(1,int(range_entry.get()))
    print(answer)

    root.mainloop()

def click():
    win1=Tk()
    win1.geometry("%dx%d" % (width, height))
    win1.configure(bg="#ff3131")

    range_img = PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/enterRange1.png",master=win1)
    range_label=Label(win1,image=range_img,bg='#ff3131')
    global range_entry
    range_entry = tk.Entry(win1,textvariable = IntVar(), font=('C059',20,'normal'),bg='white',fg='blue')
    root1.destroy()
    range_label.place(x=700,y=200)
    range_entry.place(x=750,y=400)
    next_img=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/nextBtn.png",master=win1)
    nextBtn = Button(win1, image=next_img, bd = '5',
                          command = main_win)
    nextBtn.place(x=830,y=500)
    
    win1.mainloop()

def rules():
    rules_win=Tk()
    rules_win.geometry("%dx%d" % (width, height))
    rules_win.configure(bg='#ff3131')
    rules_img=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/rules.png",master=rules_win)
    rules_label=Label(rules_win,image=rules_img,bg="dark red")
    rules_label.place(x=380,y=100)
    letsplay_img=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/letsplay.png",master=rules_win)
    letsplay_btn=Button(rules_win, image=letsplay_img,command=click,bg="dark red",activeforeground = "dark red",activebackground="dark red", pady=10)
    letsplay_btn.place(x=750,y=700)
    #date
    date = datetime.datetime.now()
    labelDate= Label(rules_win, text=f"{date:%A, %B %d, %Y}", font=("Courier New", 20),bg="red",fg='white')
    labelDate.pack(pady=20)
    labelDate.place(x=0,y=0)
    rules_win.mainloop()

presstart_image=PhotoImage(file=r"/home/shraddha/Pictures/Screenshots/pressstart.png",master=root1)
pressstart_btn=Button(root1, image=presstart_image, command=rules,bg="dark red",activeforeground = "dark red",activebackground="dark red", pady=10)
pressstart_btn.place(relx=0.41,rely=0.6)

root1.mainloop()

