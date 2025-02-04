"""Classify"""
def main() :
    """Classify"""
    num_list = []
    num_count = []
    while True :
        num = input()
        if num == "END" :
            break
        num_list.append([int(num[:2]), int(num[2:4])])
    num_list.sort()
    while num_list :
        count = 0
        for i in num_list :
            if num_list[0] == i :
                count += 1
            else :
                break
        num_count.append([num_list[0][0], num_list[0][1], count])
        for _ in range(count) :
            num_list.remove(num_list[0])
    len_count = len(num_count)
    for i in range(len_count) :
        if not i :
            print(f"{num_count[i][0]} {num_count[i][1]} {num_count[i][2]}")
        elif num_count[i][0] == num_count[i - 1][0] :
            print(f"-- {num_count[i][1]} {num_count[i][2]}")
        else :
            print(f"{num_count[i][0]} {num_count[i][1]} {num_count[i][2]}")
main()
