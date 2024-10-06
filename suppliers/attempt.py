import json
import matplotlib.pyplot as plt

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
  total_cost = 0
  total_tax = 0
  supplier_revenue = {}
  supplier_cost = {}

  for invoice in data:
    # Assuming 'total ammount' represents revenue and 'Net + tax' represents cost
    revenue = invoice['total ammount']
    cost = invoice['Net + tax']
    tax = invoice['tax']
    supplier = invoice['supplier category']

    total_revenue += revenue
    total_cost += cost
    total_tax += tax

    if supplier in supplier_revenue:
      supplier_revenue[supplier] += revenue
      supplier_cost[supplier] += cost
    else:
      supplier_revenue[supplier] = revenue
      supplier_cost[supplier] = cost

  gross_profit_margin = ((total_revenue - total_cost) / total_revenue) * 100 if total_revenue else 0
  average_tax_rate = (total_tax / total_revenue) * 100 if total_revenue else 0
  supplier_gpm = {supplier: ((supplier_revenue[supplier] - supplier_cost[supplier]) / 
                               supplier_revenue[supplier]) * 100 
                   if supplier_revenue[supplier] else 0
                   for supplier in supplier_revenue}

  return {
    "gross_profit_margin": gross_profit_margin,
    "average_tax_rate": average_tax_rate,
    "supplier_gpm": supplier_gpm,
  }

# Load the JSON data from the file
with open('receipts_received_converted.json', 'r') as f:
  data = json.load(f)

# Calculate the KPIs
kpis = calculate_kpis(data)

# Print the KPIs
print(f"Overall Gross Profit Margin: {kpis['gross_profit_margin']:.2f}%")
print(f"Average Tax Rate: {kpis['average_tax_rate']:.2f}%")

# Print and visualize the GPM for each supplier category
print("\nGross Profit Margin per Supplier Category:")
for supplier, gpm in kpis['supplier_gpm'].items():
    print(f"- {supplier}: {gpm:.2f}%")

# Create a bar chart for GPM across supplier categories
plt.figure(figsize=(12, 6))
plt.bar(kpis['supplier_gpm'].keys(), kpis['supplier_gpm'].values())
plt.xlabel('Supplier Category')
plt.ylabel('Gross Profit Margin (%)')
plt.title('Gross Profit Margin Across Supplier Categories')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()