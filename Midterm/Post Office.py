"""Post Office"""
def e(w) :
    """envelop"""
    if w > 1000 :
        b = 68
    elif w > 500 :
        b = 48
    elif w > 250 :
        b = 33
    elif w > 100 :
        b = 28
    elif w > 20 :
        b = 23
    elif w > 10 :
        b = 18
    else :
        b = 16
    return b

def p(w) :
    """Package"""
    if w > 1000 :
        b = 70
    elif w > 500 :
        b = 55
    else :
        b = 45
    return b

def main(n, m) :
    """Post Office"""
    total = (n * 13) + (m * 15)
    for _ in range(n) :
        w = float(input())
        total += e(w)
    for _ in range(m) :
        w = float(input())
        total += p(w)
    print(total)
main(int(input()), int(input()))
