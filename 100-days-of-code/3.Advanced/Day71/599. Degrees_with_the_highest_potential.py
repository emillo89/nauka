# -*- coding: utf-8 -*-
"""Day71.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qsz9DcDAZhhtbgmdPmMPSvhfUhUFllOU
"""

import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')
clean_df = df.dropna()

#subtract two columns
spread_col = clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
print(spread_col)

#add column to the dataframe
clean_df.insert(1,'Spread', spread_col)
print(clean_df.head())

#sort value
low_risk = clean_df.sort_values('Spread')
print(low_risk)
print(low_risk[['Undergraduate Major', 'Spread']])

#find 5 degrees with highest values in the 90th percentile
highest_potentioal = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
print(highest_potentioal[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())

#find 5 degrees with highest spread
highest_spread = clean_df.sort_values('Spread', ascending=False)
print(highest_spread[['Undergraduate Major','Spread' ]].head())

