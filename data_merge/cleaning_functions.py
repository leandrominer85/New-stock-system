import pandas as pd
import numpy as np

# Functions to initially process the dataframes that need some work:
'''
suppliers that are manufacturers: mte, ima
added hard coded "bosch" for Polipecas 
'''

def mte_process(df):
        
    # Remove first row as it is empty
    df.drop(    index=df.index[0], 
                axis=0, 
                inplace=True)
    df["COD MTE"] =df["COD MTE"].str.replace("R","")

    df.rename({'COD MTE' : 'Partnumber', 'PREÇO' : 'Price' ,
               'QTD. ESTOQUE':'Quantity'}, axis=1, inplace= True)
    
    df['Manufacturer'] = 'mte'
    
    df= df[["Manufacturer", "Partnumber", "Quantity", "Price"]]
    
    return df

def sueyasu_process(df):
    # Remove first row (unwanted data)
    df.drop(    index=df.index[0], 
                axis=0, 
                inplace=True)
    return df

def polipecas_process(df): 
    ###WHAT IF THERE IS ZERO IN THE BEGINNING OF PART NUMBER

    # Add manufacturer column and hard coding "bosch" in it
    df.insert(    loc=0, 
                column='new col', 
                value=['bosch' for i in range(df.shape[0])])

    # Add empty quantity column
    df.insert(    loc=2, 
                column='new col2', 
                value=['' for i in range(df.shape[0])])
    # Insert zeros in the dataframe Price col
    df.Price = 0
    return df

def ima_process(df):
    
    df.rename({'Código' : 'Partnumber',
               'Múltiplos':'Quantity', "Preço C/Imp SP":"Price"}, axis=1, inplace= True)
    
    df['Manufacturer'] = 'ima'
    df= df[["Manufacturer", "Partnumber", "Quantity", "Price"]]

    return df

def compel_process(df):
    # Remove first row (unwanted data)
    df.drop(    index=df.index[:2], 
                axis=0, 
                inplace=True)
    return df

def jahu_process(df):
    
    
    df2 = df[df["Marca"] == 'JAHU PLACA PRETA              ']
    df2["Cód.Fabricante"] = df2["Produto"]
    df[df.Marca == 'JAHU PLACA PRETA              '] = df2

    df.rename({'Marca': 'Manufacturer',
               'Cód.Fabricante' : 'Partnumber', 'Preco' : 'Price' ,
               'Disponivel':'Quantity'}, axis=1, inplace= True)
    
    df= df[["Manufacturer", "Partnumber", "Quantity", "Price"]]
    
    
    return df

def real_process(df):
    
    
        #Coding the prices
    real = {'A' : '4',
    'B' : '11'}

    # Changing real
    df = df.replace(real, regex=True)

    #Selecting the collumns and assing to a new df
    cols= ['QTDE_SPNORTE' ,'PRECO_SPNORTE','QTDE_ABC','PRECO_ABC','QTDE_SPLESTE','PRECO_SPLESTE']
    df2 = df[cols]
    
    #coding as strings
    df2[cols] = df2[cols].astype(str)
    
    # Replacing the commas
    for col in cols:
        df2[col] = df2[col].apply(lambda x: x.replace(',','.'))
        
    #Transforming to numeric
    df2[cols] = df2[cols].apply(pd.to_numeric, errors='coerce')
    
    #replace all zeros with NaN values
    prices= ['PRECO_SPNORTE','PRECO_ABC','PRECO_SPLESTE']
    df2[prices] = df2[prices].replace(0.0, np.nan)
    
    #Get a list with the minimum values
    minimun = df2[['PRECO_SPNORTE','PRECO_ABC','PRECO_SPLESTE']].min(axis=1)
    
    
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
        
    df['sumed_quantity_for_best_price_only'] = quantities
    df['best_price_with_stock'] = prices
    
    
    df.rename({'NOME_FANTASIA': 'Manufacturer',
               'COD_FABRICANTE' : 'Partnumber', 'best_price_with_stock' : 'Price' ,
               'sumed_quantity_for_best_price_only':'Quantity'}, axis=1, inplace= True)

    df= df[["Manufacturer", "Partnumber", "Quantity", "Price"]]

    
    
    return df


