import pandas as pd

def calculate_kpis_per_supplier_category(df):
    # Ensure necessary columns exist
    required_columns = ['Net Tax Taxed', 'tax', 'total ammount', 'supplier category']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("Missing required columns in dataset.")

    # Gross Profit Margin = (Total Amount - Tax) / Total Amount * 100
    df['Gross Profit Margin'] = (df['total ammount'] - df['tax']) / df['total ammount'] * 100

    # Average Tax Rate = Tax / Net Tax Taxed * 100
    df['Tax Rate'] = df['tax'] / df['Net Tax Taxed'] * 100

    # Calculate overall metrics (mean gross profit margin and tax rate)
    avg_gross_profit_margin = df['Gross Profit Margin'].mean()
    avg_tax_rate = df['Tax Rate'].mean()

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

    return {
        'Overall KPIs': {
            'Average Gross Profit Margin (%)': avg_gross_profit_margin,
            'Average Tax Rate (%)': avg_tax_rate
        },
        'Supplier Category KPIs': supplier_category_kpi
    }

# Load data from JSON
df = pd.read_json('receipts_received_converted.json')

# Calculate KPIs
kpis = calculate_kpis_per_supplier_category(df)

# Display KPIs
print("Overall KPIs:")
print(kpis['Overall KPIs'])

print("\nSupplier Category KPIs:")
print(kpis['Supplier Category KPIs'])
