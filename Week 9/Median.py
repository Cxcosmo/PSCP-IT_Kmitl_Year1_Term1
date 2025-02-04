"""Median"""
import math
def main(n) :
    """Median"""
    num = []
    for _ in range(n) :
        num.append(float(input()))
    num.sort()
    median = (n + 1) / 2
    if not n % 2 :
        print(f"{(num[(math.floor(median)) - 1] + num[(math.ceil(median)) - 1]) / 2:.3f}")
    else :
        print(f"{num[int(median) - 1]:.3f}")
main(int(input()))
