"""Parallelogram"""
def main():
    """Restauraunt"""
    word = input()
    num = len(word)
    for i in range(1,num + 1):
        when = 0
        for j in range(1,num + 1):
            if j <= num - i:
                print(" ", end = "")
            else:
                print(word[when],end = "")
                when += 1
        print()
    for i in range(1,num):
        when = i
        for j in range(1,num + 1):
            if j <= num - i:
                print(word[when], end = "")
                when += 1
        print()
main()
