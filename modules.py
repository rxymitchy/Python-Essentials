#Modules - importing functions stored in another file
import converters
print("Importing the whole module: converters Example kg to lbs function is used")
print(converters.kg_to_lbs(70))

from converters import lbs_to_kg
print("importing specific funtion in the module: lbs to kg")
print(lbs_to_kg(500))


#simple calc
print("Sum: " + str(converters.add(10, 2)))

from converters import find_max
numbers = [3, 6, 2 ,8, 4, 10]
converters = find_max(numbers)#avoid using ax as it is an inbuilt function
print("The largest number in the list is:")
print(converters)


# import standard math module 
import math

# use math.pi to get value of pi
print("The value of pi is", math.pi)

#dir() list all funtions in a module

print("The functions in converters are: " + str(dir(converters)))
