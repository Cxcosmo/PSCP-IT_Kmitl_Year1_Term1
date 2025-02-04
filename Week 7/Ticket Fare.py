"""Ticket Fare"""
def main(n) :
    """Ticket Fare"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    g = int(input())
    cost = 0
    if f > n or g > n :
        print("Error")
        return
    if f > g :
        f, g = g, f
    g -= f
    f = 1
    if f <= a < g :
        cost += b
        f = a
    elif f <= a and g <= a :
        print(b)
        return
    if f < g and f <= c + a :
        if g <= c + a :
            cost += (g - f) * d
            print(cost)
            return
        cost += c * d
        f += c
    if f < g :
        cost += (g - f) * e
    print(cost)
main(int(input()))
