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

"""# The Effect of Handwashing"""

# Date when handwashing was made mandatory
handwashing_start = pd.to_datetime('1847-06-01')

#"pct_deaths" to df_monthly that has the percentage of deaths per birth for each row.
df_monthly['pct_deaths'] = df_monthly.deaths/df_monthly.births

before_washing = df_monthly[df_monthly.date < handwashing_start]
after_washing = df_monthly[df_monthly.date >= handwashing_start]

print(before_washing)
print(after_washing)

#The death rate per birth before and after handwashing
before_rate = before_washing.deaths.sum() / before_washing.births.sum()
after_rate = after_washing.deaths.sum() / after_washing.births.sum()

print(f"Average death rate before 1847 was {before_rate:.4}%")
print(f"Average death rate after 1847 was {after_rate:.3}%")

#6 month rolling average death rate prior to mandatory handwashing
roll_df = before_washing.set_index('date')
print(roll_df)
roll_df = roll_df.rolling(window=6).mean()
print(roll_df)

#to plot the monthly death rates
plt.figure(figsize=(14,8), dpi=200)
plt.title('Percentage of Monthly Deaths over Time', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

plt.ylabel('Percentage of deaths',color='crimson', fontsize=18)

ax = plt.gca()
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)
ax.set_xlim([df_monthly.date.min(), df_monthly.date.max()])

plt.grid(color='grey', linestyle='--')

ma_line = plt.plot(roll_df.index,
                   roll_df.pct_deaths,
                   color='crimson',
                   linewidth=3,
                   linestyle='--',
                   label='6m Moving Average')
bw_line = plt.plot(before_washing.date,
                   before_washing.pct_deaths,
                   color='black',
                   linewidth=1,
                   linestyle='--',
                   label='before Handwashing')
aw_line = plt.plot(after_washing.date,
                   after_washing.pct_deaths,
                   color='skyblue',
                   linewidth=3,
                   marker='o',
                   label='After handwashing')
plt.legend([ma_line, bw_line, aw_line], fontsize=18)
plt.show()

"""### Statistics - Calculate the Difference in the Average Monthly Death Rate"""

#Difference in the Average Monthly Death Rate
avg_before_hand = before_washing.pct_deaths.mean() * 100
avg_after_hand = after_washing.pct_deaths.mean() * 100
mean_diff = avg_before_hand - avg_after_hand
times = avg_before_hand / avg_after_hand

print(f"Chance of death during childbirth before handwashing {avg_before_hand:.3}%!")
print(f"Handwashing reduced the monthly proportion ofdeaths by {mean_diff:.3}%.")
print(f"This is a {times:.2}x improvement!")

"""### Use Box Plots to Show How the Death Rate Changed Before and After Handwashing"""

#add a column to df_monthly that shows if a particular date was before or after the start of handwashing.
df_monthly['washing_hands'] = np.where(df_monthly.date < handwashing_start,'No','Yes')
print(df_monthly)

#box plot of the data before and after handwashing
box = px.box(df_monthly,
             x='washing_hands',
             y='pct_deaths',
             color='washing_hands',
             title='How Have the Stats Changed with Handwashing?'
             )
box.update_layout(xaxis_title='Washing Hands?',
                  yaxis_title='Percentage of Monthly Deaths')
box.show()

"""### Use Histograms to Visualise the Monthly Distribution of Outcomes"""

#Histograms to Visualise the Monthly Distribution of Outcomes
hist = px.histogram(df_monthly,
                    x='pct_deaths',
                    color='washing_hands',
                    nbins=30,
                    opacity=0.6,
                    barmode='overlay',
                    histnorm='percent',
                    marginal='box'
                    )
hist.update_layout(xaxis_title='Proportion of MonthlyDeaths',
                   yaxis_title='Count')
hist.show()



"""### Use a Kernel Density Estimate (KDE) to visualise a smooth distribution"""

#two kernel density estimates of the pct_deaths, one for before handwashing and one for after.
plt.figure(dpi=200)
sns.kdeplot(before_washing.pct_deaths, shade=True)
sns.kdeplot(after_washing.pct_deaths, shade=True)
plt.title('Est. Distribution of monthly death arate before and after handwashing')
plt.show()

#without minus pct_deaths
plt.figure(dpi=200)
sns.kdeplot(before_washing.pct_deaths,
            shade=True,
            #start 0
            clip=(0,1))
sns.kdeplot(after_washing.pct_deaths,
            shade=True,
            clip=(0,1))
plt.title('Est. Distribution of monthly death arate before and after handwashing')
plt.xlim(0, 0.40)
plt.show()

"""### Use a T-Test to Show Statistical Significance"""

import scipy.stats as stats

t_stat, p_value = stats.ttest_ind(a=before_washing.pct_deaths,
                                  b=after_washing.pct_deaths)
print(f'p-value is {p_value:.10f}')
print(f't-statistic is {t_stat:.4}')