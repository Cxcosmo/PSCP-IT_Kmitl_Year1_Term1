"""ProgressiveTax"""
def main(money) :
    """ProgressiveTax"""
    tax = 0
    if money > 4000000:
        over = money - 4000000
        tax += over * 0.35
        money = 4000000
    if money > 2000000:
        over = money - 2000000
        tax += over * 0.3
        money = 2000000
    if money > 1000000:
        over = money - 1000000
        tax += over * 0.25
        money = 1000000
    if money > 750000:
        over = money - 750000
        tax += over * 0.2
        money = 750000
    if money > 500000:
        over = money - 500000
        tax += over * 0.15
        money = 500000
    if money > 300000:
        over = money - 300000
        tax += over * 0.1
        money = 300000
    if money > 150000:
        over = money - 150000
        tax += over * 0.05
        money = 150000
    print(int(tax))
main(int(input()))
