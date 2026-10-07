import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books_clean.csv")

# Chart 1: distribution of prices
plt.figure(figsize=(8, 5))
plt.hist(df["price"], bins=20, edgecolor="black")
plt.title("Distribution of Book Prices")
plt.xlabel("Price (GBP)")
plt.ylabel("Number of books")
plt.tight_layout()
plt.savefig("images/price_distribution.png", dpi=150)
plt.close()

# Chart 2: number of books per rating
rating_counts = df["rating"].value_counts().sort_index()
plt.figure(figsize=(8, 5))
plt.bar(rating_counts.index, rating_counts.values, edgecolor="black")
plt.title("Number of Books by Star Rating")
plt.xlabel("Star rating")
plt.ylabel("Number of books")
plt.tight_layout()
plt.savefig("images/rating_counts.png", dpi=150)
plt.close()

# Chart 3: average price by category (genres with at least 10 books)
real = df[~df["category"].isin(["Default", "Add a comment"])]
stats = real.groupby("category")["price"].agg(["count", "mean"])
stats = stats[stats["count"] >= 10].sort_values("mean")
plt.figure(figsize=(8, 6))
plt.barh(stats.index, stats["mean"], edgecolor="black")
plt.title("Average Price by Category (10+ books)")
plt.xlabel("Average price (GBP)")
plt.tight_layout()
plt.savefig("images/avg_price_by_category.png", dpi=150)
plt.close()

print(stats.round(2))
print("Charts saved")