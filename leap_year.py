print("leap year program")
a=int(input("please enter a number:"))
print(a)

if (a%4==0):
   print("leap year")
elif(a%4==0 and a%100==0):
   print("not a leap year")
elif(a%4==0 and a%100==0 and a%400==0):
   print("leap year")
else:
    print("it is not a leap year")
