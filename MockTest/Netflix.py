"""Netflix"""
def result(count_mobile, count_basic, count_standard, count_premium, total) :
    """result"""
    if count_premium :
        print(f"Premium x {count_premium}")
    if count_standard :
        print(f"Standard x {count_standard}")
    if count_basic :
        print(f"Basic x {count_basic}")
    if count_mobile :
        print(f"Mobile x {count_mobile}")
    print(f"Total = {total} THB")

def main(num_screens, num_device, unlimited_movies, w_mobile, w_tv, hd, uhd) :
    """Netflix"""
    unlimited_movies += ""
    w_mobile += ""
    count_mobile = 0
    count_basic = 0
    count_standard = 0
    count_premium = 0
    total = 0
    while num_device > 0 and num_screens > 0 :
        if (w_tv == "Yes" or hd == "Yes" or uhd == "Yes") and (num_screens >= 3 or num_device >= 3) :
            total += 419
            count_premium += 1
            num_device -= 4
            num_screens -= 4
        elif (w_tv == "Yes" or hd == "Yes") and (num_screens >= 2 or num_device >= 2) :
            total += 349
            count_standard += 1
            num_device -= 2
            num_screens -= 2
        elif w_tv == "Yes" and hd == "No" and uhd == "No" :
            total += 279
            count_basic += 1
            num_device -= 1
            num_screens -= 1
        else :
            if uhd == "Yes" :
                total += 419
                count_premium += 1
                num_device -= 4
                num_screens -= 4
            elif hd == "Yes" :
                total += 349
                count_standard += 1
                num_device -= 2
                num_screens -= 2
            elif w_tv == "Yes" :
                total += 279
                count_basic += 1
                num_device -= 1
                num_screens -= 1
            else :
                total += 99
                count_mobile += 1
                num_device -= 1
                num_screens -= 1
    result(count_mobile, count_basic, count_standard, count_premium, total)
main(int(input()), int(input()), input(), input(), input(), input(), input())
