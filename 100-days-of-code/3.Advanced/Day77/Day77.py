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

"""Filtering on Multiple Conditions"""

#Filtering on Multiple Conditions
international_releases = data.loc[(data.USD_Domestic_Gross == 0) & (data.USD_Worldwide_Gross != 0)]
print(international_releases)

#.query() function to accomplish the same thing
international_releases = data.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
print(international_releases)

#Unreleased Films
# Date of Data Collection
scrape_date = pd.Timestamp('2018-5-1')
print(scrape_date)

# Which films were not released yet as of the time of data collection (May 1st, 2018).
data.sort_values('Release_Date', ascending=False)

#How many films are included in the dataset that have not yet
print(len(data[data.Release_Date >= scrape_date]))
future_releases = data[data.Release_Date >= scrape_date]
print(future_releases)

#or data.loc[(data.Release_Date >= scrape_date)]

#data_clean that does not include these films
data_clean = data.drop(future_releases.index)
print(data_clean)

"""Films that Lost Money"""
#What is the percentage of films where the production costs exceeded the worldwide gross revenue?
print(data_clean.describe())

money_losing = data_clean.loc[data_clean.USD_Production_Budget > data_clean.USD_Worldwide_Gross]
print(len(money_losing))

#percentage money losing
percentage = money_losing.shape[0] / data_clean.shape[0]
print(percentage)

"""# Seaborn for Data Viz: Bubble Charts"""

#Seaborn for Data Viz: Bubble Charts
import seaborn as sns

"""### Plotting Movie Releases over Time"""

#create the following Bubble Chart:
plt.figure(figsize=(8,4), dpi=200)
sns.scatterplot(data=data_clean,
               x='USD_Production_Budget',
               y='USD_Worldwide_Gross')

plt.figure(figsize=(8,4), dpi=200)
ax = sns.scatterplot(data=data_clean,
               x='USD_Production_Budget',
               y='USD_Worldwide_Gross',
               #color
               hue = 'USD_Worldwide_Gross',
               #size
               size='USD_Worldwide_Gross')
ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions')
plt.show()

plt.figure(figsize=(8,4), dpi=200)
#set styling on a single chart
with sns.axes_style('darkgrid'):
  ax = sns.scatterplot(data=data_clean,
               x='USD_Production_Budget',
               y='USD_Worldwide_Gross',
               #color
               hue = 'USD_Worldwide_Gross',
               #size
               size='USD_Worldwide_Gross')
  ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions')
plt.show()

#
plt.figure(figsize=(8,4), dpi=200)
ax = sns.scatterplot(data=data_clean,
               x='Release_Date',
               y='USD_Production_Budget',
               #color
               hue = 'USD_Worldwide_Gross',
               #size
               size='USD_Worldwide_Gross')
ax.set(ylim=(0, 450000000),
       xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
       ylabel='Budget in $100 milliones',
       xlabel='Year')
plt.show()


#Create a DatetimeIndex object
dt_index = pd.DatetimeIndex(data_clean.Release_Date)
print(dt_index)
years = dt_index.year
print(years)

#Create new column = Decade
decades = years//10*10
data_clean['Decade'] = decades

"""Separate the "old" (before 1969) and "New" (1970s onwards) Films"""

#create new dataFrame old_movie < 1970
print(data_clean)
old_films = data_clean[data_clean.Decade <= 1960]

#create new dataFrame new_films
new_films = data_clean[data_clean.Decade > 1960]

#How many films were released prior to 1970?
old_films.describe()

#What was the most expensive film made prior to 1970?
print(old_films.sort_values('USD_Production_Budget', ascending=False).head())
