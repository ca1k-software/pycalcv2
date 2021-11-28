
#-------------------------------------------------------------------------------
# Name:        statcalc
# Purpose:     to demonstrate a statistical calculator in python
#
# Author:      CA1K
#
# Created:     27/10/2021
#-------------------------------------------------------------------------------

import tkinter
from tkinter import *
import tkinter.ttk as ttk
import matplotlib as mpl
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import numpy as np
import warnings as warnings
import statistics as s
import os

warnings.simplefilter('ignore') #ignores console warnings
size = 1 #figure size
l1 = "Statistical Calculator" #title text
l2 = "Graph" #text for the graph button
l3 = "Main" #text for the button that switches calculators
l4 = "Calculator by CA1K.XKOTTO.COM" #label at the top
l6 = "Clear" #text for the clear button
l7 = "Save" #text for the save button
l8 = "Load" #text for the load button
l9 = "File" #text for the file button
sn = 'untitled.txt' #default save name
stat = [] #point array
stat2 = [] #point array #2
sp = 111 #sub-plot
mp = 10 #message padding

def err(msg): #error message window script
    t = tkinter.Tk()
    t.resizable(0,0)
    t.title("Error")
    l = Label(t,text=msg,padx=mp,pady=mp)
    l.grid(row=0,column=0,sticky=W+E)
    b1 = Button(t,text="OK",command=lambda:t.destroy())
    b1.grid(row=1,column=0,sticky=W+E)
    t.mainloop()

def sl(): #save location window script
    t = tkinter.Tk()
    t.resizable(0,0)
    t.title("Save location")
    l = Label(t,text="Save directory:",padx=mp,pady=mp)
    l.grid(row=0,column=0,sticky=W+E)
    se = Entry(t)
    se.grid(row=0,column=1,sticky=W+E,padx=mp,pady=mp,ipadx=(mp*8))
    se.insert(0,sn)
    b1 = Button(t,text="OK",command=lambda:cs(t,se.get()))
    b1.grid(row=1,column=0,sticky=W+E,columnspan=2)
    t.mainloop()

def cs(t,com): #changes the save name
    global sn
    sn = str(com)
    t.destroy()

def trw(en): #throws error with error message
    if(en == 0): #you have characters that are not recognized by the program
        err("Invalid value(s). Plotting failed.")
    if(en == 1): #you left empty inputs
        err("Field(s) empty")

def tm(m): #switches to the main window
    m.destroy()
    os.popen("__main__.pyw")

def upd(en,en2): #updates the graph in the window
    proceed = True #check for errors before plotting
    a = 0
    b = 0
    if len(en) == 0: #cant leave the entry empty
        trw(1)
        proceed = False
    if len(en2) == 0:
        trw(1)
        proceed = False
    try:
        a = eval(en)
        b = eval(en2)
    except:
        trw(0) #nor use letters
        proceed = False
    if proceed:
        stat.append(a) #add values to cache
        stat2.append(b) #add values to 2nd cache
        ax.cla()
        ax.set_xlabel("X axis")
        ax.set_ylabel("Y axis")
        ax.grid()
        ax.plot(stat,stat2)
        graph.draw()
        updl(stat2)

def res():
    del stat[:] 
    del stat2[:]
    ax.cla()
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.grid()
    ax.plot(0,0) #helps reset the graph back to a 0,0 point
    graph.draw()
    updl(stat2)

def updl(st):
    try:
        L['text'] = '[mean: ' + str(s.mean(st)) + ']'
    except s.StatisticsError:
        L['text'] = '[mean: 0]'
    try:
        L2['text'] = '[median: ' + str(s.median(st)) + ']'
    except s.StatisticsError:
        L2['text'] = '[median: 0]'
    try:
        L3['text'] = '[mode: ' + str(s.mode(st)) + ']'
    except s.StatisticsError:
        L3['text'] = '[mode: 0]'
    
def sv(n): #writes a combo array of the x and y arrays
    f = [] #make a new array for merging
    for i in range(0,len(stat)):
        f.append(stat[i])
    for i in range(0,len(stat2)):
        f.append(stat2[i])
    o = open(n,'w+')
    o.write(str(f)) #write the raw array in text
    o.close()

def ld(n):
    o = open(n,'r')
    t = str(o.read())
    o.close()
    stat = eval(t) #translate text to python
    stat2 = stat.copy()
    r = int(len(stat2)/2)
    for i in range(0,r):
        stat2.pop(0) #remove first index items until halved
    r = int(len(stat)/2)
    for i in range(0,r):
        stat.pop(r) #remove midpoint index items until halved
    ax.cla()
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.grid()
    ax.plot(stat,stat2)
    graph.draw()
    updl(stat2)

#window and title
root = tkinter.Tk()
root.resizable(0,0)
root.wm_title(l1)

#graphing code
fig = Figure()
ax = fig.add_subplot(sp)
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.grid()
graph = FigureCanvasTkAgg(fig,master=root)

graph.get_tk_widget().pack(fill=tkinter.X)
e = Entry(root)
e.pack(fill=tkinter.X)
e2 = Entry(root)
e2.pack(fill=tkinter.X)
b1 = Button(root,text=l2,bg="gray",fg="white",command=lambda:upd(e.get(),e2.get()))
b1.pack(fill=tkinter.X)
f = Frame(root)
f.pack(fill=tkinter.X)
b2 = Button(f,text=l3,bg="black",fg="white",command=lambda:tm(root))
b2.grid(row=0,column=0)
b3 = Button(f,text=l6,bg="#111",fg="white",command=lambda:res())
b3.grid(row=0,column=1)
b4 = Button(f,text=l7,bg="#222",fg="white",command=lambda:sv(sn))
b4.grid(row=0,column=2)
b5 = Button(f,text=l8,bg="#333",fg="white",command=lambda:ld(sn))
b5.grid(row=0,column=3)
b6 = Button(f,text=l9,bg="#444",fg="white",command=lambda:sl())
b6.grid(row=0,column=4)

L = Label(f,text="")
L.grid(row=0,column=5)
L2 = Label(f,text="")
L2.grid(row=0,column=6)
L3 = Label(f,text="")
L3.grid(row=0,column=7)
toolbar = NavigationToolbar2Tk(graph,root)
toolbar.update()
#main loop
root.mainloop()

#def main():
#    pass

#if __name__ == '__main__':
#    main()

