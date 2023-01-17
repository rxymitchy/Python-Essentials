#while loops
print("This section uses while loops")
i = 1
while i <= 5:
    print(i)
    i = i + 1#ensures program terminsates and doesnt run forever
j = 1
print("Ateriks:")
while j <= 10:
    
    print(j * '*')#in python you can multiply a number with a string, the asteriks give the values of the number
    j = j + 1

i = 0
numbers =[1, 2, 3, 4, 5]
print("While loops")
while i < len(numbers):#longer listing method $ complex
   
    print(numbers[i])
    i = i + 1


# program to print odd numbers from 1 to 10
print("Using continue")
num = 0

while num < 10:
    num += 1
    
    if (num % 2) == 0:
        continue

    print(num)

# program to find first 5 multiples of 6
print("Using break")
i = 1

while (i<=10):
    print('6 * ',(i), '=',6 * i)

    if i >= 5:
        break
    
    i = i + 1