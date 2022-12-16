[![author](https://img.shields.io/badge/author-LeandroMinervino-red.svg)](https://www.linkedin.com/in/leandro-minervino-b469681b/) [![](https://img.shields.io/badge/python-3.7.12+-blue.svg)](https://www.python.org/downloads/release/python-365/) 

# New-stock-system

## Contents

```
│   README.md
├───data
│   ├───etl
│   │       first_etl.csv
│   │       second_etl.csv
│   │       
│   ├───merged_database
│   │       combined.csv
│   │       
│   ├───originals
│   │       00-Prod_Metal_001.xlsx
│   │       ARQUIVO-RUFATO-29-11-2022-HR12-00.TXT
│   │       Arquivo_Compel-29-11-22.csv
│   │       Estoque Carbwel 20 10 22 Karhub.xls
│   │       Estoque IMA CONEXÃO 29.11.2022.xlsx
│   │       Estoque real 29 11.csv
│   │       estoque_jahu_20221129.csv
│   │       medauto_stock_220916.xlsx
│   │       MTE_ESTOQUE_INTERNET-2.XLSX
│   │       NISSI - LISTA DE PREÇO KARHUB.xls
│   │       paccini_stock_220909.xlsx
│   │       polipecas_stock_220919.xlsx
│   │       Relatorio-lucios.xls
│   │       Sueyasu - 27-09-22.xlsx
│   │       
│   └───raw_analysis
│           patnumber_by_manufacturer.xlsx
│           price_by_manufacturer.xlsx
│           price_zero_by_manufacturer.xlsx
│           quantity_blank_by_manufacturer.xlsx
│           quantity_by_manufacturer.xlsx
│           quantity_zero_by_manufacturer.xlsx
│           unique_manufacturer.xlsx
│           
├───data_merge
│   │   cleaning_functions.ipynb
│   │   cleaning_functions.py
│   │   main.ipynb
│   │   main.py
│   │   
│   ├───.ipynb_checkpoints
│   │       main-checkpoint.ipynb
│   │       
│   └───__pycache__
│           cleaning_functions.cpython-39.pyc
│           
├───etl
│   │   etl_1+2.ipynb

│           
├───raw_analysis
│   │   raw_analysis.html
│   │   raw_analysis.ipynb
           
```

## How to use

### Data Merge

There are two programs : cleaning_functions and main.
The cleaning_functions is a repository for the functions that provide the read process for the main function (when the file need). It only needs further modification if more data is added or some entry is modified.

The main function reads the cleaning_functions functions and receives a list of data provided in the folder data/originals. With this it proceed to read each file accordingly to its format and the parameters provided by the dictionary inside the file. Then it saves a combined dataframe in the folder merged_database with the columns: "Manufacturer", "Partnumber", "Quantity", "Price".

For further modification one needs to add a new entry in the file_columns dictionary as this example:

```
"sueyasu":     {    "header": 0, 
                    "columns": ["NOME DO FABRICANTE", "CODIGO DA PEÇA (FABRICANTE)", "QUANTIDADE EM ESTOQUE", "PREÇO"],
                    "special_operation": sueyasu_process
                }
```        
Where the header the indicator if there is or not a header in the file, the columns are the original names of the file columns to be used and the special operation is only used if some function of the cleaning_functions is needed for that file







## Software & Libraries

Python 3 and the following libraries:

-   [Pandas](http://pandas.pydata.org/)
-   [glob](https://docs.python.org/3/library/glob.html)
-   [re](https://docs.python.org/3/library/re.html)
-   [Numpy](https://numpy.org/)


-   [plotly](https://plotly.com/)


**My Links:**
* [LinkedIn](https://www.linkedin.com/in/leandro-minervino-b469681b/)
* [Medium](https://medium.com/@leandro-minervino)
