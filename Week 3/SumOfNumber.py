"""SumOfNumber"""
def main(x, y) :
    """main"""
    while x != y :
        z = int(input())
        if z == -1 :
            break
        x += z
    print(x)
main(0, int(input()))
