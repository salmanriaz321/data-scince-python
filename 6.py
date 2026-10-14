import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('your_dataset.csv')

print('--- Categorical Features Frequency Values ---')
categorical_cols = df.select_dtypes(include=['O', 'category']).columns

for col in categorical_cols:
  print(f'\nFrequency distribution for: {col}')
  print(df[col].value_counts())

  print(f'Mode (Most Frequent Value) for {col}: {df[col].mode()[0]}')

print('\n--- Visualizing Categorical Features ---')
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
  plt.title(f'Frequency Count Plot of {col}')
  plt.xticks(rotation=45)
  plt.xlabel(col)
  plt.ylabel('Frequency')
  plt.show()

print('\n--- Transforming Categorical Features ---')
