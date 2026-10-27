import pandas as pd
from pathlib import Path

def generate_excel_report(
stats,
category_sales,
top_products,
monthly_sales,
output_path=None
):
"""Generate an Excel workbook containing sales analysis."""

if output_path is None:
    output_path = (
        Path(__file__).resolve().parent
        / "reports"
        / "sales_report.xlsx"
    )
else:
    output_path = Path(output_path)

output_path.parent.mkdir(parents=True, exist_ok=True)

summary = pd.DataFrame(
    list(stats.items()),
    columns=["Metric", "Value"]
)

with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    summary.to_excel(
        writer,
        sheet_name="Summary",
        index=False
    )

    category_sales.to_excel(
        writer,
        sheet_name="Category Analysis"
    )

    top_products.to_excel(
        writer,
        sheet_name="Top Products"
    )

    monthly_sales.to_excel(
        writer,
        sheet_name="Monthly Trends"
    )

print(f"Excel report generated successfully: {output_path}")
return output_path

if name == "main":
print("Excel report generator module is ready.")
