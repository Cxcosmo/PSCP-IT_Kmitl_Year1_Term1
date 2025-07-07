"""OverlapCircle"""
def main(x1, y1, r1, x2, y2) :
    """OverlapCircle"""
    r2 = int(input())
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if distance > r1 + r2:
        print("no overlapping")
    else:
        print("overlapping")
main(int(input()), int(input()), int(input()), int(input()), int(input()))
