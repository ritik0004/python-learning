
# Part 1: Identify Data Types

## Q1. Create the following variables and print their data types.

print(type(25))     #int
print(type("Gaurang"))   #str
print(type(35000.50))    #float
print(type(True))        #boolean
print(type(["SQL", "Python", "Excel"]))   #list
print(type({"role": "Prdouct Analyst", "experience":2}))   #dictonary
print(type((28.45, 77.02)))       #tuple
print(type({"Delhi", "Mumbai", "Pune"}))    #set

# Part 2: Indexing Practice

skills = ["SQL", "Python", "Excel", "Power BI", "Google Analytics"]

## Q2. Print the first skill.
print(skills[0])

## Q3. Print the third skill.
print(skills[2])

## Q4. Print the last skill using positive indexing.
print(skills[4])

## Q5. Print the last skill using negative indexing.
print(skills[-1])

# Part 3: Dictionary Access
employee = {
    "name": "Gaurang",
    "role": "Product Analyst",
    "salary": 35000,
    "skills": ["SQL", "Python", "GA4"]
}
## Q6. Print the employee name.
print(employee["Gaurang"])

## Q7. Print the employee role.
print(employee["Product Analyst"])

## Q8. Print the second skill from the `skills` list inside the dictionary.
print(employee["skills"][1])

# Part 4: Mutability Practice

## Q9. Create a list and change its second value.
numbers = [10, 20, 30, 40]

print(numbers)
skills[1] = 200
print(numbers)


## Q10. Create a dictionary and update the value of `role`.
profile = {
    "name": "Gaurang",
    "role": "Product Analyst"
}

print(profile)
profile["role"] = "Data Engineer"
print(profile)
 
 ## Q11. Try changing a tuple value.
numbers_tuple = (10, 20, 30)
#Try to change `20` to `200`.

##Write the error message as a comment.
#print(numbers_tuple)
#numbers_tuple[1] = 200
#TypeError: 'tuple' obejct does not support item assignment

## Q12. Try changing a string value.
name = "Gaurang"

#print(name)
#name[0] = "S"
#print(name)
#TypeError : 'str' object does not support item assignment

# Part 5: Set Practice

## Q13. Convert the list into a set to remove duplicates.

cities = {'Delhi', 'Mumbai', 'Pune', 'Bangalore'}

cities = set(cities)
print(cities)

## Q14. Check whether `"Delhi"` exists in the set.
print("Delhi" in cities)

## Q15. Add `"Chennai"` to the set.
cities.add("Chennai")
print(cities)

# Part 6: Big O Understanding
# Big 0 is used to measure the time complexity , performance & efficiency of code. It help us to understand,how much code is efficient or not.
# Its performance in large data set. It is used to comapre the performance of different algorithims.                                                                             

## Q16. What is Big O notation?
#Big o notation tells us how fast or slow a programs runs as the data increases. It is used to measure the performance and efficiency of code.

## Q17. What is the time complexity of accessing a list item by index?
#Example

#```python
numbers = [10, 20, 30]
print(numbers[1])
#```

0(1) 
#constant time comlexity.
# execution time remains constant regardless of the size of the list.

## Q18. What is the time complexity of searching for a value in a list?
#Example:

#```python
numbers = [10, 20, 30, 40]
print(30 in numbers)
#```

#o(n) 
# LINEAR TIME COMPLEXITY
#Data is increased, checking each item in the list takes more time, seaching was slower as the list grows. 

## Q19. What is the average time complexity of searching for a key in a dictionary?

#Example:

#```python
profile = {"name": "Gaurang", "role": "Product Analyst"}
print("name" in profile)
#```

#O(1)
#CONSTANT TIME COMPLEXITY
#Key searching in a dictionary is very fast, regardless of the size of the dictionary. It uses a hash table to store key value.

## Q20. What is the average time complexity of searching for a value in a set?

#Example:

#```python
cities = {"Delhi", "Mumbai", "Pune"}
print("Delhi" in cities)
#```
#cd assignment2o(1)
# Constant time complexity

# Part 7: Mini Practical Task

## Q21. Create a student profile using a dictionary.

#The dictionary should contain the following keys:

#Example:

#```python
student_profile = {
    "name": "Gaurang",
    "age": 25,
    "current_role": "Product Analyst",
    "target_role": "Data and AI Engineer",
    "skills": ["SQL", "Python", "Excel", "GA4"],
    "monthly_salary": 35000
}
#```

#Now print the following:

#1. Name
#2. Current role
#3. Target role
#4. First skill
#5. Total number of skills

print(student_profile["name"])
print(student_profile["current_role"])
print(student_profile["target_role"])
print(student_profile["skills"][0])
print(len(student_profile["skills"]))










