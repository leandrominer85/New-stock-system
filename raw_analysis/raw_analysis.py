#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import glob
import re


# In[2]:


pd.options.display.float_format = '{:.1f}'.format


# In[3]:


path = r'E:\Dropbox\Pessoal\Python\trabalho\Upwork\New-stock-system\data\originals\*'
files = glob.glob(path)


# ## Files Used:

# In[4]:


for f in files:
    print(f)


# In[5]:


df = pd.read_csv('../data/merged_database/combined.csv' , index_col=0)


# In[6]:


df['Price'] = df['Price'].astype(str)


# In[7]:


df['Price'] = df['Price'].apply(lambda x: x.replace(',','.'))


# In[8]:


df['Price'] = pd.to_numeric(df['Price'],errors='coerce')


# In[9]:


df['Quantity'] = pd.to_numeric(df['Quantity'],errors='coerce')


# ## Total unique Manufacturers:

# In[10]:


df.Manufacturer.nunique()


# ## Manufacturers by suppliers

# In[11]:


df.groupby('supplier')['Manufacturer'].count()


# ## total unique manufacturers by supplier

# In[12]:


df.groupby('supplier')['Manufacturer'].nunique()


# ## Unique manufacturer names:

# In[13]:


pd.DataFrame(df.Manufacturer.unique()).to_excel('../data/raw_analysis/unique_manufacturer.xlsx')
#Save with timestamp
pd.DataFrame(df.Manufacturer.unique()).to_csv('../data/text_output/unique_manufacturer_{}.txt'.format(pd.datetime.now().strftime("%Y-%m-%d %H-%M-%S")))


# ## Unique Partnumbers:

# In[14]:


df.Partnumber.nunique()


# ## Partnumbers by Manufacturer

# In[15]:


df.groupby('Manufacturer')['Partnumber'].count().to_excel('../data/raw_analysis/patnumber_by_manufacturer.xlsx')
df.groupby('Manufacturer')['Partnumber'].count().to_csv('../data/text_output/patnumber_by_manufacturer_{}.txt'.format(pd.datetime.now().strftime("%Y-%m-%d %H-%M-%S")))


# ## Partnumbers by supplier

# In[16]:


df.groupby('supplier')['Partnumber'].count()


# ## total unique partnumbers by manufacturer is a long table. So its better to download as excel file:

# In[17]:


df.groupby('Manufacturer')['Partnumber'].nunique().to_excel('../data/raw_analysis/unique_partnumbers__manufacturer.xlsx')
#Save with timestamp
df.groupby('Manufacturer')['Partnumber'].nunique().to_csv('../data/text_output/unique_partnumbers__manufacturer_{}.txt'.format(pd.datetime.now().strftime("%Y-%m-%d %H-%M-%S")))


# ## Total Price (some prices have more than two decimal digits in the database):

# In[18]:


print('R$' + str(df.Price.sum()))


# ## The Total Price by manufacturer is a long table. So its better to download as excel file:

# In[19]:


(df.groupby('Manufacturer')['Price'].sum()).to_excel('../data/raw_analysis/price_by_manufacturer.xlsx')
#Save with timestamp
(df.groupby('Manufacturer')['Price'].sum()).to_csv('../data/text_output/price_by_manufacturer_{}.txt'.format(pd.datetime.now().strftime("%Y-%m-%d %H-%M-%S")))


# ## Total Price by supplier:

# In[20]:


df.groupby('supplier')['Price'].sum()


# ## Total quantity:

# In[21]:


df.Quantity.sum()


# ## The Total Quantity by manufacturer is a long table. So its better to download as excel file:

# In[22]:


df.groupby('Manufacturer')['Quantity'].sum().to_excel('../data/raw_analysis/quantity_by_manufacturer.xlsx')
#Save with timestamp
df.groupby('Manufacturer')['Quantity'].sum().to_csv('../data/text_output/quantity_by_manufacturer_{}.txt'.format(pd.datetime.now().strftime("%Y-%m-%d %H-%M-%S")))


# ## Total Quantity by supplier:

# In[23]:


df.groupby('supplier')['Quantity'].sum()


# ## Sum of zero quantity:

# In[24]:


df.Quantity[df.Quantity==0.0].count()


# ## The Total zero Quantity by manufacturer is a long table. So its better to download as excel file:

# In[25]:


df[df.Quantity==0.0].groupby('Manufacturer')['Quantity'].count().to_excel('../data/raw_analysis/quantity_zero_by_manufacturer.xlsx')
#Save with timestamp
df[df.Quantity==0.0].groupby('Manufacturer')['Quantity'].count().to_csv('../data/text_output/quantity_zero_by_manufacturer_{}.txt'.format(pd.datetime.now().strftime("%Y-%m-%d %H-%M-%S")))


# ## Total zero Quantity by supplier:

# In[26]:


df[df.Quantity==0.0].groupby('supplier')['Quantity'].count()


# ## Sum of zero Price:

# In[27]:


df.Price[df.Price==0.0].count()


# ## The Total zero Price by manufacturer is a long table. So its better to download as excel file:

# In[28]:


df[df.Price==0.0].groupby('Manufacturer')['Price'].count().to_excel('../data/raw_analysis/price_zero_by_manufacturer.xlsx')
#Save with timestamp
df[df.Price==0.0].groupby('Manufacturer')['Price'].count().to_csv('../data/text_output/price_zero_by_manufacturer_{}.txt'.format(pd.datetime.now().strftime("%Y-%m-%d %H-%M-%S")))


# ## Total zero Price by supplier:

# In[29]:


df[df.Price==0.0].groupby('supplier')['Price'].count()


# ## Quantity in blank:

# ### Note: for the all the blank analysis the aggregation (manufacturer, supplier) doesn't show the same count as there is blank values in both columns

# for this i'm using the original dataframe without the transformation of the data to numeric

# In[30]:


df2 = pd.read_csv('../data/merged_database/combined.csv'  , index_col=0)


# In[31]:


df2.Quantity.isna().sum()


# ## The blank zero Quantity by manufacturer is a long table. So its better to download as excel file:

# In[32]:


df2[df2.Quantity.isna()==True].groupby('Manufacturer')['Manufacturer'].count().to_excel('../data/raw_analysis/quantity_blank_by_manufacturer.xlsx')
#Save with timestamp
df2[df2.Quantity.isna()==True].groupby('Manufacturer')['Manufacturer'].count().to_csv('../data/text_output/quantity_blank_by_manufacturer_{}.txt'.format(pd.datetime.now().strftime("%Y-%m-%d %H-%M-%S")))


# ## Total Blank Quantity by supplier:

# In[33]:


df2[df2.Quantity.isna()==True].groupby('supplier')['supplier'].count()


# ## Price in blank:

# for this i'm using the original dataframe without the transformation of the data to numeric

# In[34]:


df2.Price.isna().sum()


# ## Blank zero Price by manufacturer :

# In[35]:


df2[df2.Price.isna()==True].groupby('Manufacturer')['Manufacturer'].count()


# ## Total Blank Price by supplier:

# In[36]:


df2[df2.Price.isna()==True].groupby('supplier')['supplier'].count()


# ## Manufacturer in blank:

# for this i'm using the original dataframe without the transformation of the data to numeric

# In[37]:


df2.Manufacturer.isna().sum()


# ## Total Blank Manufacturer by supplier:

# In[38]:


df2[df2.Manufacturer.isna()==True].groupby('supplier')['supplier'].count()


# ## Partnumber in blank:

# for this i'm using the original dataframe without the transformation of the data to numeric

# In[39]:


df2.Partnumber.isna().sum()


# ## Blank zero Partnumber by manufacturer :

# In[40]:


df2[df2.Partnumber.isna()==True].groupby('Manufacturer')['Manufacturer'].count()


# ## Total Blank Price by supplier:

# In[41]:


df2[df2.Partnumber.isna()==True].groupby('supplier')['supplier'].count()


# ## Quantity of strings in the field:

# In[42]:


print( 'Price: ' +  str(df2["Price"].apply(type).value_counts()[0]) + ' of ' + str(len(df2.Price)))
print( 'Quantity: ' +  str(df2["Quantity"].apply(type).value_counts()[0]) + ' of ' + str(len(df2.Quantity)))


# In[ ]:




