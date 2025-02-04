"""Century"""
import math as m
def main() :
    """Century"""
    for _ in range(int(input())) :
        year_input = input()
        type_year = year_input[:4]
        year = int(year_input[5:])
        if type_year == "B.E." :
            year -= 543
        if year < 0 :
            print("ERROR")
        else :
            print(m.ceil(year/100))
main()
