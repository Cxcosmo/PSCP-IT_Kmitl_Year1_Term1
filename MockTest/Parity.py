"""Parity"""
def main(bit, odd_even) :
    """bit"""
    c = 0
    for i in bit :
        if int(i) :
            c += 1
    if odd_even == "Even" :
        if not c % 2 :
            bit += "0"
        else :
            bit += "1"
    else :
        if not c % 2 :
            bit += "1"
        else :
            bit += "0"
    print(bit)
main(input(), input())
