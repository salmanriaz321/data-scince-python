import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('your_dataset.csv')

print('--- First 5 Rows ---')
display(df.head())

print('\n--- Dataset Info ---')
df.info()

print('\n--- Summary Statistics (Numerical) ---')
display(df.describe())

print('\n--- Summary Statistics (Categorical) ---')
display(df.describe(include=['O']))

# 3. Data Cleaning & Missing Values
print('\n--- Missing Values Per Column ---')
print(df.isnull().sum())

df = df.drop_duplicates()

numerical_cols = df.select_dtypes(include=[np.number]).columns
for col in numerical_cols:
  plt.figure(figsize=(8, 4))
  sns.histplot(df[col], kde=True, bins=30)
  plt.title(f'Distribution of {col}')
  plt.show()

categorical_cols = df.select_dtypes(include=['O']).columns
for col in categorical_cols:
  plt.figure(figsize=(8, 4))
  sns.countplot(
      data=df,
      x=col,
      order=df[col].value_counts().index,
      palette='viridis',
      hue=col,
      legend=False,
  )
  plt.title(f'Count Plot of {col}')
  plt.xticks(rotation=45)
  plt.show()

plt.figure(figsize=(10, 8))
correlation = df[numerical_cols].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()
