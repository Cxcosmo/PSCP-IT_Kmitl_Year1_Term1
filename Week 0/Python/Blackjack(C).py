"""Blackjack"""
def main() :
    """Blackjack"""
    n = int(input())
    p = 0
    a = 0
    for i in range(n) :
        i += 1
        point = input()
        if point in "A" :
            a += 1
        elif point in ("J","Q","K") :
            p += 10
        else :
            p += int(point)
    for j in range(a) :
        j += 1
        if p + (a * 11) > 21 :
            p += 1
            a -= 1
        else :
            p += 11
            a -= 1
    print(p)
main()
