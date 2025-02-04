"""Distribute"""
def main(n, k):
    """Distribute"""
    if n < k or k < 1:
        return -1
    max_givers = 0
    money = n - k
    for givers in range(k + 1):
        money_left = money - 8 * givers
        if money_left < 0:
            break
        if money_left <= (k - givers) * 3 :
            max_givers = max(max_givers, givers)
    print(max_givers)
main(int(input()), int(input()))
