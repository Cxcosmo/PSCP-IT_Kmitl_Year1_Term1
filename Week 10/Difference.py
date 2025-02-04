"""Difference"""
def main(n, m) :
    """Difference"""
    a = {"a"}
    b = {"a"}
    for _ in range(n) :
        a.add(input())
    for _ in range(m) :
        b.add(input())
    x = sorted(a.difference(b))
    y = ""
    for i in x :
        y += i + " "
    if not y.strip() :
        return
    else :
        print(y.strip())
main(int(input()), int(input()))
