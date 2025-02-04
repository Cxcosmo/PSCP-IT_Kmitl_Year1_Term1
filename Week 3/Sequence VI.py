"""Sequence VI"""
def main(x) :
    """main"""
    for i in range(x) :
        for j in range(i + 1) :
            print(j + 1, end = " ")
        print()
main(int(input()))
