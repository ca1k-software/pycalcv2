#-------------------------------------------------------------------------------
# Name:        main
# Purpose:     switches between calculator windows
#
# Author:      CA1K
#
# Created:     17/02/2019
#-------------------------------------------------------------------------------

#import(s)
import os
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#variables
ti = "PyCalc v2"
tl = "Choose a type of calculator."
tb1 = "Scientific"
tb2 = "Graphing"
tb3 = "Statistic"
bw = 15 #button width
mode = -1 #variable that determines the switching between the calculator apps

def cm(v,w): #changes the mode and closes the window
    global mode
    mode = v
    w.destroy()

def wc(): #the window that changes the mode
    t = tk.Tk()
    t.resizable(0,0)
    t.title(ti)
    i = ImageTk.PhotoImage(Image.open('derivatest.png').resize((888,450),Image.ANTIALIAS))
    l = Label(t,image=i)
    l.pack(fill=tk.X)
    b1 = Button(t,text=tb1,width=bw,bg="#111",fg="white",command=lambda:cm(0,t))
    b1.pack(fill=tk.X)
    b2 = Button(t,text=tb2,width=bw,bg="#222",fg="white",command=lambda:cm(1,t))
    b2.pack(fill=tk.X)
    b3 = Button(t,text=tb3,width=bw,bg="#333",fg="white",command=lambda:cm(2,t))
    b3.pack(fill=tk.X)
    t.mainloop()

def main():
    wc()
    if(mode == 0):
        os.popen("scalc.pyw")
    elif(mode == 1):
        os.popen("gcalc.pyw")
    elif(mode == 2):
        os.popen("statcalc.pyw")

if __name__ == '__main__':
    main()
