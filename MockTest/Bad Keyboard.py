"""Bad Keyboard"""
def main(text) :
    """ioIO"""
    t = ""
    for i in text :
        if i == "o" :
            t += "i"
        elif i == "O" :
            t += "I"
        elif i == "i" :
            t += "o"
        elif i == "I" :
            t += "O"
        else :
            t += i
    print(t)
main(input())
