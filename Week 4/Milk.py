"""Milk"""
def main(a,b,c,d) :
    """main"""
    x = d // a
    total = 0
    if not b :
        print(x)
    else :
        for _ in range(x) :
            total += 1
            if not total % b :
                total += c
                x -= b
                x += c
        print(total)
main(int(input()),int(input()),int(input()),int(input()))
