"""100 meters"""
def check_run(time1,time2,time3,gold,silver,bronze):
    """Check"""
    if time3 < time2 :
        time2,time3 = time3,time2
        bronze,silver = silver,bronze
    if time2 < time1 :
        time1,time2 = time2,time1
        gold,silver = silver,gold
    if time3 < time2 :
        time2,time3 = time3,time2
        bronze,silver = silver,bronze
    return time1, time2, time3, gold, silver, bronze
def main() :
    """Run"""
    time1,time2,time3,gold,silver,bronze = check_run(float(input()),
                                                     float(input()),float(input()),1,2,3)
    for i in range(4, 9) :
        time4 = float(input())
        if time4 < time3 :
            time3 = time4
            bronze = i
        time1,time2,time3,gold,silver,bronze = check_run(time1,time2,time3,gold,silver,bronze)
    print(f"{gold} {silver} {bronze}")
main()
