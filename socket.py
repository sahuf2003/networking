import socket
import sys

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("socket connection successful")
except socket.error as err:
    print(f"socket connection failed")

port = 80
try:
    host_ip = socket.gethostbyname("www.github.com")
except socket.gaierror:
    print("error resolving the host")
    sys.exit()
s.connect((host_ip,port))
print("socket successfully connected ")
