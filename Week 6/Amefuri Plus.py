"""あめふり"""
def day(climate) :
    """day"""
    w = 0
    if climate in ("C","c") :
        w += 0.50
    elif climate in ("N","n") :
        w += 1.00
    elif climate in ("W","w") :
        w += 1.50
    return w

def night(climate) :
    """night"""
    w = 0
    if climate in ("C","c") :
        w += 0.25
    elif climate in ("N","n") :
        w += 0.50
    elif climate in ("W","w") :
        w += 0.75
    return w

def rain(climate) :
    """rain"""
    w = 0
    if climate in ("R","r") :
        w += 2.00
    elif climate in ("S","s") :
        w += 3.00
    return w

def main(time, climate, wet) :
    """あめふり"""
    for i in climate :
        if i in ("H","h") :
            print("Lost")
            return
        if i in ("R","r","S","s") :
            wet += rain(i)
            if wet > 16 :
                wet = 16
        if 6 <= time < 18 :
            wet -= day(i)
        else :
            wet -= night(i)
        if wet <= 0 :
            print("Dry")
            return
        time += 1
        if time >= 24 :
            time -= 24
    print(f"Still Wet (Wet Level: {wet:.2f})")
main(int(input()), input(), 8)
