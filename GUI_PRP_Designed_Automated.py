# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:26:24 2020

@author: Emanuel
"""

from tkinter import *


#Global Variables
swi1= None
sor1= None
kro1= None
krw1= None
equality=None


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

window=Tk()




window.wm_title("Pseudo Relative Permeabilities")

#=====================================================================Images
# adding image (remember image should be PNG and not JPG) 
img = PhotoImage(file = r"C:\Users\Emanuel\Desktop\Python\Pseudo Relative Permeabilities\Functions\PRP_Guide.png") 
img1 = img.subsample(2, 2) 
# setting image with the help of label 
Label(window, image = img1).grid(row = 1, column = 5, 
       columnspan = 2, rowspan = 5, padx = 5, pady = 5)


# adding image (remember image should be PNG and not JPG) 
img2 = PhotoImage(file = r"C:\Users\Emanuel\Desktop\Python\Pseudo Relative Permeabilities\Functions\prp_final.png") 
img3 = img2.subsample(1, 1) 
# setting image with the help of label 
Label(window, image = img3).grid(row = 7, column = 5, 
       columnspan = 2, rowspan = 3, padx = 5, pady = 5)

#---------------------------------------------------------------Buttons


b1=Button(window,text="Load Data", width=20)
b1.grid(row=1,column=2)

b2=Button(window,text="Plot", width=12,)
b2.grid(row=9,column=2)

b3=Button(window,text="Export Data", width=12, )
b3.grid(row=9,column=3)

b4=Button(window,text="Quit", width=20, command=window.destroy)
b4.grid(row=1,column=3)
#================================================================Tags



l1=Label(window,text=" Swi ")
l1.grid(row=2,column=1)

swi1=DoubleVar()
e1=Entry(window,textvariable=swi1)
e1.grid(row=3,column=1)

l2=Label(window,text=" 1-Sor ")
l2.grid(row=2,column=2)

sor1=DoubleVar()
e2=Entry(window,textvariable=sor1)
e2.grid(row=3,column=2)

l3=Label(window,text=" Kro @ Swi ")
l3.grid(row=2,column=3)

kro1=DoubleVar()
e3=Entry(window,textvariable=kro1)
e3.grid(row=3,column=3)


l4=Label(window,text=" Krw @ 1-Sor ")
l4.grid(row=2,column=4)

krw1=DoubleVar()
e4=Entry(window,textvariable=krw1)
e4.grid(row=3,column=4)


l5=Label(window,text=" kr(reference), krw=kro ")
l5.grid(row=4,column=2)

krr=DoubleVar()
e5=Entry(window,textvariable=krr)
e5.grid(row=5,column=2)

l6=Label(window,text=" Sw(reference), krw=kro ")
l6.grid(row=4,column=3)

krw1=DoubleVar()
e6=Entry(window,textvariable=krw1)
e6.grid(row=5,column=3)



#============================================= Building Pseudos

l7=Label(window,text=" now [1.8 - 0.5]")
l7.grid(row=7,column=2)

krw1=DoubleVar()
e7=Entry(window,textvariable=krw1)
e7.grid(row=8,column=2)

l8=Label(window,text=" nw ")
l8.grid(row=7,column=3)

krw1=DoubleVar()
e8=Entry(window,textvariable=krw1)
e8.grid(row=8,column=3)



#=============================================Closing Window

window.mainloop()
