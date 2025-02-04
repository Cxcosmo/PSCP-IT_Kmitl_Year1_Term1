"""diamond"""
def main(r) :
    """Diamond = Pet? == Dog?!!"""
    l = r // 2
    for i in range (-l, l + 1) :
        for j in range(-l, l + 1) :
            if l - abs(i) == abs(j) or not i :
                print("*", end = "")
            else :
                print(" ", end = "")
        print()
main(int(input()))
