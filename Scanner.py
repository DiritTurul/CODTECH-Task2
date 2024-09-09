import os
import socket

def scan_network(ip_address, subnet_mask):
    # Calculate the network address and broadcast address
    network_address = ip_address + "/" + subnet_mask
    broadcast_address = get_broadcast_address(network_address)

    # Create a list to store the results
    clients_list = []

    # Iterate over the possible IP addresses in the network
    for i in range(1, 255):
        ip = broadcast_address.split('.')[0] + '.' + broadcast_address.split('.')[1] + '.' + broadcast_address.split('.')[2] + '.' + str(i)
        try:
            # Try to ping the IP address
            response = os.system("ping -c 1 " + ip)
            if response == 0:
                # If the ping is successful, get the hostname and IP address
                hostname = socket.gethostbyaddr(ip)[0]
                clients_list.append({"ip": ip, "hostname": hostname})
        except socket.herror:
            # Ignore any socket errors
            pass

    # Return the list of clients
    return clients_list

def get_broadcast_address(network_address):
    # Calculate the broadcast address from the network address
    network_parts = network_address.split('/')
    network_ip = network_parts[0].split('.')
    subnet_mask = int(network_parts[1])
    broadcast_ip = list(network_ip)
    for i in range(32 - subnet_mask, 32):
        broadcast_ip[i // 8] = str(int(broadcast_ip[i // 8]) | (1 << (7 - i % 8)))
    return '.'.join(broadcast_ip)

# Example usage
ip_address = "192.168.1.0"
subnet_mask = "24"
clients = scan_network(ip_address, subnet_mask)

# Print the results
for client in clients:
    print("IP Address: ", client["ip"], " Hostname: ", client["hostname"])