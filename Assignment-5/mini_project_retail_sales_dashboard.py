import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / "retail_sales.csv"
CHART_FILE = BASE_DIR / "retail_sales_dashboard.png"


def initialize_sales_csv():
    """Creates retail_sales.csv with sample monthly retail data if missing."""
    if not CSV_FILE.exists():
        rows = [
            ["month", "category", "units_sold", "unit_price", "ad_spend", "revenue"],
            ["Jan", "Electronics", 120, 450, 4200, 54000],
            ["Jan", "Apparel", 310, 80, 2100, 24800],
            ["Jan", "Home", 180, 140, 2500, 25200],
            ["Feb", "Electronics", 135, 450, 4600, 60750],
            ["Feb", "Apparel", 290, 80, 1950, 23200],
            ["Feb", "Home", 195, 140, 2700, 27300],
            ["Mar", "Electronics", 160, 450, 5300, 72000],
            ["Mar", "Apparel", 340, 80, 2400, 27200],
            ["Mar", "Home", 210, 140, 2900, 29400],
            ["Apr", "Electronics", 150, 450, 4900, 67500],
            ["Apr", "Apparel", 380, 80, 2650, 30400],
            ["Apr", "Home", 225, 140, 3100, 31500],
            ["May", "Electronics", 185, 450, 6100, 83250],
            ["May", "Apparel", 410, 80, 2850, 32800],
            ["May", "Home", 240, 140, 3300, 33600],
            ["Jun", "Electronics", 210, 450, 6800, 94500],
            ["Jun", "Apparel", 430, 80, 3000, 34400],
            ["Jun", "Home", 260, 140, 3600, 36400],
        ]
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(rows)


def load_sales_data():
    """Reads retail_sales.csv and returns structured records."""
    records = []
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(
                {
                    "month": row["month"],
                    "category": row["category"],
                    "units_sold": int(row["units_sold"]),
                    "unit_price": float(row["unit_price"]),
                    "ad_spend": float(row["ad_spend"]),
                    "revenue": float(row["revenue"]),
                }
            )
    return records


def main():
    initialize_sales_csv()
    records = load_sales_data()

    revenues = np.array([r["revenue"] for r in records])
    units = np.array([r["units_sold"] for r in records])
    ad_spends = np.array([r["ad_spend"] for r in records])

    monthly_revenue = defaultdict(float)
    category_revenue = defaultdict(float)
    month_order = []

    for r in records:
        if r["month"] not in month_order:
            month_order.append(r["month"])
        monthly_revenue[r["month"]] += r["revenue"]
        category_revenue[r["category"]] += r["revenue"]

    print("=== Retail Sales Dashboard Summary ===")
    print(f"Total Records Analyzed : {len(records)}")
    print(f"Total Revenue (H1)     : INR {np.sum(revenues):,.2f}")
    print(f"Average Record Revenue : INR {np.mean(revenues):,.2f}")
    print(f"Total Units Sold       : {np.sum(units):,}")
    print(f"Top Performing Category: {max(category_revenue, key=category_revenue.get)}")

    print("\n--- Monthly Revenue Breakdown ---")
    for m in month_order:
        print(f"  {m:<5}: INR {monthly_revenue[m]:>10,.2f}")

    # Build 3-panel matplotlib dashboard (Line, Bar, Scatter plots)
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.8))
    fig.suptitle("Retail Sales Performance Dashboard (H1)", fontsize=14, fontweight="bold")

    # 1. Line Plot: Monthly Revenue Trend
    m_vals = [monthly_revenue[m] for m in month_order]
    axes[0].plot(month_order, m_vals, marker="o", color="#1f77b4", linewidth=2.2)
    axes[0].set_title("Monthly Revenue Trend")
    axes[0].set_xlabel("Month")
    axes[0].set_ylabel("Revenue (INR)")
    axes[0].grid(True, linestyle="--", alpha=0.5)

    # 2. Bar Chart: Total Revenue by Category
    categories = list(category_revenue.keys())
    c_vals = [category_revenue[c] for c in categories]
    axes[1].bar(categories, c_vals, color=["#2ca02c", "#ff7f0e", "#9467bd"], width=0.55)
    axes[1].set_title("Revenue by Product Category")
    axes[1].set_xlabel("Category")
    axes[1].set_ylabel("Total Revenue (INR)")
    axes[1].grid(axis="y", linestyle="--", alpha=0.5)

    # 3. Scatter Plot: Ad Spend vs Revenue
    axes[2].scatter(ad_spends, revenues, color="#d62728", alpha=0.8, edgecolors="black", s=60)
    axes[2].set_title("Ad Spend vs. Revenue")
    axes[2].set_xlabel("Ad Spend (INR)")
    axes[2].set_ylabel("Revenue (INR)")
    axes[2].grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig(CHART_FILE, dpi=150)
    print(f"\nDashboard chart saved to: {CHART_FILE.name}")
    plt.show()


if __name__ == "__main__":
    main()