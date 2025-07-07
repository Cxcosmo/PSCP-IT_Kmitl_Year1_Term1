"""Median"""
import math
def main(num) :
    """Median"""
    num = [float(i) for i in num]
    num.sort()
    median = (len(num) + 1) / 2
    if not len(num) % 2 :
        print(f"{(num[(math.floor(median)) - 1] + num[(math.ceil(median)) - 1]) / 2:.2f}")
    else :
        print(f"{num[int(median) - 1]:.2f}")
main(input().split(", "))
