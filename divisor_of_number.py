#create a program tghat asks the uswr for a number and then prints out a list of all the divisors of that number
num=int(input("enetr any number:"))
for i in range(1,num+1):
    if(num%i==0):
        print(i)
