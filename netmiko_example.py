from netmiko import ConnectHandler

sw03 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.2.57',
    'username': 'XXXXX',
    'password': 'XXXXXX',
}

commands = [
    'show ip int brief',
    'show version',
]

sw03_session = ConnectHandler(**sw03)
#print(sw03_session.send_command('show ip int brief'))

# loop through commands
results = [sw03_session.send_command(i) for i in commands]

for i in results:
    print(i)
