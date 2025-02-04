"""Timing II"""
s = int(input())
d = s // (24 * 60 * 60)
s -= d * (24 * 60 * 60)
h = s // (60 * 60)
s -= h * (60 * 60)
m = s // 60
s -= m * 60
if d > 9999 or s < 0 :
    print("ERR_:__:__:__")
else :
    print(f"{d:04}:{h:02}:{m:02}:{s:02}")
