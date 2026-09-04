import pandas as pd
import matplotlib.pyplot as plt

countries_df = pd.read_csv('countries.csv')
countries = countries_df
countries.head(3)

c_52 = countries.loc[countries['year'] == 1952]
c_52.head()

c_07 = countries.loc[countries['year'] == 2007]
c_07.head()

type(c_52)

c_merge = c_52.merge(c_07, left_on='country',right_on='country')
c_merge.head()

c_merge.drop(['year_x', 'year_y'], axis=1)
c_merge.head()

c_merge['population_growth'] = c_merge['population_y'] - c_merge['population_x']

31889923 - 8425333

c_merge.shape, type(c_merge)

c_merge = c_merge.sort_values('population_growth', ascending=False).head(10)
c_merge.head(10)

names = ['China', 'India', 'United States', 'Indonesia', 'Brazil', 'Pakistan', 'Bangladesh', 'Nigeria', 'Mexico', 'Philippines']
pop_grow = (c_merge['population_growth']/ 10**6)

plt.figure(figsize=(15,9))
plt.bar(names,pop_grow,width=0.6)
plt.xlabel('Country')
plt.ylabel('Population_Growth(Millions)')
plt.title('Top 10 countriesw/the Biggest Population Growth from 1952 to 2007')
plt.xtickets(rotation=45)

for x,y in zip(names,pop_grow):
    label = "({:.2f})".format(y)

    plt.annonate(label, 
                (x,y),
                textcoords="offset points",
                xytext=(0,10),
                ha='center')
plt.show()
