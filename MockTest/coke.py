"""Coke"""
def main(sell, pro, new_sell, need) :
    """Pepsi"""
    if not need :
        print(0)
    elif not pro :
        print(sell * need)
    else :
        count_pro = need // pro
        left = need - (count_pro * pro)
        if not left :
            count_pro -= 1
        buy = need - count_pro
        print((sell * buy) + (count_pro * new_sell))
main(int(input()), int(input()), int(input()), int(input()))
