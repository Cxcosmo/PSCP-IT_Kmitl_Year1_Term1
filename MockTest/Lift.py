"""Lift"""
def main(n, total) :
    """Lift"""
    wt1 = 0
    wt2 = 0
    if not n :
        print("Safe")
    else :
        for _ in range(n) :
            age = int(input())
            w = float(input())
            if age >= 12 :
                wt1 += w
            else :
                wt2 += w
        if wt1 > 0 :
            wt1 += wt2
        if not wt1 or total < wt1 :
            print("Not Safe")
        elif total >= wt1 :
            print("Safe")
main(int(input()), float(input()))
