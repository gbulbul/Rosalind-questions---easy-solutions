dict_strings = {
    '>Rosalind_1': 'GATTACA',
    '>Rosalind_2': 'TAGACCA',
    '>Rosalind_3': 'ATACA'
}

values = list(dict_strings.values())
list_of_pairs = []

common_substrings = {}

for a in range(len(values)):
    for b in range(a+1,len(values)):
        value1=values[a]
        value2=values[b]
        pair=(value1,value2)
        
        for k in range(2, min(len(value1), len(value2)) + 1):

            for i in range(len(value1) - k + 1):

                for j in range(len(value2) - k + 1):
                    if value1[i:i+k] == value2[j:j+k]:

                        if pair not in list_of_pairs:
                            list_of_pairs.append(pair)
                            common_substrings[pair] = []

                        if value1[i:i+k] not in common_substrings[pair]:
                            common_substrings[pair].append(value1[i:i+k])

common_substrings.values()
for a in range(len(common_substrings)):
    for b in range(a+1,len(common_substrings)):
        for c in range(b+1,len(common_substrings)):
            value1=list(common_substrings.values())[a]
            value2=list(common_substrings.values())[b]
            value3=list(common_substrings.values())[c]
            common=set(value1) & set(value2) & set(value3) 
            print(*common)
    