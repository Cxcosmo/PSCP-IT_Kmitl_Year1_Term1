"""WordSequence II"""
def main(text1, text2) :
    """WordSequence II"""
    for i in range(max(len(text1), len(text2)) + 1) :
        print(text2[:i] + text1[i:])
main(input(), input())
