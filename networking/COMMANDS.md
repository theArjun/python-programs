# WLAN Commands

Shows WLAN profiles list

        netsh wlan show profiles 

Adds WLAN profile to PC

        netsh wlan add profile filename="xml file here"

Shows WIFI password

        netsh wlan show profiles name="ssid" key=clear

Exports WLAN profile to XML File

        netsh wlan export profile name="ssid" folder="path" key=clear