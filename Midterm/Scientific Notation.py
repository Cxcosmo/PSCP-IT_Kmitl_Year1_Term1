"""Scientific Notation"""
def numb(num) :
    """Change num to sci"""
    f_dot = num.find(".")
    if f_dot >= 0 :
        num_dot = num[:f_dot]
        count_zero = 0
        if not float(num_dot) :
            n = num.replace(".", "")
            for i in range(len(n) - 1) :
                if n[i] != "0" :
                    j = i
                    break
                if n[i] == "0" :
                    count_zero += 1
            n = n[j:]
            result = f"{n[0]}.{n[1:]} x 10^-{count_zero}"
        else :
            len_num_dot = len(num_dot) - 1
            num = num.replace(".", "")
            result = f"{num[0]}.{num[1:]} x 10^{len_num_dot}"
    else :
        num = str(int(num))
        count_zero = 0
        len_num = len(num)
        for i in range(len_num - 1,0,-1) :
            if num[i] != "0" :
                break
            if num[i] == "0" :
                count_zero += 1
        if count_zero > 0 :
            num = num[:-count_zero]
            len_num = (len(num) - 1) + count_zero
            result = f"{num[0]}.{num[1:]} x 10^{len_num}"
        else :
            result = f"{num[0]}.{num[1:]} x 10^{len_num - 1}"
    return result

def sci(num) :
    """Change sci to num"""
    ten = int(num[num.find("^") + 1:])
    f_x = num.find("x")
    num = float(num[:f_x - 1])
    if ten >= 0 :
        result = int(num * (10 ** ten))
    else :
        result = num * (10 ** ten)
    return result

def main(num) :
    """Nai ya sum kan"""
    m = 0
    if num[0] == "-" :
        m += 1
        num = num[1:]
    if num.find("^") >= 0 :
        print(("-" * m) + str(sci(num)))
    else :
        if not float(num) :
            print(0)
        else :
            print(("-" * m) + str(numb(num)))
main(input())
