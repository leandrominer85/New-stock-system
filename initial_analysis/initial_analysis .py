#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re


# In[2]:


df = pd.read_csv('../data/etl/second_etl.csv' , index_col=0)


# ## Total unique Manufacturers:

# In[3]:


df.Manufacturer.nunique()


# ## Manufacturers by suppliers

# In[4]:


df.groupby('supplier')['Manufacturer'].count()


# ## total unique manufacturers by supplier

# In[5]:


df.groupby('supplier')['Manufacturer'].nunique()


# ## Unique manufacturer names:

# In[6]:


pd.DataFrame(df.Manufacturer.unique()).to_excel('../data/initial_analysis/unique_manufacturer.xlsx')


# ## Unique Partnumbers:

# In[7]:


df.Partnumber.nunique()


# ## Partnumbers by Manufacturer

# In[8]:


df.groupby('Manufacturer')['Partnumber'].count().to_excel('../data/initial_analysis/patnumber_by_manufacturer.xlsx')


# ## Partnumbers by supplier

# In[9]:


df.groupby('supplier')['Partnumber'].count()


# ## total unique partnumbers by manufacturer is a long table. So its better to download as excel file:

# In[10]:


df.groupby('Manufacturer')['Partnumber'].nunique().to_excel('../data/initial_analysis/unique_partnumbers__manufacturer.xlsx')


# ## Total Price (some prices have more than two decimal digits in the database):

# In[11]:


print('R$' + str(df.Price.sum()))


# ## The Total Price by manufacturer is a long table. So its better to download as excel file:

# In[12]:


(df.groupby('Manufacturer')['Price'].sum()).to_excel('../data/initial_analysis/price_by_manufacturer.xlsx')


# ## Total Price by supplier:

# In[13]:


df.groupby('supplier')['Price'].sum()


# ## Total quantity:

# In[14]:


df.Quantity.sum()


# ## The Total Quantity by manufacturer is a long table. So its better to download as excel file:

# In[15]:


df.groupby('Manufacturer')['Quantity'].sum().to_excel('../data/initial_analysis/quantity_by_manufacturer.xlsx')


# ## Total Quantity by supplier:

# In[16]:


df.groupby('supplier')['Quantity'].sum()


# in initial_anaysis, add the following items:
# 
# 
# by manufacturer
# by supplier
# 

# ## the average price (i.g. price/quantity)  in total:

# In[17]:


df.Price.sum()/df.Quantity.sum()


# ## the average price (i.g. price/quantity)  by manufacturer:

# In[18]:


pd.DataFrame(df.groupby("Manufacturer")["Price"].sum()/df.groupby("Manufacturer")["Quantity"].sum()).to_excel('../data/initial_analysis/avg_price_by_manufacturer.xlsx')


# ## the average price (i.g. price/quantity)  by supplier:

# In[19]:


df.groupby("supplier")["Price"].sum()/df.groupby("supplier")["Quantity"].sum()


# for each supplier, a separate excel report with the following by manufacturer:
# count of partnumbers
# sum of quantity
# average price 
# 

# ## count of partnumbers for each supplier by manufacturer:
# 

# In[20]:


df.groupby(["supplier","Manufacturer"])["Partnumber"].count().to_excel('../data/initial_analysis/partnumbers_supplier_manufacturer.xlsx')


# ## sum of quantity of partnumbers for each supplier by manufacturer:

# In[21]:


df.groupby(["supplier","Manufacturer"])["Quantity"].sum().to_excel('../data/initial_analysis/quantity_supplier_manufacturer.xlsx')


# In[22]:


df.groupby(["supplier","Manufacturer"])["Price"].mean().to_excel('../data/initial_analysis/price_supplier_manufacturer.xlsx')


# In[ ]:




