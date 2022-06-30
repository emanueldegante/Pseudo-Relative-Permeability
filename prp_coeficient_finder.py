# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:52:31 2020

@author: Emanuel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def prp_calc(swi,sor,krocw,krwro):
    
    swi=.15
    sor=.32
    now=1.8
    nw=4
    krocw=1
    krwro=.18
    tolerance= 0.011
    
    #Water Oil System
    
    sw=np.round(np.arange(swi,(1-sor),0.01),2)
    
    kro=np.round((krocw*((1-sw-sor)/(1-swi-sor))**(now)),2)
    
    krw= np.round((krwro*((sw-swi)/(1-swi-sor))**(nw)),2)
    
    #--------------------------------------------------------Identification of Intersection
    #--------------------------------------------------------Krw=kro & Sw
    
    swi_range=int(swi*100)
    sor_range=int((1-sor)*100)
    
    j=-1
    for i in range(swi_range,sor_range):
        j+=1
        if abs(kro[j]-krw[j]) <= tolerance :
            break
      
        sw_int=sw[j+1]                       # Water Saturation where kro and krw meets
        krw_int=krw[j+1]                     # krw where it is equal to kro
        kro_int=kro[j+1]                     # kro where it is equal to kro
        print(i+1,kro[j+1],krw[j+1])
    
    print("Krw and kro is:", kro_int)
    print("Saturation is:", sw_int)
    
    
    #======================================================  First Plot
    
    plt.plot(sw,kro,'blue')
    plt.plot(sw,krw,'blue')
    plt.title("Relative Permeability for 2 Phase Oil/Water Undersaturated Reservoir")
    plt.xlabel("Water Saturation - Sw")
    plt.ylabel("Relative Permeability kro,krw")
    
    
    #====================================================== Generate Pseudo Kro (pkro)
    
    pnow=1
    
    pkro=np.round((krocw*((1-sw-sor)/(1-swi-sor))**(pnow)),2)
    
    j_1=0
    for o in pkro:
        j_1+=1
        if (pkro[j_1]==kro_int) or ((pkro[j_1]-kro_int) <= tolerance):
            break
    
    print(sw[j_1], pkro[j_1])
    
    swpkr=sw[j_1]
    fpkro=pkro[j_1]
    
    #====================================================  Identifiy Exponent for pnw
    
    pnw=np.arange(1,100)
    nw=np.arange(1,100)
    
    j=-1
    e=1
    i=-1
    for sw_i in sw:  
        pkrw= krwro*((sw_i-swi)/(1-swi-sor))**(nw)
        pkrw=np.round(pkrw,2)
        i+=1
        if (sw_i==swpkr):  
            for nw_i in nw:
                pkrw= krwro*((sw_i-swi)/(1-swi-sor))**(nw_i)
                pkrw=np.round(pkrw,2)
                j+=1
                if ((abs(pkrw-fpkro))<= tolerance):
                    print(sw_i, pkrw, nw_i)
                    break
    
    
    
    #==============================================   Generate Pseudo Relative Permeabilities
    
    
    nw2=nw_i
    
    krw2= np.round((krwro*((sw-swi)/(1-swi-sor))**(nw2)),2)
    
    
    plt.plot(sw,kro,'blue')
    plt.plot(sw,krw,'blue')
    plt.plot(sw,pkro,'red')
    plt.plot(sw,krw2,'red')
    plt.title("Relative Permeability for 2 Phase Oil/Water Undersaturated Reservoir")
    plt.xlabel("Water Saturation - Sw")
    plt.ylabel("Relative Permeability kro,krw")
    plt.legend()
