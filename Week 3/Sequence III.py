"""Sequence III"""
def main(x) :
    """main"""
    for i in range(x) :
        for j in range(i + 2, i + x + 2) :
            print(j, end = " ")
        print()
main(int(input()))
