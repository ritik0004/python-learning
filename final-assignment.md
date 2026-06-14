# Python Jumbo Assignment: Month 1 Revision

## Objective

This assignment is designed to revise and test all Python concepts covered in Month 1.

You will practice:

| Concept                  | What You Should Be Able To Do                                     |
| ------------------------ | ----------------------------------------------------------------- |
| Data types               | Use `int`, `float`, `str`, `list`, `dict`, `tuple`, `set`, `bool` |
| Indexing                 | Access values from lists, tuples, strings, and dictionaries       |
| Mutability               | Understand which objects can and cannot be changed                |
| Big O basics             | Understand simple access/search complexity                        |
| Conditions               | Use `if`, `elif`, `else`                                          |
| Logical operators        | Use `and`, `or`, `not`                                            |
| Loops                    | Use `for` and `while`                                             |
| `break` / `continue`     | Control loop flow                                                 |
| Functions                | Define and call functions                                         |
| Parameters and arguments | Pass inputs to functions                                          |
| Return values            | Return results from functions                                     |
| Scope                    | Understand local variables                                        |
| Default arguments        | Use default parameter values                                      |
| Exception handling       | Use `try`, `except`, `finally`, and `raise`                       |
| List of dictionaries     | Process record-like data                                          |

---

## Submission Instructions

Create one Python file with the following name:

```python
month_01_jumbo_assignment.py
```

Add comments before every question like this:

```python
# Q1. Create variables and print their data types
```

Rules:

1. Do not skip any question.
2. If you cannot solve a question, write your understanding as a comment.
3. Use clean variable names.
4. Use proper indentation.
5. Wherever a function is asked, solve it using a function.
6. Wherever exception handling is asked, use `try-except`.
7. Push the final file to GitHub and share the link.

---

# Part 1: Data Types

## Q1. Create variables and print their data types

Create the following variables:

| Variable         | Value                                          |
| ---------------- | ---------------------------------------------- |
| `student_name`   | `"Gaurang"`                                    |
| `age`            | `26`                                           |
| `monthly_salary` | `35000.50`                                     |
| `is_working`     | `True`                                         |
| `skills`         | `["SQL", "Python", "Excel", "GA4"]`            |
| `profile`        | `{"role": "Product Analyst", "experience": 2}` |
| `coordinates`    | `(28.45, 77.02)`                               |
| `unique_cities`  | `{"Delhi", "Mumbai", "Pune"}`                  |

Print the type of each variable.

Expected style:

```python
print(type(student_name))
print(type(age))
```

---

## Q2. Create a student profile dictionary

Create a dictionary called `student_profile` with these keys:

| Key              | Value                     |
| ---------------- | ------------------------- |
| `name`           | Your name                 |
| `age`            | Your age                  |
| `current_role`   | Your current role         |
| `target_role`    | `"Data and AI Engineer"`  |
| `skills`         | List of at least 4 skills |
| `monthly_salary` | Your monthly salary       |

Print the complete dictionary.

---

# Part 2: Indexing and Access

Use this list for Q3 to Q6:

```python
skills = ["SQL", "Python", "Excel", "Power BI", "GA4"]
```

## Q3. Print the first skill

Expected output:

```text
SQL
```

---

## Q4. Print the third skill

Expected output:

```text
Excel
```

---

## Q5. Print the last skill using positive indexing

Expected output:

```text
GA4
```

---

## Q6. Print the last skill using negative indexing

Expected output:

```text
GA4
```

---

Use this dictionary for Q7 to Q10:

```python
employee = {
    "name": "Gaurang",
    "role": "Product Analyst",
    "salary": 35000,
    "skills": ["SQL", "Python", "GA4"]
}
```

## Q7. Print the employee name

Expected output:

```text
Gaurang
```

---

## Q8. Print the employee role

Expected output:

```text
Product Analyst
```

---

## Q9. Print the second skill from the skills list inside the dictionary

Expected output:

```text
Python
```

---

## Q10. Print the total number of skills

Expected output:

```text
3
```

---

# Part 3: Mutability

## Q11. Update a list

Use this list:

```python
numbers = [10, 20, 30, 40]
```

Change `20` to `200`.

Expected output:

```text
[10, 200, 30, 40]
```

---

## Q12. Update a dictionary

Use this dictionary:

```python
profile = {
    "name": "Gaurang",
    "role": "Product Analyst"
}
```

Change role to:

```text
Data Engineer
```

Expected output:

```text
{'name': 'Gaurang', 'role': 'Data Engineer'}
```

---

## Q13. Try changing a tuple

Use this tuple:

```python
numbers_tuple = (10, 20, 30)
```

Try to change `20` to `200`.

Write the error message as a comment.

Expected learning:

```text
Tuple is immutable.
```

---

## Q14. Try changing a string

Use this string:

```python
name = "Gaurang"
```

Try to change the first character from `G` to `S`.

Write the error message as a comment.

Expected learning:

```text
String is immutable.
```

---

# Part 4: Sets

Use this list for Q15 to Q17:

```python
cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Bangalore"]
```

## Q15. Convert the list into a set to remove duplicates

Expected output may appear in any order:

```text
{'Delhi', 'Mumbai', 'Pune', 'Bangalore'}
```

---

## Q16. Check whether `"Delhi"` exists in the set

Expected output:

```text
True
```

---

## Q17. Add `"Chennai"` to the set

Expected output should include:

```text
Chennai
```

---

# Part 5: Big O Basics

Answer Q18 to Q21 as comments.

## Q18. What is Big O notation?

Write 2–3 lines.

---

## Q19. What is the time complexity of accessing a list item by index?

Example:

```python
numbers = [10, 20, 30]
print(numbers[1])
```

Expected answer:

```text
O(1)
```

---

## Q20. What is the time complexity of searching for a value in a list?

Example:

```python
numbers = [10, 20, 30, 40]
print(30 in numbers)
```

Expected answer:

```text
O(n)
```

---

## Q21. What is the average time complexity of searching for a key in a dictionary?

Example:

```python
profile = {"name": "Gaurang", "role": "Product Analyst"}
print("name" in profile)
```

Expected answer:

```text
O(1)
```

---

# Part 6: Conditions

## Q22. Check loan eligibility using credit score

Create:

```python
credit_score = 720
```

Rules:

| Condition           | Output                |
| ------------------- | --------------------- |
| credit_score >= 700 | Eligible for loan     |
| credit_score < 700  | Not eligible for loan |

Expected output:

```text
Eligible for loan
```

---

## Q23. Create credit score bands

Create:

```python
credit_score = 760
```

Rules:

| Credit Score | Band      |
| -----------: | --------- |
|       >= 750 | Excellent |
|      700–749 | Good      |
|      650–699 | Average   |
|        < 650 | Poor      |

Expected output:

```text
Excellent
```

---

## Q24. Check high-value loan

Create:

```python
loan_amount = 800000
```

Rules:

| Condition             | Output          |
| --------------------- | --------------- |
| loan_amount >= 500000 | High value loan |
| loan_amount < 500000  | Normal loan     |

Expected output:

```text
High value loan
```

---

## Q25. Check employment type

Create:

```python
employment_type = "Salaried"
```

Rules:

| Employment Type   | Output                  |
| ----------------- | ----------------------- |
| `"Salaried"`      | Stable income profile   |
| `"Self-Employed"` | Business income profile |
| Anything else     | Other income profile    |

Expected output:

```text
Stable income profile
```

---

# Part 7: Logical Operators

## Q26. Loan eligibility using credit score and salary

Create:

```python
credit_score = 720
monthly_salary = 40000
```

Rules:

| Condition                                       | Output       |
| ----------------------------------------------- | ------------ |
| credit_score >= 700 and monthly_salary >= 30000 | Eligible     |
| otherwise                                       | Not eligible |

Expected output:

```text
Eligible
```

---

## Q27. Metro city check

Create:

```python
city = "Delhi"
```

Rules:

| Condition                           | Output         |
| ----------------------------------- | -------------- |
| city is Delhi, Mumbai, or Bangalore | Metro city     |
| otherwise                           | Non-metro city |

Expected output:

```text
Metro city
```

---

## Q28. Risk profile check

Create:

```python
credit_score = 620
loan_amount = 900000
```

Rules:

| Condition                                   | Output                  |
| ------------------------------------------- | ----------------------- |
| credit_score < 650 and loan_amount > 500000 | High risk application   |
| otherwise                                   | Normal risk application |

Expected output:

```text
High risk application
```

---

## Q29. Rejection check using `not`

Create:

```python
loan_status = "Pending"
```

Rules:

| Condition                   | Output                       |
| --------------------------- | ---------------------------- |
| loan_status is not Approved | Application not approved yet |
| loan_status is Approved     | Application approved         |

Expected output:

```text
Application not approved yet
```

---

# Part 8: For Loops

## Q30. Print all skills

Use:

```python
skills = ["SQL", "Python", "Excel", "Power BI"]
```

Expected output:

```text
SQL
Python
Excel
Power BI
```

---

## Q31. Print high-value loans from a list

Use:

```python
loan_amounts = [200000, 500000, 750000, 1000000, 300000]
```

Print only amounts greater than or equal to `500000`.

Expected output:

```text
500000
750000
1000000
```

---

## Q32. Count approved applications

Use:

```python
loan_statuses = ["Approved", "Rejected", "Approved", "Pending", "Approved"]
```

Expected output:

```text
Approved Applications: 3
```

---

## Q33. Count rejected and pending applications

Use:

```python
loan_statuses = ["Approved", "Rejected", "Approved", "Pending", "Rejected", "Pending"]
```

Expected output:

```text
Rejected Applications: 2
Pending Applications: 2
```

---

# Part 9: Break, Continue, and While Loop

## Q34. Stop loop when loan amount is greater than 700000

Use:

```python
loan_amounts = [200000, 400000, 600000, 800000, 1000000]
```

Print amounts one by one, but stop when amount is greater than `700000`.

Expected output:

```text
200000
400000
600000
```

---

## Q35. Skip pending applications

Use:

```python
loan_statuses = ["Approved", "Pending", "Rejected", "Pending", "Approved"]
```

Print all statuses except `"Pending"`.

Expected output:

```text
Approved
Rejected
Approved
```

---

## Q36. Print numbers from 1 to 5 using a while loop

Expected output:

```text
1
2
3
4
5
```

---

## Q37. Keep reducing loan balance

Create:

```python
loan_balance = 500000
monthly_payment = 100000
```

Using a while loop, reduce the loan balance by `monthly_payment` until the balance becomes `0`.

Expected output:

```text
Remaining Balance: 400000
Remaining Balance: 300000
Remaining Balance: 200000
Remaining Balance: 100000
Remaining Balance: 0
Loan fully paid
```

---

# Part 10: Functions

## Q38. Create a function to print your name

Function name:

```python
print_name()
```

Expected output:

```text
Gaurang
```

---

## Q39. Create a function to calculate square

Function name:

```python
square(num)
```

The function should return the square of the number.

Example:

```python
print(square(5))
```

Expected output:

```text
25
```

---

## Q40. Create a function to calculate cube

Function name:

```python
cube(num)
```

Expected output:

```text
27
```

when called with:

```python
print(cube(3))
```

---

## Q41. Create a function to add two numbers

Function name:

```python
add(a, b)
```

Expected output:

```text
30
```

when called with:

```python
print(add(10, 20))
```

---

## Q42. Create a function to divide two numbers

Function name:

```python
divide(a, b)
```

Expected output:

```text
5.0
```

when called with:

```python
print(divide(20, 4))
```

---

## Q43. Create a greeting function with default value

Function name:

```python
greet_user(name, greeting="Hello")
```

Expected output:

```text
Hello, Gaurang!
Hi, Gaurang!
```

when called with:

```python
print(greet_user("Gaurang"))
print(greet_user("Gaurang", "Hi"))
```

---

## Q44. Create a function to calculate approval rate

Function name:

```python
calculate_approval_rate(total_applications, approved_applications)
```

Formula:

```text
approved_applications / total_applications * 100
```

Expected output:

```text
60.0
```

when called with:

```python
print(calculate_approval_rate(10, 6))
```

If `total_applications` is `0`, return `0`.

---

## Q45. Create a function to check loan eligibility

Function name:

```python
check_loan_eligibility(credit_score)
```

Rules:

| Credit Score | Output       |
| -----------: | ------------ |
|       >= 700 | Eligible     |
|        < 700 | Not Eligible |

Expected output:

```text
Eligible
```

when called with:

```python
print(check_loan_eligibility(720))
```

---

## Q46. Create a function to return credit score band

Function name:

```python
get_credit_score_band(credit_score)
```

Rules:

| Credit Score | Band      |
| -----------: | --------- |
|       >= 750 | Excellent |
|      700–749 | Good      |
|      650–699 | Average   |
|        < 650 | Poor      |

Expected output:

```text
Excellent
```

when called with:

```python
print(get_credit_score_band(760))
```

---

# Part 11: Scope and Local Variables

## Q47. Local variable example

Create a function called:

```python
show_message()
```

Inside the function, create:

```python
message = "This is a local variable"
```

Print the message inside the function.

Then try to print `message` outside the function.

Write the error message as a comment.

Expected learning:

```text
Local variables cannot be accessed outside the function.
```

---

## Q48. Calculate bonus

Create a function called:

```python
calculate_bonus(salary)
```

Inside the function:

```python
bonus = salary * 0.10
```

Return the bonus.

Expected output:

```text
5000.0
```

when called with:

```python
print(calculate_bonus(50000))
```

Also write as a comment whether `bonus` can be accessed outside the function.

---

# Part 12: Exception Handling

## Q49. Handle division by zero

Create:

```python
a = 10
b = 0
```

Use `try-except` to handle division by zero.

Expected output:

```text
Error: Cannot divide by zero
```

---

## Q50. Handle invalid number conversion

Create:

```python
value = "abc"
```

Try to convert it using:

```python
int(value)
```

Handle the error.

Expected output:

```text
Error: Invalid number conversion
```

---

## Q51. Handle list index error

Use:

```python
numbers = [10, 20, 30]
```

Try to access:

```python
numbers[5]
```

Handle the error.

Expected output:

```text
IndexError occurred
```

---

## Q52. Handle dictionary key error

Use:

```python
student = {
    "name": "Gaurang",
    "role": "Product Analyst"
}
```

Try to access:

```python
student["salary"]
```

Handle the error.

Expected output:

```text
KeyError occurred
```

---

## Q53. Use finally block

Create:

```python
a = 10
b = 0
```

Use `try-except-finally`.

Expected output:

```text
Error: Cannot divide by zero
Execution completed
```

---

## Q54. Raise custom error for negative loan amount

Create:

```python
loan_amount = -50000
```

If loan amount is less than `0`, raise a `ValueError`.

Expected output:

```text
Error: Loan amount cannot be negative
```

---

## Q55. Create a safe division function

Create a function:

```python
safe_divide(a, b)
```

Rules:

| Condition                  | Output                           |
| -------------------------- | -------------------------------- |
| If division is successful  | Return result                    |
| If division by zero occurs | Return `"Cannot divide by zero"` |

Expected output:

```text
5.0
Cannot divide by zero
```

when called with:

```python
print(safe_divide(10, 2))
print(safe_divide(10, 0))
```

---

# Part 13: List of Dictionaries

Use this data for Q56 to Q65:

```python
loan_applications = [
    {"application_id": "APP001", "customer_id": "C001", "loan_amount": 500000, "credit_score": 760, "loan_status": "Approved", "city": "Delhi"},
    {"application_id": "APP002", "customer_id": "C002", "loan_amount": 300000, "credit_score": 620, "loan_status": "Rejected", "city": "Mumbai"},
    {"application_id": "APP003", "customer_id": "C003", "loan_amount": 750000, "credit_score": 710, "loan_status": "Approved", "city": "Delhi"},
    {"application_id": "APP004", "customer_id": "C004", "loan_amount": 200000, "credit_score": 580, "loan_status": "Pending", "city": "Bangalore"},
    {"application_id": "APP005", "customer_id": "C005", "loan_amount": 1000000, "credit_score": 800, "loan_status": "Approved", "city": "Pune"}
]
```

## Q56. Print application ID and loan status for each application

Expected output:

```text
APP001 Approved
APP002 Rejected
APP003 Approved
APP004 Pending
APP005 Approved
```

---

## Q57. Print eligible or not eligible for each application

Rule:

| Condition           | Output       |
| ------------------- | ------------ |
| credit_score >= 700 | Eligible     |
| credit_score < 700  | Not Eligible |

Expected output:

```text
APP001 Eligible
APP002 Not Eligible
APP003 Eligible
APP004 Not Eligible
APP005 Eligible
```

---

## Q58. Count total applications

Expected output:

```text
Total Applications: 5
```

---

## Q59. Count total approved applications

Expected output:

```text
Approved Applications: 3
```

---

## Q60. Calculate total loan amount requested

Expected output:

```text
Total Loan Amount Requested: 2750000
```

---

## Q61. Calculate total approved loan amount

Only include applications where loan status is `"Approved"`.

Expected output:

```text
Total Approved Loan Amount: 2250000
```

---

## Q62. Calculate average loan amount

Expected output:

```text
Average Loan Amount: 550000.0
```

---

## Q63. Count applications by city manually

Do not use external libraries.

Expected output:

```text
Delhi: 2
Mumbai: 1
Bangalore: 1
Pune: 1
```

---

## Q64. Create a new list of high-value approved applications

Rule:

```text
loan_status is "Approved" and loan_amount >= 700000
```

Expected output should include APP003 and APP005.

---

## Q65. Create a summary dictionary

Create a dictionary with the following keys:

```python
{
    "total_applications": 5,
    "approved_applications": 3,
    "rejected_applications": 1,
    "pending_applications": 1,
    "total_requested_amount": 2750000,
    "total_approved_amount": 2250000,
    "average_loan_amount": 550000.0
}
```

Print the dictionary.

---

# Part 14: Functions With List of Dictionaries

Use the same `loan_applications` data.

## Q66. Create a function to count total applications

Function name:

```python
count_total_applications(applications)
```

Expected output:

```text
5
```

---

## Q67. Create a function to count approved applications

Function name:

```python
count_approved_applications(applications)
```

Expected output:

```text
3
```

---

## Q68. Create a function to calculate total approved loan amount

Function name:

```python
calculate_total_approved_amount(applications)
```

Expected output:

```text
2250000
```

---

## Q69. Create a function to return high-value approved applications

Function name:

```python
get_high_value_approved_applications(applications)
```

Rule:

```text
loan_status is "Approved" and loan_amount >= 700000
```

Expected output should include APP003 and APP005.

---

## Q70. Create a function to generate full loan summary

Function name:

```python
generate_loan_summary(applications)
```

The function should return this dictionary:

```python
{
    "total_applications": 5,
    "approved_applications": 3,
    "rejected_applications": 1,
    "pending_applications": 1,
    "total_requested_amount": 2750000,
    "total_approved_amount": 2250000,
    "average_loan_amount": 550000.0,
    "approval_rate": 60.0
}
```

---

# Part 15: Business Validation Mini Task

Use this data:

```python
raw_loan_applications = [
    {"application_id": "APP001", "customer_id": "C001", "loan_amount": 500000, "credit_score": 760},
    {"application_id": "APP002", "customer_id": "C002", "loan_amount": -300000, "credit_score": 620},
    {"application_id": "APP003", "customer_id": "", "loan_amount": 750000, "credit_score": 710},
    {"application_id": "APP004", "customer_id": "C004", "loan_amount": 200000, "credit_score": 950},
    {"application_id": "APP005", "customer_id": "C005", "loan_amount": 1000000, "credit_score": 800}
]
```

## Q71. Validate loan amount

Loop through the data.

If `loan_amount` is greater than `0`, print:

```text
APP001 Valid loan amount
```

If not, print:

```text
APP002 Invalid loan amount
```

---

## Q72. Validate customer ID

If `customer_id` is not empty, print:

```text
APP001 Valid customer ID
```

If empty, print:

```text
APP003 Invalid customer ID
```

---

## Q73. Validate credit score

Valid credit score range:

```text
300 to 900
```

Expected output should include:

```text
APP001 Valid credit score
APP004 Invalid credit score
```

---

## Q74. Create valid and rejected application lists

Create two empty lists:

```python
valid_applications = []
rejected_applications = []
```

Rules:

| Condition                                | Error Message        |
| ---------------------------------------- | -------------------- |
| loan_amount <= 0                         | Invalid loan amount  |
| customer_id is empty                     | Missing customer ID  |
| credit_score < 300 or credit_score > 900 | Invalid credit score |

If the application is valid, add it to `valid_applications`.

If invalid, add this format to `rejected_applications`:

```python
{
    "application_id": "APP002",
    "error": "Invalid loan amount"
}
```

Expected result:

```python
valid_applications = [
    {"application_id": "APP001", "customer_id": "C001", "loan_amount": 500000, "credit_score": 760},
    {"application_id": "APP005", "customer_id": "C005", "loan_amount": 1000000, "credit_score": 800}
]

rejected_applications = [
    {"application_id": "APP002", "error": "Invalid loan amount"},
    {"application_id": "APP003", "error": "Missing customer ID"},
    {"application_id": "APP004", "error": "Invalid credit score"}
]
```

---

## Q75. Create a validation summary

Using the result from Q74, print:

```text
Total Applications: 5
Valid Applications: 2
Rejected Applications: 3
```

---

# Bonus Section

## Q76. Create a reusable validation function

Function name:

```python
validate_application(application)
```

Rules:

| Condition                                | Error                |
| ---------------------------------------- | -------------------- |
| loan_amount <= 0                         | Invalid loan amount  |
| customer_id is empty                     | Missing customer ID  |
| credit_score < 300 or credit_score > 900 | Invalid credit score |

If valid, return:

```python
{
    "is_valid": True,
    "error": None
}
```

If invalid, return:

```python
{
    "is_valid": False,
    "error": "Invalid loan amount"
}
```

---

## Q77. Use `validate_application()` on all applications

Use the function from Q76 and create:

```python
valid_applications = []
rejected_applications = []
```

Expected result should be the same as Q74.

---

## Q78. Explain `print()` vs `return`

Write 4–5 lines as comments explaining the difference between `print()` and `return`.

---

## Q79. Explain why exception handling is useful

Write 4–5 lines as comments explaining why exception handling is useful in real-world data engineering projects.

---

## Q80. Explain why list of dictionaries is important

Write 4–5 lines as comments explaining why list of dictionaries is useful when working with APIs, JSON, and tabular records.

---

# Evaluation Criteria

| Area                                    | Marks |
| --------------------------------------- | ----: |
| Data types, indexing, mutability        |    10 |
| Sets and Big O basics                   |    10 |
| Conditions and logical operators        |    10 |
| Loops, break, continue, while           |    10 |
| Functions and return values             |    15 |
| Scope and default arguments             |     5 |
| Exception handling                      |    10 |
| List of dictionaries                    |    15 |
| Business validation task                |    10 |
| Clean code, comments, GitHub submission |     5 |

**Total: 100 marks**

---

# Final Note

This is a revision assignment. The goal is not speed.

The goal is to make sure you can write clean Python code using all the basics covered in Month 1.

Focus especially on:

1. Correct syntax
2. Proper indentation
3. `print()` vs `return`
4. Loops inside functions
5. List of dictionaries
6. Exception handling
7. Clean and readable code
