"""Heron of Alexandria"""
def main(a, b, c) :
    """abc"""
    s = (a + b + c) / 2
    ans = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f"{ans:.3f}")
main(float(input()), float(input()), float(input()))
