#lists
print("This section uses lists")
names = ["John", "Jane", "Mitch", "Jace","Ren"]
print("First name:")
print(names[0])#first element in list
print("Last name:")
print(names[-1])#last element in list
print("Change spelling of John:")
names[0]= "Jon" #changes the spelling of John
print(names[0:3])#python excludes the last index
print(names[2:])#prints from Mitch

#list methods
print("This section uses list methods")
numbers =[1, 2, 3, 4, 5]
print(numbers)
numbers.insert(-1,6)
print("Insert 6:")
print(numbers)
numbers.remove(3)
print("Remove 3:")
print(numbers)
print("Search for 1:")
print(1 in numbers)#returns boolean
print("No of elements in list:")
print(len(numbers))#means length
numbers.clear()
print("Clear numbers:")
print(numbers)


#lists part 2
#2D lists- each item in the list is another list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Item in the first row, second column is:")
matrix[0][1] = 20#changes from 2 to 20
print(matrix[0][1])

matrix[0][1] = 20#changes from 2 to 20
print(matrix[0][1])


for row in matrix:
    for item in row:
        print(item)
