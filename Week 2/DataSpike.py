"""DataSpike"""
def main() :
    """main"""
    a = 0
    for _ in range(8) :
        b = int(input())
        if b > a :
            a = b
    print(a)
main()
