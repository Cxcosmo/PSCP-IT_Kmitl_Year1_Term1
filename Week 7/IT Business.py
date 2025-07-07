"""IT Business"""
def deposit(bank_money, my_money, money) :
    """Deposit"""
    err = 0
    my_money -= money
    if my_money >= 0 :
        bank_money += money
    else :
        my_money += money
        err += 1
    return bank_money, my_money, err

def window(bank_money, my_money, money) :
    """window"""
    err = 0
    bank_money -= money
    if bank_money >= 0 :
        my_money += money
    else :
        bank_money += money
        err += 1
    return bank_money, my_money, err

def main(bank_money, my_money) :
    """bank"""
    err = 0
    while True :
        transaction = input()
        if transaction == "end" :
            break
        select = transaction[0]
        money = float(transaction[2:])
        if select == "D" :
            bank_money, my_money, error = deposit(bank_money, my_money, money)
            if not error :
                err = 0
            else :
                err += error
        else :
            bank_money, my_money, error = window(bank_money, my_money, money)
            if not error :
                err = 0
            else :
                err += error
        if err == 3 :
            break
    print(f"{bank_money:.2f}")
    print(f"{my_money:.2f}")
main(float(input()), float(input()))
