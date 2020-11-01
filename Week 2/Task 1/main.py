# WEEK_1 TASK_1

# FUNCTION_1


def my_function(data): # this is a parameter
    return type(data)


isRunning = True

print(my_function(78)) # this is an argument
print(my_function(isRunning))
print(my_function("Hello, my friend!"))


# FUNCTION_2


def another_function():
    firstname = "Yeehoo"

print(firstname)


another_function()

# the name variable is not available to use outside the function
# because locally created variables can be used within the parent functions only


# FUNCTION_3


def more_function(yeah):
    pass


more_function("Hello, dude!")

print(yeah)

# parameters of the functions can be used only within the function



# FUNCTION_4

lastname = "Yada"


def last_function():
    lastname = "Leela"
    print(lastname)


last_function()
print(lastname)

# value of the variable defined outside the function can be changed within the function.
# but globally set value will be kept outside of the function

