"""FOR!F-Ball"""
def main(step,n1,n2,n3) :
    """swap"""
    for i in step :
        if i == "A" :
            n1,n2 = n2,n1
        elif i == "B" :
            n2,n3 = n3,n2
        elif i == "C" :
            n1,n3 = n3,n1
    if n1 :
        print(1)
    elif n2 :
        print(2)
    elif n3 :
        print(3)
main(input(),1,0,0)
