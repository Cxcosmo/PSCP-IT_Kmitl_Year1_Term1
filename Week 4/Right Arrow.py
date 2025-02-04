"""Left Arrow"""
def main(k,n) :
    """Arrow"""
    for i in range(0 - (n // 2), n - (n // 2)) :
        for j in range(k + abs((n // 2) - abs(i))) :
            if j < abs((n // 2) - abs(i)) :
                print(" ", end = "")
            else :
                print("*", end = "")
        print()
main(int(input()),int(input()))
