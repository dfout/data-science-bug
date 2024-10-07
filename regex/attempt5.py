import re
import pandas as pd
import matplotlib.pyplot as plt

def analyze_log(log_file):
    """
    Analyzes the log file to extract node failures, not-responding nodes,
    and configured-out nodes, and generates a report.

    Args:
        log_file (str): The path to the log file.
    """

    # Regular expressions for different log entry types
    node_failure_regex = re.compile(r'node-(?P<node>\d+).*?psu failure')
    not_responding_regex = re.compile(r'node-(?P<node>\d+).*?not responding')
    configured_out_regex = re.compile(r'node-(?P<node>\d+).*?configured out')

    node_failures = {}
    not_responding_nodes = {}
    configured_out_nodes = set()

    with open(log_file, 'r') as f:
        for line in f:
            # Check for node failures
            match = node_failure_regex.search(line)
            if match:
                node = match.group('node')
                node_failures[node] = node_failures.get(node, 0) + 1

            # Check for not-responding nodes
            match = not_responding_regex.search(line)
            if match:
                node = match.group('node')
                not_responding_nodes[node] = not_responding_nodes.get(node, 0) + 1

            # Check for configured-out nodes
            match = configured_out_regex.search(line)
            if match:
                node = match.group('node')
                configured_out_nodes.add(f"node-{node}")

    # Create a dataframe for analysis and plotting
    df = pd.DataFrame({
        'Node': list(set(node_failures.keys()) | set(not_responding_nodes.keys())),
        'Failures': [node_failures.get(str(node), 0) for node in range(256)],
        'Not Responding': [not_responding_nodes.get(str(node), 0) for node in range(256)]
    })

    # Save the dataframe to a CSV file
    df.to_csv('node_status_report.csv', index=False)

    # Sort dataframe by node for a more organized chart
    df = df.sort_values(by='Node')
    df = df.reset_index(drop=True)
    
    # Create a bar chart
    plt.figure(figsize=(15, 6))  # Adjust figure size as needed
    plt.bar(df['Node'], df['Failures'], label='Failures')
    plt.bar(df['Node'], df['Not Responding'], bottom=df['Failures'], label='Not Responding')
    plt.xlabel('Node')
    plt.ylabel('Count')
    plt.title('Node Failure and Not Responding Analysis')
    plt.xticks(rotation=90) 
    plt.legend()
    plt.tight_layout()  # Adjust layout to prevent labels from overlapping
    plt.show()

    # Print configured-out nodes
    print("\nConfigured Out Nodes:")
    print({ "conOut": list(configured_out_nodes) })

# Analyze the log file
analyze_log('HPC_PZSlP.log')