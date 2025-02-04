"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def descend(num1, num2, num3) :
    """descend"""
    if num1 >= num2 > num3 :
        print(f"{num1:.2f}, {num2:.2f}, {num3:.2f}")
    elif num1 >= num3 > num2:
        print(f"{num1:.2f}, {num3:.2f}, {num2:.2f}")
    elif num2 >= num1 > num3 :
        print(f"{num2:.2f}, {num1:.2f}, {num3:.2f}")
    elif num2 >= num3 > num1 :
        print(f"{num2:.2f}, {num3:.2f}, {num1:.2f}")
    elif num3 >= num1 > num2 :
        print(f"{num3:.2f}, {num1:.2f}, {num2:.2f}")
    elif num3 >= num2 > num1 :
        print(f"{num3:.2f}, {num2:.2f}, {num1:.2f}")
    else :
        print(f"{num1:.2f}, {num2:.2f}, {num3:.2f}")

def ascend(num1, num2, num3) :
    """ascend"""
    if num1 >= num2 > num3 :
        print(f"{num3:.2f}, {num2:.2f}, {num1:.2f}")
    elif num1 >= num3 > num2:
        print(f"{num2:.2f}, {num3:.2f}, {num1:.2f}")
    elif num2 >= num1 > num3 :
        print(f"{num3:.2f}, {num1:.2f}, {num2:.2f}")
    elif num2 >= num3 > num1 :
        print(f"{num1:.2f}, {num3:.2f}, {num2:.2f}")
    elif num3 >= num1 > num2 :
        print(f"{num2:.2f}, {num1:.2f}, {num3:.2f}")
    elif num3 >= num2 > num1 :
        print(f"{num1:.2f}, {num2:.2f}, {num3:.2f}")
    else :
        print(f"{num1:.2f}, {num2:.2f}, {num3:.2f}")

def main(ty, num1, num2, num3) :
    """main"""
    if ty == "Ascend" :
        ascend(num1, num2, num3)
    else :
        descend(num1, num2, num3)
main(input(), float(input()), float(input()), float(input()))
