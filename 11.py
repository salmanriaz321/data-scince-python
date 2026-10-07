import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("titanic.csv")

data.head(5)
sns.countplot(data=data, x='Sex', hue='Survived')

plt.title("Survival by Gender")
plt.show()
sns.countplot(data=data, x='Pclass', hue='Survived')

plt.title("Suvival by Passenger Class")
plt.show()

sns.histplot(data['Age'], bins=40, kde=False)

plt.title("Distribution of Passenger Age")
plt.xlabel("Age")
plt.ylabel("Numbers of Passengers")
plt.show()

sns.countplot(data=data, x='Sex')

plt.title("Passengers by Gender")
plt.show()

sns.ocuntplot(
    data=data,
    x='Survived',
    hue='Parch',
    palette="mako"
)

plt.title("Survival by Number of Parents/Children")
plt.show()

sns.histplot(data['Fare'], kde=True)

plt.title("Distribution by Passenger Class")
plt.show()

numeric_data = data.selact_dtypes(include=['number'])

plt.figure(figsize=(10, 7))

sns.heatmap(
    numeric_data.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Corection Heatmap")
plt.show()
