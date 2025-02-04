"""Rectangle"""
def area(h,w) :
    """area"""
    return h * w
def circumference(h,w) :
    """circumference"""
    return h * 2 + w * 2
def main(h = int(input()),w = int(input())):
    """main"""
    print(area(h,w))
    print(circumference(h,w))
main()
