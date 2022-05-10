 
# here a,b,c are 3 user defined integer 
a = int(input(" This program script is intended to predict the highest integer from three user  define intger" )) 
print("Welcome to my program ") 
print ("This program will provide the highest integer among three user defined  integer ") 
a=int(input("enter first integer:")) 
b = int(input("Enter second integer:")) 
c = int(input("Enter third integer:")) 
#Comparison

if a>b and a>c: 
 # print(a,"is greater than",b,",",c) 
 print("{} is geater than {},{}".format(a,b,c)) 
elif b>a and b>c: 
 #print(b,"is greater than",a,",",c) 
 print("{} is geater than {},{}".format(b,a,c)) 
else: 
 # 
 print(c,"is greater than",a,",",b) 
 print("{} is geater than {},{}".format(c,b,a)) 
