import pandas as pd

def clean_sales_data(df):
"""Clean sales data and prepare it for analysis."""

if df is None or df.empty:
    print("No data available for cleaning.")
    return pd.DataFrame()

df = df.copy()

# Remove duplicate records
initial_rows = len(df)
df = df.drop_duplicates()
print(f"Duplicate rows removed: {initial_rows - len(df)}")

# Remove records without essential information
essential_columns = [
    col for col in ["order_id", "total_amount"]
    if col in df.columns
]

if essential_columns:
    df = df.dropna(subset=essential_columns)

# Convert numeric columns
numeric_columns = ["quantity", "unit_price", "total_amount"]

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Fill missing numerical values with the column median
for col in numeric_columns:
    if col in df.columns and df[col].isna().any():
        median_value = df[col].median()

        if pd.notna(median_value):
            df[col] = df[col].fillna(median_value)

# Convert order dates
if "order_date" in df.columns:
    df["order_date"] = pd.to_datetime(
        df["order_date"], errors="coerce"
    )

print(f"Rows remaining after cleaning: {len(df)}")
print("Data cleaning completed successfully!")

return df

if name == "main":
print("Data cleaner module is ready.")
