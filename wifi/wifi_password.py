import os
from sys import argv

ssid = argv[1]
# Key=clear shows password
command = 'netsh wlan show profiles name="{}" key=clear'.format(ssid)
os.system(command)
