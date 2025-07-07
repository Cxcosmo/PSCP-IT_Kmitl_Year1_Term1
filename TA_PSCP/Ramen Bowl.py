"""Ramen Bowl"""
def main() :
    """Ramen Bowl"""
    bowls = [int(input()) for _ in range(int(input()))]
    bowls.sort()
    total = 0
    while len(bowls) >= 1 :
        if bowls.count(bowls[0]) > total :
            total = bowls.count(bowls[0])
        bowls.pop(0)
    print(total)
main()
