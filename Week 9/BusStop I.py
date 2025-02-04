"""BusStop I"""
def main(max_people, bus_stop) :
    """BusStop I"""
    bus = []
    count = 0
    for _ in range(bus_stop) :
        num = list(map(int, input().split()))
        if num[0] in bus :
            c = bus.count(num[0])
            count += c
            for _ in range(c) :
                bus.remove(num[0])
        take = max_people - len(bus)
        for _ in range(take) :
            len_num = len(num)
            for j in range(1,len_num) :
                if num[j] > num[0] :
                    bus.append(num[j])
                    num.remove(num[j])
                    break
    print(count)
main(int(input()),int(input()))
