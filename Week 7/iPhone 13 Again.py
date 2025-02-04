"""iPhone 13 Again"""
def iphone13mini(gb) :
    """iphone13mini"""
    if gb == "128 GB" :
        print("25900")
    elif gb == "256 GB" :
        print("29900")
    elif gb == "512 GB" :
        print("37900")
    else :
        print("Not Available")

def iphone13(gb) :
    """iphone13"""
    if gb == "128 GB" :
        print("29900")
    elif gb == "256 GB" :
        print("33900")
    elif gb == "512 GB" :
        print("41900")
    else :
        print("Not Available")

def iphone13pro(gb) :
    """iphone13pro"""
    if gb == "128 GB" :
        print("38900")
    elif gb == "256 GB" :
        print("42900")
    elif gb == "512 GB" :
        print("50900")
    elif gb == "1 TB" :
        print("58900")
    else :
        print("Not Available")

def iphone13m(gb) :
    """iphone13pro"""
    if gb == "128 GB" :
        print("42900")
    elif gb == "256 GB" :
        print("46900")
    elif gb == "512 GB" :
        print("54900")
    elif gb == "1 TB" :
        print("62900")
    else :
        print("Not Available")

def main(tr,gb) :
    """Don't Use IOS"""
    if tr == "iPhone 13 mini" :
        iphone13mini(gb)
    elif tr == "iPhone 13" :
        iphone13(gb)
    elif tr == "iPhone 13 Pro" :
        iphone13pro(gb)
    elif tr == "iPhone 13 Pro Max" :
        iphone13m(gb)
    else :
        print("Not Available")
main(input(),input())
