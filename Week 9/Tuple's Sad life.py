"""Tuple's Sad life"""
def main(num,n) :
    """Tuple's Sad life"""
    count = num.count(n)
    index_n = num.index(n,0)
    for _ in range(count) :
        for _ in range(count) :
            print(index_n, end = " ")
        print()
main(tuple(input().split()), input())
