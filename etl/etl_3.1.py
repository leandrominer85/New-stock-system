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
        df2.Quantity = 0
        df[df.supplier == s] = df2
        


# In[6]:


#Changing the type to str
df.Partnumber = df.Partnumber.astype(str)


# In[7]:


# Creating a temp DF to retain the desired data
temp = df[df.Manufacturer =='monroeaxios']


# In[8]:


#Reading the data with the partnumbers
df2 = pd.read_excel('../data/synonyms/manufacturers_pn_list.xlsx', dtype='object')
df2 = df2.astype(str)


# In[9]:


#Changing to lower and assign to a list
monroe = [x.lower() for x in list(df2.monroe_pn)]


# In[10]:


#Changing to lower and replacing the float point and assign to a list
axios = [x.lower() for x in list(df2.axios_pn)]
axios = [x.rstrip('.0') for x in axios ]


# In[11]:


# Changing the values in the temp using the lists
temp.loc[temp.Partnumber.isin(monroe), 'Manufacturer'] = 'monroe'
temp.loc[temp.Partnumber.isin(axios), 'Manufacturer'] = 'axios'


# In[12]:


# Updating the original DF
df.update(temp)


# In[13]:


df.to_csv('../data/etl/estoque.csv')


# In[14]:


#Save with timestamp
df.to_csv('../data/text_output/estoque{}.txt'.format(pd.datetime.now().strftime("%Y-%m-%d %H-%M-%S")))


# In[ ]:




