"""Diamond I"""
def main(n, m, a = 0) :
    """Diamond I"""
    list_diamond = []
    for _ in range(n) :
        list_diamond.append(input().split())
    for i in range(m) :
        sum_num = 0
        for j in range(n) :
            sum_num += int(list_diamond[j][i])
        if sum_num > a :
            a = sum_num
    print(a)
main(int(input()),int(input()))
