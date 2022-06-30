# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:52:31 2020

@author: Emanuel
"""

import pandas as pd
import numpy as np

def prp_points_obtainer():

    dataset=pd.read_csv('prp_input.csv')
    swi_dataset=dataset.iloc[:,0].values
    swi=swi_dataset[0]
    sor=np.round(1-swi_dataset[-1],2)
    krw=dataset.iloc[:,2].values
    krwro=krw[-1]
    kro=dataset.iloc[:,1].values
    krocw=kro[0]
    
    sw=dataset.iloc[:,0].values
    
    tolerance= 0.011
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
    