import pandas as pd
import matplotlib.pyplot as plt

""" Read the Data"""

df_tesla = pd.read_csv('data/TESLA Search Trend vs Price.csv')
df_btc_search = pd.read_csv('data/Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('data/Daily Bitcoin Price.csv')
df_unemployment = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-19.csv')


#Tesla - data exploration

#shapes of the dataframes
print(df_tesla.shape)

#column names
print(df_tesla.columns)

#largest/smallest number in the search data column
web_search_max = df_tesla['TSLA_WEB_SEARCH'].max()

web_search_min = df_tesla['TSLA_WEB_SEARCH'].min()

print(f'Largest value for Tesla in Web Search: {web_search_max} ')
print(f'Smallest value for Tesla in Web Search: {web_search_min}')

#describe() function
print(df_tesla.describe())

"""### Unemployment Data"""

#uneployment - data exploration

print(df_unemployment.shape)

#max value
print(df_unemployment.columns)
benefits_max = df_unemployment['UE_BENEFITS_WEB_SEARCH'].max()
print(benefits_max)

print('Largest value for "Unemployemnt Benefits" '
      f'in Web Search: {benefits_max}')

"""### Bitcoin"""

#Bitcoin - data exploration
print(df_btc_price.shape)

print(df_btc_search.shape)

btc_search_max = df_btc_search['BTC_NEWS_SEARCH'].max()

print(f'largest BTC News Search: {btc_search_max} ')

"""Data Cleaning"""

#Finding the missing values
mis_tesla = df_tesla.isna().values.any()
mis_unemployment = df_unemployment.isna().values.any()
mis_btc_search = df_btc_search.isna().values.any()
mis_btc_price = df_btc_price.isna().values.any()

print(f'Missing values for Tesla?: {mis_tesla}')
print(f'Missing values for U/E?: {mis_unemployment}')
print(f'Missing values for BTC Search?: {mis_btc_search}')
print(f'Missing values for BTC price?: {mis_btc_price} ')

number_missing_value = df_btc_price.isna().values.sum()
print(f'Number of missing values: {number_missing_value}')

"""Remove any missing values that you found."""
#Remove any missing values that you found.
print(df_btc_price[df_btc_price.CLOSE.isna()])

df_btc_price.dropna(inplace=True)
df_btc_price[df_btc_price.CLOSE.isna()]

"""Converting from Daily to Monthly Data"""
#Convert any strings in to Datetime objects.
print(df_btc_price.DATE)
df_btc_monthly = df_btc_price.resample('M', on='DATE').last()
print(df_btc_monthly)