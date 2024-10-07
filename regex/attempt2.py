import re

def extract_node_failures(log_file):
    """
    Extracts node failure entries from a log file using regex.

    Args:
        log_file (str): The path to the log file.

    Returns:
        list: A list of strings, each representing a node failure entry.
    """

    failure_pattern = re.compile(r"\d+ node-\d+ node psu \d+ \d+ psu failure")  # Regex for failure pattern
    failures = []

    with open(log_file, 'r') as f:
        for line in f:
            match = failure_pattern.search(line)
            if match:
                failures.append(line.strip())

    return failures

# Example usage:
log_file = "HPC_PZSlP.log"  # Replace with your actual log file name
node_failures = extract_node_failures(log_file)

if node_failures:
    print("Node Failures Found:")
    for failure in node_failures:
        print(failure)
else:
    print("No Node Failures Found.")