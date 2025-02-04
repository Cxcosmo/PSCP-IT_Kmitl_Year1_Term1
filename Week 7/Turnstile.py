"""Turnstile"""
def main() :
    """CP"""
    save_action = ""
    count = 0
    while True :
        action = input()
        if action == "END" :
            break
        if action == "C" :
            save_action = "C"
        if save_action == "C" and action == "P" :
            count += 1
            save_action = ""
    print(count)
main()
