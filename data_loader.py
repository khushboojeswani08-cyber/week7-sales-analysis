import pandas as pd
from pathlib import Path

def load_sales_data(file_path=None):
"""Load sales data from a CSV file."""

if file_path is None:
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "data" / "raw" / "sales_data.csv"

try:
    df = pd.read_csv(file_path)

    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(
            df["order_date"], errors="coerce"
        )

    print("Sales data loaded successfully!")
    print(f"Total rows: {df.shape[0]}")
    print(f"Total columns: {df.shape[1]}")

    return df

except FileNotFoundError:
    print(f"Error: CSV file not found at {file_path}")
    return None

except Exception as error:
    print(f"Error loading sales data: {error}")
    return None

if name == "main":
sales_df = load_sales_data()

if sales_df is not None:
    print("\nFirst five records:")
    print(sales_df.head())
