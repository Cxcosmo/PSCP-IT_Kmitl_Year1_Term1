"""Doc"""
def main() :
    """Doc"""
    n = int(input())
    weightCon = input().split()
    REM = 0
    count = 0
    weightCon = list(map(int,weightCon))
    weightCon.sort()
    while count != n-1 :
        calCon = []
        for i in range(len(weightCon)-1) :
            j = i + 1
            calCon.append(weightCon[j] - weightCon[i])
        REM += weightCon.pop(calCon.index(min(calCon))+1) - weightCon.pop(calCon.index(min(calCon)))
        count += 1
    print(REM)
main()
