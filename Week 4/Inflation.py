"""Inflation"""
def main(n,k):
    """main"""
    for _ in range(k) :
        n += n * 381 // 10000
        print(n)
    if not n :
        print("0.00")
    else :
        print(f"{str(n)[0 : len(str(n)) - 2]}.{int(str(n)[len(str(n)) - 2 : len(str(n))]):02}")
main(int(float(input()) * 100),int(input()))
