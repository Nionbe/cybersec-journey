import socket
from datetime import datetime

<<<<<<< HEAD
def scan(target, start_port, end_port):
     
      print(f"Scanning {target}")
      print(f"Started: {datetime.now()}")

      for port in range(start_port, end_port + 1 ):
         s = socket.socket()
         s.settimeout(1)

         result = s.connect_ex((target, port))
         if result == 0:
            print(f"Port {port} is open")


         s.close()

target = input("Enter target IP: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

scan(target, start_port, end_port)
=======
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
>>>>>>> 6829b5b7d3b6bdc277c2b1af73534094a736793d
