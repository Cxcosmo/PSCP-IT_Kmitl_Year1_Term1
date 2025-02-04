"""Taking Turns"""
import json
def main(lst) :
    """Taking Turns"""
    new_list = []
    n = 1
    lst.reverse()
    while lst :
        if n == 2 :
            lst.reverse()
            n = 0
        new_list.append(lst[0])
        lst.pop(0)
        n += 1
    print(new_list)
main(json.loads(input()))
