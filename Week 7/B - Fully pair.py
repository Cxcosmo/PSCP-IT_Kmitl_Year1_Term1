"""B - Fully pair?"""
def main(text):
    """B - Fully pair?"""
    alpha = []
    lost_friend = ""
    check = ""
    for i in text :
        if i != check :
            alpha.append(i)
            check = i
    for i in alpha :
        if text.count(i) % 2 and not i in lost_friend :
            lost_friend += i
    if not lost_friend :
        print("fully paired")
    else :
        print(lost_friend)
main(input())
