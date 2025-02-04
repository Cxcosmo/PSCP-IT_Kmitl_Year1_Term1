"""Longer"""
import math
def main(r, a, b) :
    """Longer"""
    pc = 2 * (math.pi) * r
    ps = (a * 2) + (b * 2)
    if pc > ps :
        print("Circle is longer")
    elif pc < ps :
        print("Rectangle is longer")
    else :
        print("Equal")
    print(f"{abs(pc - ps):.5f}")
main(float(input()), float(input()), float(input()))
