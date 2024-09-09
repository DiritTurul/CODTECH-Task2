# Network Scanner

A simple network scanner written in Python that scans a given network for active hosts and retrieves their IP addresses and hostnames.

## Description

This script uses the `os` and `socket` libraries to ping all possible IP addresses in a given network and retrieve the hostnames of active hosts. The network is defined by an IP address and a subnet mask.

## Features

* Scans a network for active hosts
* Retrieves IP addresses and hostnames of active hosts
* Handles socket errors and ignores unreachable hosts

## Usage

1. Clone the repository
2. Install the required libraries (`os` and `socket` are part of the Python standard library, so no installation is required)
3. Run the script with the IP address and subnet mask of the network you want to scan as arguments

## Example Usage

```python
ip_address = "192.168.1.0"
subnet_mask = "24"
clients = scan_network(ip_address, subnet_mask)

# Print the results
for client in clients:
    print("IP Address: ", client["ip"], " Hostname: ", client["hostname"])
