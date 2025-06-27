"""SigmaStep"""
def main(x, y, z):
    """SigmaStep"""
    if x == y :
        print(x)
        return
    if not z or (x > y and z > 0) or (x < y and z < 0):
        print("error")
        return
    num = 0
    for i in range(x, y + z, z):
        num += i
    print(num)
main(int(input()), int(input()), int(input()))
