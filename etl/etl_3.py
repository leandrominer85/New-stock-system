#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing modules
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")


# In[2]:


#Reading the dataframe
df = pd.read_csv('..\\data\\originals\\Estoque real 29 11.csv',header=0,
            sep = ";|\|", 
            encoding = "ISO-8859-1", #This encoding is important to work with most of the files
            engine = "python")


# In[3]:


#Coding the prices
real = {'A' : '4',
'B' : '11'}

# Changing real
df = df.replace(real, regex=True)


# In[4]:


#Selecting the collumns and assing to a new df
cols= ['QTDE_SPNORTE' ,'PRECO_SPNORTE','QTDE_ABC','PRECO_ABC','QTDE_SPLESTE','PRECO_SPLESTE']
df2 = df[cols]


# In[5]:


#coding as strings
df2[cols] = df2[cols].astype(str)


# In[6]:


# Replacing the commas
for col in cols:
    df2[col] = df2[col].apply(lambda x: x.replace(',','.'))


# In[7]:


#Transforming to numeric
df2[cols] = df2[cols].apply(pd.to_numeric, errors='coerce')


# In[8]:


#replace all zeros with NaN values
prices= ['PRECO_SPNORTE','PRECO_ABC','PRECO_SPLESTE']
df2[prices] = df2[prices].replace(0.0, np.nan)


# In[9]:


#Get a list with the minimum values
minimun = df2[['PRECO_SPNORTE','PRECO_ABC','PRECO_SPLESTE']].min(axis=1)


# In[10]:


#Start with empty lists of price and quantities
prices = []
quantities = []


#Iterate trought the minimun list and for each value select the corresponding quantity value

for i in enumerate(minimun):
    
    
    # If all columns have the minimum value:
    if (df2.iloc[i[0],1] == i[1]) & (df2.iloc[i[0],3] == i[1]) & (df2.iloc[i[0],5] == i[1]):
        quantity = np.nansum([df2.iloc[i[0],0]] + [df2.iloc[i[0],2]] + [df2.iloc[i[0],4]])
        price = i[1]
        prices.append(price)
        quantities.append(quantity)
    
    #If the first two columns have the minimum value
    elif (df2.iloc[i[0],1] == i[1]) & (df2.iloc[i[0],3] == i[1]) & (df2.iloc[i[0],5] != i[1]):
        quantity = np.nansum([df2.iloc[i[0],0]] + [df2.iloc[i[0],2]])
        price = i[1]
        prices.append(price)
        quantities.append(quantity)

        
    #If the middle col dosen´t have the minimum value:
    elif (df2.iloc[i[0],1] == i[1]) & (df2.iloc[i[0],3] != i[1]) & (df2.iloc[i[0],5] == i[1]):
        quantity = np.nansum([df2.iloc[i[0],0]]  + [df2.iloc[i[0],4]])
        price = i[1]
        prices.append(price)
        quantities.append(quantity)

    #If the first col dosen´t have the minimum value:
    elif (df2.iloc[i[0],1] != i[1]) & (df2.iloc[i[0],3] == i[1]) & (df2.iloc[i[0],5] == i[1]):
        quantity = np.nansum([df2.iloc[i[0],2]] + [df2.iloc[i[0],4]])
        price = i[1]
        prices.append(price)
        quantities.append(quantity)
    
    #If there is just one collum with the minimum:
    elif (df2.iloc[i[0],1] == i[1]) & (df2.iloc[i[0],3] != i[1]) & (df2.iloc[i[0],5] != i[1]):
        quantity = np.nansum([df2.iloc[i[0],0]])
        price = i[1]
        prices.append(price)
        quantities.append(quantity)  
        
    elif (df2.iloc[i[0],1] != i[1]) & (df2.iloc[i[0],3] == i[1]) & (df2.iloc[i[0],5] != i[1]):
        quantity = np.nansum([df2.iloc[i[0],2]])
        price = i[1]
        prices.append(price)
        quantities.append(quantity)  
        
    elif (df2.iloc[i[0],1] != i[1]) & (df2.iloc[i[0],3] != i[1]) & (df2.iloc[i[0],5] == i[1]):
        quantity = np.nansum([df2.iloc[i[0],4]])
        price = i[1]
        prices.append(price)
        quantities.append(quantity)
        
    else:
        quantity = 0
        price = i[1]
        prices.append(price)
        quantities.append(quantity)
        


# In[11]:


df['sumed_quantity_for_best_price_only'] = quantities
df['best_price_with_stock'] = prices


# In[13]:


df.to_csv('../data/etl/third_etl.csv')


# In[14]:


#Save with timestamp
df.to_csv('../data/text_output/third_etl_{}.txt'.format(pd.datetime.now().strftime("%Y-%m-%d %H-%M-%S")))


# In[ ]:




