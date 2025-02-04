"""Pre - Indicator_Left"""
def main():
    """Pre - Indicator_Left"""
    k = int(input())
    n = int(input())
    m = n // 2
    for i in range(n) :
        print(" " * abs(m) + "*" * k)
        m -= 1
        i += 1
main()
