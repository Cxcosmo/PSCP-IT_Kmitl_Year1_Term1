"""Gift II"""
A = 0
for i in range(8) :
    w = int(input())
    if not w % 2 :
        A += w
    i += 1
print(A)
