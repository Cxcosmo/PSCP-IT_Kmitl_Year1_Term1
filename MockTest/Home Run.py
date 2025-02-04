"""Home Run"""
def main(n, ball) :
    """Home Run"""
    count = 0
    for _ in range(n) :
        s = float(input())
        if ball > s :
            count += 1
    print(count)
main(int(input()), float(input()))
