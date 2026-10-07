import pandas as pd

df = pd.read_csv("data/superstore_clean.csv", parse_dates=["Order Date", "Ship Date"])


def summarize(column):
    result = df.groupby(column).agg(
        sales=("Sales", "sum"),
        profit=("Profit", "sum"),
        loss_share=("Loss", "mean"),
    )
    result["margin_pct"] = result["profit"] / result["sales"] * 100
    result["loss_share"] = result["loss_share"] * 100
    return result.sort_values("profit", ascending=False).round(1)


print("--- Totals ---")
print("Total sales:", round(df["Sales"].sum()))
print("Total profit:", round(df["Profit"].sum()))
print("Overall profit margin %:", round(df["Profit"].sum() / df["Sales"].sum() * 100, 1))

print()
print("--- By category ---")
print(summarize("Category"))

print()
print("--- By sub-category ---")
print(summarize("Sub-Category"))

print()
print("--- By market ---")
print(summarize("Market"))

print()
print("--- By region ---")
print(summarize("Region"))

print()
print("--- By segment ---")
print(summarize("Segment"))