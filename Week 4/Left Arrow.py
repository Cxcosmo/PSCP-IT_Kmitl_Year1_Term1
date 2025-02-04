"""Left Arrow"""
def main(k,n) :
    """Arrow"""
    x = n // 2
    for _ in range(n) :
        for j in range(k + abs(x)) :
            if j < abs(x) :
                print(" ", end = "")
            else :
                print("*", end = "")
        x -= 1
        print()
main(int(input()),int(input()))
