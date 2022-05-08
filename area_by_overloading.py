#area by overloading
class A:
    def area(self,r=None,l=None):
        ar=0
        if(r!=None and l==None):
            ar=22/7*r*r
        elif(l!=None and r!=None):
            ar=l*r
        else:
            ar="no value provided"
        return ar
s1=A()
a=s1.area()
print(a)
c=s1.area(2,3)
print("area of rectangle",c)

b=s1.area(2)
print("area of circle is",b)

