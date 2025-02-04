"""Books"""
import math
def main(n, k, x, y) :
    """book"""
    count = 0
    a = 0
    m = k
    while n > 0 :
        m -= math.ceil(((x + a) / (y + a)) * k)
        if math.ceil(((x + a) / (y + a)) * k) >= k :
            break
        count += 1
        if m <= 0 :
            n -= 1
            m = k
            a += 1
        else :
            a += 1
    if n > 0 :
        count += n
    print(count)
main(int(input()), int(input()), int(input()), int(input()))
