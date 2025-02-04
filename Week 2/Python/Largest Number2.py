"""Largest Number"""
A = input()
B = input()
C = input()
X = 0
def check(x,y) :
    """Check"""
    if y > x :
        return y
    return x
X = check(X,int(A + B + C))
X = check(X,int(A + C + B))
X = check(X,int(B + A + C))
X = check(X,int(B + C + A))
X = check(X,int(C + A + B))
X = check(X,int(C + B + A))
print(X)
