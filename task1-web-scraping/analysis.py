import pandas as pd

df = pd.read_csv("books_clean.csv")

print("--- Duplicate title ---")
print(df[df["title"].duplicated(keep=False)][["title", "category", "price", "product_url"]])

print("--- Price summary ---")
print(df["price"].describe())

print("--- Rating counts ---")
print(df["rating"].value_counts().sort_index())

print("--- Cheapest and most expensive ---")
print(df.nsmallest(3, "price")[["title", "price"]])
print(df.nlargest(3, "price")[["title", "price"]])
print("--- Books per category (top 10) ---")
print(df["category"].value_counts().head(10))

category_stats = df.groupby("category").agg(
    books=("title", "count"),
    avg_price=("price", "mean"),
    avg_rating=("rating", "mean"),
).round(2)

print("--- Highest average price ---")
print(category_stats.sort_values("avg_price", ascending=False).head(5))

print("--- Lowest average price ---")
print(category_stats.sort_values("avg_price").head(5))

print("--- Average price by rating ---")
print(df.groupby("rating")["price"].mean().round(2))