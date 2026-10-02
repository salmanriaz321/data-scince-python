import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('titanic.csv')

data.head(5)

minimum_age = data['Age'].min()

maximum_age = data['Age'].max()

bins = [0, 15, 30, 45, 60, 75]

data['binned_age'] = pd.cut(data['Age'], bins)

print(data[['binned_age', 'Age']].head())

age_labels = ['Young', 'Young - Adult', 'Middle Aged', 'Middle-Older Age', 'Senior']

data['binned_age'] = pd.cut(data['Age'], bins, labels = age_labels)

data['binned_age'].value_counts().plot(kind='bar')

plt.title('Dance Class Age Distribution')
plt.xlabel('Ages')
plt.ylabel('Count')

labels = ['PassengerId','Survived','Pclass','Age','SibsSp','Parch','Fare']
for label in labels:
    print('Distribution of', label)
    sns.distplot(data[label])
    plt.show()
    print('Skeweness -', data[label].skew())

data['lgo_SibSp'] = np.log(data['SibSp'])
data['lgo_Parch'] = np.log(data['Parch'])
data['lgo_Fare'] = np.log(data['Fare'])
