dna_string_1='GAGCCTACTAACGGGAT'
dna_string_2='CATCGTAATGACGGCCT'
def hamming_dist(string_1,string_2):
    sum=0
    for s1,s2 in zip(string_1,string_2):
        if s1 != s2:
           sum+=1
        else:
           sum+=0
    return print(sum)
hamming_dist(dna_string_1,dna_string_2)
           
           