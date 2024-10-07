import re

def extract_node_failure_messages(log_file):
     # The log file is in the same directory
    print(log_file.readlines())

    try:
        # Open the log file and read its content
        with open(log_file, 'r') as file:
            log_lines = file.readlines()

        # List to store extracted failure messages
        failure_messages = []

        # Regex pattern to match node failure messages
        failure_pattern = re.compile(r'node-\d+ .*? state_change\.unavailable .*? Component "(.*?)" is in the unavailable state')

        # Iterate through the log lines and extract messages
        for line in log_lines:
            match = failure_pattern.search(line)
            if match:
                failure_messages.append(match.group(1))

        return failure_messages

    except FileNotFoundError:
        return "The log file 'HPC_PZSlP.log' was not found in the current directory."

# Example usage: Call the function to extract failure messages
if __name__ == "__main__":
    file = 'HPC/HPC_PZSIP.log'
    messages = extract_node_failure_messages(file)
    if isinstance(messages, list):
        for message in messages[:10]:  # Display the first 10 messages
            print(message)
    else:
        print(messages)
