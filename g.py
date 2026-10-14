import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns

print('--- Numerical Features Skewness ---')
numerical_cols = df.select_dtypes(include=[np.number]).columns
skewness = df[numerical_cols].skew()
print(skewness)

# Visualize Skewness
for col in numerical_cols:
  plt.figure(figsize=(6, 3))
  sns.histplot(df[col], kde=True, bins=30)
  plt.title(f'Distribution of {col} (Skewness: {skewness[col]:.2f})')
  plt.show()

print('\n--- Correlation Matrix (Numerical Features) ---')
plt.figure(figsize=(10, 8))
correlation = df[numerical_cols].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Feature Correlation Matrix')
plt.show()
