"""Circular II"""
def main() :
    """main"""
    xn = float(input())
    yn = float(input())
    rn = float(input())
    x = float(input())
    y = float(input())
    r = float(input())
    z = (((xn - x) ** 2) + ((yn - y) ** 2)) ** 0.5
    if z < rn + r :
        print("Yes")
    else :
        print("No")
main()
