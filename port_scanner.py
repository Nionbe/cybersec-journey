import socket
from datetime import datetime

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