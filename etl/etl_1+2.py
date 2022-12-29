#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re


# ## First ETL

# ### Function to clean strings:

# In[2]:


def string_cleaner(dataframe,col):
    
    """
    Remove all special characters, remove '&' and '-', remove double spaces and end and start string spaces.
    Return the cleaned Dataframe
    
    Inputs:
    
    dataframe : A pandas dataframe
    col : A collumn name as string
    
    """
    df[col] = df[col].str.lower().replace('[^a-zA-Z0-9]', '')
    df[col] = df[col].str.replace('[&-/]', ' ')
    df[col] = df[col].str.replace('  ', ' ')
    df[col] = df[col].str.strip()
    return df


# In[3]:


#Original DF
df = pd.read_csv('../data/merged_database/combined.csv' , index_col=0, dtype={'Quantity': str, 'Price': str})


# In[4]:


#Original size:
df.info()


# In[5]:


# Cleaning the two string cols:
string_cleaner(df,'Manufacturer')
string_cleaner(df,'Partnumber')


# ### Transforming the price col:

# In[6]:


df['Price'] = df['Price'].astype(str)
df['Price'] = df['Price'].apply(lambda x: x.replace(',','.'))
df['Price'] = pd.to_numeric(df['Price'],errors='coerce').round(2)


# ### Dics to alter the quantity col:

# In[7]:


compel = {"Indisponível" : '0',
'A': '3',
'B' : '15',
 'C': '20'}


# In[8]:


real = {'A' : '4',
'B' : '11'}


# In[9]:


# Changing compel
df[df.supplier == 'compel'] = df[df.supplier == 'compel'].replace(compel, regex=True)


# In[10]:


# Changing real
df[df.supplier == 'real'] = df[df.supplier == 'real'].replace(compel, regex=True)


# ### Modifying the Quantity col:

# In[11]:


# Replace '>' and white spaces
df.Quantity = df.Quantity.str.replace('>', '')
df.Quantity = df.Quantity.str.strip()


# In[12]:


#transforming to numeric
df.Quantity =pd.to_numeric(df['Quantity'],errors='coerce')


# In[13]:


# Creating the key col:
df['key'] = df.Manufacturer+df.Partnumber


# In[14]:


#Creating the pointer col:
df['pointer'] = df.supplier+df.Manufacturer+df.Partnumber


# In[15]:


# Size of the first etl dataframe
df.info()


# In[16]:


# Partnumber as string
df.Partnumber = df.Partnumber.astype(str)


# In[17]:


# Removing the dots in Partnumber
df.Partnumber = df.Partnumber.str.replace(".","")


# In[18]:


#Removing white space in Partnumber
df.Partnumber = df.Partnumber.str.strip()
df.Partnumber = df.Partnumber.str.replace(" ","")


# In[19]:


# Manufacturer as string
df.Manufacturer = df.Manufacturer.astype(str)


# In[20]:


# Removing the dots in Partnumber
df.Manufacturer = df.Manufacturer.str.replace(".","")


# In[21]:


#Removing white space in Partnumber
df.Manufacturer = df.Manufacturer.str.strip()
df.Manufacturer = df.Manufacturer.str.replace(" ","")


# In[22]:


#Removing white space in key
df.key = df.key.str.strip()
df.key = df.key.str.replace(" ","")


# In[23]:


#Removing white space in pointer
df.Partnumber = df.pointer.str.strip()
df.Partnumber = df.pointer.str.replace(" ","")


# In[24]:


# Fill Nans with 0
df = df.replace("", 0)
df = df.replace("nan",0)
df = df.fillna(0)


# In[25]:


# Removing empty Manufactures
df = df[df.Manufacturer != 0]


# In[26]:


df.to_csv('../data/etl/first_etl.csv')


# In[27]:


#Save with timestamp
df.to_csv('../data/text_output/first_etl{}.txt'.format(pd.datetime.now().strftime("%Y-%m-%d %H-%M-%S")))


# ## Second ETL (for each step i show the size of the modifield dataframe)

# In[28]:


#parts having a quantity equal to 0

df = df[df['Quantity'] !=0]


# In[29]:


df.info()


# In[30]:


df.supplier.value_counts()


# In[31]:


#parts having the quantity blank

df = df[df['Quantity'].isna() == False]


# In[32]:


df.info()


# In[33]:


df.supplier.value_counts()


# In[34]:


#parts having a negative quantity

df = df[df['Quantity'] > 0]


# In[35]:


df.info()


# In[36]:


#parts having a price equal to 0

df = df[df['Price'] != 0.]


# In[37]:


df.info()


# In[38]:


#parts having the price blank
df = df[df['Price'].isna() == False]


# In[39]:


df.info()


# In[40]:


#parts having the manufacturer blank
df = df[df['Manufacturer'].isna() == False]


# In[41]:


df.info()


# In[42]:


# parts have the partnumber blank
df = df[df['Partnumber'].isna() == False]


# In[43]:


df.info()


# In[44]:


# Read the synonyms data
syn = pd.read_excel("../data/synonyms/manufacturers_synonyms.xlsx")


# In[45]:


# for each entrie replace the values with the syn dataframe:
for n,i in enumerate(syn.name_to_be_replaced):
    df = df.replace(i,syn.iloc[n,1])


# In[ ]:





# In[46]:


df.to_csv('../data/etl/second_etl.csv')


# In[47]:


#Save with timestamp
df.to_csv('../data/text_output/second_etl{}.txt'.format(pd.datetime.now().strftime("%Y-%m-%d %H-%M-%S")))


# In[48]:


# save in excel
df.to_excel('../data/etl/second_etl.xlsx')


# In[ ]:




