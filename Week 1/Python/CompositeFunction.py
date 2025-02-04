"""CompositeFunction"""
def f(x) :
    """F"""
    return 2 * x
def g(x) :
    """G"""
    return (x / 2) + 1
def main(x = float(input())):
    """main"""
    print(f"{f(g(x)):.2f}")
    print(f"{g(f(x)):.2f}")
main()
