"""Align"""
def main(size,lo,text) :
    """pai"""
    sp = size - len(text)
    if lo == "left" :
        print(text + " " * sp)
    elif lo == "center" :
        print(" " * ((sp // 2) + (sp % 2)) + text + " " * (sp // 2))
    elif lo == "right" :
        print(sp * " " + text)
main(int(input()),input(),input())
