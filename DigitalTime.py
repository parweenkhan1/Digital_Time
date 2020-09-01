import sys
from tkinter import *
from PIL import ImageTk
import time

def times():
    current_time = time.strftime("%H  :  %M  :  %S  ")
    clock_lbl.config(text=current_time,fg='green')
    clock_lbl.after(200,times)





root = Tk()
root.geometry('500x500+450+150')
root.title('SmartClock')
root.iconbitmap('clock.ico')
root.resizable(False,False)
########## IMAGE ###############
bg_image = ImageTk.PhotoImage(file='bg.jpg')
bg_lbl = Label(root,image=bg_image).place(x=0,y=0)

frame_lbl = Frame(root,bg='#e6ffe6')
frame_lbl.place(x=50,y=40,height=300,width=400)

head_lbl = Label(frame_lbl,text='Digital Clock',font=('times new roman',40,'bold'),bg='#e6ffe6',fg='green')
head_lbl.place(x=45,y=10)

title_lbl = Label(frame_lbl,text='hours   minutes   seconds  ',font=('times new roman',25),fg='green',bg='#e6ffe6')
title_lbl.place(x=45,y=100)

clock_lbl = Label(frame_lbl,font=('times new roman',40,'bold'),bg='#e6ffe6')
clock_lbl.place(x=50,y=200)
times()

root.mainloop()