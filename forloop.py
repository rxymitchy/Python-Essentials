#for loops
print("This section uses for loops:")
numbers =[1, 2, 3, 4, 5]
print("For loops")
for item in numbers:#shorter listing method
    
    print(item)

#range in for loops
print("this section uses range:")
numbers = range(5, 10)
print(" numbers from 5 to 10")
for number in numbers:
    print(number)
print("Jumps two numbers from 5 to 10")
numbers = range(5, 10, 2)#Jumping 2 umbers
for number in numbers:
    print(number)
print("Dispalys from 0 to 4")
for number in range(5):
    print(number)

print("Using continue")
for i in range(5):
    if i == 3:
        continue
    print(i)
print("Using break")
for i in range(5):
    if i == 3:
        break
    print(i)