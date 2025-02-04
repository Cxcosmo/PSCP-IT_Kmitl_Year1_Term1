"""Heads and Legs"""
def main(head, leg) :
    """Heads and Legs"""
    rabbit = (leg // 2) - head
    bird = head - rabbit
    if (rabbit * 4) + (bird * 2) != leg or rabbit < 0 or bird < 0 :
        print("Impossible")
        return
    print(f"{rabbit} {bird}")
main(int(input()), int(input()))
