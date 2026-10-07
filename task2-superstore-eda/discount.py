import pandas as pd
from scipy import stats

df = pd.read_csv("data/superstore_clean.csv", parse_dates=["Order Date", "Ship Date"])

df["Discount band"] = pd.cut(
    df["Discount"],
    bins=[-0.01, 0, 0.2, 0.4, 1.0],
    labels=["No discount", "1-20%", "21-40%", "Over 40%"],
)


def band_summary(data):
    result = data.groupby("Discount band", observed=True).agg(
        lines=("Profit", "count"),
        avg_profit=("Profit", "mean"),
        loss_share=("Loss", "mean"),
        sales=("Sales", "sum"),
        profit=("Profit", "sum"),
    )
    result["margin_pct"] = result["profit"] / result["sales"] * 100
    result["loss_share"] = result["loss_share"] * 100
    return result.round(1)


print("--- All products, by discount band ---")
print(band_summary(df))

rho, p_value = stats.spearmanr(df["Discount"], df["Profit"])
print()
print("Spearman correlation (Discount vs Profit):", round(rho, 3))
print("p-value:", f"{p_value:.3g}")

print()
print("--- Tables only, by discount band ---")
tables = df[df["Sub-Category"] == "Tables"]
print(band_summary(tables))

print()
print("Average discount, Tables:", round(tables["Discount"].mean(), 3))
print("Average discount, all other products:", round(df[df["Sub-Category"] != "Tables"]["Discount"].mean(), 3))