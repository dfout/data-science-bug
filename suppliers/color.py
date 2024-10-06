import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def calculate_kpis(data):
    """
    Calculates Key Performance Indicators (KPIs) from a list of invoice data.

    Args:
      data: A list of dictionaries, where each dictionary represents an invoice.

    Returns:
      A dictionary containing the calculated KPIs:
        - gross_profit_margin: The overall gross profit margin.
        - average_tax_rate: The average tax rate across all invoices.
        - supplier_gpm: A dictionary containing the gross profit margin for 
                         each supplier category.
    """
    
    total_revenue = 0
    total_tax = 0
    supplier_revenue = {}
    supplier_tax = {}
    
    for invoice in data:
        revenue = invoice['total ammount']
        tax = invoice['tax']
        supplier = invoice['supplier category']

        total_revenue += revenue
        total_tax += tax

        if supplier in supplier_revenue:
            supplier_revenue[supplier] += revenue
            supplier_tax[supplier] += tax
        else:
            supplier_revenue[supplier] = revenue
            supplier_tax[supplier] = tax

    # Calculate overall GPM and average tax rate
    gross_profit_margin = ((total_revenue - total_tax) / total_revenue) * 100 if total_revenue else 0
    average_tax_rate = (total_tax / total_revenue) * 100 if total_revenue else 0
    
    # Calculate supplier GPM
    supplier_gpm = {
        supplier: ((supplier_revenue[supplier] - supplier_tax[supplier]) / 
                    supplier_revenue[supplier]) * 100 if supplier_revenue[supplier] else 0
        for supplier in supplier_revenue
    }

    return {
        "gross_profit_margin": gross_profit_margin,
        "average_tax_rate": average_tax_rate,
        "supplier_gpm": supplier_gpm,
        "supplier_revenue": supplier_revenue,  # Added for order count analysis
    }

def visualize_gpm(supplier_gpm):
    """
    Visualizes the Gross Profit Margin (GPM) across supplier categories with unique colors.

    Args:
      supplier_gpm: A dictionary containing GPM for each supplier category.
    """
    # Create a color map with unique colors for each category
    categories = list(supplier_gpm.keys())
    colors = plt.cm.viridis(np.linspace(0, 1, len(categories)))  # Use colormap

    plt.figure(figsize=(12, 6))
    plt.bar(categories, supplier_gpm.values(), color=colors)
    plt.xlabel('Supplier Category')
    plt.ylabel('Gross Profit Margin (%)')
    plt.title('Gross Profit Margin Across Supplier Categories')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def visualize_order_counts(data):
    """
    Visualizes the number of orders per supplier category.

    Args:
      data: A list of dictionaries, where each dictionary represents an invoice.
    """
    
    df = pd.DataFrame(data)
    order_counts = df['supplier category'].value_counts()
    
    plt.figure(figsize=(12, 6))
    order_counts.plot(kind='bar', color='skyblue')
    plt.xlabel('Supplier Category')
    plt.ylabel('Number of Orders')
    plt.title('Number of Orders per Supplier Category')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Load the JSON data from the file
with open('receipts_received_converted.json', 'r') as f:
    data = json.load(f)

# Calculate the KPIs
kpis = calculate_kpis(data)

# Print overall GPM and average tax rate (no other prints)
print(f"Overall Gross Profit Margin: {kpis['gross_profit_margin']:.2f}%")
print(f"Average Tax Rate: {kpis['average_tax_rate']:.2f}%")

# Visualize GPM across supplier categories
visualize_gpm(kpis['supplier_gpm'])

# Visualize the number of orders per supplier category
visualize_order_counts(data)
