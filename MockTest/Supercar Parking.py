"""Supercar Parking"""
def main(car) :
    """Supercar Parking"""
    count = 0
    c = 0
    car_list = []
    for i in car :
        car_list.append(int(i))
    if not car_list[0] and not car_list[1] :
        count += 1
    car_list.append(0)
    for j in range(2, len(car_list) - 1) :
        if not car_list[j] and not car_list[j - 1] and not car_list[j + 1] :
            if not c :
                c += 1
                count += c
            else :
                c = 0
    print(count)
main(input())
