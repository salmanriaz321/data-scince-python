# import libraries
import pandas as pd
import statistics as stats
import seaborn as sns
import numpy as np

# import dataset
data = sns.load_dataset('iris')

# find mean of feature sepal length
mode_species = data['species'].value_counts().index[0]
print("Mode Species: ", mode_species)