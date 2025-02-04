"""Easy Histogram"""
def main(text) :
    """Easy Histogram"""
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
        c = 0
        if isinstance(i, int):
            for j in text :
                if chr(i) == j :
                    c += 1
            print(f"{chr(i)} = {c}")
        else :
            for j in text :
                if chr(int(i + 32.1)) == j :
                    c += 1
            print(f"{chr(int(i + 32.1))} = {c}")
main(input())
