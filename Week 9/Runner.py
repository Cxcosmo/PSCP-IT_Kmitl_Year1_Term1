"""Runner"""
def main(s) :
    """Runner"""
    time = 0
    v = 0
    fasted = 1
    for i in range(int(input())) :
        run = input().split()
        if not i :
            time = (s - int(run[1])) / int(run[0])
            v = int(run[0])
            fasted = 1
        if time > (s - int(run[1])) / int(run[0]) :
            time = (s - int(run[1])) / int(run[0])
            fasted = i + 1
            v = int(run[0])
        elif time == (s - int(run[1])) / int(run[0]) and v < int(run[0]) :
            time = (s - int(run[1])) / int(run[0])
            fasted = i + 1
            v = int(run[0])
    print(fasted)
main(int(input()))
