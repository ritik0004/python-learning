# Python Control Flow

# Control flow is the order in which the code is executed. In Python, we have several control flow statements that allow us to control the flow of our program.

# If statement
# The if statement is used to execute a block of code if a condition is true.

x = 10
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5

# If-else statement
# The if-else statement is used to execute a block of code if a condition is true, and another block of code if the condition is false.

y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")  # Output: y is not greater than 5

# Elif statement
# The elif statement is used to check multiple conditions.
z = 8
if z < 5:
    print("z is less than 5")
elif z == 5:
    print("z is equal to 5")
else:
    print("z is not less than 5")  # Output: z is not less than 5

# For loop
# The for loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable object.

# Iterator is an object that can be iterated upon, meaning that you can traverse through all the values. An iterable is an object that can return an iterator.

fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# Range function
# The range function is used to generate a sequence of numbers. It can take one, two, or three arguments.

for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# Len function
# The len function is used to get the length of a sequence or collection.

print(len(fruits))  # Output: 3

# Loop with index
# The enumerate function is used to get the index and value of each item in a sequence.

for i in range(len(fruits)):
    print(i, fruits[i]) # Output: 0 apple, 1 banana, 2 cherry

# While loop
# The while loop is used to execute a block of code as long as a condition is true.

count = 0
while count < 5:
    print(count)  # Output: 0, 1, 2, 3, 4
    count += 1

