import pandas as pd
import matplotlib.pyplot as plt

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("weather_data.csv")

# =========================
# CLEAN COLUMN NAMES
# =========================

df.columns = df.columns.str.strip().str.lower()

print("\nDetected Columns:")
print(df.columns)

# =========================
# CLEAN DATA
# =========================

# Temperature cleanup (removes text like °C if any)
df["temperature"] = (
    df["temperature"]
    .astype(str)
    .str.extract(r"(-?\d+\.?\d*)")[0]
)

df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")

# Year cleanup
df["year"] = pd.to_numeric(df["year"], errors="coerce")

# Day cleanup (format like 11/6)
df["day"] = df["day"].astype(str).str.strip()

# Remove invalid rows
df = df.dropna(subset=["temperature", "year", "day"])

print("\nData Shape After Cleaning:", df.shape)

# =========================
# CREATE DATE COLUMN
# =========================

df["date"] = pd.to_datetime(
    df["year"].astype(int).astype(str) + "-" + df["day"],
    format="%Y-%m/%d",
    errors="coerce"
)

df = df.dropna(subset=["date"])

# =========================
# 1. OVERVIEW
# =========================

print("\n========== TEMPERATURE OVERVIEW ==========")
print(f"Average Temperature: {df['temperature'].mean():.2f}")

# =========================
# 2. MONTHLY ANALYSIS
# =========================

df["month"] = df["date"].dt.month_name()

month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

monthly_avg = df.groupby("month")["temperature"].mean().reindex(month_order)

print("\n========== MONTHLY AVERAGE TEMPERATURE ==========")
print(monthly_avg)

# Plot monthly averages
plt.figure(figsize=(10, 5))
monthly_avg.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =========================
# 3. HOTTEST / COLDEST
# =========================

print("\n========== HOTTEST DAY ==========")
print(df.loc[df["temperature"].idxmax()])

print("\n========== COLDEST DAY ==========")
print(df.loc[df["temperature"].idxmin()])

# =========================
# 4. TEMPERATURE TREND
# =========================

plt.figure(figsize=(12, 5))
plt.plot(df["date"], df["temperature"], color="red")
plt.title("Temperature Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.grid(True)
plt.tight_layout()
plt.show()

# =========================
# 5. SEASONAL ANALYSIS
# =========================

def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

df["season"] = df["date"].dt.month.apply(get_season)

seasonal_avg = df.groupby("season")["temperature"].mean()

print("\n========== SEASONAL AVERAGE TEMPERATURE ==========")
print(seasonal_avg)

print("\n========== ANALYSIS COMPLETE ==========")