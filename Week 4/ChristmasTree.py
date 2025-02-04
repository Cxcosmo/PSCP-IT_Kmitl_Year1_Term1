"""ChristmasTree"""
def main(n,k):
    """ChristmasTree"""
    x = 1
    y = 3
    for i in range(n + k) :
        if n == 1 :
            if not i :
                print("*")
            else :
                print("---")
        else :
            if i >= n :
                print(" " * (n - y), "---")
            else :
                for j in range(n + x - 1) :
                    if j >= n - x :
                        print("*", end = "")
                    else :
                        print(" ", end = "")
                print()
        x += 1
main(int(input()),int(input()))
