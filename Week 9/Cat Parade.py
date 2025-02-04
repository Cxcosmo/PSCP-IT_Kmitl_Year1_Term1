"""Cat Parade"""
def main() :
    """Cat Parade"""
    cat_list = []
    parade = []
    p = 0
    while True :
        cat = input().split(", ")
        if cat[0] == "END" :
            break
        for i in cat :
            p += 1
            if i == "IT'S A DOG" :
                cat_list.pop(len(cat_list) - 1)
                parade.pop(len(parade) - 1)
                p -= 2
            else :
                cat_list.append(i)
                parade.append(p)
    cat_list2 = []
    for i in cat_list :
        cat_count = cat_list.count(i)
        if not i in cat_list2 :
            cat_list2.append(i)
            cat_list2.append(f"{str(parade[cat_list.index(i)])} {cat_count}")
    cat_list3 = []
    for i in range(0,len(cat_list2) - 1,2) :
        cat_list3.append(f"{cat_list2[i]} {cat_list2[i + 1]}")
    cat_list3.sort()
    for i in cat_list3 :
        print(i)
main()
