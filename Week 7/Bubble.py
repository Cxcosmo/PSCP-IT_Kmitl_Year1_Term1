"""Bubble"""
def main(bubble) :
    """Jump"""
    count = 0
    n = 0
    while n < len(bubble) - 1 :
        c = 0
        if bubble[n] == "^" :
            count += 1
            n += 1
        elif bubble[n].islower() :
            count += 1
            n += 1
        elif bubble[n].isupper() :
            count += 1
            n += 3
            if n >= len(bubble) - 1 :
                break
            if bubble[n].islower() :
                n -= 1
                c += 1
            if bubble[n].islower() :
                n -= 1
                c += 1
            if not bubble[n].isupper() :
                n += c
            if bubble[n].isspace() :
                n -= 1
            if bubble[n].isspace() :
                n -= 1
        if bubble[n].isspace() :
            print("IMPOSSIBLE")
            print(len(bubble) - n)
            return
    print("POSSIBLE")
    print(count)
main(input())
