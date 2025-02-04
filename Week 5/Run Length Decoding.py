"""Run Length Decoding"""
def main(encode) :
    """Decode"""
    text = ""
    num = ""
    le = len(encode)
    for i in range(le):
        if encode[i].isnumeric() :
            num += encode[i]
        else :
            text += encode[i] * int(num)
            num = ""
    print(text)
main(input())
