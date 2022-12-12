#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[2]:


# Functions to process the dataframes that need some work:

def mte_process(df):
        
    #Remove first row as it is empty
    df.drop(    index=df.index[0], 
                axis=0, 
                inplace=True)
   
    df.rename({'COD MTE' : 'Partnumber', 'PREÇO' : 'Price' ,
               'QTD. ESTOQUE':'Quantity'}, axis=1, inplace= True)
    
    df['Manufacturer'] = 'Mte'
    
    df= df[["Manufacturer", "Partnumber", "Quantity", "Price"]]
    
    return df


def sueyasu_process(df):
    #Remove first row (unwanted data)
    df.drop(    index=df.index[0], 
                axis=0, 
                inplace=True)
    return df


def polipecas_process(df): 
    ###HARD CODED BOSCH 
    ###WHAT IF THERE IS ZERO IN THE BEGINNING OF PART NUMBER

    #Adding manufacturer column and hard coding BOSCH in it
    df.insert(    loc=0, 
                column='new col', 
                value=['BOSCH' for i in range(df.shape[0])])

    #Adding empty quantity column
    df.insert(    loc=2, 
                column='new col2', 
                value=['' for i in range(df.shape[0])])

    

    return df


def ima_process(df):
    
    df.rename({'Código XML' : 'Partnumber',
               'Estoque':'Quantity'}, axis=1, inplace= True)
    
    df['Manufacturer'] = 'ima'
    df['Price'] = np.nan
    df= df[["Manufacturer", "Partnumber", "Quantity", "Price"]]

    return df


def compel_process(df):
    #Remove first row (unwanted data)
    df.drop(    index=df.index[:2], 
                axis=0, 
                inplace=True)
    return df


def jahu_process(df):
    
    
    
    df.rename({'Marca': 'Manufacturer',
               'Cód.Fabricante' : 'Partnumber', 'Preco' : 'Price' ,
               'Disponivel':'Quantity'}, axis=1, inplace= True)
    
    df= df[["Manufacturer", "Partnumber", "Quantity", "Price"]]
    
    
    return df


# In[ ]:




