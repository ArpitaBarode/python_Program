#print("welcome to my calculator")
def addition(x,y):
    z=x+y
    return z
def subtraction(x,y):
    z=x-y
    return z
def multiplication(x,y):
    z=x*y
    return z
def division(x,y):
    z=x/y
    return z
def modulo(x,y):
    z=x%y
    return z
def p_square(x):
    n=int(input("enter power:"))
    z=x**n
    return z
def square(x):
    z=x*x
    return z
def cube(x):
    z=x*x*x
    return z
def square_root(x):
    z=x**(0.5)
    return z
def cube_root(x):
    z=x**(1/3)
    return z
#while true:
print("welcome to my calculator: ")
choice=str.lower(input("which type of operation unary or binary to perform"))
if(choice=='unary'):
       x=int(input("enter number:"))
if(choice=='binary'):       
       a=(input("enter which  value(int,float) you want to enter:"))
       if(a=='int'):
          x=int(input("enter first number"))
          y=int(input("enter second number"))
       elif(a=='float'):
           x=float(input("enter first number:"))
           y=float(input("enter second number:"))
       else:
           print("you enter wrong choice")
else:
    print("please enter binary or unary")

ope=input("please enter any operator to perform operation:")

if(ope=='+'):
    a=addition(x,y)
    print(x,"+",y,"=",a)
elif(ope=='-'):
    a=subtraction(x,y)
    print(x,"-",y,"=",a)
elif(ope=='/'):
    a=division(x,y)
    print(x,"/",y,"=",a)
elif(ope=='*'):
    a=multiplication(x,y)
    print(x,"*",y,"=",a)
elif(ope=='%'):
     a=modulo(x,y)
     print(x,"%",y,"=",a)
elif(ope=='p_sq'):
    a=p_square(x)
    print(x,"** =",a)
elif(ope=='sq'):
    a=square(x)
    print(x,"*",x,"=",a)
elif(ope=='cube'):
    a=cube(x)
    print(x,"*",x,"*",x,"=",a)
elif(ope=='sr'):
    a=square_root(x)
    print(x,"**0.5","=",a)
elif(ope=='cr'):
    a=cube_root(x)
    print(x,"**","=",a)
else:
    print("please enter arithmetic operator")
"""next_calculation=str.lower(input("please type yes to if you want to perform more operation:")
                           if(naxt_calculation=='yes')"""





