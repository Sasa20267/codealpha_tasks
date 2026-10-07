import pandas as pd

df = pd.read_csv("data/Global_Superstore2.csv", encoding="latin1")

print("Shape (rows, columns):", df.shape)
print()
print("Columns and data types:")
print(df.dtypes)
print()
print("Missing values per column:")
print(df.isna().sum())
print()
print(df.head(3).T)
print()
print("--- Deeper checks ---")
print("Duplicate rows:", df.duplicated().sum())

dates = pd.to_datetime(df["Order Date"], format="%d-%m-%Y", errors="coerce")
print("Dates that failed to convert:", dates.isna().sum())
print("Date range:", dates.min(), "to", dates.max())

print()
print(df[["Sales", "Quantity", "Discount", "Profit", "Shipping Cost"]].describe().round(2))
print("Rows with negative profit:", (df["Profit"] < 0).sum())

print()
print(df["Segment"].value_counts())
print(df["Category"].value_counts())
print(df["Market"].value_counts())