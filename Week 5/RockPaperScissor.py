"""RockPaperScissor"""
def main(ab) :
    """main"""
    a = 0
    b = 0
    for i in range (0,len(ab) - 1,2) :
        rps = ab[i] + ab[i + 1]
        if rps == "PS" :
            b += 1
        elif rps == "SR" :
            b += 1
        elif rps == "RP" :
            b += 1
        elif rps == "SP" :
            a += 1
        elif rps == "RS" :
            a += 1
        elif rps == "PR" :
            a += 1
    if a == b:
        print(f"DRAW {a}")
    elif a > b :
        print(f"A win {a}-{b}")
    elif b > a :
        print(f"B win {b}-{a}")
main(input())
