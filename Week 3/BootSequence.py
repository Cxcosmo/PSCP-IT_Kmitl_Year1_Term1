"""BootSequence"""
def main() :
    """main"""
    x = ""
    for i in range(1, int(input()) + 1) :
        x += str(i) + "_"
    print(x.strip("_"))
main()
