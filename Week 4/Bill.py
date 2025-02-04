"""Bill"""
def main(bill) :
    """bill"""
    service = bill * 0.10
    if service < 50 :
        bill += 50
    elif service > 1000 :
        bill += 1000
    else :
        bill += service
    cost = bill * 1.07 #bill + VAT
    print(f"{cost:.2f}")
main(int(input()))
