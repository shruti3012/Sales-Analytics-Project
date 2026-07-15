import pandas as pd

print("Hello Shruti")

orders = pd.read_csv("data/raw/orders.csv")

print("========== DATA ==========")
print(orders.head())

print("\n========== ROWS & COLUMNS ==========")
print(orders.shape)

print("\n========== COLUMN NAMES ==========")
print(orders.columns)

print("\n========== DATA TYPES ==========")
print(orders.dtypes)

print("\n========== MISSING VALUES ==========")
print(orders.isnull().sum())

print("\n========== ADDING TOTAL AMOUNT ==========")

orders["TotalAmount"] = orders["Quantity"] * orders["Price"]

print(orders.head())

# Read Customers CSV
customers = pd.read_csv("data/raw/customers.csv")

# Read Products CSV
products = pd.read_csv("data/raw/products.csv")

print("\n========== CUSTOMERS ==========")
print(customers.head())

print("\n========== PRODUCTS ==========")
print(products.head())

print("\n========== JOINING ORDERS & CUSTOMERS ==========")

sales = pd.merge(
    orders,
    customers,
    on="CustomerID",
    how="inner"
)

print(sales.head())

print("\n========== JOINING PRODUCTS ==========")

sales = pd.merge(
    sales,
    products,
    on="ProductID",
    how="inner"
)

# Remove duplicate Category column from Orders
sales = sales.drop(columns=["Category_x"])

# Rename Category_y to Category
sales = sales.rename(columns={"Category_y": "Category"})

print(sales.head())

print("\n========== SAVING PROCESSED DATA ==========")

print("\n========== CALCULATING TOTAL SALES ==========")

sales["TotalSales"] = sales["Quantity"] * sales["Price"]
print("\n========== CONVERTING ORDER DATE ==========")

sales["OrderDate"] = pd.to_datetime(
    sales["OrderDate"],
    format="%d-%m-%Y"
)

print(sales[["OrderID", "OrderDate"]].head())

print("\nData Type of OrderDate:")
print(sales["OrderDate"].dtype)

print(sales[["OrderID", "ProductName", "Quantity", "Price", "TotalSales"]].head())

print("\n========== DATA QUALITY CHECK ==========")

print("Total Rows:", len(sales))
print("Duplicate Rows:", sales.duplicated().sum())
print("Missing Values:\n")
print(sales.isnull().sum())
sales.to_csv("data/processed/final_sales.csv", index=False)

print("\n========== REGION WISE SALES ==========")

region_sales = sales.groupby("Region")["TotalSales"].sum()

print(region_sales)

print("\n========== CATEGORY WISE SALES ==========")

print(sales.columns)

category_sales = sales.groupby("Category")["TotalSales"].sum()
print(category_sales)

print("\n========== TOP CUSTOMERS ==========")

customer_sales = sales.groupby("CustomerName")["TotalSales"].sum()

print(customer_sales.sort_values(ascending=False))

print("\n========== TOP PRODUCTS ==========")

product_sales = sales.groupby("ProductName")["TotalSales"].sum()

print(product_sales.sort_values(ascending=False))

print("File saved successfully!")

print("\n========== SAVING PARQUET FILE ==========")

sales.to_parquet(
    "data/processed/final_sales.parquet",
    index=False
)

print("Parquet file saved successfully!")