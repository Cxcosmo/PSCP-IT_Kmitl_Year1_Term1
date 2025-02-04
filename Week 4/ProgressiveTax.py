"""ProgressiveTax"""
def tax5(money) :
    """tex 5%"""
    tex = 0
    if money > 150000 :
        tex += (money - 150000) * 0.05
        money -= money - 150000
    return tex

def tax10(money) :
    """tex 10%"""
    tex = 0
    if money > 300000 :
        tex += (money - 300000) * 0.10
        money -= money - 300000
    return tex + tax5(money)

def tax15(money) :
    """tex 15%"""
    tex = 0
    if money > 500000 :
        tex += (money - 500000) * 0.15
        money -= money - 500000
    return tex + tax10(money)

def tax20(money) :
    """tex 20%"""
    tex = 0
    if money > 750000 :
        tex += (money - 750000) * 0.20
        money -= money - 750000
    return tex + tax15(money)

def tax25(money) :
    """tex 25%"""
    tex = 0
    if money > 1000000 :
        tex += (money - 1000000) * 0.25
        money -= money - 1000000
    return tex + tax20(money)

def tax30(money) :
    """tex 30%"""
    tex = 0
    if money > 2000000 :
        tex += (money - 2000000) * 0.30
        money -= money - 2000000
    return tex + tax25(money)

def tax35(money) :
    """tex 35%"""
    tex = 0
    if money > 4000000 :
        tex += (money - 4000000) * 0.35
        money -= money - 40000000
    return tex + tax30(money)

def main(money) :
    """main"""
    print(int(tax35(money)))
main(int(input()))
