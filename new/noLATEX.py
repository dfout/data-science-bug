import re

def extract_log_data(log_data):
    regex = r"^(Jul\s+\d+\s+2[1-3]:\d{2}:\d{2}|Jul\s+6\s+00:00:00)\s+([\w.-]+)\s+([\w\[\]]+):\s+(.*)$"
    matches = []
    for line in log_data.splitlines():
        match = re.search(regex, line)
        if match:
            timestamp, hostname, process_info, message = match.groups()
            matches.append({
                "Timestamp": timestamp,
                "Hostname": hostname,
                "Process Info": process_info,
                "Message": message,
            })
    return matches

log_data = """
Jul  5 21:48:33 calvisitor-10-105-162-81 blued[85]: [BluetoothHIDDeviceController] EventServiceConnectedCallback
Jul  5 21:48:33 authorMacBook-Pro networkd[195]: -[NETClientConnection effectiveBundleID] using process name apsd as bundle ID (this is expected for daemons without bundle ID
Jul  5 21:48:45 authorMacBook-Pro sandboxd[129] ([10018]): QQ(10018) deny mach-lookup com.apple.networking.captivenetworksupport
Jul  5 22:29:03 calvisitor-10-105-161-231 kernel[0]: pages 1401204, wire 544128, act 416065, inact 0, cleaned 0 spec 3, zf 25, throt 0, compr 266324, xpmapped 40000
Jul  5 22:29:03 calvisitor-10-105-161-231 kernel[0]: could discard act 74490 inact 9782 purgeable 34145 spec 56242 cleaned 0
Jul  5 22:29:06 authorMacBook-Pro networkd[195]: -[NETClientConnection effectiveBundleID] using process name apsd as bundle ID (this is expected for daemons without bundle ID
Jul  5 22:29:35 calvisitor-10-105-160-22 kernel[0]: IO80211AWDLPeerManager::setAwdlAutoMode Resuming AWDL
Jul  5 22:29:37 calvisitor-10-105-160-22 com.apple.AddressBook.InternetAccountsBridge[36395]: dnssd_clientstub ConnectToServer: connect()-> No of tries: 2
Jul  5 23:09:36 calvisitor-10-105-160-22 kernel[0]: bitmap_size 0x7f0fc, previewSize 0x4028, writing 485676 pages @ 0x97144
Jul  5 23:09:36 calvisitor-10-105-160-22 kernel[0]: **** [BroadcomBluetoothHostController][SetupController] -- Delay HCI Reset by 300ms  ****
Jul  5 23:09:53 calvisitor-10-105-160-22 QQ[10018]: FA||Url||taskID[2019353593] dealloc
Jul  5 23:50:09 calvisitor-10-105-160-22 kernel[0]: AppleActuatorHIDEventDriver: stop
Jul  5 23:50:09 calvisitor-10-105-160-22 kernel[0]: **** [IOBluetoothHostControllerUSBTransport][start] -- completed -- result = TRUE -- 0xb000 ****
Jul  5 23:50:09 authorMacBook-Pro kernel[0]: AppleActuatorDeviceUserClient::start Entered
Jul  5 23:50:11 authorMacBook-Pro kernel[0]: ARPT: 729188.852474: AQM agg params 0xfc0 maxlen hi/lo 0x0 0xffff minlen 0x0 adjlen 0x0
Jul  5 23:50:51 calvisitor-10-105-162-211 locationd[82]: NETWORK: requery, 0, 0, 0, 0, 299, items, fQueryRetries, 0, fLastRetryTimestamp, 521006902.2
Jul  6 00:30:35 calvisitor-10-105-162-211 kernel[0]: polled file major 1, minor 0, blocksize 4096, pollers 5
Jul  6 00:30:35 calvisitor-10-105-162-211 kernel[0]: IOHibernatePollerOpen(0)
Jul  6 00:30:35 authorMacBook-Pro UserEventAgent[43]: assertion failed: 15G1510: com.apple.telemetry + 38574 [10D2E324-788C-30CC-A749-55AE67AEC7BC]: 0x7fc235807b90
Jul  6 00:30:37 authorMacBook-Pro ksfetch[36439]: 2017-07-06 00:30:37.064 ksfetch[36439/0x7fff79824000] [lvl=2] main() Fetcher is exiting.
Jul  6 00:30:37 authorMacBook-Pro GoogleSoftwareUpdateAgent[36436]: 2017-07-06 00:30:37.071 GoogleSoftwareUpdateAgent[36436/0x7000002a0000] [lvl=2] -[KSUpdateEngine updateAllExceptProduct:] KSUpdateEngine updating all installed products, except:'com.google.Keystone'.
Jul  6 00:30:43 authorMacBook-Pro com.apple.CDScheduler[258]: Thermal pressure state: 1 Memory pressure state: 0
Jul  6 01:11:06 authorMacBook-Pro Dropbox[24019]: [0706/011106:WARNING:dns_config_service_posix.cc(306)] Failed to read DnsConfig.
Jul  6 01:11:06 authorMacBook-Pro com.apple.WebKit.WebContent[32778]: [01:11:06.715] FigAgglomeratorSetObjectForKey signalled err=-16020 (kFigStringConformerError_ParamErr) (NULL key) at /Library/Caches/com.apple.xbs/Sources/CoreMedia/CoreMedia-1731.15.207/Prototypes/LegibleOutput/FigAgglomerator.c line 92
"""

extracted_data = extract_log_data(log_data)
for item in extracted_data:
    print(item)