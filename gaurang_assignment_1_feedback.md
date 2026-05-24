# Feedback: Python Assignment 1 — Gaurang

## Overall Feedback

Good attempt, Gaurang. You have understood many of the basic Python concepts well, especially data types, indexing, dictionary access, list mutability, and basic profile dictionary creation.

The main areas where you need to focus are set usage, Big O understanding for sets, and following the exact question requirement. In a few places, you solved the task in a different way from what was asked, so the output may work partially but does not fully match the learning objective.

---

## What You Did Well

| Area | Feedback |
|---|---|
| Data types | You correctly identified most data types like `int`, `str`, `float`, `bool`, `list`, `dict`, and `set`. |
| List indexing | You correctly used positive and negative indexing. |
| Dictionary access | You correctly accessed values using keys like `employee["name"]` and `employee["role"]`. |
| Nested list inside dictionary | You correctly accessed `employee["skills"][1]`. |
| List mutability | You correctly updated `numbers[1] = 200`. |
| Dictionary mutability | You correctly updated `profile["role"]`. |
| Tuple and string immutability | You correctly understood and documented the errors. |
| Mini profile task | You were able to create a dictionary and access values from it. |

---

## Mistakes and Corrections

## 1. Missing Tuple in Data Types

In Part 1, the tuple example was missing:

```python
coordinates = (28.45, 77.02)
print(type(coordinates))
```

Expected output:

```text
<class 'tuple'>
```

---

## 2. Set Conversion Question

The assignment asked you to convert a list into a set to remove duplicates.

You wrote:

```python
unique = list(set(cities))
print(unique)
```

This removes duplicates, but converts the result back into a list. The question asked for a set.

Better version:

```python
cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Bangalore"]
unique_cities = set(cities)
print(unique_cities)
```

Expected output:

```text
{'Delhi', 'Mumbai', 'Pune', 'Bangalore'}
```

Order can be different.

---

## 3. Membership Check Should Be Done on Set

You wrote:

```python
cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Bangalore"] 
print("Delhi" in cities)
```

This works, but the question was from set practice. Better:

```python
unique_cities = set(cities)
print("Delhi" in unique_cities)
```

Why this matters:

- Searching in a list is usually `O(n)`.
- Searching in a set is usually `O(1)`.

---

## 4. Adding Chennai Should Be Done to Set

You wrote:

```python
cities.append("Chennai")
print(cities)
```

This adds Chennai to a list, not a set. Since this question was about set practice, use `.add()`.

Correct version:

```python
unique_cities = set(cities)
unique_cities.add("Chennai")
print(unique_cities)
```

---

## 5. Big O for Set Search

You wrote that searching in a set is `O(n)`.

Correct answer:

```text
O(1) average case
```

Reason:

A set uses hashing internally, so checking whether a value exists in a set is usually very fast.

Correct explanation:

```python
# Searching for a value in a set is O(1) on average because sets use hashing.
```

---

## 6. Student Profile Key Names Changed

In the final task, the expected key was:

```python
"current_role"
```

But you used:

```python
"current role"
```

Both can work if used consistently, but in real projects we prefer clean key names using underscores:

```python
student_profile = {
    "name": "Gaurang Sharma",
    "age": 26,
    "current_role": "Product Analyst",
    "target_role": "AI Engineer",
    "skills": ["SQL", "Excel", "Python"]
}
```

Then access like this:

```python
print(student_profile["current_role"])
```

---

## Important Concepts to Revise

| Concept | Priority |
|---|---|
| Set vs list | High |
| Set `.add()` method | High |
| Big O for set search | High |
| Following exact question requirement | Medium |
| Consistent dictionary key naming | Medium |

---

## Suggested Practice Before Next Class

Try this again:

```python
cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Bangalore"]
```

Write code to:

1. Convert it to a set  
2. Print the set  
3. Check whether `Delhi` exists in the set  
4. Add `Chennai` to the set  
5. Print the final set  

Expected style:

```python
unique_cities = set(cities)
print(unique_cities)
print("Delhi" in unique_cities)
unique_cities.add("Chennai")
print(unique_cities)
```

---

## Estimated Score

| Section | Score |
|---|---:|
| Data types | 17 / 20 |
| Indexing | 15 / 15 |
| Dictionary access | 15 / 15 |
| Mutability | 15 / 15 |
| Set usage | 5 / 10 |
| Big O answers | 10 / 15 |
| Clean code and comments | 7 / 10 |

**Total: 84 / 100**

---

## Final Note

Good work overall. Your basics are stronger than before, especially dictionary access and indexing. Now focus on understanding why sets are different from lists and why set lookup is faster. Also, try to follow the exact question requirement instead of changing the structure unless needed.
