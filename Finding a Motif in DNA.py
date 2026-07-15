string_1='GATATATGCATATACTT'
string_2='ATAT'
def sub_locations(string1, string2):
    loc = []
    for i in range(len(string1) - len(string2) + 1):
        if string2 == string1[i:i + len(string2)]:
            loc.append(i + 1)
    return loc
print(sub_locations(string_1, string_2))
        
       