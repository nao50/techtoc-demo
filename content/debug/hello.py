# まず 1 本目。**つながっているか**を確かめるだけの原稿です。
#
# 右の実行ボタンを押すと、いま接続している機器へ送られて、
# 返ってきた文字が下の端末に出ます。焼き込みではありません。
import sys

print("hello from", sys.platform)
print("micropython", ".".join(str(n) for n in sys.implementation.version))
