"""SecondConverter"""
def main(k,s,m,h) :
    """Time"""
    hr = k // (m * s)
    k = k % (m * s)
    mi = k // (s)
    k = k % (s)
    hr = hr % h
    print(f"{hr}:{mi}:{k}")
main(int(input()),int(input()),int(input()),int(input()))
