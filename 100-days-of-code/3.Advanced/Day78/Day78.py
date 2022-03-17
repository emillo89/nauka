# Commented out IPython magic to ensure Python compatibility.
#upgrade plotly - google colab notebook
# %pip install --upgrade plotly

"""### Import Statements"""

import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

"""Notebook Presentation"""

pd.options.display.float_format = '{:,.2f}'.format

"""Read the Data"""

df_data = pd.read_csv('nobel_prize_data.csv')

#shape
print(df_data.shape)

#column names
print(df_data.columns)

#year was the Nobel prize first awarded
print(df_data.sort_values('year', ascending=True))

#latest year included in the dataset
print(df_data.sort_values('year', ascending=True).tail())

"""Check for Duplicates"""

#duplicate values in the dataset
print(df_data.duplicated().values.any())

"""### Check for NaN Values"""

#NaN values
print(df_data.isna().values.any())

#columns tend to have NaN values
print(df_data.isna().any())

# NaN values are there per column
print(df_data.isna().sum())

#Why do these columns have NaN values?
col_subset = ['year', 'category','laureate_type', 'birth_date',
              'full_name', 'organization_name']
df_data.loc[df_data.birth_date.isna()][col_subset]

"""Convert Year and Birth Date to Datetime"""

#Convert the birth_date column to Pandas Datetime objects
df_data.birth_date = pd.to_datetime(df_data.birth_date)

#Add a Column with the Prize Share as a Percentage
separated_values = df_data.prize_share.str.split('/', expand=True)
numerator = pd.to_numeric(separated_values[0])
denomenator = pd.to_numeric(separated_values[1])
df_data['share_pct'] = numerator / denomenator

print(df_data.share_pct)