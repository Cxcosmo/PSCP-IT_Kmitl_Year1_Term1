"""RemoveTag"""
def main():
    """RemoveTag"""
    line = input().split(">")
    r = []
    for l in line:
        spl = l.split("<")
        if not spl[0].strip():
            continue
        r.append(spl[0].strip())
    rr = []
    for l in r:
        for s in l.split(" "):
            if not s.strip():
                continue
            rr.append(s)
    print(rr)
main()
