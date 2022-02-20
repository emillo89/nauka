# -*- coding: utf-8 -*-
"""Day71.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qsz9DcDAZhhtbgmdPmMPSvhfUhUFllOU
"""

import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')

clean_df = df.dropna()

#to access a particular column
print(clean_df['Starting Median Salary'])

#highest starting salary
print(clean_df['Starting Median Salary'].max())

#find index highest salary
print(clean_df['Starting Median Salary'].idxmax())

#show value in particular row
print(clean_df['Starting Median Salary'].loc[43])

#Find Highest Mid-Carreer Salary
print(clean_df['Mid-Career Median Salary'].idxmax())
print(clean_df['Undergraduate Major'].loc[8])

#The Lowest Starting salary
print(clean_df['Starting Median Salary'].idxmin())
print(clean_df['Undergraduate Major'].loc[49])

#lowest mid-career salary
print(clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()])
print(clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()])

