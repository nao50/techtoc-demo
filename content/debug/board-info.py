# この機器は何者か。
#
# チップ・周波数・メモリ・一意な ID を出します。
# 「実機で確かめた値」を記事に載せたいとき、ここから写せます。
import gc
import os
import sys

import machine

gc.collect()

print("platform   ", sys.platform)
print("chip freq  ", machine.freq(), "Hz")
print("unique id  ", machine.unique_id().hex())
print("free mem   ", gc.mem_free(), "B")
print("alloc mem  ", gc.mem_alloc(), "B")

stat = os.statvfs("/")
print("flash free ", stat[0] * stat[3], "B")
