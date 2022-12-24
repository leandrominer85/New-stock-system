#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import glob
from cleaning_functions import *
import warnings
warnings.filterwarnings("ignore")

# Paths
# check if this is the same path used for raw_analysis
#path = r'C:/Users/jantu/Downloads/stock_system-221209/raw_stock-221206/*'
raw_combined = 'raw_combined.csv'

path = r'E:\Dropbox\Pessoal\Python\trabalho\Upwork\New-stock-system\data\originals/*'

# Get a list of files to read from the path
files = glob.glob(path)

# - Get the file path, the supplier_code (a key in the dictionary below)
# and the parameters of the dictionary below for each key. It checks the file extension and then uses the appropriate pandas function.

list1 = []

def read_file(file, supplier_code, header, special_operation):
        # Check if file is xls or xlsx
    if "xlsx" in file or "xls" in file.lower():
        df = pd.read_excel(
            io = Fr"{file}", 
            header = file_columns[supplier_code]["header"], 
            usecols = file_columns[supplier_code]["columns"]
            )[file_columns[supplier_code]["columns"]] # To maintain parsed columns orders if the dataframe require more special operations like adding blank columns or removing unwanted rows
        list1.append(file_columns[supplier_code])
        if file_columns[supplier_code]["special_operation"]:
            df = file_columns[supplier_code]["special_operation"](df)

        df.columns = ["Manufacturer", "Partnumber", "Quantity", "Price"]

        df["supplier"] = supplier_code

        #Check if file is csv or txt
    elif "csv" in file.lower() or "txt" in file.lower():
        df = pd.read_csv(
            file, 
            header = file_columns[supplier_code]["header"], 
            usecols = file_columns[supplier_code]["columns"],
            sep = ";|\|", 
            encoding = "ISO-8859-1", # This encoding is important to work with most of the files
            engine = "python" # This engine is to accept regex at sep parameter for csv with variety of delimiters
            )[file_columns[supplier_code]["columns"]] # To maintain parsed columns orders

        if file_columns[supplier_code]["special_operation"]:
            df = file_columns[supplier_code]["special_operation"](df)

        df.columns = ["Manufacturer", "Partnumber", "Quantity", "Price"]

        df["supplier"] = supplier_code

    else:
        print("unkown file formate: ", file)

    return df

# print("List1: ", list1)

# Dictionary to pass to the read function. For each file, it needs the header (where the column name is), the columns
# names and if any special operations is needed (the cleaning_functions functions)

file_columns = {
    "metal":    {    "header": 0, 
                    "columns": ["Fabricante", "Codigo_fornecedor", "quantity", "PRECO_LIQUIDO"],
                    "special_operation": None
                },

    "medauto":    {    "header": 0, 
                    "columns": ["Fornecedor", "NUMERO DA PEÇA", "ESTOQUE", "PREÇO"],
                    "special_operation": None
                },
    "lucios":     {    "header": 0, 
                    "columns": ["Fabricante", "Código Lucios", "Disponibilidade", "Preço"],
                    "special_operation": None
                },
    "carbwel":     {    "header": 0, 
                    "columns": ["Fabricante", "Código Fabricante", "Disponivel", "PrcVenda"],
                    "special_operation": None
                },
    "mte":     {    "header": 0, 
                    "columns": ["COD MTE", "QTD. ESTOQUE", "PREÇO"],
                    "special_operation": mte_process
                },
    "sueyasu":     {    "header": 0, 
                    "columns": ["NOME DO FABRICANTE", "CODIGO DA PEÇA (FABRICANTE)", "QUANTIDADE EM ESTOQUE", "PREÇO"],
                    "special_operation": sueyasu_process
                },
    "polipecas":{    "header": 2, 
                    "columns": ["COD. FORNECEDOR", "PREÇO"],
                    "special_operation": polipecas_process
                },
    "lucios":{        "header": 0, 
                    "columns": ["Fabricante", "Código Fábrica", "Disponibilidade", "Preço"],
                    "special_operation": None
                },
    "ima":{            "header": 3, 
                    "columns": ["Código","Preço C/Imp SP", "Múltiplos"],
                    "special_operation": ima_process
                },
    "compel":{        "header": 0, 
                    "columns": ["FABRICANTE", "COD FABRICA", "DISPONIBILIDADE", "PREÇO"],
                    "special_operation": compel_process
                },
    "rufato":{        "header": None, 
                    "columns": [5, 4, 3, 2],
                    "special_operation": None
                },
    "real":{        "header": 0, 
                    "columns": ["CODIGO_INTERNO", "COD_FABRICANTE","NOME_FANTASIA","PRODUTO",
                                "QTDE_EMB","UNIDADE_MEDIDA","QTDE_SPNORTE","PRECO_SPNORTE",
                                "QTDE_ABC","PRECO_ABC","QTDE_SPLESTE","PRECO_SPLESTE"],
                    "special_operation": real_process
                },
    "jahu":{        "header": 0, 
                    "columns": ['Marca','Cód.Fabricante', 'Preco','Disponivel',"Produto"],
                    "special_operation": jahu_process
                },
}

# Starts with an empty list that is populated with every data from the files list using the read_file function

all_df = []
for file in files:
    file_columns_keys = list(file_columns.keys())
    for supplier_code in file_columns_keys:
        if supplier_code in file.lower():
            print(file, "====", supplier_code, file_columns[supplier_code]["header"])
            all_df.append(read_file( #dataframes are added one by one and merged all at once
                file, 
                supplier_code, 
                header = file_columns[supplier_code]["header"], 
                special_operation = file_columns[supplier_code]["special_operation"]))
#print(list1)
#print("file_columns_keys :", file_columns_keys)

pd.concat(all_df, ignore_index = True).to_csv("../data/merged_database/combined.csv")

# save the output file in third_etl in the raw_stock folder, naming it with real_third_etl
pd.concat(all_df, ignore_index = True).to_csv("../data/raw_analysis/real_third_etl.csv")
