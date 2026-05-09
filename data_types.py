# int - integer

a = 10
print(type(a))  # <class 'int'>

b = -5
print(type(b))  # <class 'int'>

c = 'Gaurang'
print(type(c))  # <class 'str'>

d = 3.14
print(type(d))  # <class 'float'>

list_a = [1, 2, 3]
print(type(list_a))  # <class 'list'>

dict_a = {'a': 1, 'b': 2}
print(type(dict_a))  # <class 'dict'> or hashmap

tuple_a = (1, 2, 3)
print(type(tuple_a))  # <class 'tuple'>

set_a = {1, 2, 3}
print(type(set_a))  # <class 'set'>

# Strings and tupes are immutable, meaning their values cannot be changed after they are created. Lists and dictionaries are mutable, meaning their values can be changed after they are created.

# Indexing
# Indexing is the process of accessing individual elements of a data structure using their position. In Python, indexing starts at 0.

print(list_a[0])  # Output: 1
print(list_a[1])  # Output: 2
print(list_a[2])  # Output: 3

print(tuple_a[0])  # Output: 1
print(tuple_a[1])  # Output: 2
print(tuple_a[2])  # Output: 3

#0385fhwe
# |1| |2| |3|

print(dict_a['a'])  # Output: 1
print(dict_a['b'])  # Output: 2

# Big O Notation
# Big O notation is a way to describe the performance of an algorithm. It describes how the time or space complexity of an algorithm changes as the input size increases.

# List - O(n) for search, O(1) for access by index
# Dictionary - O(1) for search and access by key
# Set - O(1) for search and access by value