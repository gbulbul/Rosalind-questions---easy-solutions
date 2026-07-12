dna="AAAACCCGGT"
def reversed(dna):
    reversed_dna=dna[::-1]
    return reversed_dna
reversed_dna=reversed(dna)
complements= str.maketrans({"A": "T", "T": "A", "C": "G", "G": "C"})
def complement(reversed_dna,complements):
    complement_reversed_dna=reversed_dna.translate(complements)
    return complement_reversed_dna
complement_reversed_dna=complement(reversed_dna,complements)
print(complement_reversed_dna)

    

