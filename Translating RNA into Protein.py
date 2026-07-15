mRNA_string='AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
alphabet={

'A': ['GCU', 'GCC', 'GCA', 'GCG'],
'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
'N': ['AAU', 'AAC'],
'D': ['GAU', 'GAC'],
'C': ['UGU', 'UGC'],
'E': ['GAA', 'GAG'],
'Q': ['CAA', 'CAG'],
'G': ['GGU', 'GGC', 'GGA', 'GGG'],
'H': ['CAU', 'CAC'],
'I':['AUU', 'AUC', 'AUA'],
'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
'K': ['AAA', 'AAG'],
'M': ['AUG'], 
'F': ['UUU', 'UUC'],
'P': ['CCU', 'CCC', 'CCA', 'CCG'],
'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU',' AGC'],
'T': ['ACU', 'ACC', 'ACA', 'ACG'],
'W': ['UGG'],
'Y': ['UAU', 'UAC'],
'V': ['GUU', 'GUC', 'GUA', 'GUG']}
def codons(rna_string):
    aa=''
    for i in range(0, len(rna_string), 3):
        for key,values in alphabet.items():
            if rna_string[i:i+3] in values:
               aa+=key
    return print(aa)
codons(mRNA_string)