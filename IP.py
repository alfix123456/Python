import socket

hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print("Your Computer name is: "+hostname)
print("Your IP address is: "+IPAddr)
input("Enter any key to exit")
