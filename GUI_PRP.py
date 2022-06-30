# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 01:03:57 2020

@author: Emanuel
"""

from tkinter import *
import prp_plot as pp
import prp_saver as ps
import prp_points_obtainer as ppo




#Global Variables
swi1= None
sor1= None
kro1= None
krw1= None
equality=None

# This function is called whenever the button is pressed
def load():
    global swi1
    global sor1
    global kro1
    global krw1
    global equality

    try:

        swi = swi1.get()
        sor = sor1.get()
        krocw = kro1.get()
        krwro = krw1.get()
        sor_1.set(1-sor)
        

    except:
        pass

def plot():
    global swi1
    global sor1
    global kro1
    global krw1
    global equality
    
    try:
        swi = swi1.get()
        sor = sor1.get()
        krocw = kro1.get()
        krwro = krw1.get()
        pp.prp_calc(swi,sor,krocw,krwro)
    except:
        pass

def save():
    global swi1
    global sor1
    global kro1
    global krw1
    global equality
    
    try:
        swi = swi1.get()
        sor = sor1.get()
        krocw = kro1.get()
        krwro = krw1.get()
        ps.prp_saver(swi,sor,krocw,krwro)
    except:
        pass

    

window=Tk()


window.wm_title("Pseudo Relative Permeabilities")

# adding image (remember image should be PNG and not JPG) 
img = PhotoImage(file = r"C:\Users\Emanuel\Desktop\Python_Projects\5 - Pseudo Relative Permeabilities\Functions\PRP_Sample.png") 
img1 = img.subsample(2, 2) 

# setting image with the help of label 
Label(window, image = img1).grid(row = 1, column = 5, 
       columnspan = 2, rowspan = 2, padx = 5, pady = 5)



b1=Button(window,text="Load", width=12, command=load)
b1.grid(row=2,column=4)

b2=Button(window,text="plot", width=12, command=plot)
b2.grid(row=4,column=4)

b2=Button(window,text="Save", width=12, command=save)
b2.grid(row=7,column=4)

l1=Label(window,text="Swi")
l1.grid(row=1,column=1)

swi1=DoubleVar()
e1=Entry(window,textvariable=swi1)
e1.grid(row=1,column=2)

l2=Label(window,text="Sor")
l2.grid(row=3,column=1)

sor1=DoubleVar()
e2=Entry(window,textvariable=sor1)
e2.grid(row=3,column=2)

l3=Label(window,text="Kro @ Swi")
l3.grid(row=5,column=1) 

kro1=DoubleVar()
e3=Entry(window,textvariable=kro1)
e3.grid(row=5,column=2)

l4=Label(window,text="Krw @ [1-Sor]")
l4.grid(row=7,column=1)

krw1=DoubleVar()
e4=Entry(window,textvariable=krw1)
e4.grid(row=7,column=2)

l5=Label(window,text="[1-Sor]")
l5.grid(row=8,column=1)

sor_1=DoubleVar()
l6=Label(window, textvariable=sor_1)
l6.grid(row=8, column=2)



window.mainloop()
