from netmiko import ConnectHandler
import getpass  

ip_address = input("Enter switch IP address: ")
username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

vlan_id = 102
vlan_name = "Test2"  

try:
  device_type = 'cisco_ios'  
  connection = ConnectHandler(device_type=device_type, ip=ip_address, username=username, password=password)
  print("Connection successful!")

except Exception as e:
  print(f"Connection error: {e}")
  exit()

config_commands = []

output = connection.send_command(f"show vlan id {vlan_id}")
if f"VLAN ID  {vlan_id}" not in output:
  config_commands.append(f"vlan {vlan_id}")  
  if vlan_name:
    config_commands.append(f"name {vlan_name}") 

if config_commands:
  output = connection.send_config_set(config_commands)
  print(output)
else:
  print(f"VLAN {vlan_id} already exists.")

connection.disconnect()
