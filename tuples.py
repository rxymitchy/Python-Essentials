
#TUPLES, cannot be changed once created
print("This section uses tuples,  cannot be changed once created, parenthesis defines tuples")
this_is_an_example_tuple =(1, 2, 3, 3)#parenthesis defines tuples, brackets define list
y = this_is_an_example_tuple.count(3)#occurences of 3 in the list
print("occurences of 3:")
print(y)
x = this_is_an_example_tuple.index(1)#returns index of first element
print("returns index of first element:")
print(x)

a = {}#dictionaries
b =()#tuple
c= []#lists

c.insert(0,"mitchele")
print(c)
c.append("Jane")
print(c)
print(c[0])

#Unpacking
coordinates = (1, 2, 3)
x, y, z = coordinates #assigns items to tuple according to place values
print("Unpacking items as follows: x, y, z")
print(x)
print(y)
print(z)