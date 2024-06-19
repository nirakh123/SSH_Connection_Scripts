import getpass
import telnetlib

HOST = "10.235.3.50"
user = input("Enter your Username: ")
pwd = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if pwd:
    tn.read_until(b"Password: ")
    tn.write(pwd.encode('ascii') + b"\n")

tn.write(b"term length 0\n")
tn.write(b"show running-config\n")
tn.write(b"show ver\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
tn.close()