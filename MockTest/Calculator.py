"""Calculator"""
def main(n) :
    """Calculator"""
    count = ""
    if n > 1 :
        for i in range(1, n + 1) :
            count += str(i) + "+"
        print(len(count))
    else :
        print(1)
main(int(input()))
