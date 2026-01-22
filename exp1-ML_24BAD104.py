
import pandas as pd
import matplotlib.pyplot as plt
print("Student Name: Sanadhani")
print("Roll No: 24BAD104")
print("Experiment: E-Commerce Sales Data Analysis\n")
ecom_df = pd.read_csv(
    "data.csv.csv",
    encoding="ISO-8859-1"
)
print("HEAD:")
print(ecom_df.head())
print("\nTAIL:")
print(ecom_df.tail())
print("\nINFO:")
ecom_df.info()
print("\nDESCRIBE:")
print(ecom_df.describe())
print("\nMISSING VALUES:")
print(ecom_df.isnull().sum())
ecom_df = ecom_df.dropna(subset=["Description"])

product_sales = (
    ecom_df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
plt.figure()
product_sales.plot(kind="bar")
plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

plt.figure()
product_sales.plot(kind="line", marker="o")
plt.title("Sales Trend of Top Products")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

