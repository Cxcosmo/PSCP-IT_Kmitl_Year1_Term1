"""Sequence V"""
def main(x) :
    """main"""
    if not x % 7 :
        y = x // 7
    else :
        y = (x // 7) + 1
    for i in range(y) :
        for j in range(x, x - 7, -1) :
            if not j :
                break
            print(j, end = " ")
        i += 1
        x -= 7
        print()
main(int(input()))
