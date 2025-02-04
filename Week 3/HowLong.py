"""HowLong"""
def main(x, y) :
    """main"""
    while y // 10 :
        y = y // 10
        x += 1
    print(x + 1)
main(0,int(abs(int(input()))))
