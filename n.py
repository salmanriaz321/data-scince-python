import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('titanic.csv')
data = data.rename(columns={'Sex': 'Gender'})

print(data.head(5))
print(data.dtypes)
print(data.columns.tolist())

nominal_cat = ['Name', 'Ticket', 'Cabin']
ordinal_cat = ['Embarked', 'Gender']

data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])

print(data['Gender'].value_counts())

gender_categories = ['feamale', 'male']
data['Gender'] = pd.Categorical(data['Gender'],gender_categories, ordered=True)

median_index = np.median(data['Gender'].cat.codes)
median_gender = gender_categories[int(median_index)]

embarked_categories = ['S', 'C', 'Q']
data['Emarked'] = pd.Categorical(data['Embarked'], embarked_categories, ordered=True)

median_index = np.median(data['Embarked'].cat.codes)
median_embarked = embarked_categories[int(median_index)]
sns.set_style('whitegrid')

sns.countplot(x='Survived', data=data)
plt.show()

sns.countplot(x='Gender', hue='Survived', data=data)
plt.show()

sns.countplot(x='survived', data=data, hue='Survived', palette='wintrer', legend=False)
plt.show()
