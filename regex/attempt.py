import re

def extract_node_failures(log_file):
  """
  Extracts node failure entries from a log file using regex.

  Args:
      log_file: Path to the log file.

  Returns:
      A list of strings, where each string represents a node failure entry.
  """

  failures = []
  with open(log_file, 'r') as f:
    for line in f:
      # Regex to match lines like "191898 node-238 node psu 1131240275 1 psu failure\ ambient=28"
      match = re.search(r'\d+ node-\d+ node \w+ \d+ 1 .+ failure', line)
      if match:
        failures.append(match.group(0))
  return failures

# Example usage:
log_file_path = 'HPC_PZSLP.log'
failures = extract_node_failures(log_file_path)

if failures:
  print("Node Failures Found:")
  for failure in failures:
    print(failure)
else:
  print("No node failures found in the log file.")