from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import pandas as pd
import matplotlib.pyplot as plt

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

"""Convert the `Release_Date` column to a Pandas Datetime type. """

#Convert the Release_Date column to a Pandas Datetime type
print(data.info())

data['Release_Date'] = pd.to_datetime(data['Release_Date'])
print(data.head())

"""Descriptive Statistics"""

#average production budget of the films [mean]
print(data.describe())

#average worldwide gross revenue of films [mean]
print(data.describe())

#minimums for worldwide and domestic revenue
print(data[data.USD_Production_Budget == 1100])

print(data[(data.USD_Production_Budget < 5000000) & (data.USD_Worldwide_Gross > data.USD_Production_Budget)])

#highest production budget and highest worldwide gross revenue of any film
print(data[data.USD_Production_Budget == 425000000])

"""Investigating the Zero Revenue Films"""

#How many films grossed $0 domestically (i.e., in the United States)? What were the highest budget films that grossed nothing
print(data[data.USD_Domestic_Gross == 0].count())

"""**Challenge**: How many films grossed $0 worldwide? What are the highest budget films that had no revenue internationally?"""

#What were the highest budget films that grossed nothing?
zero_domestic = data[data.USD_Domestic_Gross == 0]
print(zero_domestic.sort_values('USD_Production_Budget', ascending=False))

#No worldwide revenue
zero_worldwide = data[data.USD_Worldwide_Gross == 0]
print(zero_worldwide.sort_values('USD_Production_Budget', ascending=False))
