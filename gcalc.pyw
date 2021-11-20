#-------------------------------------------------------------------------------
# Name:        gcalc
# Purpose:     to demonstrate a graphing calculator in python (3.9.0)
#
# Author:      CA1K
#
# Created:     16/02/2019 (edited 1/11/2021)
#-------------------------------------------------------------------------------

import tkinter
from tkinter import *
import tkinter.ttk as ttk
import matplotlib as mpl
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import numpy as np #algebra & trig
#circa 2021
import os
import warnings
import math

warnings.simplefilter('ignore')
size = 1 #figure size
indsize = 10 #range of the independent axis
l1 = "Graphing Calculator" #title text
l2 = "Graph" #text for the graph button
l3 = "Main" #text for the button that switches calculators
l4 = "Calculator by CA1K.XKOTTO.COM" #label at the top
l5 = "Load a previous function"
l6 = "Previous functions..."
fc = [] #function cache; previous functions the user entered in
px = []
py = []
sp = 111 #sub-plot
acc = 100 #accuracy variable
mp = 10 #message padding

def err(msg): #error message window script
    t = tkinter.Tk()
    t.resizable(0,0)
    t.title("Error")
    l = Label(t,text=msg,padx=mp,pady=mp)
    l.grid(row=0, column=0, sticky=W+E)
    b1 = Button(t,text="OK",command=lambda:t.destroy())
    b1.grid(row=1, column=0, sticky=W+E)
    t.mainloop()

def sel(ar): #selection window for previous functions the user entered
    if len(ar) < 1:
        trw(4)
        pass
    t = tkinter.Tk()
    t.resizable(0,0)
    t.title("Select")
    l = Label(t,text=l5,padx=mp*6,pady=mp)
    l.grid(row=0, column=0, sticky=W+E)
    cb = ttk.Combobox(t,values=ar)
    cb.set("Select a previous function.")
    cb.grid(row=1, column=0, sticky=W+E)
    b = Button(t,text="OK",command=lambda:ptg(t,cb))
    b.grid(row=2, column=0, sticky=W+E)
    t.mainloop()

def ptg(tk,com): #pass to graph function. designed for the selection window
    mden(com.get())
    tk.destroy()

def trw(en): #throws error with error message
    if(en == 0): #you have characters that are not recognized by the program
        err("Invalid letter(s). Plotting failed.")
    if(en == 1): #you have characters that are not recognized by the program
        err("Invalid syntax. Plotting failed.")
    if(en == 2): #you put in the wrong signs for the interpreter
        err("Invalid operator(s). Plotting failed. See README.")
    if(en == 3): #you divided by zero
        err("Division by zero. Plotting failed.")
    if(en == 4): #you just opened the application or haven't given an input yet
        err("No previous functions entered within the current session.")
        #circa 2021
    if(en == 5): #covers errors that 1 can't detect
        err("TypeError: Python cannot compute. (check readme)")

def tm(m): #switches to main
    m.destroy()
    os.popen("__main__.pyw")

def plindep(): #fills the x-axis up to the indsize limit
    a = []
    i = -indsize
    while(i<indsize):
        a.append(i)
        i += 1/acc #manages the amount of points plotted onto the graph
    return a

def df(f,v,m=((acc**acc)**acc)): #derivative function
    h = 1/(acc)
    if m != ((acc**acc)**acc): #if you have a 3rd arg that isnt acc^acc^acc...
        t = f(v+h,m) - f(v,m)
    else:
        t = f(v+h) - f(v)
    return t/h

#my custom logarithm method suited for the graph, set to return values
#0 and less as 0
def mlog(v,b):
    if v <= 0:
        return 0
    else:
        return math.log(v,b)
    
#used to be pldep in 2019 when only one axis could vary,
#now it's pldep for the 'dependent' variable in statistics, since not only
#the x-axis can be independent. now we can plot from x or y
def pldep(en,g,axis): #calculates the function regarding the 'dependent' variable
    px = plindep()
    py = []
    if (en in fc) != True:
        fc.append(en) #add function to cache
    for i in range(0,len(px)):
        #can't confuse the calculator with 2 variables,
        #it only analyzes functions and polynomials, not equations
        if ('x' in en) & ('y' in en):
            trw(1)
            break
    #variable and function input into the python evaluation method
        globals = {'x':px[i],'y':px[i],'sin':np.sin,'cos':np.cos,'tan':np.tan,
        'arcsin':np.arcsin,'arccos':np.arccos,'arctan':np.arctan,
        'sinh':np.sinh,'cosh':np.cosh,'tanh':np.tanh,'floor':np.floor,
        'ceil':np.ceil,'sqrt':np.sqrt,'fix':np.fix,'sinc':np.sinc,
        'e':np.e,'PI':np.pi,'df':df,'pow':np.power,'log':mlog,
        'abs':np.absolute,'arcsinh':np.arcsinh,'arccosh':np.arccosh,
        'arctanh':np.arctanh}
        try:
            r = eval(en,globals) * 1
            if np.isnan(r):
                py.append(0)
            else:
                py.append(r)
        except NameError:
            trw(0)
            break
        except SyntaxError:
            trw(1)
            break
        except AttributeError:
            trw(2)
            break
        except ZeroDivisionError:
            trw(3)
            break
        #circa 2021
        except TypeError:
            trw(5)
            break
        except ValueError: #just a bug fix for the console, don't mind it
            break
    #plot on y axis if a y is detected and not x 
    if ('y' in en) == True:
        axis.cla()
        axis.grid()
        axis.plot(py,px)
        g.draw()
    #plot on x axis if a x is detected and not y 
    if ('x' in en) == True:
        axis.cla()
        axis.grid()
        axis.plot(px,py)
        g.draw()

def mden(t): #modifies the entry text
    e.delete(0,END)
    e.insert(0,t)
    pldep(e.get(),graph,ax)

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
graph = FigureCanvasTkAgg(fig, master=root)
graph.get_tk_widget().pack(side="top",fill='both',expand=True)
toolbar = NavigationToolbar2Tk(graph,root)
toolbar.update()
#circa 2021
ax.plot(plindep(),plindep()) #basically the y=x slope is the default function on startup

e = Entry(root)
e.pack(fill=tkinter.BOTH,expand=1)
b1 = Button(root,text=l2,bg="gray",fg="white",command=lambda:pldep(e.get(),graph,ax))
b1.pack(fill=tkinter.BOTH,expand=1)
b1 = Button(root,text=l6,bg="#111",fg="white",command=lambda:sel(fc))
b1.pack(fill=tkinter.BOTH,expand=1)
b2 = Button(root,text=l3,bg="black",fg="white",command=lambda:tm(root))
b2.pack(fill=tkinter.BOTH,expand=1)

#main loop
root.mainloop()

#def main():
#    pass

#if __name__ == '__main__':
#    main()

