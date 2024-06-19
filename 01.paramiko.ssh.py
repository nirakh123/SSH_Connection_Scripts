import paramiko
import time 
from getpass import getpass

IP = input("Enter IP: ")
Username = input("Username: ")
Password =  input("Password: ")

SESSION = paramiko.SSHClient()
SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
SESSION.connect(IP, port=22,
                username=Username, 
                password=Password, 
                look_for_keys=False, 
                allow_agent=False)

DEVICE_ACCESS = SESSION.invoke_shell()
DEVICE_ACCESS.send(b'term length 0\n')
DEVICE_ACCESS.send(b"show running-config\n")
DEVICE_ACCESS.send(b"show cdp neighbors\n")
DEVICE_ACCESS.send(b'show ver\n')
time.sleep(2)
output = DEVICE_ACCESS.recv(65000)
print (output.decode('ascii'))

SESSION.close