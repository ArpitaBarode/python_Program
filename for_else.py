#prime no by for else
a=int(input("enter a no:"))
for i in range(2,a-1):
    if(a%i==0):
     print("not prime")
    break
else:
    print("prime no.")
 
