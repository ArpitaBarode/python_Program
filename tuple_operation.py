# Different types of tuples

# Empty tuple
my_tuple1 = ()
print(my_tuple1)

# Tuple having integers
my_tuple2 = (1, 2, 3)
print(my_tuple2)

# tuple with mixed datatypes
my_tuple3 = (1, "Hello", 3.4)
print(my_tuple3)

# nested tuple
my_tuple4 = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple4)
my_tuple5 = ("hello")
print(type(my_tuple5))  # <class 'str'>

# Creating a tuple having one element
my_tuple6= ("hello",)
print(type(my_tuple6))  # <class 'tuple'>

# Parentheses is optional
my_tuple7= "hello",
print(type(my_tuple7))  # <class 'tuple'>
