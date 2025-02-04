"""ฉันจะเป็น Saitama ให้ได้เลย"""
import math
def main(v,s,l,r) :
    """ฉันจะเป็น Saitama ให้ได้เลย"""
    cv = int(input())
    cs = int(input())
    cr = int(input())
    cl = int(input())
    v_cv = math.ceil(v / cv)
    s_cs = math.ceil(s / cs)
    l_cl = math.ceil(l / cl)
    r_cr = math.ceil(r / cr)
    if v_cv < s_cs :
        v_cv,s_cs = s_cs,v_cv
    if v_cv < l_cl :
        v_cv,l_cl = l_cl,v_cv
    if v_cv < r_cr :
        v_cv,r_cr = r_cr,v_cv
    print(v_cv)
main(int(input()),int(input()),int(input()),int(input()))
