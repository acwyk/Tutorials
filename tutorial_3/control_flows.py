# Importing a function from somewhere else. Don't worry, we'll cover this later.
# All that you need to know is we use randint to make a random number easily
from random import randint

# Generate a random number between 0 and 10
my_num = randint(0, 10)

# if/elif/else

# if my_num is between 0 and 4
if(my_num < 5):
    print("My number is less than 5")
elif(my_num == 5):
    print("My number is exactly 5")
else:
    print("My number is greater than 5")


# For loops

shopping_list = ["apples", "bananas", "bread", "milk"]

for item in shopping_list:
    print(item)


# While loops

miles_walked = 0

while(miles_walked < 5):
    print("I have walked " + miles_walked + " miles")

    # Careful! We don't want to loop forever!!!
    # To avoid infinite loops, we need to make sure we increment the number of miles walked!
    miles_walked = miles_walked + 1

# Do-While loop

# Python doen'st have a do-while loop, so we don't cover that.
# it's incredibly unlikely you'll ever need to use one, and if you do... rethink what you're trying to do!