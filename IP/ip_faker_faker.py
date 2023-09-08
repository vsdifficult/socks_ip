import wmi

def change_ip_address(ip_address, subnet_mask, default_gateway) -> list:
    # Create a connection to the WMI service
    connection = wmi.WMI()

    # Get the network adapter configuration
    network_config = connection.Win32_NetworkAdapterConfiguration(IPEnabled=True)

    # Set the new IP address, subnet mask, and default gateway
    network_config.Set(DHCPEnabled=False, IPAddress=[ip_address])
    network_config.Set(IPSubnet=[subnet_mask])
    network_config.Set(DefaultIPGateway=[default_gateway])

    # Enable the network adapter
    network_config.EnableStatic()

    print("IP address changed successfully!")

# Usage
ip_address = "192.168.1.100"
subnet_mask = "255.255.255.0"
default_gateway = "192.168.1.1"

change_ip_address(ip_address, subnet_mask, default_gateway)
