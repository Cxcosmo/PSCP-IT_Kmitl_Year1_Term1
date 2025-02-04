"""Kayak"""
def main():
    """Kayak"""
    n = int(input())
    w = list(map(int,input().split(" ")))
    t = 0
    w.sort()
    for j in range(n - 1) :
        a = []
        for i in range(len(w) - 1) :
            a.append(w[i + 1] - w[i])
        t += w.pop(a.index(min(a)) + 1) - w.pop(a.index(min(a)))
        j += 1
    print(t)
main()
