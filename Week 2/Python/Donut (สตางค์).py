"""Donut"""
def main():
    """main"""
    price = float(input())
    promotion = float(input())
    free = float(input())
    need = float(input())
    buy = 0
    count_buy = need // (promotion + free)
    total = count_buy * (promotion + free)
    if need > total :
        count_buy += (need - total) // promotion
        total = count_buy * (promotion + free)
    if need > total :
        buy = abs(need - total)
        buy *= price
    print(f"{(count_buy * price * promotion) + buy} {total}")
main()
