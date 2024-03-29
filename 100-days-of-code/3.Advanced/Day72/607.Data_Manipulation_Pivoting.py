# -*- coding: utf-8 -*-
"""Programming_Languages_(start).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FYe6yTUZQJtTijQOq3qRzJQu3hgtJAGj

## Get the Data

Either use the provided .csv file or (optionally) get fresh (the freshest?) data from running an SQL query on StackExchange: 

Follow this link to run the query from [StackExchange](https://data.stackexchange.com/stackoverflow/query/675441/popular-programming-languages-per-over-time-eversql-com) to get your own .csv file

<code>
select dateadd(month, datediff(month, 0, q.CreationDate), 0) m, TagName, count(*)
from PostTags pt
join Posts q on q.Id=pt.PostId
join Tags t on t.Id=pt.TagId
where TagName in ('java','c','c++','python','c#','javascript','assembly','php','perl','ruby','visual basic','swift','r','object-c','scratch','go','swift','delphi')
and q.CreationDate < dateadd(month, datediff(month, 0, getdate()), 0)
group by dateadd(month, datediff(month, 0, q.CreationDate), 0), TagName
order by dateadd(month, datediff(month, 0, q.CreationDate), 0)
</code>

## Import Statements
"""

import pandas as pd

"""## Data Exploration

**Challenge**: Read the .csv file and store it in a Pandas dataframe
"""

#Read the .csv file 
df = pd.read_csv('QueryResults.csv', names=['DATE','TAG','POSTS'], header=0)
print(df)

"""**Challenge**: Examine the first 5 rows and the last 5 rows of the of the dataframe"""

#the first 5 rows and the last 5 rows of the of the dataframe
print(df.head())
print(df.tail())

"""**Challenge:** Check how many rows and how many columns there are. 
What are the dimensions of the dataframe?
"""

#how many rows and how many columns
print(df.shape)

"""**Challenge**: Count the number of entries in each column of the dataframe"""

#Count the number of entries in each column of the dataframe
print(df.count())

"""**Challenge**: Calculate the total number of post per language.
Which Programming language has had the highest total number of posts of all time?
"""

#Calculate the total number of post per language
print(df.groupby('TAG').sum())

"""Some languages are older (e.g., C) and other languages are newer (e.g., Swift). 
The dataset starts in September 2008.

**Challenge**: How many months of data exist per language? 
Which language had the fewest months with an entry? 
"""
#How many months of data exist per language
print(df.groupby('TAG').count())

"""## Data Cleaning
Let's fix the date format to make it more readable. We need to use Pandas to change format from a string of "2008-07-01 00:00:00" 
to a datetime object with the format of "2008-07-01"""
print(df['DATE'][1])
#the same method df.DATE[1]

#convert entire column (string to datetime)
df.DATE = pd.to_datetime(df.DATE)
print(df.head())

"""## Data Manipulation"""

test_df = pd.DataFrame({'Age':['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                        'Power': [100, 80, 25, 50, 99, 75, 5, 30]})

#pivoting DataFrame example
pivot_df = test_df.pivot(index='Age', columns='Actor', values='Power')
print(pivot_df)

"""**Challenge**: What are the dimensions of our new dataframe? How many rows and columns does it have? Print out the column names and print out the first 5 rows of the dataframe."""

#Pivoting DataFrame - Challenge
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')

#show dataframe
print(reshaped_df)

#count rows and columns
print(reshaped_df.shape)

#column names 
print(reshaped_df.columns)

#the first 5 rows of the dataframe.
print(reshaped_df.head())

"""**Challenge**: Count the number of entries per programming language. Why might the number of entries be different? """

#Count the number of entries per programming language. Why might the number of entries be different?
print(reshaped_df.count())
print(reshaped_df.head())

#replace Nan values to 0
reshaped_df.fillna(0, inplace=True)
print(reshaped_df.head())

#check if there are any NaN values
print(reshaped_df.isna().values.any())






