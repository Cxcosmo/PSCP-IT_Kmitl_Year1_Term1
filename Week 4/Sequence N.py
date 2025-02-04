"""Sequence N"""
def main(n) :
    """N"""
    for i in range(n) :
        for j in range(n) :
            if not j or j == n - 1 or j == i :
                print("*", end = "")
            else :
                print(" ", end = "")
        print()
main(int(input()))
