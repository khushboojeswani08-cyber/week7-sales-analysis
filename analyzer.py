import pandas as pd

def calculate_basic_stats(df):
"""Calculate basic sales statistics."""

if df is None or df.empty:
    return {}

stats = {
    "total_sales": df["total_amount"].sum(),
    "average_order_value": df["total_amount"].mean(),
    "total_orders": len(df),
    "unique_customers": df["customer_id"].nunique(),
    "unique_products": df["product_id"].nunique()
}

return stats

def analyze_sales_by_category(df):
"""Calculate sales for each product category."""

if df is None or df.empty:
    return pd.DataFrame()

category_sales = df.groupby("category").agg(
    total_sales=("total_amount", "sum"),
    total_quantity=("quantity", "sum"),
    total_orders=("order_id", "count")
)

return category_sales.sort_values(
    by="total_sales", ascending=False
)

def analyze_top_products(df, top_n=5):
"""Find the top-selling products by revenue."""

if df is None or df.empty:
    return pd.DataFrame()

products = df.groupby(
    ["product_id", "product_name"]
).agg(
    total_sales=("total_amount", "sum"),
    quantity_sold=("quantity", "sum")
)

return products.sort_values(
    by="total_sales", ascending=False
).head(top_n)

def analyze_monthly_trends(df):
"""Analyze monthly sales trends."""

if df is None or df.empty:
    return pd.DataFrame()

if "order_date" not in df.columns:
    return pd.DataFrame()

data = df.copy()
data["order_date"] = pd.to_datetime(
    data["order_date"], errors="coerce"
)
data = data.dropna(subset=["order_date"])

data["month"] = data["order_date"].dt.to_period("M")

monthly_sales = data.groupby("month").agg(
    total_sales=("total_amount", "sum"),
    total_orders=("order_id", "count")
)

monthly_sales["growth_rate"] = (
    monthly_sales["total_sales"].pct_change() * 100
)

return monthly_sales

if name == "main":
print("Sales analyzer module is ready.")
print("Functions available:")
print("1. Calculate basic statistics")
print("2. Analyze sales by category")
print("3. Find top-selling products")
print("4. Analyze monthly sales trends")
