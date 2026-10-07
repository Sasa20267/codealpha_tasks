import pandas as pd

books = pd.read_csv("books.csv")
category_map = pd.read_csv("category_map.csv")

df = books.merge(category_map, on="product_url", how="left")

print("--- Before cleaning ---")
print(df.dtypes)
print("Missing values:")
print(df.isna().sum())
print("Duplicate rows:", df.duplicated().sum())
print("Duplicate titles:", df["title"].duplicated().sum())
print("Availability values:")
print(df["availability"].value_counts())

df["price"] = df["price"].str.replace(r"[^\d.]", "", regex=True).astype(float)
df["in_stock"] = df["availability"].str.contains("In stock")
df = df.drop(columns=["availability"])
df = df[["title", "category", "price", "rating", "in_stock", "product_url"]]

df.to_csv("books_clean.csv", index=False, encoding="utf-8-sig")

print("--- After cleaning ---")
print(df.shape)
print(df.dtypes)
print(df.head())