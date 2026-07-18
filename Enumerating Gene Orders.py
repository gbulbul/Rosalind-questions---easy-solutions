n=3

def perms_t(n):
    triples=[]
    for i in range(1,n+1):
        for k in range(1,n+1):
            for j in range(1,n+1):
                if (i,k,j) not in triples and i !=j and i!=k and k!=j:
                    triples.append((i,k,j))
    return triples
perms=perms_t(n)
print(len(perms))
for (i,j,k) in perms:
    print(*(i,j,k))






            