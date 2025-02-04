"""PhoneNumber"""
def main(num,loc) :
    """Phone"""
    n = (len(num) // 4) + 1
    pn = ""
    for i in range(-n , 0) :
        pn += num[-(4 * abs(i)):len(num) - (4 * (abs(i) - 1))] + " "
    if loc == "Domestic" :
        print(f"{pn[:len(pn) - 1]}")
    else :
        print(f"+66{pn[1:len(pn) - 1]}")
main(input(),input())
