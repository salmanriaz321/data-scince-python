print(c_merge.head(10))

# Country names

names = c_merge['country']

# Convert population growth to millions

pop_grow = c_merge['population_growth'] / 10**6

# Create bar chart

plt.figure(figsize=(15, 9))

plt.bar(names, pop_grow, width=0.6)

plt.xlabel('Country')

plt.ylabel('Population Growth (Millions)')

plt.title(

'Top 10 Countries with the Biggest Population Growth from 1952 to 2007'

)

# Rotate country names

plt.xticks(rotation=45)

# Add population values above bars

for x, y in zip(names, pop_grow):

label = "({:.2f})".format(y)

plt.annotate(

label,

(x, y),

textcoords="offset points",

xytext=(0, 10),

ha='center'

)

plt.show()