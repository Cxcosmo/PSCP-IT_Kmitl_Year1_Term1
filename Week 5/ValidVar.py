"""ValidVar"""
def main(n) :
    """Val"""
    rw = ["if", "else", "elif", "while", "for", "True", "False",
           "continue", "break", "return", "is", "in", "and", "or", 
           "from", "as", "pass", "not", "def", "None"]
    ans = ""
    for _ in range(n) :
        val = input()
        err = 0
        if val[0].isnumeric() :
            err += 1
        if val in rw :
            err += 1
        val = val.strip(" ")
        for i in val :
            if i.isspace() :
                err += 1
            elif not i.isalpha() and not i.isnumeric() :
                err += 1
            if i == "_" :
                err -= 1
        if not err :
            ans += "Valid "
        else :
            ans += "Invalid "
    ans = ans.split(" ")
    for j in ans :
        if j :
            print(j)
main(int(input()))
