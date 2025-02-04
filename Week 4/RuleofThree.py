"""RuleofThree"""
def main():
    """RuleofThree"""
    n = int(input())
    x = float(input())
    y = float(input())
    z = y / x
    for _ in range(n - 1) :
        a = float(input())
        b = float(input())
        c = b / a
        if z < c :
            x = a
            y = b
            z = c
        elif z == c :
            if x > a :
                x = a
                y = b
    print(f"{x:.2f} {y:.2f}")
main()
