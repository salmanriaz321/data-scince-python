import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Titanic.csv')

data.head(5)
data.isnull().sum()

age_q1 = np.quantile(data['Age'], 0.25)
age_q2 = np.quantile(data['Age'], 0.50)
age_q3 = np.quantile(data['Age'], 0.75)

print("Age Quartiles -")
print("Q1 -", age_q1)
print("Q2 -", age_q2)
print("Q3 -", age_q3)

IQR_age = age_q3 - age_q1
print("Interquartile Range :", IQR_age)

plt.hist(data['Age'])
plt.ylabel("Count of Passengers")
plt.xlabel("Age")
plt.show()

data.head(5)
data.isnull().sum()
plt.boxplot(data['Age'])
plt.title('Age distribution')
plt.show()

plt.boxplot(data['Pclass'])
plt.title('Passenger Class distribution')
plt.show()
