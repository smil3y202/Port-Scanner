# Michael Hipp
# 06/25/2023
# Final Project Option 2
# Port Scanner

import socket

# definition for the port scanner
def port_scan(target_host, ports):

    # for loop that checks every port that was inputted from user
    for port in ports:

        # creates an object sock with TCP and IPv4
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # sets timeout conditions for socket to be no more than 1 second
        sock.settimeout(1)

        # attempts to establish connection to the host and port given
        status = sock.connect_ex((target_host, port))

        # if the return value is 0, output that the port number is open
        if status == 0:
            print(f"Port {port} is open")

        # if the return value is anything else, output that the port number is closed
        else:
            print(f"Port {port} is closed")
        sock.close()


# error handling
try:
    # prompts the user to enter an IP address and a port or list of ports to scan
    target_host = input("Please enter the IP address of the host you want to scan: ")
    user_ports = input("Please enter a port, port list, or range of ports to begin scanning: ")

    # if there is a hyphen, map the start and endpoint as integers to the variables
    if "-" in user_ports:
        start_point, end_point = map(int, user_ports.split("-"))
        ports = range(start_point, end_point + 1)

    # if commas are present, splits the input by the commas, converts them,
    # and stores as a list of ports.
    elif "," in user_ports:
        ports = [int(port.strip()) for port in user_ports.split(",") if port.strip()]

    # assumes a single port was inputted and converted to integer
    else:
        ports = [int(user_ports)]

    # call the port_scan definition with parameters
    port_scan(target_host, ports)

# print output if error was encountered
except:
    print("Invalid IP address or port.")