import duckdb

result = duckdb.sql("""
SELECT Region,
       SUM(TotalSales) AS TotalSales
FROM 'data/processed/final_sales.csv'
GROUP BY Region
ORDER BY TotalSales DESC
""")

print(result)