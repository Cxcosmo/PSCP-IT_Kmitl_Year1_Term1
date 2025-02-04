"""Donut"""
def main(a,b,c,d) :
    """main"""
    x = 0
    n = 0
    h = 0
    while d > 0 :
        d -= 1
        x += 1
        n += 1
        if x == b :
            x = 0
            d -= c
            h += 1
    print(f"{a * n} {n + (h * c)}")
main(int(input()),int(input()),int(input()),int(input()))
