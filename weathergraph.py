import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os 

bas_dir = os.path.dirname(os.path.abspath(__file__))
data = pd.read_csv(os.path.join(base_dir, 'IMDB-Dataset.csv'))

print(data.head())
print(data.isnull().sum())
data['review'] = data['review'].str.replace(r'<br\s*/?>', ' ', regex=True)
data['word_count'] = data['review'].str.split().str.len()

data['sentiment'].value_counts().plot(kind='bar', edgecolor='black', color=['g', 'r'])
plt.ylabel("count of reviews")
plt.xlabel("Words per review")
plt.title("Distribution of review lenght")
plt.show()

bins_len = np.arange(0, 1050, 50)
plt.hist(data['word_count'].clip(upper=1000), edgecolor="black", bins=bins_len, color='g')
plt.ylabel("count of reviews")
plt.xlabel("words per review(capped at 1000)")
plt.title("Review Length Distribution")
plt.show()
