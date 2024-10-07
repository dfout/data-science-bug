import re
import pandas as pd
import matplotlib.pyplot as plt

def analyze_hpc_log(log_file):
    """
    Analyzes HPC log data to extract node failures and not-responding events,
    then generates a bar chart visualizing the frequency of each event type per node.

    Args:
        log_file (str): Path to the HPC log file.

    Returns:
        None (displays a bar chart)
    """

    node_failures = {}
    node_not_responding = {}

    with open(log_file, 'r') as f:
        for line in f:
            # Extract node failures
            failure_match = re.search(r'node-(\d+).*?psu failure', line)
            if failure_match:
                node = failure_match.group(1)
                node_failures[node] = node_failures.get(node, 0) + 1

            # Extract not responding nodes
            not_responding_match = re.search(r'node-(\d+).*?not responding', line)
            if not_responding_match:
                node = not_responding_match.group(1)
                node_not_responding[node] = node_not_responding.get(node, 0) + 1

    # Combine data for plotting
    df = pd.DataFrame({
        'Node Failures': pd.Series(node_failures),
        'Not Responding': pd.Series(node_not_responding)
    }).fillna(0)

    # Plotting
    df.plot(kind='bar', figsize=(10, 6))
    plt.title('HPC Node Issues')
    plt.xlabel('Node ID')
    plt.ylabel('Frequency')
    plt.show()

# Example usage:
analyze_hpc_log('HPC_PZSlP.log')