import sea1 as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('penguins')
df = df.dropna()

sns.histplot(data=df, x='body_mass_g', bins=20, color='black')
plt.title('Distribution of Penguin Body Mass')
plt.xlabel('Body Mass (grams)')
plt.ylabel('Count')
plt.show()

sns.kdeplot(data=df, x='flipper_mm', hue='species', fill=True)
plt.title('Flippe Length Shape by Species (KDE)')
plt.xlabel('Flipper Length (mm)')
plt.show()

sns.histplot(data=df, x='flipper_length_mm', kde=True, color='Gray')
plt.title('Flipper Length - Histogram with KDE curve')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Count')
plt.show()


sns.scattreplot(data=df, x='flipper_length_mm', y='body_mass_g', hue='species' )
plt.title('Flipper Length vs Body Mass by Species')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Count')
plt.show()

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap - Penguin Measurments')
plt.show()
