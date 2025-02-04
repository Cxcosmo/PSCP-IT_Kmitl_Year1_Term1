"""Sequence IV"""
def main(x) :
    """main"""
    for i in range(x) :
        for j in range(1 + (i * x), (x * (i + 1)) + 1) :
            print(j, end = " ")
        print()
main(int(input()))
