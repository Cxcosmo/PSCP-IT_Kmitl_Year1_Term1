"""Volleyball"""
def r_one_to_five(s, r) :
    """r"""
    a = 0
    b = 0
    err = 0
    c = ""
    w = "c"
    for i in s :
        if not err :
            if i == "A" :
                a += 1
            else :
                b += 1
            if r < 5 :
                if a >= 25 and a - b >= 2 :
                    w = "a"
                    err += 1
                elif b >= 25 and b - a >= 2 :
                    w = "b"
                    err += 1
            else :
                if a >= 15 and a - b >= 2 :
                    w = "a"
                    err += 1
                elif b >= 15 and b - a >= 2 :
                    w = "b"
                    err += 1
            c += ""
        else :
            c += i
    return c, w, f"Set {r}: A ({a}) | B ({b})"

def main(s) :
    """Volleyball"""
    a_win = 0
    b_win = 0
    j = 0
    for i in range(1,6) :
        len_s = len(s)
        if not len_s or a_win == 3 or b_win == 3 :
            break
        s, w, re = r_one_to_five(s, i)
        print(re)
        if w == "a" :
            a_win += 1
        elif w == "b" :
            b_win += 1
        j = i
    if j == 5 or a_win == 3 or b_win == 3 :
        if a_win > b_win :
            print(f"A won {a_win}:{b_win} set")
        elif a_win < b_win :
            print(f"B won {b_win}:{a_win} set")
        else :
            print("The game has not finished yet.")
    else :
        if a_win + b_win == j :
            print(f"Set {i}: A (0) | B (0)")
        print("The game has not finished yet.")
main(input())
