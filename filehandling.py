#filehandling

f=open("myfirstfile.txt",'w')
x="hello"
f.write(x)
y="india"
f.write("\n")
f.write(y)
f.close()
#reading
f=open("myfirstfile.txt",'r')
x=f.read()
y=f.read()
print(x)
f.close()
