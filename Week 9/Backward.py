"""Backward"""
def main() :
    """Backward"""
    text_list = []
    while True :
        text = input()
        if text == "NULL" :
            break
        text_list.append(text)
    text_list.reverse()
    for i in text_list :
        print(i)
main()
