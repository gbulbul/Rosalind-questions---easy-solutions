dict_string={
'>Rosalind_0498':
'AAATAAA',
'>Rosalind_2391':
'AAATTTT',
'>Rosalind_2323':
'TTTTCCC',
'>Rosalind_0442':
'AAATCCC',
'>Rosalind_5013':
'GGGTGGG'}
dict_of_pairs_w_shared={}
for key1,value1 in dict_string.items():
    for key2,value2 in dict_string.items():
        if key1 != key2:
           shared=sum(c1 == c2 for c1, c2 in zip(value1, value2[::-1]))
           if (key2,key1) not in dict_of_pairs_w_shared.keys() and shared>=3:
               print((key1,key2))
               dict_of_pairs_w_shared[(key1,key2)]=shared
           else:
               continue
        else:
            continue

