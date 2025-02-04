"""kuayyyy"""
def check_num(x):
    """FOR CHECKING IS NUM OR NOT"""
    if x.isnumeric() :
        return int(x)

def main():
    """FOR DECODING"""
    encode = input()
    decode = ""
    for i in range(len(encode)):
        num = check_num(encode[i])
        if num:
            decode += num * encode[i + 1]
            num = None
    print(decode)
main()
