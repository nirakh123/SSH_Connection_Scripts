from netmiko import ConnectHandler
import datetime
import getpass

switch_ip = input("Enter IP: ")
username = input("Username: ")
password = getpass.getpass("Password: ")  

now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_filename = f"cisco_switch_{now}.txt"

try:
  device_type = "cisco_ios"  
  connection = ConnectHandler(ip=switch_ip, username=username, password=password, device_type=device_type)
  print("Connected to switch")
except Exception as e:
  print(f"Connection error: {e}")
  exit()

try:
  command = "show running-config"
  output = connection.send_command(command)
  print("Retrieved configuration")
except Exception as e:
  print(f"Error retrieving configuration: {e}")
  connection.disconnect()
  exit()

# Save configuration to file
try:
  with open(backup_filename, "w") as f:
    f.write(output)
  print(f"Configuration saved to {backup_filename}")
except Exception as e:
  print(f"Error saving configuration: {e}")

connection.disconnect()
print("Disconnected from switch")