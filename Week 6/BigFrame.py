"""BigFrame"""
def mx(x,y) :
    """max"""
    if x > y :
        return x
    return y

def main(t1,t2,t3,t4,t5) :
    """Frame"""
    mX = mx(len(t1),len(t2))
    mX = mx(mX,len(t3))
    mX = mx(mX,len(t4))
    mX = mx(mX,len(t5))
    print("*" * (mX + 4))
    print("* "+t1 + " " * (mX - len(t1)) +" *")
    print("* "+t2 + " " * (mX - len(t2)) +" *")
    print("* "+t3 + " " * (mX - len(t3)) +" *")
    print("* "+t4 + " " * (mX - len(t4)) +" *")
    print("* "+t5 + " " * (mX - len(t5)) +" *")
    print("*" * (mX + 4))
main(input().strip(" "),input().strip(" "),input().strip(" "),input().strip(" "),input().strip(" "))
