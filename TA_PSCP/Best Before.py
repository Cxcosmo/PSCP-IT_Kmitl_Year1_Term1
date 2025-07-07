"""Best Before"""
def main(n) :
    """Best Before"""
    dmy = 0
    mdy = 0
    for _ in range(n) :
        num = input()
        a = int(num[0:2])
        b = int(num[2:4])
        if a > 12 >= b > 0:
            dmy += 1
        elif b > 12 >= a > 0 :
            mdy += 1
    if dmy and not mdy :
        print("ddmmyy")
    elif mdy and not dmy :
        print("mmddyy")
    else :
        print("no clue")
main(int(input()))
