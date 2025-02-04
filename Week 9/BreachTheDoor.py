"""BreachTheDoor"""
def main(text) :
    """BreachTheDoor"""
    new_text = ""
    for i in text :
        if len(i) > 6 :
            text_check = ""
            for j in i :
                if not j.isalpha() :
                    break
                text_check += j
            if len(text_check) > 6 :
                new_text += text_check + " "
    print(new_text.strip())
main(input().split())
