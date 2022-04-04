# import module
import os

# scan available Wifi networks
available_wifi = os.system('cmd /c "netsh wlan show networks"')
print(available_wifi)
print('\n')

try:
    # take input of the wifi name
    wifi_name = input('Enter Name of the wifi which is already saved : ')

    # connect with your wifi
    print('\n')
    os.system(f'''cmd /c "netsh wlan connect name={wifi_name}"''')
except:
    print("Try with another saved network")
