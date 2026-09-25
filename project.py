import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the dataset (replace 'bestsellers.csv' with your actual file path)
df = pd.read_csv("bestsellers.csv")

# 1. Check if any null values are present in the dataset
print("=== 1. Null Values Check ===")
print(df.isnull().sum())

# 2. Handle missing values if any
# (If null values exist, drop them or fill numeric columns with median and categorical with mode)
if df.isnull().values.any():
    # Example handling: fill missing numeric values with median, categorical with mode
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype in ["float64", "int64"]:
                df[col] = df[col].fillna(df[col].median())
            else:
                df[col] = df[col].fillna(df[col].mode()[0])
    print("\nMissing values handled successfully.")
else:
    print("\nNo missing values found in the dataset.")

# 3. Find the variance and standard deviation of the feature 'User Rating'
rating_var = df["User Rating"].var()
rating_std = df["User Rating"].std()

print("\n=== 3. User Rating Statistics ===")
print(f"Variance: {rating_var:.4f}")
print(f"Standard Deviation: {rating_std:.4f}")

# 4. Find the variance and standard deviation of the feature 'Price'
price_var = df["Price"].var()
price_std = df["Price"].std()

print("\n=== 4. Price Statistics ===")
print(f"Variance: {price_var:.4f}")
print(f"Standard Deviation: {price_std:.4f}")

# 5. Check the distribution of feature 'User Rating' using a histogram (Customized Bin Range)
plt.figure(figsize=(8, 5))
sns.histplot(
    df["User Rating"],
    bins=[3.3, 3.5, 3.7, 3.9, 4.1, 4.3, 4.5, 4.7, 4.9, 5.1],
    kde=True,
    color="skyblue",
    edgecolor="black",
)
plt.title("Distribution of User Rating", fontsize=14)
plt.xlabel("User Rating", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# 6. Check the distribution of feature 'Price' using a histogram (Customized Bin Range)
plt.figure(figsize=(8, 5))
sns.histplot(
    df["Price"],
    bins=range(0, int(df["Price"].max()) + 10, 5),
    kde=True,
    color="salmon",
    edgecolor="black",
)
plt.title("Distribution of Price", fontsize=14)
plt.xlabel("Price ($)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()