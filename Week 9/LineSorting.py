"""LineSorting"""
def main() :
    """LineSorting"""
    len_text = []
    text = []
    for _ in range(int(input())) :
        t = input()
        len_text.append(len(t))
        text.append(t)
    len_text.sort()
    for i in len_text :
        for j in text :
            if len(j) == i :
                print(j)
                text.pop(text.index(j))
main()
