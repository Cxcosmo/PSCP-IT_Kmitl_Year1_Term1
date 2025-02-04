"""PointInCircle"""
import math
def main(xn,yn,r,x,y) :
    """main"""
    z = math.floor((((xn - x) ** 2) + ((yn - y) ** 2)) ** 0.5)
    if int(z) <= int(r) :
        print("True")
    else :
        print("False")
main(int(input()),int(input()),int(input()),int(input()),int(input()))
