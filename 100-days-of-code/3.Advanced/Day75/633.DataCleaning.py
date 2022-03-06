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





