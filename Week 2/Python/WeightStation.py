"""WeightStation"""
def main(average,w1,w2,w3) :
    """main"""
    w4 = (average * 4) - (w1 + w2 + w3)
    if w1 + w2 + w3 + w4 > 15000 :
        print("Overweight")
    elif average / 2 > w1 or average / 2 > w2 or average / 2 > w3 or average / 2 > w4 :
        print("Unbalance")
    elif average * 2 < w1 or average * 2 < w2 or average * 2 < w3 or average * 2 < w4 :
        print("Unbalance")
    else :
        print(f"Pass {w4:.2f}")
main(float(input()),float(input()),float(input()),float(input()))
