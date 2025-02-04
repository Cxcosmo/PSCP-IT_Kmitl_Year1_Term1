"""Digital"""
def main(name, thai, house, age, year, money):
    """Ja dai jin mai"""
    cor = 0
    if thai in ("Yes", "True") :
        cor += 1
    if house in ("Yes", "True") :
        cor += 1
    if age >= 16 and money <= 500000 :
        cor += 1
    if money <= 500000 :
        cor += 1
    if year <= 840000 :
        cor += 1
    if cor == 5 :
        print(f"Congratulations! {name} is qualified to receive a digital \
wallet amount of 10,000 baht, sponsored by all taxpayers in Thailand.")
    else :
        print(f"Unfortunately, {name} is not qualified.")
main(input(), input(), input(), float(input()), float(input()), float(input()))
