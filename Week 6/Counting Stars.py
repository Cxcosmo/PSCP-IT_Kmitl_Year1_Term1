"""Counting Stars"""
def main(star) :
    """Comet"""
    constellation = 0
    comet = 0
    shooting_star = 0
    s = ""
    for i in star :
        s += i
        if s in ("~*", "*~") :
            comet += 1
            s = ""
        elif s == "*/" :
            shooting_star += 1
            s = ""
        elif s == "**" :
            constellation += 1
            s = ""
        elif len(s) == 2 :
            s = s[1]
    if not comet and not shooting_star and not constellation :
        print("Tonight is a quiet night.")
    else :
        print(f"constellation: {constellation}")
        print(f"comet: {comet}")
        print(f"shooting star: {shooting_star}")
main(input())
