"""One For All"""
def main(n) :
    """Allmight"""
    lun = ""
    for i in range (1,n+1) :
        name = input()
        lun += name
        if i == n :
            lun += "_" + str(i)
        elif not i % 2 :
            lun += "-" * i
        else :
            lun += "*" * i
    print(lun)
main(int(input()))
