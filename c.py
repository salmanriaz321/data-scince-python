import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Sample Data: Test scores of students
data = [45, 56, 62, 65, 68, 70, 72, 75, 78, 80, 82, 85, 88, 90, 92, 108]

# 1. Calculate Statistical Measures using Numpy
q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)  # Median
q3 = np.percentile(data, 75)
iqr = q3 - q1

# Define boundaries for outliers
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)

outliers = [x for x in data if x < lower_bound or x > upper_bound]

# Display calculated statistics
print(f"First Quartile (Q1)  : {q1}")
print(f"Median (Q2)          : {q2}")
print(f"Third Quartile (Q3)  : {q3}")
print(f"Interquartile Range : {iqr}")
print(f"Lower Bound          : {lower_bound}")
print(f"Upper Bound          : {upper_bound}")
print(f"Outliers             : {outliers}")

# 2. Visualize Data Locations using Box Plot
plt.figure(figsize=(8, 5))
sns.boxplot(x=data, color="skyblue", showmeans=True)

# Add annotations to label key points on the plot
plt.title("Boxplot of Student Test Scores", fontsize=14)
plt.xlabel("Scores", fontsize=12)

plt.axvline(q1, color="red", linestyle="--", alpha=0.7, label=f"Q1 ({q1})")
plt.axvline(q2, color="green", linestyle="-", alpha=0.7, label=f"Q2/Median ({q2})")
plt.axvline(q3, color="red", linestyle="--", alpha=0.7, label=f"Q3 ({q3})")

plt.legend()
plt.tight_layout()
plt.show()