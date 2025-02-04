"""abcdefghijklmnopqrstuvwxyz"""
def main(money):
    """for the money"""
    costed = 0
    if money > 4000000:
        cost = money - 4000000
        costed += cost * 0.35
        money -= cost
    if money > 2000000:
        cost = money - 2000000
        costed += cost * 0.3
        money -= cost
    if money > 1000000:
        cost = money - 1000000
        costed += cost * 0.25
        money -= cost
    if money > 750000:
        cost = money - 750000
        costed += cost * 0.2
        money -= cost
    if money > 500000:
        cost = money - 500000
        costed += cost * 0.15
        money -= cost
    if money > 300000:
        cost = money - 300000
        costed += cost * 0.1
        money -= cost
    if money > 150000:
        cost = money - 150000
        costed += cost * 0.05
        money -= cost
    print(int(costed))

main(int(input()))
