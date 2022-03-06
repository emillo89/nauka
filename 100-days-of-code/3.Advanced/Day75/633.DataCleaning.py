import pandas as pd

"""Notebook Presentation"""

# Show numeric output in decimal format e.g., 2.15
pd.options.display.float_format = '{:,.2f}'.format

"""Read the Dataset"""

df_apps = pd.read_csv('apps.csv')

"""Data Cleaning"""

print(df_apps.shape)

df_apps.head()

#sample(5) - method will give us 5 random rows
print(df_apps.sample(5))

"""Drop Unused Columns"""

#Remove the columns called Last_Updated and Android_Version from the DataFrame
df_apps.drop(columns=['Last_Updated', 'Android_Ver'])

"""Find and Remove NaN values in Ratings"""

#find NaN value
nan_rows = df_apps[df_apps.isna()]

print(nan_rows.shape)
print(nan_rows.head())

#drop NaN value
df_apps_clean = df_apps.dropna()
print(df_apps_clean.shape)
print(df_apps_clean.head())

"""Find and Remove Duplicates"""

#Check for duplicates
print(df_apps_clean.duplicated())

#show duplicates in the data
duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
print(duplicated_rows)

#check for an individual app
print(df_apps_clean[df_apps_clean.App == 'Instagram'])

#drop duplicates 
df_apps_clean = df_apps_clean.drop_duplicates()

print(df_apps_clean[df_apps_clean.App == 'Instagram'])
print(df_apps_clean.shape)

#subset for indentifying duplicates
df_apps_clean = df_apps_clean.drop_duplicates(subset=['App', 'Type', 'Price'])

print(df_apps_clean[df_apps_clean.App == 'Instagram'])
print(df_apps_clean.shape)


"""# Find Highest Rated Apps

**Challenge**: Identify which apps are the highest rated. What problem might you encounter if you rely exclusively on ratings alone to determine the quality of an app?
"""

df_apps_clean.Size_MBs.max()

#Find Highest Rated Apps
df_apps_clean.sort_values('Rating', ascending=False).head()

"""# Find 5 Largest Apps in terms of Size (MBs)

**Challenge**: What's the size in megabytes (MB) of the largest Android apps in the Google Play Store. Based on the data, do you think there could be limit in place or can developers make apps as large as they please? 
"""

#Find 5 Largest Apps in terms of Size (MBs)
df_apps_clean.sort_values('Size_MBs', ascending=False).head()

"""# Find the 5 App with Most Reviews

**Challenge**: Which apps have the highest number of reviews? Are there any paid apps among the top 50?
"""

#Find the 5 App with Most Reviews
df_apps_clean.sort_values('Reviews', ascending=False).head()

#Find the 50 App with Most Reviews
df_apps_clean.sort_values('Reviews', ascending=False).head(50)

"""# Plotly Pie and Donut Charts - Visualise Categorical Data: Content Ratings"""

# count Content Ratings
ratings = df_apps_clean.Content_Rating.value_counts()
print(ratings)

import pandas as pd
import plotly.express as px

#Plotly Pie
fig = px.pie(labels=ratings.index, values=ratings.values)
fig.show()

fig = px.pie(labels=ratings.index, values=ratings.values, title='Content Rating', names=ratings.index)
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.show()

#Donut Charts
fig=px.pie(labels=ratings.index, values=ratings.values, title='Content rating', names=ratings.index, hole=0.6)
fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent' )
fig.show()



