import re
from datetime import datetime

def extract_log_data(log_data):
    """
    Extracts Timestamp, Hostname, Process Info, and Message from log data for a specific hostname 
    and converts the timestamp to American format.

    Args:
        log_data: A string containing the log data.

    Returns:
        A list of tuples, where each tuple represents a log entry and contains
        (Timestamp, Hostname, Process Info, Message) with timestamps in American format.
    """

    regex = re.compile(
        r"^(Jul\s+\d+\s+\d{2}:\d{2}:\d{2})\s+"
        r"(authorMacBook-Pro)\s+"
        r"([\w\[\]\.\-\(\)\:\+]+)\:\s+"
        r"(.*)$"
    )

    start_time = datetime.strptime("Jul  5 21:48:33", "%b  %d %H:%M:%S")
    end_time = datetime.strptime("Jul  6 00:00:00", "%b  %d %H:%M:%S")

    extracted_data = []
    for line in log_data.splitlines():
        match = regex.match(line)
        if match:
            timestamp_str = match.group(1)
            hostname = match.group(2)
            process_info = match.group(3)
            message = match.group(4)

            # Parse the timestamp string into a datetime object
            timestamp_dt = datetime.strptime(timestamp_str, "%b  %d %H:%M:%S")

            # Check if the timestamp is within the desired range
            if start_time <= timestamp_dt <= end_time:
                # Convert to American format: MM/DD/YYYY hh:mm:ss
                american_format = timestamp_dt.strftime("%m/%d/%Y %H:%M:%S")
                extracted_data.append((american_format, hostname, process_info, message))

    return extracted_data


log_data = """
Jul  5 21:48:33 calvisitor-10-105-162-81 blued[85]: [BluetoothHIDDeviceController] EventServiceConnectedCallback
Jul  5 21:48:33 authorMacBook-Pro networkd[195]: -[NETClientConnection effectiveBundleID] using process name apsd as bundle ID (this is expected for daemons without bundle ID
Jul  5 21:48:45 authorMacBook-Pro sandboxd[129] ([10018]): QQ(10018) deny mach-lookup com.apple.networking.captivenetworksupport
Jul  5 22:29:03 calvisitor-10-105-161-231 kernel[0]: pages 1401204, wire 544128, act 416065, inact 0, cleaned 0 spec 3, zf 25, throt 0, compr 266324, xpmapped 40000
Jul  5 22:29:06 authorMacBook-Pro networkd[195]: -[NETClientConnection effectiveBundleID] using process name apsd as bundle ID (this is expected for daemons without bundle ID
Jul  5 23:50:09 authorMacBook-Pro kernel[0]: AppleActuatorDeviceUserClient::start Entered
Jul  6 00:30:35 calvisitor-10-105-162-211 kernel[0]: polled file major 1, minor 0, blocksize 4096, pollers 5
Jul  6 00:30:35 authorMacBook-Pro UserEventAgent[43]: assertion failed: 15G1510: com.apple.telemetry + 38574 [10D2E324-788C-30CC-A749-55AE67AEC7BC]: 0x7fc235807b90
"""

extracted_data = extract_log_data(log_data)

for timestamp, hostname, process_info, message in extracted_data:
    print(f"Timestamp: {timestamp}, Hostname: {hostname}, Process Info: {process_info}, Message: {message}")
