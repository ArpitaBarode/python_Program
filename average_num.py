print("python script to find average of number:)")
n=int(input("enter number:"))
sum=0
for num in range(1,n+1,1):
    sum=sum+num
print("sum of first",n,"number is:",sum)
average=sum/n
print("average of",n,"number is:",average)
