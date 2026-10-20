"""
Sales Performance Dashboard - Part 2
Author: Katlego Modiba | R115M Case Study
"""
import pandas as pd
import matplotlib.pyplot as plt

# 1. Create summary data
warehouses = ['Warehouse A', 'Warehouse B', 'Warehouse C']
revenue = [42.5, 38.2, 34.8]
regions = ['Gauteng', 'KZN', 'W.Cape', 'Mpumalanga']
region_rev = [45.0, 32.5, 24.2, 13.8]

print("=== R115M SALES DASHBOARD ===")
print(f"Total: R{sum(revenue)}M from 5,000 orders")
print(f"Top Warehouse: {warehouses[0]} R{revenue[0]}M")
print(f"Leakage: Warehouse B 7.5% fee = R3M loss")
print(f"Top Region: Gauteng R45M (39%)")

# 2. Create charts
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.bar(warehouses, revenue, color=['green', 'red', 'blue'])
plt.title('Revenue by Warehouse (R Millions)')
plt.ylabel('R Millions')
plt.xticks(rotation=10)

plt.subplot(1, 2, 2)
plt.bar(regions, region_rev, color='orange')
plt.title('Revenue by Region (R Millions)')
plt.xticks(rotation=10)

plt.tight_layout()
plt.savefig('sales_dashboard.png')
print("\nChart saved: sales_dashboard.png")
