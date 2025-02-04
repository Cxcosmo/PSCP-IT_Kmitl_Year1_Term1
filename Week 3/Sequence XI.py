"""Sequence XI"""
def main(x) :
    """main"""
    for i in range((x * 2) - 1) :
        n = 1
        for j in range((x * 2) - 1) :
            if i + 1 == 1 or i + 1 == (x * 2) - 1 :
                print(f"{n:02}", end = " ")
            elif i + 1 == x :
                print(f"{n:02}", end = " ")
                if j + 1 < x :
                    n += 1
                else :
                    n -= 1
            elif i < x :
                print(f"{n:02}", end = " ")
                if j + 1 < i + 1 :
                    n += 1
                elif j + 1 >= (x * 2) - i - 1 :
                    n -= 1
            else :
                print(f"{n:02}", end = " ")
                if j + 1 < x - (i - x) - 1 :
                    n += 1
                elif j + 1 >= i + 1 :
                    n -= 1
        print()
main(int(input()))
