"""PickThemAgain"""
def main(list_num) :
    """PickThemAgain"""
    count = 0
    list_num.reverse()
    for i in list_num :
        if not int(i) % 3 or not int(i) % 5 :
            print(i)
            count += 1
    if not count :
        print("Nope")
main(input().split())
