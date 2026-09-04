import pandas as pd

import matplotlib.pyplot as plt

# Read the CSV file

countries_df = pd.read_csv('countries.csv')

countries = countries_df

# View first 3 rows

print(countries.head(3))

# Get data for 1952

c_52 = countries.loc[countries['year'] == 1952]

print(c_52.head())

# Get data for 2007

c_07 = countries.loc[countries['year'] == 2007]

print(c_07.head())

# Merge 1952 and 2007 data based on country

c_merge = c_52.merge(

c_07,

left_on='country',

right_on='country'

)

print(c_merge.head())

# Drop duplicate year columns

c_merge = c_merge.drop(['year_x', 'year_y'], axis=1)

# Calculate population growth

c_merge['population_growth'] = (

c_merge['population_y'] - c_merge['population_x']

)

# Sort and get top 10 countries

c_merge = c_merge.sort_values(

'population_growth',

ascending=False

).head(10)