"""PickThem"""
import json
def main() :
    """PickThem"""
    count_even = 0
    list_num = json.loads(input())
    for i in list_num :
        if not i % 2 :
            print(i)
            count_even += 1
    if not count_even :
        print("Nope")
main()
