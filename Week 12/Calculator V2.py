"""Calculator V2"""
def main(n) :
    """Calculator V2"""
    len_n = len(str(n))
    nine = "9" * (len_n - 1)
    count = 0
    if n == 1 :
        print(1)
        return
    if not nine :
        nine = 0
    else :
        nine = int(nine)
        count += int(str(len_n - 1) + (("8") * (len_n - 1)))
    count += (n - nine) * (len_n + 1)
    print(count)
main(int(input()))
