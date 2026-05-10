# Python Assignment 1: Data Types, Indexing, Mutability, and Big O Basics

## Objective

This assignment is designed to check your understanding of the following concepts:

| Concept      | What You Should Understand                            |
| ------------ | ----------------------------------------------------- |
| Data Types   | `int`, `float`, `str`, `list`, `dict`, `tuple`, `set` |
| Indexing     | Accessing values using position or key                |
| Mutability   | Which objects can be changed and which cannot         |
| Big O Basics | Basic search and access performance                   |

---

## Submission Instructions

Create one Python file with the following name:

```python
assignment_01_python_basics.py
```

Add a comment before every question like this:

```python
# Q1. Create variables and print their data types
```

---

# Part 1: Identify Data Types

## Q1. Create the following variables and print their data types.

| Variable Name   | Value                                          |
| --------------- | ---------------------------------------------- |
| `age`           | `25`                                           |
| `name`          | `"Gaurang"`                                    |
| `salary`        | `35000.50`                                     |
| `is_working`    | `True`                                         |
| `skills`        | `["SQL", "Python", "Excel"]`                   |
| `profile`       | `{"role": "Product Analyst", "experience": 2}` |
| `coordinates`   | `(28.45, 77.02)`                               |
| `unique_cities` | `{"Delhi", "Mumbai", "Pune"}`                  |

Example:

```python
print(type(age)) int
print(type(name)) str
print(type(salary)) float
print(type(is_working)) - boolean
print(type(skills))- list
print(type(profile))- dictionary
print(type(unique_cities)) - set

```int
str

---

# Part 2: Indexing Practice

Use the following list:

```python
skills = ["SQL", "Python", "Excel", "Power BI", "Google Analytics"]
```

## Q2. Print the first skill.
print(skills[0])

Expected output:

```text
SQL    
```

## Q3. Print the third skill.
print(skills[2])

Expected output:

```text
Excel
```

## Q4. Print the last skill using positive indexing.

Expected output:
print(skills[4])
```text
Google Analytics
```

## Q5. Print the last skill using negative indexing.

Expected output:
print(skills[-1])
```text
Google Analytics
```

---

# Part 3: Dictionary Access

Use the following dictionary:

```python
employee = {
    "name": "Gaurang",
    "role": "Product Analyst",
    "salary": 35000,
    "skills": ["SQL", "Python", "GA4"]
}
```

## Q6. Print the employee name.
print(employee["name"])
Expected output:
print()
```text
Gaurang
```

## Q7. Print the employee role.

Expected output:
print(employee["role"])
```text
Product Analyst
```

## Q8. Print the second skill from the `skills` list inside the dictionary.

Expected output:
print(employee["skills"[1]])
```text
Python
```
i used or checked chatgpt

---

# Part 4: Mutability Practice

## Q9. Create a list and change its second value.

Use this list:

```python
numbers = [10, 20, 30, 40]
```

numbers[1]=200
print(numbers)
Change `20` to `200`.

Expected output:

```text
[10, 200, 30, 40]
```

---

## Q10. Create a dictionary and update the value of `role`.

Use this dictionary:

```python
profile = {
    "name": "Gaurang",
    "role": "Product Analyst"
}
```

Change the role to:

```text
Data Engineer
```profile["role"]="Data Engineer"
print(profile)

Expected output:

```text
{'name': 'Gaurang', 'role': 'Data Engineer'}
```

---

## Q11. Try changing a tuple value.

Use this tuple:

```python
numbers_tuple = (10, 20, 30)
```

Try to change `20` to `200`.

Write the error message as a comment.

ERROR!
Traceback (most recent call last):
  File "<main.py>", line 12, in <module>
TypeError: 'tuple' object does not support item assignment

Expected learning:

```text
Tuple is immutable.
```

---

## Q12. Try changing a string value.

Use this string:

```python
name = "Gaurang"
```

Try to change the first character from `G` to `S`.

Write the error message as a comment.
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 11, in <module>
TypeError: 'str' object does not support item assignment
Expected learning:

```text
String is immutable.
```

---

# Part 5: Set Practice

Use this list:

```python
cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Bangalore"]
```

## Q13. Convert the list into a set to remove duplicates.

used chatgpt to  understand
unique=list(set(cities))
print(unique)

Expected output:

```text
{'Delhi', 'Mumbai', 'Pune', 'Bangalore'}
```
print()
Note: The order may be different. That is okay.

## Q14. Check whether `"Delhi"` exists in the set.

i used chatgpt  because i was trying this 
cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Bangalore"] for i in cities : if i=="Delhi": print("true") else: print ("false") i+1

Expected output:
print("Delhi" exists in cities)
```text
True
```

## Q15. Add `"Chennai"` to the set.
cities.add("Chennai")
cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Bangalore"]

cities.append("Chennai")
print(cities)
Expected output should include:

```text
Chennai
```

---

# Part 6: Big O Understanding

Answer these questions in plain English.
big O works for time complexity and space compleaxity , as i am able to understand sometimes we have a fixed value to check time taken will
be less , but for not unique value and we have million values it takes very time taking

## Q16. What is Big O notation?

Write the answer in 2–3 lines.

---

## Q17. What is the time complexity of accessing a list item by index?

Example:

```python
numbers = [10, 20, 30]
print(numbers[1])
```

Expected answer:

```text
O(1)
``` time complexity will be low becuase position is  defined

---

## Q18. What is the time complexity of searching for a value in a list?

Example:

```python
numbers = [10, 20, 30, 40]
print(30 in numbers)
```

Expected answer:
in this time complexity will be high becuase position is not defined , each and every position is checked and verified
```text
O(n)
```

---

## Q19. What is the average time complexity of searching for a key in a dictionary?

Example:

```python
profile = {"name": "Gaurang", "role": "Product Analyst"}
print("name" in profile)
```
time complexity will be low becuase position is  defined
Expected answer:

```text
O(1)
```

---

## Q20. What is the average time complexity of searching for a value in a set?

Example:

```python
cities = {"Delhi", "Mumbai", "Pune"}
print("Delhi" in cities)
```
 time complexity will be high becuase position is not defined , each and every position is checked and verified
Expected answer:

```text
O(1)
```

---

# Part 7: Mini Practical Task

## Q21. Create a student profile using a dictionary.

The dictionary should contain the following keys:

| Key              | Value                       |
| ---------------- | --------------------------- |
| `name`           | Your name                   |
| `age`            | Your age                    |
| `current_role`   | Your current job role       |
| `target_role`    | `"Data and AI Engineer"`    |
| `skills`         | List of at least 4 skills   |
| `monthly_salary` | Your current monthly salary |

Example:

```python
student_profile = {
    "name": "Gaurang",
    "age": 25,
    "current_role": "Product Analyst",
    "target_role": "Data and AI Engineer",
    "skills": ["SQL", "Python", "Excel", "GA4"],
    "monthly_salary": 35000
}
```

Now print the following:

1. Name
2. Current role
3. Target role
4. First skill
5. Total number of skills

---
student_profile={"name":"gaurang sharma","age":26,"current role":"product analyst","target role":"AI Engineer","skills":["sql","excel","python"]}
print(student_profile["name"])
print(student_profile["current role"])
print(student_profile["AI Engineer"])
print(student_profile["skills"][0])
print(len(student_profile["skills"])) - used chatgpt
# Evaluation Criteria

| Area                     | Marks |
| ------------------------ | ----: |
| Correct data types       |    20 |
| Correct indexing         |    15 |
| Dictionary access        |    15 |
| Mutability understanding |    15 |
| Set usage                |    10 |
| Big O answers            |    15 |
| Clean code and comments  |    10 |

**Total: 100 marks**