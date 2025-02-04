"""Sequence VII"""
def main(x) :
    """main"""
    for i in range(1, (x * 2)) :
        for j in range(1, (x - abs(x - i)) + 1) :
            print(j, end = " ")
        print()
main(int(input()))
