# Functions
A function is a way to group code together to achive an objective. 

An example could be a function that converts Fahrenheit to Celsius as we'll see below.

Functions can require arguments (parameters) or nothing at all.  

## Functions without arguments

This is what a function looks like that requires no arguments:

```python
def say_hello_world():
    print("Hello, World!")

say_hello_world()
```

A function that has no arguments can be called by typing out the function's name followed by an opening and closing parentheses.

A function like the one avove is returning `void` as in it does not return any value once it's completed running.


## Functions with arguments

This is what a function looks like in Python:
```python
def convert_Fahrenheit_to_Celsius(temp_in_Fahrenheit):
    temp_in_C = (temp_in_Fahrenheit - 32) * (5/9)
    return temp_in_c
```

The above example function `convert_Fahrenheit_to_Celsius` takes in an argument/parameter `temp_in_Fahrenheit`. A function paremeter is an input to the function that it needs. Usually, a function parameter is going to be used in the function. We also see that we're using our parameter `temp_in_Fahrenheit` as a variable in our conversion equation. The last past of the function is the `return` keyword. The `return` keyword sends back something to the code that called our function.

This is what it would look like with calling code:

```python
def convert_Fahrenheit_to_Celsius(temp_in_Fahrenheit):
    temp_in_C = (temp_in_Fahrenheit - 32) * (5/9)
    return temp_in_c

converted_temp = convert_Fahrenheit_to_Celsius(104)

print("It is " + converted_temp + "°C)

# Output would be :
# It is 40°C
```

## Function return types
def convert_Fahrenheit_to_Celsius(temp_in_Fahrenheit):
A function can either return a value or `void` If a function returns void, it doesn't return anything when it's finished running. If a function has a `return` keyword, it is returning that value to the code that's called it. We can see how the `return` keyword works in our example above with the `convert_Fahrenheit_to_Celsius` function.