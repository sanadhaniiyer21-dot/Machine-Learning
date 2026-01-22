
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Sanadhani-24BAD104")

df_house = pd.read_csv("Housing.csv.CSV")

print(df_house.head())
df_house.info()

print(df_house.isnull().sum())

plt.scatter(df_house['area'], df_house['price'])
plt.title("Area vs Price")
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()

numeric_df = df_house.select_dtypes(include=['int64', 'float64'])

plt.figure(figsize=(8,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
