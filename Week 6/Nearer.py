"""Nearer"""
def main(alice,bob,ice) :
    """I scream for Icecreammmmm"""
    alice_len = abs(ice - alice)
    bob_len = abs(ice - bob)
    if alice_len < bob_len :
        print(f"Alice {alice_len}")
    elif alice_len > bob_len :
        print(f"Bob {bob_len}")
    else :
        print(f"Sundaes {alice_len}")
main(int(input()),int(input()),int(input()))
