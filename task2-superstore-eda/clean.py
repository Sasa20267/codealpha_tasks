import pandas as pd

df = pd.read_csv("data/Global_Superstore2.csv", encoding="latin1")

df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d-%m-%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%d-%m-%Y")

df = df.drop(columns=["Postal Code"])

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Loss"] = df["Profit"] < 0

df.to_csv("data/superstore_clean.csv", index=False, encoding="utf-8-sig")

print(df.shape)
print(df[["Order Date", "Year", "Month", "Loss"]].head())
print(df["Year"].value_counts().sort_index())