import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/superstore_clean.csv", parse_dates=["Order Date", "Ship Date"])

# Chart 1: profit by sub-category
sub = df.groupby("Sub-Category")["Profit"].sum().sort_values() / 1000
colors = ["tab:red" if v < 0 else "tab:blue" for v in sub.values]
plt.figure(figsize=(8, 7))
plt.barh(sub.index, sub.values, color=colors, edgecolor="black")
plt.title("Total Profit by Sub-Category")
plt.xlabel("Profit (thousand USD)")
plt.tight_layout()
plt.savefig("images/profit_by_subcategory.png", dpi=150)
plt.close()

# Chart 2: sales and profit by year
yearly = df.groupby("Year")[["Sales", "Profit"]].sum() / 1_000_000
yearly.plot(kind="bar", figsize=(8, 5), edgecolor="black")
plt.title("Sales and Profit by Year")
plt.xlabel("Year")
plt.ylabel("Million USD")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("images/sales_profit_by_year.png", dpi=150)
plt.close()

# Chart 3: monthly sales (all four years combined)
monthly = df.groupby("Month")["Sales"].sum() / 1_000_000
plt.figure(figsize=(8, 5))
plt.bar(monthly.index, monthly.values, edgecolor="black")
plt.title("Sales by Month (2011-2014 combined)")
plt.xlabel("Month")
plt.ylabel("Sales (million USD)")
plt.xticks(range(1, 13))
plt.tight_layout()
plt.savefig("images/sales_by_month.png", dpi=150)
plt.close()

# Chart 4: profit by market
market = df.groupby("Market")["Profit"].sum().sort_values() / 1000
plt.figure(figsize=(8, 5))
plt.barh(market.index, market.values, edgecolor="black")
plt.title("Total Profit by Market")
plt.xlabel("Profit (thousand USD)")
plt.tight_layout()
plt.savefig("images/profit_by_market.png", dpi=150)
plt.close()

# Chart 5: average profit by discount band
band = pd.cut(
    df["Discount"],
    bins=[-0.01, 0, 0.2, 0.4, 1.0],
    labels=["No discount", "1-20%", "21-40%", "Over 40%"],
)
avg = df.groupby(band, observed=True)["Profit"].mean()
colors = ["tab:red" if v < 0 else "tab:blue" for v in avg.values]
plt.figure(figsize=(8, 5))
plt.bar(avg.index.astype(str), avg.values, color=colors, edgecolor="black")
plt.axhline(0, color="black", linewidth=1)
plt.title("Average Profit per Order Line by Discount Band")
plt.xlabel("Discount band")
plt.ylabel("Average profit (USD)")
plt.tight_layout()
plt.savefig("images/profit_by_discount.png", dpi=150)
plt.close()

print("Charts saved")