"""Number Message"""
def main(text):
    """Number Message"""
    t = ""
    text = text.replace("13", "B").replace("12", "R").replace("1", "I").replace("3", "E")
    text = text.replace("4", "A").replace("5", "S").replace("0", "O")
    for i in text :
        if i.isalpha() or i.isspace() :
            t += i
    print(t.upper())
main(input())
