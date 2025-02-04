"""Sequence XII"""
def main(x) :
    """main"""
    for i in range((x * 2) - 1) :
        for j in range((x * 2) - 1) :
            print(f"{x + (-(abs((abs(x - (j + 1))) - (abs(x - (i + 1)))))):02}", end = " ")
        print()
main(int(input()))
