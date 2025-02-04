"""???"""
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

def num_max(num, w_tv, hd, uhd) :
    """num device or screen"""
    count_mobile = 0
    count_basic = 0
    count_standard = 0
    count_premium = 0
    total = 0
    if w_tv == "Yes" and num >= 3 :
        n = num // 4
        total += 419 * n
        count_premium += n
        num -= n * 4
        if w_tv == "Yes" and num >= 3 :
            count_premium += 1
            total += 419
            num -= 4
    if w_tv == "Yes" and uhd == "No" and num >= 2 :
        n = num // 2
        total += 349 * n
        count_standard += n
        num -= n * 2
    if w_tv == "Yes" and hd == "No" and uhd == "No" and num == 1 :
        total += 279 * num
        count_basic += num
        num = 0
    if uhd == "Yes" and num > 0 :
        total += 419
        count_premium += 1
    elif hd == "Yes" and num > 0 :
        total += 349
        count_standard += 1
    elif w_tv == "Yes" and num > 0 :
        total += 279
        count_basic += 1
    elif num > 0 :
        total += 99 * num
        count_mobile += num
    result(count_mobile, count_basic, count_standard, count_premium, total)

def main(num_screens, num_device, no_use, no, w_tv, hd, uhd) :
    """Netflix"""
    no_use += ""
    no += ""
    if num_device > num_screens :
        num_max(num_device, w_tv, hd, uhd)
    else :
        num_max(num_screens, w_tv, hd, uhd)
main(int(input()), int(input()), input(), input(), input(), input(), input())
