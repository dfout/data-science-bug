import re
from collections import Counter
import matplotlib.pyplot as plt

def extract_failures_and_not_responding_nodes(log_file):
    """
    Extracts node failures and non-responding node entries from the log file.

    Args:
        log_file (str): The path to the log file.

    Returns:
        dict: A dictionary with lists of failures and non-responding nodes.
    """

    # Regex patterns to match failures and non-responding nodes
    failure_pattern = re.compile(r"node-\d+ .*? psu \d+ \d+ psu failure")
    not_responding_pattern = re.compile(r"node-\d+ .*? not responding")

    failures = []
    not_responding = []

    with open(log_file, 'r') as file:
        for line in file:
            if failure_pattern.search(line):
                # Extract node ID from the failure log entry
                node_id = re.search(r'node-\d+', line).group()
                failures.append(node_id)
            elif not_responding_pattern.search(line):
                # Extract node ID from the not responding log entry
                node_id = re.search(r'node-\d+', line).group()
                not_responding.append(node_id)

    return {
        "failures": failures,
        "not_responding": not_responding
    }

def analyze_node_failures_and_not_responding(log_file):
    """
    Analyzes the node failures and not-responding nodes and creates a chart showing the most frequent nodes.

    Args:
        log_file (str): The path to the log file.
    """
    # Extract the data
    data = extract_failures_and_not_responding_nodes(log_file)

    # Count occurrences of failures and not responding nodes
    failure_count = Counter(data["failures"])
    not_responding_count = Counter(data["not_responding"])

    # Combine counts for nodes that both fail and don't respond
    combined_count = Counter(failure_count) + Counter(not_responding_count)

    # Plotting the results
    labels, values = zip(*combined_count.items())
    plt.bar(labels, values)
    plt.xlabel('Node IDs')
    plt.ylabel('Count of Failures and Not-Responses')
    plt.title('Nodes with Most Failures and Not-Responding Events')
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Show the chart
    plt.show()

if __name__ == "__main__":
    log_file = "HPC_PZSlP.log"  # Ensure this file is in the same directory a
