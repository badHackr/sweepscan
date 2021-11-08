# Import modules
import subprocess
import ipaddress

# Prompt the user to input a network address
# net_addr = input("Enter a network address in CIDR format(ex.192.168.1.0/24): ")

# Create the network
# ip_net = ipaddress.ip_network(net_addr)

# Get all hosts on that network
# all_hosts = list(ip_net.hosts())

all_hosts = []

def scan(host):
    # Configure subprocess to hide the console window
    info = subprocess.STARTUPINFO()
    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = subprocess.SW_HIDE

    # For each IP address in the subnet, 
    # run the ping command with subprocess.popen interface
    for i in range(len(all_hosts)):
        output = subprocess.Popen(['ping', '-n', '1', '-w', '100', str(all_hosts[i])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
    
        if "Destination host unreachable" in output.decode('utf-8'):
            print(all_hosts[i], " Unreachable")
            
        elif "Request timed out" in output.decode('utf-8'):
            print(all_hosts[i], " Request time out")
            
        else:
            print(all_hosts[i], "is Online")


with open('ips.txt') as file:
    for line in file:
        all_hosts.append(line.rstrip())
    scan(all_hosts)
    # print(all_hosts)

