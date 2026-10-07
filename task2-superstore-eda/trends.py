import pandas as pd

df = pd.read_csv("data/superstore_clean.csv", parse_dates=["Order Date", "Ship Date"])

print("--- By year ---")
yearly = df.groupby("Year").agg(
    sales=("Sales", "sum"),
    profit=("Profit", "sum"),
)
yearly["margin_pct"] = yearly["profit"] / yearly["sales"] * 100
yearly["sales_growth_pct"] = yearly["sales"].pct_change() * 100
print(yearly.round(1))

print()
print("--- By month (total across all 4 years) ---")
monthly = df.groupby("Month").agg(
    sales=("Sales", "sum"),
    profit=("Profit", "sum"),
)
print(monthly.round(0))

print()
print("--- What markets are inside these regions? ---")
shared = df[df["Region"].isin(["Central", "North", "South", "East", "West"])]
print(shared.groupby(["Region", "Market"]).size())