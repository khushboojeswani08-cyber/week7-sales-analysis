from pathlib import Path
import pandas as pd

from data_loader import load_sales_data
from data_cleaner import clean_sales_data
from analyzer import (
calculate_basic_stats,
analyze_sales_by_category,
analyze_top_products,
analyze_monthly_trends,
)
from visualizer import create_visualizations
from report_generator import generate_excel_report

BASE_DIR = Path(file).resolve().parent
OUTPUT_DIR = BASE_DIR / "data" / "processed"

def main():
print("=" * 50)
print("       SALES DATA ANALYSIS DASHBOARD")
print("=" * 50)

# 1. Load sales data
df = load_sales_data()

if df is None or df.empty:
    print("No sales data available. Please check the CSV file.")
    return

# 2. Clean data
df = clean_sales_data(df)

if df.empty:
    print("No valid records remain after cleaning.")
    return

# 3. Save cleaned data
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

cleaned_file = OUTPUT_DIR / "cleaned_sales_data.csv"
df.to_csv(cleaned_file, index=False)

print(f"\nCleaned data saved to: {cleaned_file}")

# 4. Calculate statistics
stats = calculate_basic_stats(df)

print("\n--- BASIC SALES STATISTICS ---")

for metric, value in stats.items():
    print(f"{metric.replace('_', ' ').title()}: {value:,.2f}")

# 5. Analyze category sales
category_sales = analyze_sales_by_category(df)

print("\n--- SALES BY CATEGORY ---")
print(category_sales)

# 6. Find top products
top_products = analyze_top_products(df)

print("\n--- TOP SELLING PRODUCTS ---")
print(top_products)

# 7. Analyze monthly trends
monthly_sales = analyze_monthly_trends(df)

print("\n--- MONTHLY SALES TRENDS ---")
print(monthly_sales)

# 8. Create charts
create_visualizations(
    category_sales,
    monthly_sales
)

# 9. Generate Excel report
report_path = generate_excel_report(
    stats,
    category_sales,
    top_products,
    monthly_sales
)

print("\n" + "=" * 50)
print("SALES ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 50)
print(f"Cleaned CSV: {cleaned_file}")
print(f"Excel Report: {report_path}")
print("Charts: reports/category_sales.png")
print("        reports/monthly_sales.png")

if name == "main":
main()
