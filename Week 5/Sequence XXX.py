"""SequenceXX"""
def main(n,m) :
    """X*N"""
    for i in range(-n, n + 1, 1) :
        for _ in range(m) :
            for j in range(-n, n + 1, 1) :
                if abs(i) == n or abs(j) == n:
                    print("*", end = "")
                elif abs(i) == abs(j) :
                    print("*", end = "")
                else :
                    print(" ", end = "")
            print(" ", end = "")
        print()
main(int(input()) // 2,int(input()))
