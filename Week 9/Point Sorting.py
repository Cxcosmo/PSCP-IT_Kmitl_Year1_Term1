"""Point Sorting"""
def main() :
    """Point Sorting"""
    for _ in range (int(input())) :
        num_list = []
        for _ in range (int(input())) :
            list_n = []
            num = input().split()
            for i in num :
                list_n.append(int(i))
            num_list.append(list_n)
        while num_list :
            min_num = num_list[0]
            len_num = len(num_list)
            for i in range (len_num) :
                if sum(num_list[i]) < sum(min_num) :
                    min_num = num_list[i]
                elif sum(num_list[i]) == sum(min_num) :
                    if (num_list[i])[1] > min_num[1] :
                        min_num = num_list[i]
            print(min_num[0], min_num[1])
            del num_list[num_list.index(min_num)]
main()
