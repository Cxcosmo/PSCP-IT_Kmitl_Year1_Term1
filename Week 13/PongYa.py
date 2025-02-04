"""PongYa"""
def main(num) :
    """PongYa"""
    if not num % 3 or (str(num))[-1:] == "3" :
        print("PONG")
    else :
        print(num)
main(int(input()))
