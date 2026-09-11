import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

Socer=pd.read_csv('countries.csv')

Socer.head()

Socer.info()

Socer.columns

sns.heatmap(Socer.corr(numeric_only=True),annot=True)
plt.show()
sns.pairplot(Socer)
plt.show()