"""Sequence IX"""
def main(x) :
    """main"""
    n = 0
    for i in range(x) :
        num = 1
        for j in range(x + n) :
            if j + 1 < x - i  :
                print("  ", end = " ")
            elif j + 1 >= x :
                print(f"{num:02}", end = " ")
                num -= 1
            else :
                print(f"{num:02}", end = " ")
                num += 1
        n += 1
        i += 1
        print()
main(int(input()))
