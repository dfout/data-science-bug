import re
from datetime import datetime

def extract_log_data(log_data):
    # Regex to capture log data with hostname 'authorMacBook-Pro'
    regex = re.compile(r"^(Jul\s+\d{1,2}\s+(?:2[0-3]|[01]?[0-9]):[0-5][0-9]:[0-5][0-9])\s+(authorMacBook-Pro)\s+([^:]+):\s+(.*)$")
    extracted_data = []
    
    for line in log_data.splitlines():
        match = regex.match(line)
        if match:
            timestamp = match.group(1)
            hostname = match.group(2)
            process_info = match.group(3)
            message = match.group(4)
            
            # Convert timestamp to American format (MM/DD hh:mm:ss)
            original_time = datetime.strptime(timestamp, "%b %d %H:%M:%S")
            new_time = original_time.strftime("%m/%d %H:%M:%S")
            
            # Append the matched data to the result list if within the time window
            if original_time < datetime.strptime("Jul 6 00:00:00", "%b %d %H:%M:%S"):
                extracted_data.append({
                    "Timestamp": new_time,
                    "Hostname": hostname,
                    "Process Info": process_info,
                    "Message": message
                })
    
    return extracted_data

log_data = """
Jul  5 21:48:33 calvisitor-10-105-162-81 blued[85]: [BluetoothHIDDeviceController] EventServiceConnectedCallback
Jul  5 21:48:33 authorMacBook-Pro networkd[195]: -[NETClientConnection effectiveBundleID] using process name apsd as bundle ID (this is expected for daemons without bundle ID
Jul  5 21:48:45 authorMacBook-Pro sandboxd[129] ([10018]): QQ(10018) deny mach-lookup com.apple.networking.captivenetworksupport
Jul  5 22:29:03 calvisitor-10-105-161-231 kernel[0]: pages 1401204, wire 544128, act 416065, inact 0, cleaned 0 spec 3, zf 25, throt 0, compr 266324, xpmapped 40000
Jul  5 22:29:06 authorMacBook-Pro networkd[195]: -[NETClientConnection effectiveBundleID] using process name apsd as bundle ID (this is expected for daemons without bundle ID
Jul  5 22:29:35 calvisitor-10-105-160-22 kernel[0]: IO80211AWDLPeerManager::setAwdlAutoMode Resuming AWDL
Jul  5 22:29:37 calvisitor-10-105-160-22 com.apple.AddressBook.InternetAccountsBridge[36395]: dnssd_clientstub ConnectToServer: connect()-> No of tries: 2
Jul  5 23:09:36 calvisitor-10-105-160-22 kernel[0]: bitmap_size 0x7f0fc, previewSize 0x4028, writing 485676 pages @ 0x97144
Jul  5 23:50:09 authorMacBook-Pro kernel[0]: AppleActuatorDeviceUserClient::start Entered
Jul  5 23:50:11 authorMacBook-Pro kernel[0]: ARPT: 729188.852474: AQM agg params 0xfc0 maxlen hi/lo 0x0 0xffff minlen 0x0 adjlen 0x0
Jul  6 00:30:35 authorMacBook-Pro UserEventAgent[43]: assertion failed: 15G1510: com.apple.telemetry + 38574 [10D2E324-788C-30CC-A749-55AE67AEC7BC]: 0x7fc235807b90
Jul  6 00:30:37 authorMacBook-Pro ksfetch[36439]: 2017-07-06 00:30:37.064 ksfetch[36439/0x7fff79824000] [lvl=2] main() Fetcher is exiting.
"""

extracted_data = extract_log_data(log_data)
print(extracted_data)
