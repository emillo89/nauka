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

#Convert any strings in to Datetime objects.
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)

"""Converting from Daily to Monthly Data"""
#Convert any strings in to Datetime objects.
print(df_btc_price.DATE)
df_btc_monthly = df_btc_price.resample('M', on='DATE').last()
print(df_btc_monthly)

# Plot the Tesla stock price against the Tesla search volume using a line chart and two different axes
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(df_tesla.MONTH, df_tesla['TSLA_USD_CLOSE'])
ax2.plot(df_tesla.MONTH, df_tesla['TSLA_WEB_SEARCH'])

# Plot the Tesla stock price against the Tesla search volume using a line chart and two different axes
#with different colours
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_label('Year')
ax1.set_ylabel('TSLA Stock Price', color='#E6232E')
ax2.set_ylabel('Search Trend', color='skyblue')
ax1.plot(df_tesla.MONTH, df_tesla['TSLA_USD_CLOSE'], color='#E6232E')
ax2.plot(df_tesla.MONTH, df_tesla['TSLA_WEB_SEARCH'], color='skyblue')

#Increase the figure size, fontsize,linewidth, add title, min and max value on the axes
#register data converters to avoid warning message
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
plt.figure(figsize=(14,8), dpi=120)
plt.title('Tesla Wb Search vs Price', fontsize=16)
plt.xticks(rotation=45,fontsize=14 )
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
ax1.set_ylim([0,600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])
ax1.plot(df_tesla.MONTH, df_tesla['TSLA_USD_CLOSE'], color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla['TSLA_WEB_SEARCH'], color='skyblue', linewidth=3)
plt.show()

#Adding Locator Tick Marks
import matplotlib.dates as mdates
register_matplotlib_converters()
min = df_tesla.MONTH.min()
max = df_tesla.MONTH.max()

plt.figure(figsize=(14,8), dpi=120)
plt.title('Tesla Wb Search vs Price', fontsize=16)
plt.xticks(rotation=45,fontsize=14 )
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
ax1.set_ylim([0, 600])
ax1.set_xlim([min, max])
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
ax1.plot(df_tesla.MONTH, df_tesla['TSLA_USD_CLOSE'], color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla['TSLA_WEB_SEARCH'], color='skyblue', linewidth=3)

#Bitcoin (BTC) Price v.s. Search Volume
plt.figure(figsize=(14,8), dpi=120)
plt.title('Bitcoin News Search vs Resampled Price')
plt.xticks(fontsize=14, rotation=45)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_ylabel('BTC Price', color='#F08F2E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
#the linestyle and markers
ax1.set_ylim(bottom=0, top=15000)
ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])
ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE, color='#F08F2E', linewidth=3, linestyle='--')
ax2.plot(df_btc_monthly.index, df_btc_search.BTC_NEWS_SEARCH, color='skyblue', linewidth=3, marker='o')
plt.plot()
plt.show()

#Unemployement Benefits Search vs. Actual Unemployment in the U.S.
# grid lines as dark grey lines
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

plt.figure(figsize=(14,8), dpi=120)
plt.title('Monthly Search of "Unemployment Benfits" in the U.S. vs the U/E rate')
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_ylabel('Unemployment Benefits', color='purple')
ax2.set_ylabel('FRED u/E Rate', color='skyblue')
ax1.set_ylim(bottom=3, top=10.5)
ax1.set_xlim(df_unemployment.MONTH.min(), df_unemployment.MONTH.max())
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
ax1.grid(color='grey', linestyle='--')
ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE, color='purple', linewidth=3, linestyle='--')
ax2.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH, color='skyblue', linewidth=3)
plt.plot()

#Calculate the rolling average over a 6 month window
roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()

plt.figure(figsize=(14,8), dpi=120)
plt.title('Monthly Search of "Unemployment Benfits" in the U.S. vs the U/E rate')
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_ylabel('Unemployment Benefits', color='purple')
ax2.set_ylabel('FRED u/E Rate', color='skyblue')
ax1.set_ylim(bottom=3, top=10.5)
ax1.set_xlim(df_unemployment.MONTH.min(), df_unemployment.MONTH.max())
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
ax1.grid(color='grey', linestyle='--')
ax1.plot(df_unemployment.MONTH, roll_df.UNRATE, color='purple', linewidth=3, linestyle='--')
ax2.plot(df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, color='skyblue', linewidth=3)
plt.plot()
plt.show()

# Read the data in the 'UE Benefits Search vs UE Rate 2004-20.csv'
benefits_search = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-20.csv')
benefits_search.MONTH = pd.to_datetime(benefits_search.MONTH)
plt.figure(figsize=(14, 8),dpi=120)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14,rotation=45)
plt.title('Monthly US "Unemployment Benefits" Web Search vs Unrate')
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_ylabel('Fred U/E Rate', color='purple', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
ax1.set_xlim([benefits_search.MONTH.min(), benefits_search.MONTH.max()])
ax1.plot(benefits_search.MONTH, benefits_search.UNRATE, color='purple', linewidth=3, linestyle='--')
ax2.plot(benefits_search.MONTH, benefits_search.UE_BENEFITS_WEB_SEARCH, color='skyblue', linewidth=3)
plt.plot()