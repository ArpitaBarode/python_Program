# Accessing tuple elements using indexing
my_tuple = ('p','e','r','m','i','t')

print(my_tuple[0])  
print(my_tuple[5])

# IndexError: list index out of range
# print(my_tuple[6])

# Index must be an integer
# TypeError: list indices must be integers, not float
# my_tuple[2.0]

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])       
print(n_tuple[1][1])
# Accessing tuple elements using slicing

# elements 2nd to 4th

print(my_tuple[1:4])


# Output: ('p', 'r')
print(my_tuple[:-5])

# elements 5th to end

print(my_tuple[5:])

# elements beginning to end

print(my_tuple[:])
