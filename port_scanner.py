import socket
from datetime import datetime

target = input ("Enter the target IP: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

print(f"Scanning ports {start_port} to {end_port} on {target}...")
print(f"Scan started at: {datetime.now()}")
print("-" * 40)

for port in range(start_port, end_port + 1):

   s = socket.socket()
   s.settimeout(1)

   result = s.connect_ex((target, port))
   if result == 0:
      print(f"Port {port} is open")


s.close()

print("-" * 40)
print("Scan Complete.")