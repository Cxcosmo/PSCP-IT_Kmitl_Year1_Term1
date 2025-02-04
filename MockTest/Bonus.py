"""Bonus"""
def main(money, year, month) :
    """Bonus money"""
    if month >= 10 :
        year += 1
    if year > 20 :
        year = 20
    bonus = year * money
    if bonus > 1000000 :
        bonus = 1000000
    if bonus < 5000 :
        bonus =  5000
    print(f"{bonus:.0f}")
main(float(input()), int(input()), int(input()))
