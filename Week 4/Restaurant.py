"""Restaurant"""
def main(cost,pro,sell,add):
    """Restaurant"""
    costsellget = (cost + add) - ((cost + add) * (sell / 100))
    costsell = cost - (cost * (sell / 100))
    if cost < pro :
        if costsellget > cost :
            print(f"No {costsellget - cost:.3f}")
        elif costsellget == cost :
            print("Yes")
        else :
            print(f"Yes {cost - costsellget:.3f}")
    else :
        if costsellget < costsell :
            print(f"Yes {costsell - costsellget:.3f}")
        elif costsellget > costsell :
            print(f"No {costsellget - costsell:.3f}")
        else :
            print("Yes")     
main(float(input()),float(input()),float(input()),float(input()))
 