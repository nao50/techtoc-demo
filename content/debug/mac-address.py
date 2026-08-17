# この機器の MAC アドレス。
#
# MAB（MAC アドレス認証）を試すときに使います。
# ここで出た値を、そのまま端末の登録に貼れます。
import binascii

import network

for name, iface in (("station", network.STA_IF), ("access point", network.AP_IF)):
    wlan = network.WLAN(iface)
    wlan.active(True)
    mac = binascii.hexlify(wlan.config("mac"), ":").decode()
    print("%-12s %s" % (name, mac))
