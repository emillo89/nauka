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

#check the data types on the columns
print(df_apps_clean.Installs.describe())

#check the data types on the DataFrame
print(df_apps_clean.info())
print(df_apps_clean[['App', 'Installs']].groupby('Installs').count())

#remove comma
df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',','')

#convert our data to a number
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
print(df_apps_clean[['App','Installs']].groupby('Installs').count())

#Convert the price column to numeric data
#look at the data type of the price column
print(df_apps_clean.Price.describe())

df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$','')
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)
print(df_apps_clean.sort_values('Price', ascending=False).head(20))


#apps below $250
df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
df_apps_clean.sort_values('Price', ascending=False).head(5)

"""### Highest Grossing Paid Apps (ballpark estimate)"""

#highest grossing paid apps
print(df_apps_clean.columns)

#multiply the values
df_apps_clean['Revenue_Estimate'] = df_apps_clean.Installs.mul(df_apps_clean.Price)

print(df_apps_clean.sort_values('Revenue_Estimate', ascending=False).head(10))

"""# Plotly Bar Charts & Scatter Plots: Analysing App Categories"""

#Find the number of different categories
print(df_apps_clean.Category.nunique())

#To calculate the number of apps per category
top10_category = df_apps_clean.Category.value_counts()[:10]
print(top10_category)

"""### Vertical Bar Chart - Highest Competition (Number of Apps)"""

#Vertical Bar Chart - Highest Competition (Number of Apps)
bar = px.bar(x=top10_category.index, y=top10_category.values)
bar.show()

"""### Horizontal Bar Chart - Most Popular Categories (Highest Downloads)"""

#Horizontal Bar Chart - Most Popular Categories (Highest Downloads)
category_installs = df_apps_clean.groupby('Category').agg({'Installs': pd.Series.sum})
print(category_installs.sort_values('Installs', ascending=True, inplace=True))

h_bar = px.bar(x=category_installs.Installs, y=category_installs.index, orientation='h', title='Category Popularity')
h_bar.update_layout(xaxis_title='Number of Downloads', yaxis_title='Category')
h_bar.show()

#Create a DataFrame that has the number of apps in one column and the number of installs
cat_number = df_apps_clean.groupby('Category').agg({'App':pd.Series.count})

cat_merged_df = pd.merge(cat_number,category_installs, on='Category', how='inner')
print(cat_merged_df.sort_values('Installs', ascending=False))

scatter = px.scatter(cat_merged_df,
                     x='App',
                     y='Installs',
                     title='Category Conncentration',
                     size='App',
                     hover_name = cat_merged_df.index,
                     color='Installs')
scatter.update_layout(xaxis_title='Number of Apps (Lower=More Concentrated',
                      yaxis_title="Installs",
                      yaxis=dict(type='log')
                      )
scatter.show()

"""# Extracting Nested Data from a Column"""
print(df_apps_clean.Genres)

#number of genres
print(len(df_apps_clean['Genres'].unique()))
print(df_apps_clean.Genres.value_counts().sort_values(ascending=True)[:10])

## Split the strings on the semi-colon and then .stack them.
stack = df_apps_clean.Genres.str.split(';', expand=True).stack()
num_genres = stack.value_counts()

print(num_genres)

#Colour Scales in Plotly Charts - Competition in Genres
bar = px.bar(x=num_genres.index[:15],
             y=num_genres.values[:15],
             title='Top Genres',
            #  hover_name=num_genres.index[:15],
             color=num_genres.values[:15],
             color_continuous_scale='Agsunset'
             )
bar.update_layout(xaxis_title='Genre',
                  yaxis_title='Number of Apps',
                  #will turn off scale
                  coloraxis_showscale=False
                  )

"""# Grouped Bar Charts: Free vs. Paid Apps per Category"""

print(df_apps_clean.Type.value_counts())

df_free_vs_paid = df_apps_clean.groupby(['Category','Type']).agg({'App':pd.Series.count})
print(df_free_vs_paid.head())

#add index to the table
df_free_vs_paid = df_apps_clean.groupby(['Category','Type'],as_index=False).agg({'App':pd.Series.count})
print(df_free_vs_paid.head())

#Free vs Paid Apps by Category
g_bar = px.bar(df_free_vs_paid,
               x='Category',
               y='App',
               title='Free vs Paid Apps by Category',
               #1 color paid second free
               color='Type',
               #group - two column paid and free
               barmode='group')
g_bar.update_layout(xaxis_title='Category',
                    yaxis_title='Number of Apps',
                    #Set `categoryorder` to "category ascending" or
                    #"category descending" if order should be determined by the alphanumerical order of the category nam
                    xaxis={'categoryorder':'total descending'},
                    yaxis=dict(type='log'))
g_bar.show()

#Plotly Box Plots: Lost Downloads for Paid Apps
box = px.box(df_apps_clean,
             y='Installs',
             x='Type',
             color='Type',
             notched=True,
             #With the points argument, display underlying data points with either all points (all),
             points='all',
             title='How many Downloads are Paid Apss Giving Up?')
box.update_layout(yaxis=dict(type='log'))
box.show()

df_paid_apps = df_apps_clean[df_apps_clean['Type']=='Paid']
box = px.box(df_paid_apps,
             x='Category',
             y='Revenue_Estimate',
             title='How much can paid apps earn?')
box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Ballpark revenue',
                  xaxis={'categoryorder': 'min ascending'},
                  yaxis=dict(type='log'))
box.show()

"""the median price price for a paid app? Then compare pricing by category by creating another box plot"""
box = px.box(df_paid_apps,
             x='Category',
             y='Price',
             title='Price per Category')
box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Price',
                  xaxis={'categoryorder': 'max descending'},
                  yaxis=dict(type='log'))
box.show()

