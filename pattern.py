("program to print pattern of number")
n=5
k=4
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end='')
    print()    
