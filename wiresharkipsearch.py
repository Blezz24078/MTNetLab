import pyshark
import os

def packet_contains_ip(pkt, ip_query):
    """Return True if the packet contains the IP (src or dst), even partial match."""
    try:
        if hasattr(pkt, "ip"):
            return (ip_query in pkt.ip.src) or (ip_query in pkt.ip.dst)
    except:
        pass
    return False


def main():
    print("=== Wireshark IP Search Tool ===\n")

    # --- Ask user for file path ---
    while True:
        file_path = input("Enter the full path to your .pcap or .pcapng file: ").strip()
        if os.path.isfile(file_path):
            break
        print("❌ File not found. Try again.\n")

    print(f"\nLoading capture: {file_path}")
    cap = pyshark.FileCapture(file_path, keep_packets=False)

    # --- Main IP search loop ---
    while True:
        ip_query = input("\nEnter IP (or partial IP) to search (ENTER to quit): ").strip()
        if ip_query == "":
            print("Goodbye!")
            break

        print(f"\nSearching for packets containing '{ip_query}'...\n")
        matches = []

        # Scan packets
        for pkt in cap:
            try:
                if packet_contains_ip(pkt, ip_query):
                    matches.append(pkt)
            except:
                continue

        # Reset capture for next search
        cap.reset()

        if not matches:
            print("No packets matched that IP.")
            continue

        print(f"Found {len(matches)} matching packets:\n")

        # Show summary
        for i, pkt in enumerate(matches):
            try:
                src = pkt.ip.src if hasattr(pkt, "ip") else "?"
                dst = pkt.ip.dst if hasattr(pkt, "ip") else "?"
                proto = pkt.highest_layer
                print(f"[{i}] Packet #{pkt.number}  {src} → {dst}  ({proto})")
            except:
                print(f"[{i}] Packet #{pkt.number}  (summary unavailable)")

        # Let user inspect packets
        while True:
            choice = input("\nEnter packet number to view full details (ENTER to search again): ").strip()
            if choice == "":
                break
            if not choice.isdigit():
                print("Invalid input.")
                continue

            idx = int(choice)
            if idx < 0 or idx >= len(matches):
                print("Number out of range.")
                continue

            pkt = matches[idx]
            print("\n========== PACKET DETAILS ==========")
            print(pkt)
            print("====================================\n")


if __name__ == "__main__":
    main()
