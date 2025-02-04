"""ProgressiveTax"""
def main(money) :
    """Tax"""
    tax = 0
    if money > 4000000 :
        m = money - 4000000
        tax += m * 0.35
        money -= m
    if money > 2000000 :
        m = money - 2000000
        tax += m * 0.30
        money -= m
    if money > 1000000 :
        m = money - 1000000
        tax += m * 0.25
        money -= m
    if money > 750000 :
        m = money - 750000
        tax += m * 0.20
        money -= m
    if money > 500000 :
        m = money - 500000
        tax += m * 0.15
        money -= m
    if money > 300000 :
        m = money - 300000
        tax += m * 0.10
        money -= m
    if money > 150000 :
        m = money - 150000
        tax += m * 0.05
        money -= m
    print(int(tax))
main(int(input()))
