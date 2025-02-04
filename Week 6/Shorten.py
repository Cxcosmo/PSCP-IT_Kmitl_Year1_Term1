"""Short"""
def main(memo_number) :
    """S"""
    ck_number = memo_number
    num = ""
    while ck_number != -1 :
        put_number = int(input())
        if put_number - 1 == ck_number :
            ck_number = put_number
        elif put_number - 1 != ck_number :
            if ck_number != memo_number :
                num += f"{memo_number}-{ck_number}, "
            else :
                num += f"{ck_number}, "
            memo_number = put_number
            ck_number = put_number
        if put_number == -1 :
            break
    print(num.strip(", "))
main(int(input()))
