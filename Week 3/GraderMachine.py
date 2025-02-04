"""GraderMachine"""
def main(x,y) :
    """main"""
    Ps = ""
    Sm = 0
    if x > y :
        z = -1
    else :
        z = 1
    for i in range(x,y + z,z) :
        if not i % 2 :
            Ps += str(i) + " "
            Sm += i
    print(f"pass : {Ps}")
    print(f"Sum : {Sm}")
main(int(input()),int(input()))
