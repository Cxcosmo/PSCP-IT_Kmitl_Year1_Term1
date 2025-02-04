"""Circular I"""
import math
def main(xn,yn,r,x,y) :
    """main"""
    z = math.floor((((xn - x) ** 2) + ((yn - y) ** 2)) ** 0.5)
    if int(z) <= int(r) :
        print("Yes")
    else :
        print("No")
main(float(input()),float(input()),float(input()),float(input()),float(input()))
