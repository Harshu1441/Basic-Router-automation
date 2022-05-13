import getpass
import telnetlib

# defining host values or the router IP which you need to telnet

HOST = "192.168.10.1"

# user-input/user name

user = input("Enter your remote account: ")

# getting password with getpass

password = getpass.getpass()

# enBLE PASSWORD

privilege = getpass.getpass("Enter your Privilege mode Password:  ")

# Telnet the host with telnet lib

tn = telnetlib.Telnet(HOST)

# read and write function, i.e read write

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")

# getting password with ascii encryption/encode for enable mode

if password:
    tn.read_until(b"Password: ")
    tn.write(privilege.encode('ascii') + b"\n")
tn.write(b"conf t\n")
tn.write(b"hostname R1\n")

# eigrp input

tn.write(b"router Eigrp 10\n")

# ( sample IP) enter your ip
tn.write(b"network 10.0.0.0 0.0.0.255\n")
tn.write(b"network 192.168.10.0 255.255.255.0\n")
tn.write(b"exit\n")

# OSPF input area 0
tn.write(b"router ospf 10\n")
tn.write(b"network 10.0.0.0 255.255.255.0 area 0\n")
tn.write(b"network 192.168.10.0 0.0.0.255 area 0\n")

tn.write(b"exit\n")
tn.write(b"exit\n")
tn.write(b"write\n")
tn.write(b"exit\n")

# debug line
print(tn.read_all().decode('ascii'))
