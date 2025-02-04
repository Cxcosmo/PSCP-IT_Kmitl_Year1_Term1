"""Pringles"""
def main(top,middle,bottom,finger) :
    """Aroiiiiii"""
    if finger >= len(middle) - 1 :
        print(middle.count(r")"))
        print("None.")
        print(top)
        print(" " * (len(middle) - 1) + middle[-1:])
        print(bottom)
    else :
        c = 0
        for i in range(finger) :
            if middle[i] == ")" :
                c += 1
        mc = middle.count(r")")
        print(c)
        if mc > 0 :
            print("There are still some left.")
        else :
            print("None.")
        print(top)
        print(" " * finger + middle[finger:])
        print(bottom)
main(input(),input(),input(),int(input()))
