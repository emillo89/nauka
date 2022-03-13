from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import numpy as pd

pd.options.display.float_format = '{:,.2f}'.format

"""# Read the Data"""

data = pd.read_csv('cost_revenue_dirty.csv')

#How many rows and columns does the dataset contain
print(data.shape)

#NaN values
print(data.isna())
print(data.isna().values.any())

#duplicate rows
print(data.duplicated().values.any())

#len duplitated rows
print(len(data[data.duplicated()]))

#data types of the columns
print(data.info())

"""Data Type Conversions"""

#Convert the USD_Production_Budget, USD_Worldwide_Gross, and USD_Domestic_Gross columns to a numeric format by removing $ signs and ,.
print(data)

chars_to_remove = [',', '$']
columns_to_clean = ['USD_Production_Budget',
                    'USD_Worldwide_Gross',
                    'USD_Domestic_Gross']

for col in columns_to_clean:
  for char in chars_to_remove:
    #converting dtypes using astype
    data[col] = data[col].astype(str).str.replace(char,'')
  data[col] = pd.to_numeric(data[col])

print(data.head())

#Convert the Release_Date column to a Pandas Datetime type
print(data.info())

data['Release_Date'] = pd.to_datetime(data['Release_Date'])
print(data.head())
