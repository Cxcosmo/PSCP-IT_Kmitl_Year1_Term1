"""BrickBridge"""
def main(a,b,g) :
    """main"""
    c = g // 5
    if c > b :
        g -= b * 5
    else :
        g -= c * 5
    g -= a
    if g <= 0 :
        a -= abs(g)
        print(a)
    elif g > 0 :
        print(-1)
main(int(input()),int(input()),int(input()))
