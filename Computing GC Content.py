dna_string='AGCTATAG'
def GC_content(dna_string):
    G_count,C_count,A_count,T_count=dna_string.count('G'),dna_string.count('C'),dna_string.count('A'),dna_string.count('T')
    gc_content_=(G_count+C_count)/(G_count+C_count+A_count+T_count)*100
    return round(gc_content_,6)

print(GC_content(dna_string),'%')

dict_of_strings={
'>Rosalind_6404':
'CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG',
'>Rosalind_5959':
'CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC',
'>Rosalind_0808' :'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'}
    
list_of_gc_contents=[]
for value in dict_of_strings.values():
    list_of_gc_contents.append(GC_content(value))
max_index=list_of_gc_contents.index(max(list_of_gc_contents))
max_gc_content_=list_of_gc_contents[max_index]
key= list(dict_of_strings.keys())[max_index]
print(key)
print(max_gc_content_)
    
    