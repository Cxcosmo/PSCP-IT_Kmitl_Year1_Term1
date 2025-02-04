"""Saint_Seiya"""
def main(time, lim) :
    """Saint_Seiya"""
    count = 0
    for i in range(1,time+1):
        if count >= lim :
            break
        if not i % 6 :
            count += 1
        elif not i % 2 :
            count += 165
    time -= i
    count += time * 12
    print(count)
main(int(input()), int(input()))
