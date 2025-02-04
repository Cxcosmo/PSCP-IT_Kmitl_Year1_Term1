"""CuteCat CuteFox"""
def main():
    """CuteCat CuteFox"""
    cat_fox = {"Fubuki":"Fox01", "Garfield":"Cat01"}
    cat = {}
    fox = {}
    for _ in range(int(input())) :
        cf = input()
        cat_fox[cf[2:cf.find(":") - 2]] = cf[cf.find(":") + 3:-2]
    for j in cat_fox :

    cat_fox = {v:k for k,v in cat_fox.items()}
    sort_list = sorted(cat_fox.keys())
    cat_fox = {v:k for k,v in cat_fox.items()}
    print(f"Cat : {(" ".join(sort_list)).count("Cat"# This part of the code is responsible for
    # printing the count of how many times the words
    # "Cat" and "Fox" appear in the sorted list of
    # values from the `cat_fox` dictionary.
    )}")
    print(f"Fox : {(" ".join(sort_list)).count("Fox")}")
main()
