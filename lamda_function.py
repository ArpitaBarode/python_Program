#lambda function-annonums function
"""def even(n):
    return n%2==0
list1=[2,3,46,78,90,451]
list_even=list(filter(even,list1))
print(list1,list_even)"""
#by lambda function
"""def even(n):
    return n%2==0
list1=[2,3,46,78,90,451]
list_even=list(filter(lambda x:x%2==0,list1))
print(list1,list_even)"""
#by fuilter
from functools import reduce
list1=[2,3,46,78,90,451]
list_even=list(filter(lambda x:x%2==0,list1))
list_odd=list(filter(lambda x:x%2!=0,list1))


print(list1,list_even,list_odd)
list_even2=list(map(lambda x:x*2,list_even))
print(list_even2)
sum=reduce(lambda x,y:x+y,list_even2)
print(sum)


