print('This secion is for operators, between 10 and 3')
print(10+3)#addition
print(10-3)#subtration
print(10*3)#multiplication
print(10/3)#division(single slash, returns float
print(10//3)#division double slash, returrns integer
print(10%3)#modulus, returns remainder
print(10**3) #exponential, power(multiplies 10, 3times)
#augmented assignment operator
print('This secion is for augmented assignment operators, 20 & 3')
x = 20
#x = x + 3
x += 3 #augmented assignment operator
print(x)
x //= 3
print(x)
x %= 3
print(x)
#Operator precedence in python
x= 10 + (3 * 2)
print(x)
x = (10 + 3)* 2
print(x)
#Comparison operator
print('This secion is for comparison operators between 3 and 2')
print('Equal:')
x = 3 ==2
print(x)#returns boolean, either true or false
print('Not Equal:')
x = 3 !=2
print(x)
print('Greater, Equal:')
x = 3 >=2
print(x)
print('Less , Equal:')
x = 3 <=2
print(x)
print('Greater:')
x = 3 >2
print(x)
print('ELess than:')
x = 3 <2
print(x)

#Logical Operators
print('This secion is for logical operators , price is 25 & 5')
price = 25
print('And:')
print(price > 10 and price < 30) #returns true if both are correct
price = 5
print('or:')
print(price > 10 or price < 30) #returns true if at least one is correct
print('And:')
print(price > 10 and price < 30) #returns true if both are correct
price = 5
print('Not:')
print(not price >10) #disagrees with our statement, will return true since we disagree