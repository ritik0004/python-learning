#Python Functions

# Part 1: Function Definition and Calling

# for i in range(10):
#     print(40*i)

# def print_multiples(n):
#     for i in range(10):
#         print(n*i)

# print_multiples(5)
# print_multiples(7)

# Sytax of function definition:

#```python
#def function_name(parameters):
#    # function body
#    return value          
#```

# Example:
# Function to calculate the square of a number  
def square(num):
    num = num ** 2
    return num

print(square(5))

# Part 2: Function Parameters and Arguments

# Example:
def greet(name):
    return f"Hello, {name}!"    

print(greet("Gaurang"))

# Part 3: Return Values from Functions  
# Example:
def add(a, b):
    return a + b        

result = add(3, 5)
print(result)

# Part 4: Function Scope and Local Variables
# Example:
def outer_function():       
    outer_var = "I am outside!"  # This variable is in the scope of outer_function

    def inner_function():
        inner_var = "I am inside!"  # This variable is in the scope of inner_function
        outer_var = "I am modified in inner_function!"  # Modifying outer_var in inner_function
        print(outer_var)  # Accessing outer_var from inner_function
        print(inner_var)  # Accessing inner_var from inner_function

    inner_function()
    # print(inner_var)  # This will raise an error because inner_var is not in the scope of outer_function


outer_function()

# Part 5: Function Arguments and Default Values

# Example:
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"       

print(greet("Gaurang"))  # Using default greeting
print(greet("Gaurang", "Hi"))  # Providing a custom greeting

