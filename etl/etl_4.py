#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing modules
import pandas as pd
import numpy as np


# In[2]:


#reading the estoque dataframe
df = pd.read_csv('../data/etl/estoque.csv',index_col=0 )


# In[3]:


#Getting repeated keys
keys = df.groupby(['key']).supplier.nunique()
keys = keys[keys>1].keys()


# In[4]:


# Copy of dataframe with the repeated keys
df2=df[df['key'].isin(keys)].sort_values(by = 'key')


# In[5]:


# Creating a dataframe with the mim price and quantities
min_df = df2.groupby(['key', 'supplier'])['Price','Quantity'].min().unstack()


# In[6]:


print(min_df.head())


# In[7]:


#Creating a dataframe to get only the prices
df_price_min = df2.groupby(by=['key', 'supplier'])['Price'].min().unstack()


# In[8]:


# Get a array with the minimun price for each row
price_min = df_price_min.min(axis=1).values


# In[9]:


# Start with a empty list for the quantities and other for temporary use
min_q=[]
temp = []
sumed=[]

#Iterate through the range of the min DF
for row in range(len(min_df)):
    #Iterate through each key tuple
    for k in min_df.keys():
        # If the key is 'Price' and the correponding row and price column are equal to the minimum from the price array
        # then append the corresponding supplier row to the temp list 
        if k[0] == 'Price' and min_df['Price'][k[1]][row] == price_min[row]:
            temp.append(min_df['Quantity'][k[1]][row])
    # If there is any value in the temp list get the min and the sum and append to the min_q and sumed lists
    # , then reset the list
    if len(temp) > 0:
            min_q.append(np.min(temp))
            sumed.append(sum(temp))
            temp=[]
    else:
        temp=[]


# In[10]:


# Add the col to the dataframe
min_df['sum_min_quantity'] = min_q


# In[11]:


min_df


# In[12]:


min_df.to_csv('../data/etl/fourth_etl.csv')


# In[13]:


#Save with timestamp
min_df.to_csv('../data/text_output/fourth_etl{}.txt'.format(pd.datetime.now().strftime("%Y-%m-%d %H-%M-%S")))


# In[ ]:




