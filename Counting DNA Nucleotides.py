string="ATGCTTCAGAAAGGTCTTACG"
nts=['A','T','G','C']
nts_counts=[]

def NTS_COUNTS(nts,string):
    for i in nts:
        nts_counts.append(string.count(i))
    return print(*nts_counts) 

NTS_COUNTS(nts,"AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
    
    
    
