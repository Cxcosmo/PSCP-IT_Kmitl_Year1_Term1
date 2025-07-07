"""Tuple's Sad life"""
def main(num,n) :
    """Tuple's Sad life"""
    count = num.count(n)
    index_n = num.index(n,0)
    for _ in range(count) :
        for i in range(count) :
            if i == count - 1 :
                print(index_n)
            else :
                print(index_n, end = " ")
main(tuple(input().split()), input())
