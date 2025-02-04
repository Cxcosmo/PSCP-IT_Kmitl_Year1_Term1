"""Alcohol"""
def male(g, kg) :
    """male"""
    a = (g / (kg * 0.68 * 10)) * 10
    return a

def female(g, kg) :
    """female"""
    a = (g / (kg * 0.55 * 10)) * 10
    return a

def main(sex, kg, card, cc, al, kp, h) :
    """Alcohol"""
    g = (al * (cc * kp))
    if card == "No" :
        print("Not Safe")
    else :
        if sex == "Male" :
            alcohol = male(g, kg)
        else :
            alcohol = female(g, kg)
        if  alcohol - (h * 15) > 50 :
            print("Not Safe")
        else : 
            print("Safe")
main(input(), float(input()), input(), float(input()), float(input()), int(input()), int(input()))
