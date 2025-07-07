"""GCD_N"""
import math
def main() :
    """GCD_N"""
    num = [int(input()) for _ in range(int(input()))]
    print(math.gcd(*num))
main()
