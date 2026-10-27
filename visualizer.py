import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from pathlib import Path

def create_visualizations(category_sales, monthly_sales, output_dir=None):
"""Create and save sales charts."""

if output_dir is None:
    output_dir = Path(__file__).resolve().parent / "reports"
else:
    output_dir = Path(output_dir)

output_dir.mkdir(parents=True, exist_ok=True)

# Category-wise sales chart
if category_sales is not None and not category_sales.empty:
    if "total_sales" in category_sales.columns:
        values = category_sales["total_sales"]
    else:
        values = category_sales.iloc[:, 0]

    plt.figure(figsize=(9, 5))
    values.sort_values(ascending=False).plot(kind="bar")
    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales (Rs.)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(output_dir / "category_sales.png")
    plt.close()

# Monthly sales trend chart
if monthly_sales is not None and not monthly_sales.empty:
    if "total_sales" in monthly_sales.columns:
        values = monthly_sales["total_sales"]
    else:
        values = monthly_sales.iloc[:, 0]

    plt.figure(figsize=(10, 5))
    values.plot(kind="line", marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales (Rs.)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_dir / "monthly_sales.png")
    plt.close()

print(f"Charts saved in: {output_dir}")

if name == "main":
print("Sales visualization module is ready.")
