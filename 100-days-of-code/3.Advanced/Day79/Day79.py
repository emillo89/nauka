"""### Import Statements"""

import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

"""### Notebook Presentation"""

pd.options.display.float_format = '{:,.2f}'.format

# Create locators for ticks on the time axis
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

"""### Read the Data"""

df_yearly = pd.read_csv('annual_deaths_by_clinic.csv')
# parse_dates avoids DateTime conversion later
df_monthly = pd.read_csv('monthly_deaths.csv',
                      parse_dates=['date'])

#shape of df_yearly and df_monthly
print(df_yearly.shape)
print(df_monthly.shape)

#columns name
print(df_yearly.columns)
print(df_monthly.columns)

#Which years are included in the dataset?
print(df_yearly.head())
print(df_yearly.tail())
print(df_monthly.head())
print(df_monthly.tail())

"""### Check for Nan Values and Duplicates"""
#Check for Nan Values and Duplicates
print(df_yearly.info())
print(df_monthly.info())

print(df_yearly.duplicated().values.any())
print(df_monthly.duplicated().values.any())

"""### Percentage of Women Dying in Childbirth"""
print(df_yearly)

prob = df_yearly.deaths.sum() / df_yearly.births.sum() * 100
print(f'Chances of dying in the 1840s in Vienna: {prob:.3}%')

"""# Visualise the Total Number of Births and Deaths over Time"""

#Total Number of Births and Deaths over Time
plt.figure(figsize=(14,8),dpi=200)
plt.title('Total Number of Monthly Births and Deaths', fontsize=18)
ax1=plt.gca()
ax2=ax1.twinx()
ax1.grid(color='grey', linestyle='--')
ax1.plot(df_monthly.date,
         df_monthly.births,
         color='skyblue',
         linewidth=3)
ax2.plot(df_monthly.date,
         df_monthly.deaths,
         color='crimson',
         linewidth=2,
         linestyle='--')
plt.show()

#To get the tickmarks showing up on the x-axis, we need to use mdates
#Create locators for ticks on the time axis
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

plt.figure(figsize=(14,8), dpi=200)
plt.title('Total Number of Monthly Births and Deaths', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('Births', color='skyblue', fontsize=18)
ax2.set_ylabel('Deaths', color='crimson', fontsize=18)

#use locators
ax1.set_xlim([df_monthly.date.min(), df_monthly.date.max()])
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.grid(color='grey', linestyle='--')

ax1.plot(df_monthly.date,
         df_monthly.births,
         color='skyblue',
         linewidth=3)
ax2.plot(df_monthly.date,
         df_monthly.deaths,
         color='crimson',
         linewidth=2,
         linestyle='--')
plt.show()


"""# The Yearly Data Split by Clinic"""

#create line charts of the births and deaths of the two different clinics at the Vienna General Hospital.
print(df_yearly)

line = px.line(df_yearly,
               x='year',
               y='births',
               color='clinic',
               title='Total Yearly Births by Clinic')
line.show()

line = px.line(df_yearly,
              x='year',
              y='deaths',
              color='clinic',
              title='Total Yearly Deaths by Clinic')
line.show()

"""### Calculate the Proportion of Deaths at Each Clinic"""

#percentage of deaths for each row in the df_yearly
df_yearly['pct_deaths'] = df_yearly.deaths/ df_yearly.births
print(df_yearly)

#The average death rate for the entire time period for clinic 1 and 2
clinic_1 = df_yearly[df_yearly.clinic == 'clinic 1']
avg_clinic_1 = clinic_1.deaths.sum() / clinic_1.births.sum() * 100
clinic_2 = df_yearly[df_yearly.clinic == 'clinic 2']
avg_clinic_2 = clinic_2.deaths.sum() / clinic_2.births.sum() * 100
print(f'Average death rate in clinic 1 is {avg_clinic_1:.3}%')
print(f'Average death rate in clinic 2 is {avg_clinic_2:.3}%')

"""### Plotting the Proportion of Yearly Deaths by Clinic"""

line = px.line(df_yearly,
               x='year',
               y='pct_deaths',
               color='clinic',
               title='proportion of Yearly deaths by Clinic')
line.show()
