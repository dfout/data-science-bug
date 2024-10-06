import json
import matplotlib.pyplot as plt

def calculate_kpis(filename="receipts_received_converted.json"):
    """
    Calculates KPIs from a JSON file containing invoice data.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        tuple: A tuple containing:
            - gross_profit_margin (float): The overall gross profit margin.
            - average_tax_rate (float): The average tax rate.
            - supplier_gpm (dict): A dictionary of gross profit margins per supplier category.
            - supplier_order_counts (dict): A dictionary of order counts per supplier category.
    """

    with open(filename, 'r') as f:
        data = json.load(f)

    total_revenue = 0
    total_cost = 0
    total_tax = 0
    supplier_gpm = {}
    supplier_order_counts = {}

    for invoice in data:
        revenue = float(invoice['total ammount'])
        cost = float(invoice['tax'])  # Assuming 'tax' as the cost
        tax = float(invoice['tax'])
        supplier_category = invoice['supplier category']

        total_revenue += revenue
        total_cost += cost
        total_tax += tax

        if supplier_category not in supplier_gpm:
            supplier_gpm[supplier_category] = {'revenue': 0, 'cost': 0}
        supplier_gpm[supplier_category]['revenue'] += revenue
        supplier_gpm[supplier_category]['cost'] += cost

        if supplier_category not in supplier_order_counts:
            supplier_order_counts[supplier_category] = 0
        supplier_order_counts[supplier_category] += 1

    gross_profit_margin = (total_revenue - total_cost) / total_revenue if total_revenue else 0
    average_tax_rate = total_tax / total_revenue if total_revenue else 0

    for category, values in supplier_gpm.items():
        supplier_gpm[category] = (values['revenue'] - values['cost']) / values['revenue'] if values['revenue'] else 0

    return gross_profit_margin, average_tax_rate, supplier_gpm, supplier_order_counts

# --- Calculate KPIs ---
gross_profit_margin, average_tax_rate, supplier_gpm, supplier_order_counts = calculate_kpis()
print(f"Overall Gross Profit Margin: {gross_profit_margin:.2%}")
print(f"Average Tax Rate: {average_tax_rate:.2%}")

# --- Visualize GPM per Supplier Category ---
plt.figure(figsize=(12, 6))
bars = plt.bar(supplier_gpm.keys(), supplier_gpm.values(), color='skyblue')
plt.xlabel("Supplier Category")
plt.ylabel("Gross Profit Margin")
plt.title("Gross Profit Margin by Supplier Category")
plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for readability
plt.tight_layout() 

# Add data labels to the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, f'{yval:.2%}', ha='center', va='bottom')

plt.show()

# --- Visualize Order Counts per Supplier Category ---
plt.figure(figsize=(12, 6))
plt.bar(supplier_order_counts.keys(), supplier_order_counts.values(), color='salmon')
plt.xlabel("Supplier Category")
plt.ylabel("Number of Orders")
plt.title("Order Count by Supplier Category")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()