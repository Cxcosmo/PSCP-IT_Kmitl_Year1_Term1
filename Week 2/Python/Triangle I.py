"""Triangle I"""
a = [float(input()), float(input()), float(input())]
b = []
if a[0] >= a[1] > a[2] :
    b.append(a[0])
    b.append(a[1])
    b.append(a[2])
elif a[0] >= a[2] > a[1] :
    b.append(a[0])
    b.append(a[2])
    b.append(a[1])
elif a[1] >= a[0] > a[2] :
    b.append(a[1])
    b.append(a[0])
    b.append(a[2])
elif a[1] >= a[2] > a[0] :
    b.append(a[1])
    b.append(a[2])
    b.append(a[0])
elif a[2] >= a[0] > a[1] :
    b.append(a[2])
    b.append(a[0])
    b.append(a[1])
elif a[2] >= a[1] > a[0] :
    b.append(a[2])
    b.append(a[1])
    b.append(a[0])
else :
    b = a
if b[0] == ((b[1] ** 2) + (b[2] ** 2)) ** 0.5 :
    print("Yes")
else :
    print("No")
