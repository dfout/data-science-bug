import re
from collections import defaultdict
import matplotlib.pyplot as plt

def analyze_log(log_file):
    """
    Analyzes the log file for node failures and not-responding events.

    Args:
        log_file (str): The path to the log file.

    Returns:
        tuple: A tuple containing two dictionaries, one for node failures and one for not-responding events. 
               Each dictionary has node names as keys and counts as values.
    """

    node_failures = defaultdict(int)
    not_responding = defaultdict(int)

    with open(log_file, 'r') as f:
        for line in f:
            # Match node failures
            match_failure = re.search(r'node-(\d+).*?(psu failure|failure)', line)
            if match_failure:
                node_failures[match_failure.group(1)] += 1

            # Match not responding events
            match_not_responding = re.search(r'node-(\d+).*?not responding', line)
            if match_not_responding:
                not_responding[match_not_responding.group(1)] += 1

    return node_failures, not_responding

def plot_results(node_failures, not_responding):
    """
    Plots the node failure and not-responding counts.

    Args:
        node_failures (dict): Dictionary of node failures.
        not_responding (dict): Dictionary of not-responding events.
    """

    # Combine the dictionaries and sort by node number
    combined_data = defaultdict(lambda: {'failures': 0, 'not_responding': 0})
    for node, count in node_failures.items():
        combined_data[int(node)]['failures'] = count
    for node, count in not_responding.items():
        combined_data[int(node)]['not_responding'] = count
    sorted_data = dict(sorted(combined_data.items()))

    # Extract data for plotting
    nodes = list(sorted_data.keys())
    failures = [data['failures'] for data in sorted_data.values()]
    not_responding_counts = [data['not_responding'] for data in sorted_data.values()]

    # Create bar chart
    fig, ax = plt.subplots(figsize=(15, 6))  # Adjust figure size if needed

    bar_width = 0.35
    index = range(len(nodes))

    bar1 = ax.bar(index, failures, bar_width, label='Failures')
    bar2 = ax.bar([i + bar_width for i in index], not_responding_counts, bar_width, label='Not Responding')

    # Add labels and title
    ax.set_xlabel('Node Number')
    ax.set_ylabel('Count')
    ax.set_title('Node Failures and Not Responding Events')
    ax.set_xticks([i + bar_width/2 for i in index])
    ax.set_xticklabels(nodes, rotation=90)  # Rotate x-axis labels if needed
    ax.legend()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    log_file = 'HPC_PZSlP.log'  # Update with the actual file name
    node_failures, not_responding = analyze_log(log_file)
    plot_results(node_failures, not_responding)