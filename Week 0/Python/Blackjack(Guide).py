"""Pre - Blackjack"""
def main():
    """Pre - Blackjack"""
    c = int(input())
    point = 0
    Acount = 0
    for i in range(c):
        i = input()
        if i.upper() in ("K","Q","J"):
            point += 10
        elif i.upper() == "A" :
            Acount += 1
        else :
            point += int(i)
    while Acount :
        if point + (Acount * 11) > 21 :
            point += 1
            Acount -= 1
        else :
            point += 11
            Acount -= 1
    print(point)
main()
  