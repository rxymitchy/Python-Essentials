print("Implicit type casting")
print("Coverting integer to float")
integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

print("Value" , new_number)
print("Data Type:" , type(new_number))

print("Explicit type casting")#uses inbuilt functions
num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:" , type(num_string))

num_string = int(num_string)

print("Data type of num_string after Type Casting:" , type(num_string))

num_sum = num_string + num_integer
print("(Sum:" , num_sum)
print("Data type of num_sum:",type(num_sum))