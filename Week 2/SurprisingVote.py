"""SurprisingVote"""
S = float(input())
Mx = float(input())
if Mx - ((S - Mx) // 2) >= 2 :
    a = [Mx, S % Mx, S - (S % Mx)]
    if max(a) - min(a) >= 2 :
        print("Surprising")
    else :
        print("Not surprising")
else :
    print("Not surprising")
