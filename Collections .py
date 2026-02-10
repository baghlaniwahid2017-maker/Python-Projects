# Python Collections 

# Comprision Operations
#a = 10
#b = 20


#print(a == b)   # False
#print(a != b)   # True
#print(a > b)    # False
#print(a < b)    # True
#print(a >= 10)  # True
#print(b <= 20)  # True

#x = 20
#y = 40

#print(x == y)
#print (x != y)
#print( x > y)
#print (x < y)
#print (x >= 10)
#print (y >= 15)

# List Methods and Slicing 

# fruits = ["apple", "orange" , "banana"]
# print(fruits)
# print(type(fruits))

# we can use the Append(always at the end), insert (we can tell to add in specific place), and remove methods 

# fruits = ["apple", "orange" , "banana"]

# # fruits.append("strawberry")
# # fruits.insert(2,"mango")
# fruits.remove("banana")
# print(fruits)

# Slicing 
#print(fruits)
#print (fruits[:1])

# list comprehensive , identity and Membership
# first example 
#Squares = [x ** 2 for x in range (9)]
#print(Squares)
# Second Exampel 
#Squares = [x ** 2 for x in range (7)]
#print(Squares)

# Conditional list Comprehensive
# evens = [x for x in range (10) if x % 2 == 0]
# print ("evens")

#Identity Vs Equality 

a = [1, 2, 3]
b = a
c = [1, 2, 3]

# print(a == b)
# print (b == a)
# print (c == a)
# print (b == c)

print( a is c)
#print (a is b)
#print ( b is c)

# Membership

#print (2 in a)
#print ( 5 in b)
#print ( 2, b, a )

# print (a is c)
# print ( a == c)
# a. append(8)
# print(a)
# a.insert(3, 55)
# print(a)
