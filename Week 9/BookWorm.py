"""BookWorm"""
def main() :
    """BookWorm"""
    for _ in range(int(input())) :
        time = float(input())
        time_list = []
        count = 0
        sum_time = 0
        for _ in range(int(input())) :
            time_list.append(float(input()))
        while sum_time <= time :
            if not time_list :
                count += 1
                break
            sum_time += min(time_list)
            time_list.remove(time_list[time_list.index(min(time_list))])
            count += 1
        print(count - 1)
main()
