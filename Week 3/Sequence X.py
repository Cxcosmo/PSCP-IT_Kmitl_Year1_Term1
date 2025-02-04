"""Sequence X"""
def main(x):
    """main"""
    n = -1
    for i in range((x * 2) - 1) :
        num = 1
        if i < x :
            n += 1
        else :
            n -= 1
        for j in range(x + n) :
            if j < abs(x - (i + 1)) :
                print("  ", end = " ")
            elif j + 1 >= x :
                print(f"{num:02}", end = " ")
                num -= 1
            else :
                print(f"{num:02}", end = " ")
                num += 1
        i += 1
        print()
main(int(input()))
