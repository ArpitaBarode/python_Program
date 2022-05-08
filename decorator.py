#dcorater
#def div(x,y):
    #return x/y
#from support import *
def smart_div(func):
    def inner(m,n):
        if m<n:
            m,n=n,m
        return func(m,n)
    return inner
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=div(a,b)
div=smart_div(div)
d=div(a,b)
print(a)
print(b)
print(c)    
            
