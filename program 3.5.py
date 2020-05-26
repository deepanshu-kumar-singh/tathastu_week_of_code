  
l1=[]
l3=[]
n=int(input("enter the limit"))
for i in range(0,n):
    items=int(input("enter the element:"))
    l1.append(items)
print(l1)
l2=[]
n=int(input("enter the limit"))
for i in range(0,n):
    items=int(input("enter the element:"))
    l2.append(items)
print(l2)
for i in l1:
    for j in l2:
        if(i==j):
            l3.append(j)
print("list of common elements is ",l3)
