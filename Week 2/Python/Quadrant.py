"""Quadrant"""
x = int(input())
y = int(input())
if not x and not y :
    print("O")
elif not x :
    print("Y")
elif not y :
    print("X")
elif x > 0 and y > 0 :
    print("Q1")
elif y > 0 > x :
    print("Q2")
elif x < 0 and y < 0 :
    print("Q3")
elif y < 0 < x :
    print("Q4")
