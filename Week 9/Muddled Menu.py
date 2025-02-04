"""Muddled Menu"""
def main() :
    """Muddled Menu"""
    menu_list = []
    while True :
        menu = input()
        if menu == "DONE" :
            break
        if menu == "CLOSED" :
            print("Full Course: [] Reversed: []")
            return
        if menu.find("Can't do:") != -1 :
            menu_list.remove(menu[menu.find(":") + 2:])
        elif menu == "SOMETHING'S WRONG" :
            menu_list.clear()
        else :
            menu_info = menu.split(" #")
            if menu_info[1].isnumeric():
                menu_list.insert(int(menu_info[1])-1, menu_info[0])
            else:
                menu_list.append(menu_info[0])
    print(f"Full Course: {menu_list}", end = " ")
    menu_list.reverse()
    print(f"Reversed: {menu_list}")
main()
