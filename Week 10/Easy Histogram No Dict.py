"""Easy Histogram No Dict"""
def main(text) :
    """Easy Histogram No Dict"""
    text_list = []
    text_ascii = []
    for i in text :
        if not i in text_list and i.isalpha() :
            text_list.append(i)
    for i in text_list :
        if i.islower() :
            text_ascii.append(ord(i) - 32.1)
        else :
            text_ascii.append(ord(i))
    text_ascii.sort()
    for i in text_ascii :
        if isinstance(i, int):
            print(f"{chr(i)} = {text.count(chr(i))}")
        else :
            print(f"{chr(int(i + 32.1))} = {text.count(chr(int(i + 32.1)))}")
main(input())
