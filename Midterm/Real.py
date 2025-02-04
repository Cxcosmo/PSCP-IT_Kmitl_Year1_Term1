"""Real"""
def seven_seg(bit) :
    """7segment"""
    err = 0
    num = ""
    if bit == "1111110" :
        num += "0"
    elif bit == "0110000" :
        num += "1"
    elif bit == "1101101" :
        num += "2"
    elif bit == "1111001" :
        num += "3"
    elif bit == "0110011" :
        num += "4"
    elif bit == "1011011" :
        num += "5"
    elif bit == "1011111" :
        num += "6"
    elif bit == "1110000" :
        num += "7"
    elif bit == "1111111" :
        num += "8"
    elif bit == "1111011" :
        num += "9"
    else :
        err += 1
    return err, num

def main() :
    """Sooksun"""
    err = 0
    num = ""
    d = 0
    for _ in range(3) :
        bit = ""
        for _ in range(7) :
            on_off = input()
            if on_off == "on" :
                bit += "1"
            else :
                bit += "0"
        er, n = seven_seg(bit)
        err += er
        num += n
        on_off = input()
        if on_off == "on" :
            num += "."
            d += 1
    if err > 0 or d > 1 :
        print("Error")
    else :
        print(f"{float(num):.2f}")
main()
