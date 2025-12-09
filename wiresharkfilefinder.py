import pyshark
import os

# -----------------------------------------------------------
#  Function: Check if a packet contains the hostname
# -----------------------------------------------------------
def packet_contains_hostname(pkt, hostname):
    hostname = hostname.lower()

    # ---- DNS (normal) ----
    try:
        if hasattr(pkt, "dns"):
            if hasattr(pkt.dns, "qry_name") and pkt.dns.qry_name and hostname in pkt.dns.qry_name.lower():
                return True

            # DNS answers
            for attr in dir(pkt.dns):
                if "name" in attr:
                    val = getattr(pkt.dns, attr)
                    if isinstance(val, str) and hostname in val.lower():
                        return True
    except:
        pass

    # ---- MDNS (Bonjour) ----
    try:
        if hasattr(pkt, "mdns"):
            for attr in dir(pkt.mdns):
                val = getattr(pkt.mdns, attr)
                if isinstance(val, str) and hostname in val.lower():
                    return True
    except:
        pass

    # ---- LLMNR ----
    try:
        if hasattr(pkt, "llmnr"):
            for attr in dir(pkt.llmnr):
                val = getattr(pkt.llmnr, attr)
                if isinstance(val, str) and hostname in val.lower():
                    return True
    except:
        pass

    # ---- DHCP Hostname (BOOTP options) ----
    try:
        if hasattr(pkt, "bootp"):
            for attr in dir(pkt.bootp):
                val = getattr(pkt.bootp, attr)
                if isinstance(val, str) and hostname in val.lower():
                    return True
    except:
        pass

    # ---- HTTP Host ----
    try:
        if hasattr(pkt, "http") and hasattr(pkt.http, "host"):
            if pkt.http.host and hostname in pkt.http.host.lower():
                return True
    except:
        pass

    # ---- TLS SNI ----
    try:
        if hasattr(pkt, "tls"):
            for attr in dir(pkt.tls):
                if "server_name" in attr.lower():
                    val = getattr(pkt.tls, attr)
                    if isinstance(val, str) and hostname in val.lower():
                        return True
    except:
        pass

    return False


# -----------------------------------------------------------
#  MAIN PROGRAM
# -----------------------------------------------------------
def main():
    print("=== Wireshark Hostname Search Tool ===\n")

    # Ask user for pcapng file
    while True:
        file_path = input("Enter the path to your .pcapng file: ").strip()
        if os.path.isfile(file_path):
            break
        print("❌ File not found. Try again.\n")

    print("\nLoading capture... (this may take a moment)")
    cap = pyshark.FileCapture(file_path, keep_packets=False)

    # MAIN SEARCH LOOP
    while True:
        hostname = input("\nEnter hostname to search for (or press ENTER to quit): ").strip()
        if hostname == "":
            print("Goodbye!")
            break

        print(f"\nSearching for '{hostname}'...\n")
        matches = []

        # Scan packets
        for pkt in cap:
            try:
                if packet_contains_hostname(pkt, hostname):
                    matches.append(pkt)
            except:
                continue

        # Reset capture so we can search again later
        cap.reset()

        # If nothing matched
        if not matches:
            print("No packets matched that hostname.")
            continue

        print(f"\nFound {len(matches)} matching packets:\n")

        # Print summary
        for i, pkt in enumerate(matches):
            try:
                src = pkt.ip.src if hasattr(pkt, "ip") else "?"
                dst = pkt.ip.dst if hasattr(pkt, "ip") else "?"
                layer = pkt.highest_layer
                print(f"[{i}] Packet #{pkt.number}  {layer}  {src} → {dst}")
            except:
                print(f"[{i}] Packet #{pkt.number}  (Summary unavailable)")

        # Let user inspect specific packets
        while True:
            choice = input("\nEnter packet number for details (or ENTER to search again): ").strip()
            if choice == "":
                break
            if not choice.isdigit() or int(choice) >= len(matches):
                print("Invalid choice.")
                continue

            pkt = matches[int(choice)]
            print("\n---------- PACKET DETAILS ----------")
            print(pkt)
            print("------------------------------------")


if __name__ == "__main__":
    main()
