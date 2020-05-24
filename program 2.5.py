n,k=5,3
for i in range(1,4):
    n=n-1
    for j in range(1,n):
        if j--k:
            print(k)
        else:
            print(k,'*',end='')
    k=k-1
for i in range(1,4):
    for l in  range(1,4):
        if l==i:
            print(k)
            break
        else:
            print(k, '*', end='')
