"""Run Length Encoding"""
def main(text) :
    """Encode"""
    lt = [text[0]]
    lc = []
    encode = ""
    j = text[0]
    count = 0
    for i in text :
        if j == i :
            count += 1
        else :
            lc.append(count)
            lt.append(i)
            count = 1
        j = i
    lc.append(count)
    y = len(lt)
    for x in range(y) :
        encode += str(lc[x]) + lt[x]
    print(encode)
main(input())
