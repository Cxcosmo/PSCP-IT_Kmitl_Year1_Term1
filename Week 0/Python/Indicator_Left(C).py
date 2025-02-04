"""Indicator_Left"""
def main() :
    """Indicator_Left"""
    k = int(input())
    n = int(input())
    a = n // 2
    l = n - 1
    for row in range(n) :
        for col in range(k + abs(a)) :
            if row + col < n // 2 :
                print(" ", end = "")
            elif l + col < n // 2 :
                print(" ", end = "")
            else :
                print("*", end = "")
        a -= 1
        if not n % 2 :
            if not a :
                a -= 1
        l -= 1
        print()
main()
