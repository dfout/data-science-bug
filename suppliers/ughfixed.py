import json
import matplotlib.pyplot as plt
import numpy as np

def calculate_kpis(filename="receipts_received_converted.json"):
    """
    Calculates KPIs from a JSON file containing invoice data.

    Args:
        filename (str, optional): The name of the JSON file. 
                                    Defaults to "receipts_received_converted.json".

    Returns:
        tuple: A tuple containing the overall gross profit margin, 
               average tax rate, and a dictionary of GPM per supplier category.
    """

    with open(filename, 'r') as f:
        data = json.load(f)

    total_revenue = 0
    total_cost = 0  # Assuming 'tax' as the cost
    total_tax = 0
    supplier_category_data = {}
    supplier_category_counts = {}

    for invoice in data:
        revenue = float(invoice['total ammount'])
        cost = float(invoice['tax']) 
        tax = float(invoice['tax'])
        category = invoice['supplier category']

        total_revenue += revenue
        total_cost += cost
        total_tax += tax

        if category not in supplier_category_data:
            supplier_category_data[category] = {'revenue': 0, 'cost': 0, 'count': 0}
        supplier_category_data[category]['revenue'] += revenue
        supplier_category_data[category]['cost'] += cost
        supplier_category_data[category]['count'] += 1

        if category not in supplier_category_counts:
            supplier_category_counts[category] = 0
        supplier_category_counts[category] += 1

    # Overall KPIs
    gross_profit_margin = ((total_revenue - total_cost) / total_revenue) * 100 if total_revenue else 0
    average_tax_rate = (total_tax / total_revenue) * 100 if total_revenue else 0

    # GPM per supplier category
    supplier_category_gpm = {}
    for category, values in supplier_category_data.items():
        category_gpm = ((values['revenue'] - values['cost']) / values['revenue']) * 100 if values['revenue'] else 0
        supplier_category_gpm[category] = category_gpm

    print(f"Overall Gross Profit Margin: {gross_profit_margin:.2f}%")
    print(f"Average Tax Rate: {average_tax_rate:.2f}%")

    # Visualization for GPM across supplier categories
    categories = list(supplier_category_gpm.keys())
    gpm_values = list(supplier_category_gpm.values())
    
    # Assigning unique colors for each category in GPM chart
    colors = plt.cm.viridis(np.linspace(0, 1, len(categories))) 

    plt.bar(categories, gpm_values, color=colors)
    plt.xlabel("Supplier Category")
    plt.ylabel("Gross Profit Margin (%)")
    plt.title("Gross Profit Margin by Supplier Category")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout() 
    plt.show()

    # Visualization for Order Count by Supplier Category
    plt.figure(figsize=(8, 6)) 
    #  Assigning unique colors for each category in Order Count chart
    order_colors = plt.cm.viridis(np.linspace(0, 1, len(supplier_category_counts)))

    plt.bar(supplier_category_counts.keys(), supplier_category_counts.values(), color=order_colors)
    plt.xlabel("Supplier Category")
    plt.ylabel("Number of Orders")
    plt.title("Order Count by Supplier Category")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout() 
    plt.show()

    return gross_profit_margin, average_tax_rate, supplier_category_gpm

# Call the function to calculate KPIs
calculate_kpis()