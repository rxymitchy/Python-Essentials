# global_var is in the global namespace
global_var = 10

def outer_function():
    #  outer_var is in the local namespace 
    outer_var = 20

    def inner_function():
        #  inner_var is in the nested local namespace 
        inner_var = 30

        print(inner_var)

    print(outer_var)

    inner_function()

# print the value of the global variable
print(global_var)

# call the outer function and print local and nested local variables
outer_function()


# define global variable 
global_var = 10

def my_function():
    # define local variable
    local_var = 20

    # modify global variable value 
    global global_var
    global_var = 30

# print global variable value
print(global_var)

# call the function and modify the global variable
my_function()

# print the modified value of the global variable
print(global_var)