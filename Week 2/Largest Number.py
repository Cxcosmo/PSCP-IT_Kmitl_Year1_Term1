"""Largest Number"""
A = 0
X = int(input())
Y = int(input())
Z = int(input())
C = X

def mx(a,b) :
    """max"""
    if b > a :
        return b
    return a

def mid(x,y,z) :
    """middle"""
    if x > y > z :
        return y
    if x > z > y :
        return z
    if y > x > z :
        return x
    if y > z > x :
        return z
    if z > x > y :
        return x
    else :
        return y
    
def mi(a,b) :
    """min"""
    if b < a :
        return b
    return a

A = mx(A,X)
A = mx(A,Y)
A = mx(A,Z)
B = mid(X,Y,Z)
C = mi(C,X)
C = mi(C,Y)
C = mi(C,Z)

print(f"{A}{B}{C}")
