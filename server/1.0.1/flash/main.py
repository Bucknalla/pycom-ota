from network import WLAN
import socket
import time
from OTA import WiFiOTA
from time import sleep
import pycom
import binascii

from config import WIFI_SSID, WIFI_PW, SERVER_IP

# Turn on GREEN LED
pycom.heartbeat(False)
pycom.rgbled(0xff)

# Setup OTA
ota = WiFiOTA(WIFI_SSID,
              WIFI_PW,
              SERVER_IP,  # Update server address
              8000)  # Update server port

# Turn off WiFi to save power
# w = WLAN()
# w.deinit()

print("Firmware v1.0.1")
print("Checking for OTA...")

ota.connect()

print("Connected to server.")
print("Attempting to update...")

ota.update()

sleep(5)