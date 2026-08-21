import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
df = df.dropna()

sns.barplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Average Total Bill per Day by Gender')
plt.xlabel('Day')
plt.ylabel('Average Bill($)')
plt.show(block=True)

sns.countplot(x='day', hue='sex', data=df)
plt.title('Average Total Bill per Day by Gender')
plt.xlabel('Day')
plt.ylabel('count')
plt.show(block=True)

sns.boxplot(x='day', y='total_bil', data=df)
plt.title('Average Total Bill per Day by Gender')
plt.xlabel('Day')
plt.ylabel('Average Bill($)')
plt.show(block=True)

sns.stripplot(x='day', y='total_bill', data=df)
plt.title('Average Total Bill per Day by Gender')
plt.xlabel('Day')
plt.ylabel('Average Bill($)')
plt.show(block=True)

sns.swarmplot(x='day', y='total_bill', data=df)
plt.title('Every Bill Amount  per Day (Swarm Plot)')
plt.xlabel('Day')
plt.ylabel('Average Bill($)')
plt.show(block=True)

sns.pointplot (x='day', y='total_bill', hue='sex', data=df)
plt.title('Average Total Bill per Day by Gender')
plt.xlabel('Day')
plt.ylabel('Average Bill($)')
plt.show(block=True)

sns.lmplot(x='total_bill', y='tip', data=df)
plt.title('Total Bill vs Tip - Trend Line')
plt.show(block=True) 

sns.jointplot(x='total_bill', y='tip', data=df)
plt.subtitle('Total Bill vs Tip', y=1.02)
plt.show(block=True) 

sns.pairplot(x='total_bill', y='tip', data=df)
plt.subtitle('Pair Plot - Bill, Tip and Party Size', y=1.02)
plt.show(block=True) 
