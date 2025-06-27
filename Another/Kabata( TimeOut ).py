"""Kabata"""
def main() :
    """Kabata"""
    for _ in range(int(input())) :
        kabata = input()
        pre = kabata[0:2]
        mem = True
        a = 0
        for i in range(0, len(kabata), 2) :
            cur =  kabata[i + a : i + 2 + a]
            if not cur :
                break
            if (not cur in ("ta", "ka", "ba", "kk")) or (pre in ("ta", "ka") and not cur in ("ta", "ka", "ba")) :
                print("no")
                mem = False
                break
            if pre == "ba" and cur == "ka" :
                print("no")
                mem = False
                break
            if cur == "kk" :
                a += 1
                cur = kabata[i + a : i + 2 + a]
            pre = cur
        if mem :
            print("yes")
        mem = True
main()
