dna_dict={
'>Rosalind_1':'ATCCAGCT',
'>Rosalind_2':'GGGCAACT',
'>Rosalind_3':'ATGGATCT',
'>Rosalind_4':'AAGCAACC',
'>Rosalind_5':'TTGGAACT',
'>Rosalind_6':'ATGCCATT',
'>Rosalind_7':'ATGGCACT'
}
from statistics import mode
profile_0,profile_1,profile_2,profile_3,profile_4,profile_5,profile_6,profile_7='','','','','','','','',''
for value in dna_dict.values():
    for i in enumerate(value):
        if i[0]==0:
           profile_0+=i[1]
        elif i[0]==1:
           profile_1+=i[1]
        elif i[0]==2:
           profile_2+=i[1]
        elif i[0]==3:
           profile_3+=i[1]
        elif i[0]==4:
           profile_4+=i[1]
        elif i[0]==5:
           profile_5+=i[1]
        elif i[0]==6:
            profile_6+=i[1]
        else:
            profile_7+=i[1]
list_profiles=[mode(profile_0),mode(profile_1),mode(profile_2),mode(profile_3),mode(profile_4),mode(profile_5),mode(profile_6),mode(profile_7)]
consensus='' 
for profiles in enumerate(list_profiles):
    consensus+=profiles[1]
print(consensus)

list_n_A,list_n_T, list_n_C,list_n_G=[],[],[],[]
for i in range(0,len(dna_dict),1):
    n_A, n_T, n_C, n_G = 0, 0, 0, 0
    for key, values in dna_dict.items():
        #print(values[i])
        if values[i] == 'A':
           n_A+=1
        elif values[i] == 'T':
            n_T+=1
        elif values[i] == 'C':
            n_C+=1
        else:
            n_G+=1
    list_n_A.append(n_A)
    #print(*list_n_A)
    list_n_T.append(n_T)
    #print(list_n_T)
    list_n_C.append(n_C)
    #print(list_n_C)
    list_n_G.append(n_G)
    #print(list_n_G)
print('A:',*list_n_A)
print('C:',*list_n_C)
print('G:',*list_n_G)
print('T:',*list_n_T)

    
        
       
  
    
       
    
       
    

        
        
        
           

            