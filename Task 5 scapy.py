from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        # Determine protocol name
        protocol_map = {6: "TCP", 17: "UDP", 1: "ICMP"}
        proto_name = protocol_map.get(proto, str(proto))

        print(f"\n[+] New Packet: {src_ip} -> {dst_ip} | Protocol: {proto_name}")

        # If the packet has a payload (Raw data)
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            # Print a snippet of the payload (truncated for readability)
            print(f"    Payload: {payload[:50]}...")

def main():
    print("Starting Network Sniffer... (Press Ctrl+C to stop)")
    # 'prn' defines the function to run on each packet
    # 'store=0' prevents memory buildup by not saving packets in RAM
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
    