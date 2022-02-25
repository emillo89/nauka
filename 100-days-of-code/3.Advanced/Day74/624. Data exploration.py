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
