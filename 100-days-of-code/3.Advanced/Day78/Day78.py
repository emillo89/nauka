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

#how many prizes went to men compared to how many prizes went to women
sex = df_data.value_counts('sex')
print(sex)

fig = px.pie(labels=sex.index,
             values=sex.values,
             title='ercentage of Male vs. Female Winners',
             names=sex.index,
             hole=0.4)
fig.update_traces(textposition='inside',textfont_size=15, textinfo='percent')
fig.show()

"""# Who were the first 3 Women to Win the Nobel Prize?"""

#names of the first 3 female Nobel laureates
df_data[df_data.sex == 'Female'].sort_values('year', ascending=True)[:3]

#people get a Nobel Prize more than once
winner = df_data.duplicated(subset=['full_name'],keep=False)
multiply_winners = df_data[winner]
col_subset = ['year', 'category', 'laureate_type', 'full_name' ]
multiply_winners[col_subset]

"""# Number of Prizes per Category"""

# categories are prizes awarded
print(df_data.category.nunique())

prizes_per_category = df_data.category.value_counts()
print(prizes_per_category)

#number of prizes awarded by category
plt_bar = px.bar(x=prizes_per_category.index,
                 y=prizes_per_category.values,
                 color=prizes_per_category.values,
                 color_continuous_scale='Aggrnyl',
                 title='Number of Prizes Awarded per Category')
plt_bar.update_layout(xaxis_title='Nobel Prize Category',
                      yaxis_title='Number of Prizes')

plt_bar.show()

#first prize in the field of Economics award
df_data[df_data.category == 'Economics'].sort_values('year', ascending=True).head()

#Male and Female Winners by Category
men_women = df_data.groupby(['category', 'sex']).agg({'prize' : pd.Series.count})
print(men_women)
print(men_women.sort_values('prize', ascending=False))

import plotly.graph_objects as go
#https://plotly.com/python/categorical-axes/
male_cat = df_data.query('@df_data.sex == "Male"')['category'].value_counts()
female_cat = df_data.query('@df_data.sex == "Female"')['category'].value_counts()
fig = go.Figure(
    data=[
          go.Bar(name='Male', x=male_cat.index, y=male_cat.values),
          go.Bar(name='Female', x=female_cat.index, y=female_cat.values)
    ])
fig.update_layout(barmode='stack', xaxis_title="Catagory", yaxis_title="Amount of Awards Given")
fig.show()

"""# Number of Prizes Awarded Over Time"""

#Count the number of prizes awarded every year.
prize_per_year = df_data.groupby('year').count().prize
print(prize_per_year)

#5 year rolling average of the number of prizes
moving_average = prize_per_year.rolling(window=5).mean()
print(moving_average)

#Show a tick mark on the x-axis for every 5 years from 1900 to 2020.
plt.figure(figsize=(14,8))
plt.scatter(x=prize_per_year.index,
            y=prize_per_year.values,
            c='dodgerblue',
            alpha=0.7,
            s=100)
plt.plot(prize_per_year.index,
         moving_average.values,
         c='crimson',
         linewidth=3)

plt.show()

#little styling, this chart could look better
plt.figure(figsize=(16,8))
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5),
           fontsize=14,
           rotation=45)

ax = plt.gca()
ax.set_xlim(1900,2020)

ax.scatter(x=prize_per_year.index,
           y=prize_per_year.values,
           c='dodgerblue',
           alpha=0.7,
           s=100)
ax.plot(prize_per_year.index,
        moving_average.values,
        c='crimson',
        linewidth=3)
plt.show()

"""# Are More Prizes Shared Than Before?"""

print(df_data)

#Calculate the average prize share of the winners on a year by year basis.
yearly_avg_share = df_data.groupby('year').agg({'share_pct': pd.Series.mean})
print(yearly_avg_share)

#Calculate the 5 year rolling average of the percentage share
share_moving_average = yearly_avg_share.rolling(window=5).mean()

plt.figure(figsize=(16,8), dpi=200)
plt.title('Number od Nobel Prizes Awarded per year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5),
           fontsize=14,
           rotation=45)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_xlim(1900, 2020)

ax1.scatter(x=prize_per_year.index,
            y=prize_per_year.values,
            c='dodgerblue',
            alpha=0.7,
            s=100)
ax1.plot(prize_per_year.index,
         moving_average.values,
         c='crimson',
         linewidth=3)
ax2.plot(prize_per_year.index,
         share_moving_average.values,
         c='grey',
         linewidth=3)
plt.show()

plt.figure(figsize=(16,8), dpi=200)
plt.title('Number od Nobel Prizes Awarded per year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5),
           fontsize=14,
           rotation=45)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_xlim(1900, 2020)

#can invert axis
ax2.invert_yaxis()
ax1.scatter(x=prize_per_year.index,
            y=prize_per_year.values,
            c='dodgerblue',
            alpha=0.7,
            s=100)
ax1.plot(prize_per_year.index,
         moving_average.values,
         c='crimson',
         linewidth=3)
ax2.plot(prize_per_year.index,
         share_moving_average.values,
         c='grey',
         linewidth=3)
plt.show()


# ranking for the top 20 countries in terms of the number of prizes
top_countries = df_data.groupby(['birth_country_current'], as_index=False).agg({'prize': pd.Series.count})
top_countries.sort_values('prize', inplace=True)
top20_countries = top_countries[-20:]
print(top20_countries)

#create a horizontal bar chart showing the number of prizes won by each country
h_bar = px.bar(y=top20_countries.birth_country_current,
               x=top20_countries.prize,
               orientation='h',
               color=top20_countries.prize,
               color_continuous_scale='Viridis',
               title='Top 20 Countries by Number of Prizes'
               )
h_bar.update_layout(xaxis_title='Number of Prizes',
                    yaxis_title='Country',
                    coloraxis_showscale=False)
h_bar.show()

"""Choropleth Map to Show the Number of Prizes Won by Country"""

#Choropleth Map to Show the Number of Prizes Won by Country
df_countries = df_data.groupby(['birth_country_current', 'ISO'], as_index=False).agg({'prize':pd.Series.count})
df_countries.sort_values('prize', ascending=False)

#hover_name for example, Poland, Germany (name)
world_map = px.choropleth(df_countries,
                          locations='ISO',
                          color='prize',
                          hover_name='birth_country_current',
                          color_continuous_scale=px.colors.sequential.matter)
world_map.update_layout(coloraxis_showscale=True)
world_map.show()

"""# In Which Categories are the Different Countries Winning Prizes? """

# which categories made up the total number of prizes
cat_country = df_data.groupby(['birth_country_current','category'], as_index=False).agg({'prize': pd.Series.count})
cat_country.sort_values('prize',ascending=False)

merged_df = pd.merge(cat_country, top20_countries, on='birth_country_current')

print(merged_df)

#change column names
merged_df.columns = ['birth_country', 'category', 'cat_prize', 'total_prize']

merged_df.sort_values('total_prize', inplace=True)

print(merged_df)

cat_cntry_bar = px.bar(x=merged_df.cat_prize,
                     y=merged_df.birth_country,
                     color=merged_df.category,
                     orientation='h',
                     title='top 20 Countries by Number of Prize and Category')
cat_cntry_bar.update_layout(xaxis_title='Number of Prizes',
                            yaxis_title='Country')
cat_cntry_bar.show()



"""### Number of Prizes Won by Each Country Over Time"""

#number of prizes by country by year
prize_by_year = df_data.groupby(by=['birth_country_current','year'], as_index=False).count()
print(prize_by_year)

prize_by_year.sort_values('year')[['year','birth_country_current','prize']]

#cumulative sum for the number of prizes won
cumulative_prizes = prize_by_year.groupby(by=['birth_country_current','year']).sum().groupby(level=[0]).cumsum()
print(cumulative_prizes)

cumulative_prizes.reset_index(inplace=True)

l_chart =px.line(cumulative_prizes,
                 x='year',
                 y='prize',
                 color='birth_country_current',
                 hover_name='birth_country_current')
l_chart.update_layout(xaxis_title='Year',
                      yaxis_title='Number of Prizes')
l_chart.show()
