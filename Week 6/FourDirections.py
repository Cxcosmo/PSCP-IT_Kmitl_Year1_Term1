"""FourDirections"""
def up(i,j) :
    """up"""
    if i == abs(j) :
        print("*", end = "")
    elif not j :
        print("*", end = "")
    else :
        print(" ", end = "")

def down(i,j) :
    """down"""
    if 4 - i == abs(j) :
        print("*", end = "")
    elif not j :
        print("*", end = "")
    else :
        print(" ", end = "")

def left(i,j) :
    """left"""
    if abs(i - (4 - i)) == (j + 2) * 2 :
        print("*", end = "")
    elif not abs(i - (4 - i)) :
        print("*", end = "")
    else :
        print(" ", end = "")

def right(i,j) :
    """right"""
    if abs(i - (4 - i)) == abs(j - 2) * 2 :
        print("*", end = "")
    elif not abs(i - (4 - i)) :
        print("*", end = "")
    else :
        print(" ", end = "")

def main(code) :
    """main"""
    for i in range(5) :
        for t in code :
            for j in range(-2,3) :
                if t == "U" :
                    up(i,j)
                elif t == "D" :
                    down(i,j)
                elif t == "L" :
                    left(i,j)
                elif t == "R" :
                    right(i,j)
            print(" ", end = "")
        print()
main(input())
