######from scapy.all import ICMP, IP, sr1
######from multiprocessing import Pool
######import time
######import socket
######
#######Function to perform a single ping request to a specific IP address
######def ping_ip(ip):
######    start_time = time.time()
######    
######    packet = IP(dst=ip) / ICMP()
######    response = sr1(packet, timeout=1, verbose=False)
######    
######    # Calculate round-trip time
######    round_trip_time = round((time.time() - start_time) * 1000, 2) if response else None
######    
######    # Get hostname via reverse DNS lookup
######    try:
######        hostname = socket.gethostbyaddr(ip)[0]
######    except socket.herror:
######        hostname = None
######    
######    # Return detailed information
######    if response:
######        return f"{ip} is live, Hostname: {hostname}, RTT: {round_trip_time}ms"
######    else:
######        return f"{ip} is not reachable, Hostname: {hostname}"
######
###### Function to scan a range of IP addresses in parallel using all CPU cores
######def scan_network(network):
######    # Generate list of IPs to scan
######    ip_list = [f"{network}.{i}" for i in range(1, 255)]
######    
######    # Using Pool to parallelize the task across multiple CPU cores
######    with Pool() as pool:
######        results = pool.map(ping_ip, ip_list)
######        
######        for result in results:
######            print(result)
######
######if __name__ == "__main__":
######    network = input("Enter the network prefix (e.g., 192.168.1): ")
######    start_time = time.time()
######    scan_network(network)
######    print(f"Scan completed in {time.time() - start_time:.2f} seconds.")
######
######from scapy.all import ICMP, IP, sr1
######from multiprocessing import Pool
######import time
######import socket
######
###### Function to perform a single ping request to a specific IP address
######def ping_ip(ip):
######    start_time = time.time()
######    
######    packet = IP(dst=ip) / ICMP()
######    response = sr1(packet, timeout=1, verbose=False)
######    
######    # Calculate round-trip time
######    round_trip_time = round((time.time() - start_time) * 1000, 2) if response else None
######    
######    # Get hostname via reverse DNS lookup
######    try:
######        hostname = socket.gethostbyaddr(ip)[0]
######    except socket.herror:
######        hostname = "Unknown"  # Set a default value instead of None
######    
######    # Return detailed information
######    if response:
######        return f"{ip} is live, Hostname: {hostname}, RTT: {round_trip_time}ms"
######    else:
######        return f"{ip} is not reachable, Hostname: {hostname}"
######
###### Function to scan a range of IP addresses in parallel using all CPU cores
######def scan_network(network):f
######    # Generate list of IPs to scan
######    ip_list = [f"{network}.{i}" for i in range(1, 255)]
######    
######    # Using Pool to parallelize the task across multiple CPU cores
######    with Pool() as pool:
######        results = pool.map(ping_ip, ip_list)
######        
######        for result in results:
######            print(result)
######
######if __name__ == "__main__":
######    network = input("Enter the network prefix (e.g., 192.168.1): ")
######    start_time = time.time()
######    scan_network(network)
######    print(f"Scan completed in {time.time() - start_time:.2f} seconds.")n
##
from scapy.all import ICMP, IP, sr1
from multiprocessing import Pool
import time
import socket

# Function to perform a single ping request to a specific IP address
def ping_ip(ip):
    start_time = time.time()
    
    packet = IP(dst=ip) / ICMP()
    response = sr1(packet, timeout=1, verbose=False)
    
    # Calculate round-trip time
    round_trip_time = round((time.time() - start_time) * 1000, 2) if response else None
    
    # Get hostname via reverse DNS lookup
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        hostname = "Unknown"  # Set a default value instead of None
    
    # Return detailed information
    if response:
        return f"{ip} is live, Hostname: {hostname}, RTT: {round_trip_time}ms"
    else:
        return f"{ip} is not reachable, Hostname: {hostname}"

# Function to scan a range of IP addresses in parallel using all CPU cores
def scan_network(network, range_start, range_end):
    # Generate list of IPs to scan based on the provided range
    ip_list = [f"{network}.{i}.{j}" for i in range(range_start, range_end) for j in range(1, 255)]
    
    # Using Pool to parallelize the task across multiple CPU cores
    with Pool() as pool:
        results = pool.map(ping_ip, ip_list)
        
        for result in results:
            print(result)

if __name__ == "__main__":
    network = input("Enter the network prefix (e.g., 10.1): ")
    range_start = int(input("Enter the start value for the third octet: "))
    range_end = int(input("Enter the end value for the third octet: "))
    
    start_time = time.time()
    scan_network(network, range_start, range_end)
    print(f"Scan completed in {time.time() - start_time:.2f} seconds.")
