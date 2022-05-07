print("program script to find greater between three numbers")
a=input("plese enter first no:")
b=input("please enter second no:")
c=input("please enter third no:")

a=int(a)
b=int(b)
c=int(c)
if(a==b==c):
    print("all values are equal")
elif(a==b and a>c and b>c):
    print("a and b are equal and greater than c ")
elif(a==c and a>b and c>b):
    print("a and c are equal and greater than c")
elif(b==c and b>a and c>a):
    print("b and c are equal and greater than  a")
elif(a>b and a>c):
    print(a,"is greater than",b,"and",c)
elif(b>a and b>c):
    print(b,"is greater than ",a,"and",c)
else:
    print( c,"is greater than",a,"and",b)
    
