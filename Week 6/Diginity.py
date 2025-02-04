"""Diginity"""
def main() :
    """all for one"""
    while True :
        x = int(input())
        if not x :
            break
        while len(str(x)) > 1 :
            y = 0
            for i in str(x) :
                y += int(i)
            x = str(y)
        print(x)
main()
