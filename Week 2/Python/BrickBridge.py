"""BrickBridge"""
def main(a, b, g) :
    c = 0
    while g > 0 :
        g -= 5
        b -= 1
        if not b :
            break
    while g > 0 :
        g -= 1
        a -= 1
        c += 1
        if a < 0 :
            print(-1)
            g += 1
            break
    if not g :
        print(c)
main(int(input()),int(input()),int(input()))
