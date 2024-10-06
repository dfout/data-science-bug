import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

# Load JSON data
with open('receipts_received_converted.json', 'r') as f:
    data = json.load(f)

# Convert JSON array into a DataFrame
df = pd.DataFrame(data)

# Optionally, inspect the first few rows of the data
print(df.head())

# Select relevant columns for heatmap (assuming numerical or categorical data for the heatmap)
# Modify this based on your actual data columns, here as an example:
heatmap_data = df.pivot_table(index='tax', columns='total ammount', values='autorization code', aggfunc='sum')

# Generate the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, cmap='coolwarm', annot=True)

# Set labels and title
plt.title('Heatmap of Received Quantities by Send Date and Article')
plt.xlabel('Article')
plt.ylabel('Send Date')

# Show the heatmap
plt.tight_layout()
plt.show()
