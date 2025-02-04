"""MAC"""
def len_check(hx) :
    """len check"""
    if hx.find(":") > 0 and len(hx) != 17 :
        return "ERROR"
    if hx.find("-") > 0 and len(hx) != 17 :
        return "ERROR"
    if hx.find(".") > 0 and len(hx) != 14 :
        return "ERROR"
    return ""

def index_check(hx, i) :
    """Check"""
    if hx.find(":") > 0 and not i % 3 and hx[i - 1].isalnum() :
        return "ERROR"
    if hx.find("-") > 0 and not i % 3 and hx[i - 1].isalnum() :
        return "ERROR"
    if hx.find(".") > 0 and not i % 5 and hx[i - 1].isalnum() :
        return "ERROR"
    return ""

def main(hx) :
    """MAC"""     
    for i in hx :
        if "0123456789ABCDEF:-.".find(i) < 0 :
            print("ERROR")
            return
    x = len_check(hx)
    if x == "ERROR" :
        print("ERROR")
        return
    for i in range(1,len(hx)) :
        if hx[i - 1] == ":" and i % 3 :
            print("ERROR")
            return
        if hx[i - 1] == "-" and i % 3 :
            print("ERROR")
            return
        if hx[i - 1] == "." and i % 5 :
            print("ERROR")
            return
        y = index_check(hx, i)
        if y == "ERROR" :
            print("ERROR")
            return
    if hx.find("-") > 0 > hx.find(":") and hx.find(".") < 0 :
        print("VALID 1")
    elif hx.find(":") > 0 > hx.find("-") and hx.find(".") < 0 :
        print("VALID 2")
    elif hx.find(".") > 0 > hx.find("-") and hx.find(":") < 0 :
        print("VALID 3")
    else :
        print("ERROR")
main(input().upper())
