#filehandling
def fact(x):
    fact=1
    if x==1 or x==0:
        return 1
    else:
        for i in range(1,x+1):
            fact=fact*i
        return fact
#user_input=13
for i in range(5,11):
    y=fact(i)
    print(i,y)
#y=fact(user_input)
#print(user_input,y) 
z="factorial of" +str(i)+" is"+str(y)
 
#z="factorial of" +str(user_input)+" is"+str(y)


#f=open("sample.txt","w")
f=open("sample.txt","a")
f.write(z)
f.write("\n")
#f.write("++++++++")
f.close()
f=open("sample.txt","r")
a=f.read()
print("this is read operation")
print(a)
dataline=a.split("\n")
#b=f.read("\n")
print(dataline)
dataline.pop()
print(dataline)


f.close()
      
        
