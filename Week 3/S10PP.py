"""I Love Drawing"""
n = int(input())
for i in range(1, 2*n):
    for j in range(1, 2*n):
        value = min(i, j, 2*n-i, 2*n-j, n)
        print(f"{value:02}", end = " ")
    print()
