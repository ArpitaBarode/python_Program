#python script for factorial of number
print("FACTORIAL OF USER DEFINED NUMBER")
x=int(input("Enter the value:")) 
choice = x 
fact =1 
if x>0: 
 while x>0: 
    fact = fact * x 
    x=x-1 
 print("Factorial of {} is {}".format(choice,fact)) 
elif x<0: 
     print("Factorial of Negative Integer is Not Defined") 
elif x == 0: 
    print("Factorial of {} is {}".format(0,1)) 
else:
    print("Invalid Choice") 
