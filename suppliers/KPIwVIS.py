import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_kpis(df):
    # Ensure necessary columns exist
    required_columns = ['Net Tax Taxed', 'tax', 'total ammount', 'supplier category']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("Missing required columns in dataset.")

    # Gross Profit Margin = (Total Amount - Tax) / Total Amount * 100
    df['Gross Profit Margin'] = (df['total ammount'] - df['tax']) / df['total ammount'] * 100

    # Average Tax Rate = Tax / Net Tax Taxed * 100
    df['Tax Rate'] = df['tax'] / df['Net Tax Taxed'] * 100

    # KPI analysis per supplier category
    supplier_category_kpi = df.groupby('supplier category').agg({
        'total ammount': 'sum',
        'tax': 'sum',
        'Gross Profit Margin': 'mean'
    }).reset_index()

    supplier_category_kpi.rename(columns={
        'total ammount': 'Total Revenue',
        'tax': 'Total Tax',
        'Gross Profit Margin': 'Average Gross Profit Margin'
    }, inplace=True)

    # Plot the bar chart for Total Revenue, Total Tax, and Average Gross Profit Margin
    plt.figure(figsize=(14, 7))

    # Subplot 1: Total Revenue per Supplier Category
    plt.subplot(1, 3, 1)
    sns.barplot(x='supplier category', y='Total Revenue', data=supplier_category_kpi)
    plt.title('Total Revenue by Supplier Category')
    plt.xticks(rotation=45, ha='right')

    # Subplot 2: Total Tax per Supplier Category
    plt.subplot(1, 3, 2)
    sns.barplot(x='supplier category', y='Total Tax', data=supplier_category_kpi, palette='Blues_d')
    plt.title('Total Tax by Supplier Category')
    plt.xticks(rotation=45, ha='right')

    # Subplot 3: Average Gross Profit Margin per Supplier Category
    plt.subplot(1, 3, 3)
    sns.barplot(x='supplier category', y='Average Gross Profit Margin', data=supplier_category_kpi, palette='Greens_d')
    plt.title('Average Gross Profit Margin by Supplier Category')
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.show()

    # Pie chart for the overall revenue breakdown by supplier category
    plt.figure(figsize=(8, 8))
    plt.pie(supplier_category_kpi['Total Revenue'], labels=supplier_category_kpi['supplier category'], autopct='%1.1f%%', startangle=140)
    plt.title('Revenue Breakdown by Supplier Category')
    plt.show()

# Load data from JSON
df = pd.read_json('receipts_received_converted.json')

# Visualize KPIs
visualize_kpis(df)
