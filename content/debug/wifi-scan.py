# 周りの Wi-Fi を数えて、強い順に 5 つ出す。
#
# RADIUS の検証で「どのアクセスポイントに届いているか」を
# 確かめるときに使います。
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

nets = sorted(wlan.scan(), key=lambda n: n[3], reverse=True)
print("found", len(nets))

for ssid, bssid, channel, rssi, security, hidden in nets[:5]:
    print("%-24s ch=%-3d rssi=%d" % (ssid.decode() or "(hidden)", channel, rssi))
