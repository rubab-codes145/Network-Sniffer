from scapy.all import sniff, wrpcap

# List to store captured packets
packets = []

# Function to process each captured packet
def packet_callback(packet):
    print(packet.summary())  # Print packet info to console
    packets.append(packet)   # Save packet to list

def main():
    print("=== Network Sniffer ===")
    
    # Let user choose a port to sniff
    port = input("Enter the port number to sniff (e.g., 445): ").strip()
    
    print(f"\nStarting network sniffing on port {port}... Press Ctrl+C to stop.\n")
    
    try:
        # Start sniffing packets
        sniff(prn=packet_callback, store=0, filter=f"port {port}")
    
    except KeyboardInterrupt:
        # Stop sniffing on Ctrl+C
        print("\nSniffing stopped.")
        
        if packets:
            # Save captured packets to a file
            filename = f"captured_packets_port{port}.pcap"
            wrpcap(filename, packets)
            print(f"Packets saved to {filename}")
        else:
            print("No packets were captured.")

if __name__ == "__main__":
    main()



