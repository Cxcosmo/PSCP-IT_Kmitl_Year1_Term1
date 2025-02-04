"""WordSequence I"""
def main(text) :
    """WordSequence I"""
    lenght_text = len(text)
    for i in range(lenght_text) :
        for j in range(0,i + 1) :
            print(text[j], end = "")
        print()
main(input())
