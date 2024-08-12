from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        payload = ""

        if TCP in packet:
            payload = packet[TCP].payload
            protocol = "TCP"
        elif UDP in packet:
            payload = packet[UDP].payload
            protocol = "UDP"
        elif Raw in packet:
            payload = packet[Raw].load

        # Print packet details
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {protocol}")
        print(f"Payload: {payload}\n")

def start_sniffer(interface=None):
    print("Starting packet sniffer...")
    # Start sniffing on the specified interface, or all interfaces if None
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    # Replace 'eth0' with the network interface you want to sniff on, or leave as None for default
    start_sniffer(interface=None)

