"""Coffee Shop"""
def main(sell, sell1, sell2, pro, need) :
    """Coffee Shop"""
    pro1 = sell + (((need - 1) * sell) * ((100 - sell1) / 100 ))
    pro2 = need * sell
    if pro2 >= pro :
        pro2 *= (100 - sell2) / 100
    if pro1 < pro2 :
        print(1)
        print(f"{pro1:.2f}")
    else :
        print(2)
        print(f"{pro2:.2f}")
main(float(input()),float(input()),float(input()),float(input()),int(input()))
