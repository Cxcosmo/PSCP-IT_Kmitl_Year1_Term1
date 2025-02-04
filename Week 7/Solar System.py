"""Solar System"""
def calculate_star(index_solar, find_sun, solar) :
    """Hot"""
    num = ""
    hs = ""
    num_sun = 0
    n = 0
    for j in index_solar :
        if j.isspace() :
            int_num = int(num)
            num = ""
            if num_sun :
                hs += str(int_num)
                break
            if not num_sun and int_num != find_sun :
                hs = ""
                hs += str(int_num) + " "
            n += 1
            if int_num == find_sun :
                num_sun += 1
                index_sun = n
        else :
            num += j
    hs = hs.strip() + " "
    hot = ""
    n = ""
    for i in hs :
        if i.isspace() :
            int_n = int(n)
            n = ""
            for j in range(int_n ,len(solar)) :
                if solar[j].isspace():
                    break
                hot += solar[j]
            hot += " "
        else :
            n += i
    return hot, index_sun

def cool_for(index_solar, int_num, solar) :
    """for"""
    cool = ""
    x = ""
    n = 0
    for j in index_solar :
        if j.isspace() :
            n += 1
            if n == int_num :
                for k in range(int(x), len(solar)) :
                    if solar[k].isspace():
                        break
                    cool += solar[k]
                cool += " "
            else :
                x = ""
        else :
            x += j
    return cool

def cool_cal(str_long, index_solar, solar) :
    """;-;"""
    num = ""
    cool = ""
    for i in str_long :
        if i.isspace() :
            int_num = int(num)
            num = ""
            cool += cool_for(index_solar, int_num, solar)
        else :
            num += i
    return cool

def cool_star(index_star, index_sun, index_solar, solar) :
    """Cool"""
    num = ""
    long_star = 1
    str_long = ""
    for i in index_star :
        if i.isspace() :
            int_num = int(num)
            num = ""
            if abs(int_num - index_sun) > abs(index_sun - long_star) :
                long_star = int_num
                str_long = str(int_num)
            elif abs(int_num - index_sun) == abs(index_sun - long_star) :
                str_long += " " + str(int_num)
        else :
            num += i
    str_long = str_long.strip(" ") + " "
    cool = cool_cal(str_long, index_solar, solar)
    return cool

def main(solar) :
    """Solar System"""
    hot = ""
    cool = ""
    s = ""
    find_sun = 0
    len_solar = len(solar)
    for i in range(len_solar) :
        if solar[i].isspace() :
            if s == "Sun" :
                find_sun = i - 3
            s = ""
        else :
            s += solar[i]
    index_solar = "0 "
    n = 1
    index_star = "1 "
    for i in range(len(solar) - 1) :
        if solar[i].isspace() :
            n += 1
            index_solar += str(i + 1) + " "
            index_star += str(n) + " "
    h, index_sun = calculate_star(index_solar, find_sun, solar)
    hot += h
    cool += cool_star(index_star, index_sun, index_solar, solar)
    cool = cool.strip(" ")
    hot = hot.strip(" ")
    print(f"Hot: {hot}")
    print(f"Cool: {cool}")
main(input() + " ")
