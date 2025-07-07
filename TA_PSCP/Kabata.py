"""Kabata"""
def main() :
    """Kabata"""
    for _ in range(int(input())) :
        kabata = input()
        if "baka" in kabata :
            print("no")
            continue
        kabata = kabata.replace("bakka", "")
        kabata = kabata.replace("ta", "").replace("ka", "").replace("ba", "")
        if not kabata :
            print("yes")
            continue
        print("no")
main()
