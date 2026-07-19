# Feedback: Python Assignment 1 — Raman

## Overall Feedback

Good attempt, Raman. You have understood the basic idea of Python data types, indexing, mutability, sets, and Big O at a beginner level. You were able to attempt almost all questions, which is a positive sign.

The main areas to improve are dictionary access, variable usage, clean code formatting, and being careful with syntax. Some answers show that you understand the concept, but the implementation has small mistakes that would cause errors while running the code.

---

## What You Did Well

| Area | Feedback |
|---|---|
| Data types | You correctly identified most basic data types such as `int`, `str`, `float`, `bool`, `list`, `dict`, `tuple`, and `set`. |
| List indexing | You correctly used positive and negative indexing for lists. |
| Tuple and string immutability | You correctly understood that tuples and strings cannot be modified after creation. |
| Dictionary update | You correctly updated the value of `role` in a dictionary. |
| Set operations | You were able to check membership using `in` and add a new value using `.add()`. |
| Big O understanding | Your explanation shows that you understand the basic idea of performance changing with input size. |
| Mini task | You correctly created and accessed values from the student profile dictionary. |

---

## Mistakes and Corrections

## 1. Dictionary Access

You wrote:

```python
print(employee["Gaurang"])
print(employee["Product Analyst"])
```

This is incorrect because dictionaries are accessed using **keys**, not values.

Correct version:

```python
print(employee["name"])
print(employee["role"])
```

Remember:

```python
employee = {
    "name": "Gaurang",
    "role": "Product Analyst"
}
```

Here, `name` and `role` are keys. `Gaurang` and `Product Analyst` are values.

---

## 2. List Mutability Question

You were asked to update this list:

```python
numbers = [10, 20, 30, 40]
```

But you wrote:

```python
skills[1] = 200
print(numbers)
```

This updates the wrong list. You should update `numbers`, not `skills`.

Correct version:

```python
numbers = [10, 20, 30, 40]
numbers[1] = 200
print(numbers)
```

Expected output:

```text
[10, 200, 30, 40]
```

---

## 3. Set Practice

The assignment gave this list:

```python
cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Bangalore"]
```

You directly created a set instead:

```python
cities = {'Delhi', 'Mumbai', 'Pune', 'Bangalore'}
```

This works, but it skips the actual learning point. The goal was to convert a list with duplicates into a set.

Correct version:

```python
cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Bangalore"]
unique_cities = set(cities)
print(unique_cities)
```

---

## 4. Big O Syntax Issue

You wrote:

```python
0(1)
```

This is not valid Python and will cause an error. Since Big O answers are theoretical, write them as comments:

```python
# O(1)
```

or as text in a comment:

```python
# Accessing a list item by index is O(1).
```

---

## 5. Spelling and Code Cleanliness

There are some spelling mistakes such as:

| Written | Correct |
|---|---|
| `Prdouct` | `Product` |
| `dictonary` | `dictionary` |
| `obejct` | `object` |
| `comlexity` | `complexity` |
| `algorithims` | `algorithms` |

These are not major coding issues, but clean spelling helps when writing comments and documentation.

---

## Important Concepts to Revise

| Concept | Priority |
|---|---|
| Dictionary keys vs values | High |
| List indexing and updating values | High |
| Difference between list and set | Medium |
| Writing clean comments | Medium |
| Big O notation syntax | Medium |

---

## Suggested Practice Before Next Class

Try these again independently:

```python
employee = {
    "name": "Raman",
    "role": "Student",
    "skills": ["SQL", "Python", "Excel"]
}
```

Write code to print:

1. Name  
2. Role  
3. First skill  
4. Last skill  
5. Total number of skills  

Then update:

```python
employee["role"] = "Data Engineer"
```

and print the updated dictionary.

---

## Estimated Score

| Section | Score |
|---|---:|
| Data types | 15 / 20 |
| Indexing | 15 / 15 |
| Dictionary access | 5 / 15 |
| Mutability | 10 / 15 |
| Set usage | 7 / 10 |
| Big O answers | 10 / 15 |
| Clean code and comments | 5 / 10 |

**Total: 67 / 100**

---

## Final Note

Good first attempt. Your basics are forming, but you need to slow down and focus on the exact variable or key being asked in the question. Most mistakes are not because you do not understand Python, but because of small implementation errors. Fixing these will improve your code quickly.
