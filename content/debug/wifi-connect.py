# Wi-Fi につないで、IP を確かめる。
#
# SSID とパスワードは**この行だけ**書き換えてください。
# 認証の検証をする前に、まずここが通ることを確認します。
import time

import network

SSID = "changeme"
PASSWORD = "changeme"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if wlan.isconnected():
    print("already connected")
else:
    print("connecting to", SSID)
    wlan.connect(SSID, PASSWORD)

    for _ in range(30):
        if wlan.isconnected():
            break
        time.sleep(0.5)

if wlan.isconnected():
    ip, mask, gateway, dns = wlan.ifconfig()
    print("ip     ", ip)
    print("gateway", gateway)
    print("dns    ", dns)
    print("rssi   ", wlan.status("rssi"))
else:
    print("failed:", wlan.status())
