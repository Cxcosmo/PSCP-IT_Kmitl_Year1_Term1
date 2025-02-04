"""Stuttering"""
def main(text) :
    """Stuttering"""
    new_text = ""
    c = ""
    for i in text :
        if i != c :
            new_text += i + " "
        c = i
    print(new_text.strip())
main(input().split())
