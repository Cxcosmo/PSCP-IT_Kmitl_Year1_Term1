"""Elo"""
def main(ra, rb, ab) :
    """Win rate"""
    ea = 1 / (1 + (10 ** ((rb - ra) / 400)))
    eb = 1 / (1 + (10 ** ((ra - rb) / 400)))
    if ab == "A" :
        print(f"{ea:.2f}")
    else :
        print(f"{eb:.2f}")
main(int(input()), int(input()), input())
