"""Sequence VIII"""
def main(x) :
    """main"""
    y = x
    for i in range(x) :
        num = 1
        for j in range(x) :
            if j + 1 < y :
                print("  ", end = " ")
            else :
                print(f"{num:02}", end = " ")
                num += 1
        y -= 1
        i += 1
        print()
main(int(input()))