"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def main(text) :
    """AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
    text_list = []
    for i in text:
        total = i.count("a") + i.count("e") + i.count("i") + i.count("o") + i.count("u")
        if total >= 2:
            text_list.append(i)
    if not text_list :
        print("Nope")
        return
    text_list.sort()
    for j in text_list:
        print(j)
main(input().replace(".", "").split())
