"""Password"""
import math
def main(password) :
    """Pass"""
    l = 0
    u = 0
    na = 0
    n = 0
    for i in password :
        if i.islower() :
            l = 1
        if i.isupper() :
            u = 1
        if not i.isalnum() :
            na = 1
        if i.isnumeric() :
            n = 1
    r = (l * 26) + (u * 26) + (na * 32) + (n * 10)
    lp = len(password)
    e = math.floor(math.log((r ** lp), 2))
    print(e)
    if e < 28 :
        print("Very Weak")
    elif e < 36 :
        print("Weak")
    elif e < 60 :
        print("Reasonable")
    elif e < 128 :
        print("Strong")
    else :
        print("Very Strong")
main(input())
