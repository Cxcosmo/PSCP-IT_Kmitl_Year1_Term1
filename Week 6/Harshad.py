"""Harshad"""
def main() :
    """Harshad"""
    for _ in range (10) :
        num = str(abs(int(input())))
        sn = 0
        if num == "0" :
            print("No")
        elif len(num) > 1 :
            for i in num :
                sn += int(i)
            if not int(num) % sn :
                print("Yes")
            else :
                print("No")
        else :
            print("Yes")
main()
