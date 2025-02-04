"""Lotto"""
def prize1(p1) :
    """prize"""
    if p1 == "000000" :
        return "999999","000001"
    if p1 == "999999" :
        return "999998","000000"
    return f"{str(int(p1) - 1):>06}",f"{str(int(p1) + 1):>06}"

def main(p1,pb2,pf31,pf32,pb31) :
    """lost your money"""
    pb32 = input()
    mb = input()
    p1n1,p1n2 = prize1(p1)
    gm = 0
    if mb == p1 :
        gm += 6000000
    if mb[4:] == pb2 :
        gm += 2000
    if mb[:3] in pf31 :
        gm += 4000
    if mb[:3] in pf32 :
        gm += 4000
    if mb[3:] in pb31 :
        gm += 4000
    if mb[3:] in pb32 :
        gm += 4000
    if mb in (p1n1,p1n2) :
        gm += 100000
    print(gm)
main(input(),input(),input(),input(),input())
