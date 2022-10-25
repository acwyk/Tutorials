#The function takes no arguments
def my_function():
    names = ["Bob", "Alice"]
    
    for name in names:
        if (name == "alice"):
            print(name + " wants to send a message")
        else:
            print(name + " wants to receive a message")

# This is how you call a function with no arguments:
my_function()


# This function has arguments
def my_age_is(age):
    print("I am " + age + " years old")

# This is how you call a function with arguments:
my_age_is(5)