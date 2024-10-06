import json
import matplotlib.pyplot as plt

def calculate_kpis(file_path):
    """
    Calculates and visualizes KPIs from invoice data.

    Args:
        file_path (str): The path to the JSON file containing invoice data.

    Returns:
        None. Prints the overall GPM and average tax rate. 
              Displays a chart of GPM across supplier categories.
    """

    with open(file_path, 'r') as f:
        data = json.load(f)

    total_revenue = sum(entry['total ammount'] for entry in data)
    total_cost = sum(entry['tax'] for entry in data)  # Assuming 'tax' represents the cost
    total_tax = sum(entry['tax'] for entry in data)

    # Calculate overall GPM
    gross_profit = total_revenue - total_cost
    gpm = (gross_profit / total_revenue) * 100 if total_revenue else 0

    # Calculate average tax rate
    average_tax_rate = (total_tax / (total_revenue- total_tax)) * 100 if total_revenue else 0

    # Calculate GPM per supplier category
    supplier_category_gpm = {}
    for entry in data:
        category = entry['supplier category']
        revenue = entry['total ammount']
        cost = entry['tax'] 
        profit = revenue - cost

        if category not in supplier_category_gpm:
            supplier_category_gpm[category] = {'profit': 0, 'revenue': 0}
        supplier_category_gpm[category]['profit'] += profit
        supplier_category_gpm[category]['revenue'] += revenue

    for category, values in supplier_category_gpm.items():
        supplier_category_gpm[category]['gpm'] = (values['profit'] / values['revenue']) * 100 if values['revenue'] else 0

    # Visualization
    categories = list(supplier_category_gpm.keys())
    gpm_values = [supplier_category_gpm[category]['gpm'] for category in categories]

    plt.figure(figsize=(10, 6))  # Adjust figure size as needed
    plt.bar(categories, gpm_values, color=plt.cm.viridis(gpm_values)) 
    plt.xlabel('Supplier Category')
    plt.ylabel('Gross Profit Margin (%)')
    plt.title('Gross Profit Margin by Supplier Category')
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  

    print(f"Overall Gross Profit Margin: {gpm:.2f}%")
    print(f"Average Tax Rate: {average_tax_rate:.2f}%")

    plt.show()

# Example usage:
file_path = 'receipts_received_converted.json'
calculate_kpis(file_path)