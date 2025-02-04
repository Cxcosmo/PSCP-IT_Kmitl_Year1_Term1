"""Donut"""
def main(a,b,c,d) :
    """main"""
    y = d // (b + c)
    x = y * (b + c)
    if d - x >= b :
        x += b + c
        y += 1
    else :
        x += d - x
    print(f"{(x - (y * c)) * a} {x}")
main(int(input()),int(input()),int(input()),int(input()))
