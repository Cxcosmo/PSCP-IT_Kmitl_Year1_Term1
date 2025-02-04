"""Kaprekar"""
def mx(num) :
    """max"""
    n = []
    for i in num :
        n.append(i)
    number = ""
    for i in range(3,0,-1) :
        x = n[i]
        for j in n :
            if int(x) < int(j) :
                x = j
        number += str(n.pop(n.index(str(x))))
    number += n[0]
    return number

def mn(num) :
    """min"""
    n = []
    for i in num :
        n.append(i)
    number = ""
    for i in range(3,0,-1) :
        x = n[i]
        for j in n :
            if int(x) > int(j) :
                x = j
        number += str(n.pop(n.index(str(x))))
    number += n[0]
    return number

def main(num) :
    """6174"""
    mX = mx(str(num))
    mN = mn(str(num))
    c = 0
    x = 0
    while True :
        x = str(int(mX) - int(mN))
        c += 1
        if x == "6174" :
            break
        if len(x) < 4 :
            x += "0"
        mX = mx(x)
        mN = mn(x)
    print(c)
main(int(input()))
