"""Grade III"""
def main(c) :
    """main"""
    g = 0
    for i in range (c) :
        score = float(input())
        if score >= 95 :
            g += 4
        elif score >= 90 :
            g += 3.5
        elif score >= 85 :
            g += 3
        elif score >= 80 :
            g += 2.5
        elif score >= 75 :
            g += 2
        elif score >= 70 :
            g += 1.5
        elif score >= 65 :
            g += 1
        elif score >= 60 :
            g += 0.5
        i += 1
    print(f"{int((g / c) * 100) / 100 :.2f}")
main(int(input()))
