"""Meteorite"""
def main(a, b, c) :
    """Meteorite"""
    count = 1
    n = 0
    if a >= c :
        n += 1
        a /= b
        while a >= c :
            a /= b
            count *= b
            n += count
    print(n)
main(float(input()), int(input()), float(input()))
