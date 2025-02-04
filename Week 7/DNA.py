"""DNA"""
def main(dna1, dna2, long_dna) :
    """DNA"""
    for x in dna2 :
        if not x in "ACGT" :
            print("Error")
            return
    for i in range (len(dna1)) :
        dna_check = ""
        for j in range (i, len(dna1)) :
            if not dna1[j] in "ACGT" :
                print("Error")
                return
            dna_check += dna1[j]
            if dna2.find(dna_check) != -1 and len(dna_check) > len(long_dna) :
                long_dna = dna_check
    if not long_dna :
        print("None")
    else :
        print(long_dna)
main(input(), input(), "")
