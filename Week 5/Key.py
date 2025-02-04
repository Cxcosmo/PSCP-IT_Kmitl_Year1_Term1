"""Key"""
def main(key) :
    """KEYYYYYYYYYY"""
    ls = 0
    lt = (int(key[len(key) - 3:len(key)])) * 10
    for i in key :
        ls += int(i)
    ky = str(ls + lt)
    if ls + lt < 1000 :
        ky = str(int(ky) + 1000)
        print(ky[len(ky) - 4:len(ky)])
    else :
        print(ky[len(ky) - 4:len(ky)])
main(str(input()))
