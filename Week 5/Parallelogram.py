"""Parallelogram"""
def main(text) :
    """Parallelogram"""
    l = len(text)
    for i in range(-(l - 1),l) :
        for j in range(l) :
            if i <= 0 :
                if j >= abs(i) :
                    print(text[abs(j - abs(i))], end = "")
                else :
                    print(" ",end = "")
            else :
                if l - j > i :
                    print(text[j + i], end = "")
                else :
                    print(" ",end = "")
        print()
main(input())
