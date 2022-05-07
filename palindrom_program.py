#palindrom program
#palindrom ex-121
"""
str1=input("enter any word:")
if(str1==str1[::-1]):
   print("the string is palindrom")
else:
    print("string is not palindrom")
    """
#method2
num=int(input("enter a number:"))
temp=num
rev=0
while(num>0):
 dig=num%10
 rev=rev*10+dig
 num=num//10
if(temp==rev):
    print("palindrome number")
else:
    print("not palindrome ")
