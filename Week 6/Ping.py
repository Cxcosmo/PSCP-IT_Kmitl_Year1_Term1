"""Ping"""
def mx(ma_x,ms) :
    """max"""
    if ms > ma_x :
        return ms
    return ma_x

def mn(mi_n,ms) :
    """min"""
    if ms < mi_n :
        return ms
    return mi_n

def main() :
    """Ping"""
    lost = 0
    received = 4
    average = 0
    ma_x = 0
    mi_n = 999
    ip = ""
    for _ in range(3) :
        local = input()
        front = local.find("[")
        back = local.find("]")
        if front >= 0 :
            ip = local[front + 1:back]
        else :
            if local.find("ping") >= 0 :
                ip = local[local.find("ping") + 5 :]
    for _ in range(4) :
        status = input()
        c = status.find("Reply from ")
        if c >= 0 :
            tf = status.find("time=") + 5
            ms = status.find("ms")
            if tf >= 5 :
                average += int(status[tf:ms])
                ma_x = mx(ma_x,int(status[tf:ms]))
                mi_n = mn(mi_n,int(status[tf:ms]))
        else :
            lost += 1
            received -= 1
    if mi_n == 999 :
        mi_n = 0
    print(f"Ping statistics for {ip}:")
    print(f"    Packets: Sent = 4, Received = {received}, Lost = {lost} ({lost * 25}% loss),")
    if lost < 4 :
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {mi_n}ms, Maximum = {ma_x}ms, Average = {average // received}ms")
main()
