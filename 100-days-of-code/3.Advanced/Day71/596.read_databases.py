# -*- coding: utf-8 -*-
"""Day71.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qsz9DcDAZhhtbgmdPmMPSvhfUhUFllOU
"""

import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')

#read 5 first rows
print(df.head())

#How many rows and columns dataframes have
print(df.shape)

#names of columns
print(df.columns)

#look for NaN values
print(df.isna())

#last 5 rows in database
print(df.tail())

#delete the last row in databes
clean_df = df.dropna()
print(clean_df.tail())

print(df.tail())

