number = (int(input("Number: ")))

# check if number is greater than 0
if number > 0:
    if number ==0:
        print("Number is 0")
    else:
        print("Number is positive")
else:
    print("Number is negative")

print('The if statement is easy')

#If statements
print("If Else Statements")
temperature = float(input("Enter Temperature:"))
if temperature > 30:#executed if true, 
    print("It's a hot day")
    print("Drink plenty pf water")#uses indentstion to show block of code
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print("done")#not part of the if else chain
weight=float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight/0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " +str(converted))

n = 10

# use pass inside if statement if no info is inside yet
if n > 10:
    pass

print('Goodbye')