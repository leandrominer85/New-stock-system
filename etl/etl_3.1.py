#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing modules
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")


# In[2]:


# Reading the cleaned dataframe
df =pd.read_csv('../data/etl/second_etl.csv' , index_col=0)


# In[3]:


#Reading the dataframe with the stock data
estoque = pd.read_excel('../data/controle_do_estoque/Controle do estoque.xlsx')


# In[4]:


# Selecting the columns
estoque = estoque[["supplier", "days_late"]]


# In[5]:


# Iterate through each supplier and if the days_late is superior than 10 them it make a slice of the dataframe with
# the corresponding supplier and them reset the price to zero and reassign to the original dataframe 
for s in estoque.supplier:
    if np.where(estoque[estoque.supplier == s].days_late > 10,0,99) == 0:
        df2 = df[df.supplier == s]
        df2.Price = 0
        df[df.supplier == s] = df2
        


# In[6]:


df.to_csv('../data/etl/estoque.csv')


# In[7]:


#Save with timestamp
df.to_csv('../data/text_output/estoque{}.txt'.format(pd.datetime.now().strftime("%Y-%m-%d %H-%M-%S")))

