"""Paper Cut"""
def main():
    """Paper Cut"""
    paper = input().split()
    mn = input().split()
    x = input().split()
    y = input().split()
    x.append(paper[0])
    y.append(paper[1])
    a = 0
    b = 0
    area = []
    for i in range(int(mn[0]) + 1):
        for j in range(int(mn[1]) + 1):
            area.append((int(x[i]) - a) * (int(y[j]) - b))
            b = int(y[j])
        a = int(x[i])
        b = 0
    area.sort()
    print(area[-1])
    print(area[-2])
main()
