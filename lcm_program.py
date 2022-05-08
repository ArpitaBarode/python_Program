#find lcm of two numbers
def cal_lcm(x,y):
    if(x>y):
        greater=x
    else:
         greater=y
    while(True):
         if(greater%x==0 and greater%y==0):
             lcm=greater
             break
         greater=greater+1
    return lcm    
def user_input():
    x=int(input("enter first value:"))
    y=int(input("enter second value:"))
    return (x,y)
x,y=user_input()
print("lcm of the numbers is:",cal_lcm(x,y))
