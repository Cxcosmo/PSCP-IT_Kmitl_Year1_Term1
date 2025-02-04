"""Sequence I"""
def main(x) :
    """main"""
    for i in range(x) :
        for j in range(x) :
            print(j + 1, end = " ")
        i += 1
        print()
main(int(input()))
