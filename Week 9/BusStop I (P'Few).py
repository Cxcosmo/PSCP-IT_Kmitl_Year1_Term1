"""Thank you P'Few"""
def main():
    """BusStop I"""
    amount = int(input())
    count = int(input())
    list_str = []
    list_int = []
    at_home = 0
    for _ in range(count):
        bus = input().split()
        list_str.append(bus)
    list_str.sort(key=lambda i: int(i[0]))
    for i in list_str:
        bus_stop = int(i[0])
        len_int = len(list_int)
        if len_int :
            list_int2 = list_int.copy()
            for j in list_int:
                if j == bus_stop:
                    list_int2.remove(j)
                    at_home += 1
            list_int = list_int2
        for j in range(1, len(i)):
            if len(list_int) == amount:
                break
            if bus_stop < int(i[j]):
                list_int.append(int(i[j]))
    print(at_home)
main()
