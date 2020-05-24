#1)wap to check whether number is even or not.
n=int(input("enter a number to check even or odd"))
if (n%2==0):
    print("yes it is an  even number")
else:
    print("no its an odd number")
#2) wap to check whether number is prime or not.
n=int(input("enter a number to check whether prime or not"))
for i in range(2,n):
    if (n%i==0):
        print("no its not a prime number")
        break
    else:
        print("its a prime number")
        break
#3) wap to check whether number is palindrome or not. 
n=int(input("enter a number to check whether it is palindrome or not"))
temp=n
rev=0
while(n!=0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(rev==temp):
    print("yes its a palindrome number")
else:
    print("better luck next time its not an palindrome number")
#4) wap to check whether number is armstrong or not.
n=int(input("enter a number to check whether it is armstrong or not"))
temp=n
new_number=0
sum=0
while(temp>0):
    dig=temp%10
    new_number=dig**3
    sum=sum+new_number
    temp//=10
if(sum==n):
    print("yes its an armstrong number")
else:
    print("better luck next time its not an armstrong number")

