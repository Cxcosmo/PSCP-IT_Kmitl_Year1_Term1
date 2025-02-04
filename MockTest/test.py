"""Stamps"""
def main(count, pro, stamp, use, sale, have_stamp, total) :
    """Stamps"""
    for _ in range(count) :
        cost = int(input())
        while cost > 0 and have_stamp >= use :
            have_stamp -= use
            cost = max(cost - sale, 0)
        total += cost
        have_stamp += stamp * (cost // pro)
    print(total)
    print(have_stamp)
main(int(input()), int(input()), int(input()), int(input()), int(input()), 0, 0)
