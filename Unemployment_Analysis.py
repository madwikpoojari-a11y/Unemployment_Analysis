import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Unemployment in India.csv")
df.columns = df.columns.str.strip()
df = df.drop_duplicates()
df["Date"] = pd.to_datetime(df["Date"].str.strip(),dayfirst=True, errors="coerce")
rate = "Estimated Unemployment Rate (%)"
df[rate] = pd.to_numeric(df[rate], errors="coerce")
df = df.dropna(subset=["Date", rate])
df = df[df[rate] >= 0]
print("First five rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nAverage unemployment rate:",
      round(df[rate].mean(), 2), "%")

print("Maximum unemployment rate:",
      round(df[rate].max(), 2), "%")

print("Minimum unemployment rate:",
      round(df[rate].min(), 2), "%")
monthly = df.groupby(df["Date"].dt.to_period("M"))[rate].mean()
monthly.index = monthly.index.to_timestamp()
monthly.plot(figsize=(10, 5), marker="o")
plt.title("Unemployment Rate in India Over Time")
plt.xlabel("Month")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.tight_layout()
plt.show()
df["Period"] = df["Date"].apply(
    lambda d: "Before COVID-19" if d < pd.Timestamp("2020-03-25")
    else "During/After COVID-19")
print("\nCOVID-19 comparison:")
print(df.groupby("Period")[rate].mean().round(2))
df.groupby("Period")[rate].mean().plot(
    kind="bar", color=["skyblue", "orange"])
plt.title("Unemployment Before and During/After COVID-19")
plt.ylabel("Average Unemployment Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
df.groupby("Region")[rate].mean().sort_values().plot(
    kind="bar", figsize=(12, 5))
plt.title("Average Unemployment Rate by State/Region")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()
df.groupby(df["Date"].dt.month)[rate].mean().plot(
    kind="line", marker="o", figsize=(8, 4))
plt.title("Monthly Unemployment Pattern")
plt.xlabel("Month (1 = January, 12 = December)")
plt.ylabel("Average Unemployment Rate (%)")
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()
plt.show()
