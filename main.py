import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(file).resolve().parent
DATA_FILE = BASE_DIR / "data" / "raw" / "sales_data.csv"
OUTPUT_DIR = BASE_DIR / "data" / "processed"
REPORT_DIR = BASE_DIR / "reports"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

def main():
print("=" * 45)
print("       SALES DATA ANALYSIS DASHBOARD")
print("=" * 45)

# Load sales data
df = pd.read_csv(DATA_FILE)
df["order_date"] = pd.to_datetime(df["order_date"])

# Clean data
df = df.drop_duplicates()
df = df.dropna(subset=["order_id", "total_amount"])

df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["total_amount"] = pd.to_numeric(
    df["total_amount"], errors="coerce"
)
df = df.dropna(subset=["quantity", "total_amount"])

# Basic analysis
total_sales = df["total_amount"].sum()
average_order = df["total_amount"].mean()
total_orders = len(df)
total_customers = df["customer_id"].nunique()

print(f"\nTotal Sales: Rs. {total_sales:,.2f}")
print(f"Average Order Value: Rs. {average_order:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Unique Customers: {total_customers}")

# Sales by category
category_sales = df.groupby("category")["total_amount"].sum()
category_sales = category_sales.sort_values(ascending=False)

print("\nSales by Category:")
print(category_sales)

# Monthly sales analysis
df["month"] = df["order_date"].dt.to_period("M").astype(str)
monthly_sales = df.groupby("month")["total_amount"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Save cleaned data
df.to_csv(OUTPUT_DIR / "cleaned_sales_data.csv", index=False)

# Save analysis report
with pd.ExcelWriter(REPORT_DIR / "sales_report.xlsx") as writer:
    pd.DataFrame({
        "Metric": [
            "Total Sales",
            "Average Order Value",
            "Total Orders",
            "Unique Customers"
        ],
        "Value": [
            total_sales,
            average_order,
            total_orders,
            total_customers
        ]
    }).to_excel(writer, sheet_name="Summary", index=False)

    category_sales.to_frame("Total Sales").to_excel(
        writer, sheet_name="Category Analysis"
    )

    monthly_sales.to_frame("Total Sales").to_excel(
        writer, sheet_name="Monthly Trends"
    )

# Create monthly sales chart
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (Rs.)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(REPORT_DIR / "monthly_sales.png")
plt.close()

# Create category sales chart
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales (Rs.)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(REPORT_DIR / "category_sales.png")
plt.close()

print("\nFiles generated successfully!")
print("Cleaned data: data/processed/cleaned_sales_data.csv")
print("Excel report: reports/sales_report.xlsx")
print("Charts: reports/monthly_sales.png and category_sales.png")

if name == "main":
main()
