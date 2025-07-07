"""Stroke Zero"""
def main(n):
    """Stroke Zero"""
    for row in range(n):
        for col in range(row + 1) :
            if row == col :
                print(0)
            elif n <= 3 :
                print(0, end=' ')
            elif row == n - 1 :
                print(0, end=' ')
            elif row >= 2 and col != n - 1 :
                if not col :
                    print(0, end=' ')
                else :
                    print(1, end=' ')
            elif row < 3 :
                print(0, end=' ')
main(int(input()))
