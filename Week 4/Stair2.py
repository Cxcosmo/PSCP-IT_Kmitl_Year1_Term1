"""Stair"""
def main(y,n):
    """Bundai ;-;"""
    count = 0
    err = 0
    stair = y
    for _ in range(n) :
        x = int(input())
        if x <= y :
            count += 1
        else :
            err += 1
        if x + stair <= y :
            stair = x + stair
            count -= 2
            count += 1
        else :
            stair = x
    if err > 0 :
        print("NO")
    else :
        print(count)
main(int(input()),int(input()))
