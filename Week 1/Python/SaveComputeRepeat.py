"""SaveComputeRepeat"""
def main():
    """SaveComputeRepeat"""
    start = 492137954293754252786
    ms = start
    s = ms // 1000
    ms = ms % 1000
    m = s // 60
    s = s % 60
    h = m // 60
    m = m % 60
    d = h // 24
    h = h % 24
    print(f"{d} {h} {m} {s} {ms}")
main()
