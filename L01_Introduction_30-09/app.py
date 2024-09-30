a = 5
print(a)

print(id(a)) # id(a) returns the memory address of a
b = 6

a= 4

print(id(a)) # now a references something else in memory --> some objects are immutable 
# once created won't change and a new object will be instead created, losing the old one 

print(a)

a = None

print(type(a))

# Tuples 
print((a, "4.2", 4, b, 5, 4))
