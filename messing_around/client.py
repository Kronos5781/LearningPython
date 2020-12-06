import socket
import sys
from timeit import default_timer as timer

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ("192.168.1.59", 2114)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

output = open("Output.txt", "w")
time = 0

try:

    while time < 10:
        start = timer()
        data = sock.recv(16)
        output.write(str(data))
        #print(data)
        end = timer()
        time += end - start
        print(time)

finally:
    print('closing socket')
    sock.close()