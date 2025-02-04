"""Stamps"""
def main(n,a,b,c,d) :
    """stamps"""
    s = 0
    total = 0
    for _ in range(n) :
        cost = int(input())
        check = 0
        count = 0
        if s >= c :
            count = s // c
            check = cost // d
            if not check :
                check += 1
            if count > check + 1 :
                count = check + 1
        if not cost - ((count - 1) * d) :
            count -= 1
        s -= count * c
        cost -= count * d
        if cost < 0 :
            cost = 0
        total += cost
        if cost >= a :
            s += (cost // a) * b
    print(total)
    print(s)
main(int(input()),int(input()),int(input()),int(input()),int(input()))
