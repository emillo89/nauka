

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/colors.csv')
print(df)

#How many different colours does the LEGO company produce?
print(df['name'].nunique())

"""**Challenge**: Find the number of transparent colours where <code>is_trans == 't'</code> versus the number of opaque colours where <code>is_trans == 'f'</code>. See if you can accomplish this in two different ways."""

#Find the number of transparent colours where is_trans == 't'
#1 method
print(df.groupby('is_trans').count())

#2 method
print(df.is_trans.value_counts())

#Read the sets.csv data
df = pd.read_csv('data/sets.csv')

#the first and last couple of rows
print(df.head())
print(df.tail())

"""**Challenge**: In which year were the first LEGO sets released and what were these sets called?"""
print(df.sort_values('year').head())

"""**Challenge**: How many different sets did LEGO sell in their first year? 
How many types of LEGO products were on offer in the year the company started?"""

#How many different sets did LEGO sell in their first year? 
print(df[df['year'] == 1949])

"""**Challenge**: Find the top 5 LEGO sets with the most number of parts. """

#Find the top 5 LEGO sets with the most number of parts.
print(df.sort_values('num_parts', ascending=False).head())

"""**Challenge**: Use <code>.groupby()</code> and <code>.count()</code> to show the number of LEGO sets released year-on-year. How do the number of sets released in 1955 compare to the number of sets released in 2019? """

#show the number of LEGO sets released year-on-year.
sets_by_year = df.groupby('year').count()

print(sets_by_year.set_num.head())
print(sets_by_year.set_num.tail())

"""**Challenge**: Show the number of LEGO releases on a line chart using Matplotlib. <br>
<br>
Note that the .csv file is from late 2020, so to plot the full calendar years, you will have to exclude some data from your chart. Can you use the slicing techniques covered in Day 21 to avoid plotting the last two years? The same syntax will work on Pandas DataFrames. 
"""

#Show the number of LEGO releases on a line chart using Matplotlib.
plt.plot(sets_by_year.index,sets_by_year.set_num)
plt.plot(sets_by_year.index[:-2],sets_by_year.set_num[:-2])

"""### Aggregate Data with the Python .agg() Function

Let's work out the number of different themes shipped by year. This means we have to count the number of unique theme_ids per calendar year.
"""

# number of different themes shipped by year. This means we have to count the number of unique theme_ids per calendar year.
r = df.groupby('year')['theme_id'].nunique()
print(r)

# number of different themes shipped by year. This means we have to count the number of unique theme_ids per calendar year.
#agg method
themes_by_year = df.groupby('year').agg({'theme_id':'nunique'})

themes_by_year

"""**Challenge**: Plot the number of themes released by year on a line chart. Only include the full calendar years (i.e., exclude 2020 and 2021). """

#Plot the number of themes released by year on a line chart. Only include the full calendar years (i.e., exclude 2020 and 2021).
plt.plot(themes_by_year.index[-2:], themes_by_year.theme_id[-2:])
plt.plot(r.index[-2:], r.values[-2:])
plt.plot(themes_by_year.index, themes_by_year.theme_id)
plt.show()
"""### Line Charts with Two Seperate Axes"""

# to configure and plot our data on two separate axes on the same chart.
sets_by_year = df.groupby('year').count()
themes_by_year = df.groupby('year').agg({'theme_id':'nunique'})

"""**Challenge**: Use the <code>.groupby()</code> and <code>.agg()</code> function together to figure out the average number of parts per set. How many parts did the average LEGO set released in 1954 compared to say, 2017?"""

#Line Charts with Two Seperate Axes
#gca - get current axis
#twinx - crate another axis that shares the same x-axis
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='b')
ax2.plot(themes_by_year.index[:-2], themes_by_year.theme_id[:-2], color='g')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of sets', color='green')
ax2.set_ylabel('Number of Themes', color='blue')

"""### Scatter Plots in Matplotlib

**Challenge**: Has the size and complexity of LEGO sets increased over time based on the number of parts? Plot the average number of parts over time using a Matplotlib scatter plot. See if you can use the [scatter plot documentation](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.scatter.html) before I show you the solution. Do you spot a trend in the chart?
"""

#Scatter Plots in Matplotlib
#as the size and complexity of LEGO sets increased over time based on the number of parts? 
parts_per_set = df.groupby('year').agg({'num_parts': 'mean'})
print(parts_per_set)

plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
plt.show()
"""### Number of Sets per LEGO Theme

LEGO has licensed many hit franchises from Harry Potter to Marvel Super Heros to many others. But which theme has the largest number of individual sets?
"""

#Number of Sets per LEGO Theme
theme = df['theme_id'].value_counts()
print(theme)

#Explore the themes.csv. How is it structured? Search for the name 'Star Wars'. 
#How many ids correspond to this name in the themes.csv?
themes = pd.read_csv('data/themes.csv')

print(themes.head())

themes[themes.name == 'Star Wars']

print(df[df.theme_id == 18])
print(df[df.theme_id == 209])

"""### Merging (i.e., Combining) DataFrames based on a Key"""

#Merging sets and themes DataFrames (df = sets.csv, themes= themes.csv)
#Merge two dataframes
#example merged
merged_df = pd.merge(left=df, right=themes, left_on='theme_id', right_on='id')
print(merged_df)

set_theme_count = df['theme_id'].value_counts()
set_theme_count = pd.DataFrame({'id':set_theme_count.index, 'set_count': set_theme_count.values})
merged_df = pd.merge(set_theme_count, themes, on='id')
print(merged_df)

#Creating a Bar Chart
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.xlabel('Nr of sets', fontsize=14)
plt.ylabel('Theme Name', fontsize=14)
plt.bar(merged_df.name[:10], merged_df.set_count[:10] )
plt.show()