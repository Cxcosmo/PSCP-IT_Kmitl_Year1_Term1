"""BTSMRT"""
def main(day,old,high) :
    """Day"""
    if day == "Children Day" and old < 14 and high <= 140 :
        print("FREE")
    elif old < 14 and high < 90 :
        print("FREE")
    elif day == "Senior Day" and old >= 60 :
        print("FREE")
    else :
        print("PAY")
main(input(),float(input()),float(input()))
