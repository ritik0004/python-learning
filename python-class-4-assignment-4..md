# Python Assignment 4: Exception Handling

## Objective

This assignment is designed to check your understanding of exception handling in Python.

You will practice:

| Concept             | What You Should Understand                                                             |
| ------------------- | -------------------------------------------------------------------------------------- |
| `try` block         | Code that may produce an error                                                         |
| `except` block      | Handling an error gracefully                                                           |
| Specific exceptions | Handling errors like `ZeroDivisionError`, `ValueError`, `KeyError`, `IndexError`, etc. |
| `finally` block     | Code that runs whether an error occurs or not                                          |
| `raise`             | Manually raising an error                                                              |
| Error messages      | Understanding and printing meaningful error messages                                   |

---

## Submission Instructions

Create one Python file with the following name:

```python
assignment_04_exception_handling.py
```

Add a comment before every question like this:

```python
# Q1. Handle division by zero
```

Do not skip any question. If you are unable to solve a question, write your understanding as a comment.

---

# Part 1: Basic Try-Except

## Q1. Handle division by zero

Create two variables:

```python
a = 10
b = 0
```

Try to divide `a` by `b`.

Use `try-except` to handle the error.

Expected output:

```text
Error: Cannot divide by zero
```

---

## Q2. Handle valid division

Create two variables:

```python
a = 20
b = 5
```

Divide `a` by `b` inside a `try` block.

Expected output:

```text
Result: 4.0
```

---

## Q3. Handle invalid number conversion

Create a variable:

```python
value = "abc"
```

Try to convert it into an integer using:

```python
int(value)
```

Handle the error using `except`.

Expected output:

```text
Error: Invalid number conversion
```

---

## Q4. Handle valid number conversion

Create a variable:

```python
value = "100"
```

Convert it into an integer inside a `try` block.

Expected output:

```text
Converted value: 100
```

---

# Part 2: Handling Specific Exceptions

## Q5. Handle `ZeroDivisionError`

Write a program where:

```python
x = 10 / 0
```

Handle only `ZeroDivisionError`.

Expected output:

```text
ZeroDivisionError occurred
```

---

## Q6. Handle `ValueError`

Write a program where:

```python
number = int("Python")
```

Handle only `ValueError`.

Expected output:

```text
ValueError occurred
```

---

## Q7. Handle `IndexError`

Use this list:

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
IndexError occurred: List index is out of range
```

---

## Q8. Handle `KeyError`

Use this dictionary:

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
KeyError occurred: Key does not exist
```

---

## Q9. Handle `TypeError`

Create this code:

```python
result = "10" + 5
```

Handle the error.

Expected output:

```text
TypeError occurred: Unsupported operation between string and number
```

---

# Part 3: Multiple Except Blocks

## Q10. Handle multiple possible errors

Create this code:

```python
values = [10, 20, 30]
index = 5
divisor = 0
```

First try to access:

```python
value = values[index]
```

Then divide:

```python
result = value / divisor
```

Handle both:

1. `IndexError`
2. `ZeroDivisionError`

Expected output:

```text
IndexError occurred
```

---

## Q11. Change the index and test division error

Use:

```python
values = [10, 20, 30]
index = 1
divisor = 0
```

Now the index is valid, but division will fail.

Expected output:

```text
ZeroDivisionError occurred
```

---

## Q12. Handle general exception

Use this code:

```python
data = {"amount": "abc"}
result = int(data["amount"]) / 2
```

Use a general `except Exception as e` block and print the actual error.

Expected output should include an error message like:

```text
Error occurred:
```

---

# Part 4: Finally Block

## Q13. Use `finally` with division

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

## Q14. Finally should run even when there is no error

Create:

```python
a = 20
b = 5
```

Use `try-except-finally`.

Expected output:

```text
Result: 4.0
Execution completed
```

---

## Q15. File closing simulation using finally

Create a variable:

```python
file_open = True
```

Inside `try`, print:

```text
Processing file
```

Inside `finally`, print:

```text
Closing file
```

Expected output:

```text
Processing file
Closing file
```

---

# Part 5: Raise Custom Errors

## Q16. Raise error for negative loan amount

Create a variable:

```python
loan_amount = -50000
```

If `loan_amount` is less than `0`, raise a `ValueError` with this message:

```text
Loan amount cannot be negative
```

Handle the error using `except`.

Expected output:

```text
Error: Loan amount cannot be negative
```

---

## Q17. Raise error for invalid credit score

Create:

```python
credit_score = 950
```

Valid credit score should be between `300` and `900`.

If credit score is less than `300` or greater than `900`, raise a `ValueError`.

Expected output:

```text
Error: Invalid credit score
```

---

## Q18. Raise error for missing customer ID

Create:

```python
customer_id = ""
```

If `customer_id` is empty, raise a `ValueError`.

Expected output:

```text
Error: Customer ID is required
```

---

# Part 6: Exception Handling Inside Functions

## Q19. Create a safe division function

Create a function:

```python
def safe_divide(a, b):
    # your code here
```

Rules:

| Condition                  | Output                           |
| -------------------------- | -------------------------------- |
| If division is successful  | Return result                    |
| If division by zero occurs | Return `"Cannot divide by zero"` |

Example:

```python
print(safe_divide(10, 2))
print(safe_divide(10, 0))
```

Expected output:

```text
5.0
Cannot divide by zero
```

---

## Q20. Create a safe integer conversion function

Create a function:

```python
def safe_int_conversion(value):
    # your code here
```

Rules:

| Condition                   | Output                    |
| --------------------------- | ------------------------- |
| If conversion is successful | Return converted integer  |
| If conversion fails         | Return `"Invalid number"` |

Example:

```python
print(safe_int_conversion("100"))
print(safe_int_conversion("abc"))
```

Expected output:

```text
100
Invalid number
```

---

## Q21. Create a function to validate loan amount

Create a function:

```python
def validate_loan_amount(loan_amount):
    # your code here
```

Rules:

| Condition        | Output                        |
| ---------------- | ----------------------------- |
| loan_amount > 0  | `"Valid loan amount"`         |
| loan_amount <= 0 | Raise and handle `ValueError` |

Example:

```python
print(validate_loan_amount(500000))
print(validate_loan_amount(-10000))
```

Expected output:

```text
Valid loan amount
Invalid loan amount
```

---

## Q22. Create a function to validate credit score

Create a function:

```python
def validate_credit_score(credit_score):
    # your code here
```

Rules:

| Condition                        | Output                   |
| -------------------------------- | ------------------------ |
| credit_score between 300 and 900 | `"Valid credit score"`   |
| otherwise                        | `"Invalid credit score"` |

Use `try-except` and `raise ValueError`.

Example:

```python
print(validate_credit_score(720))
print(validate_credit_score(950))
```

Expected output:

```text
Valid credit score
Invalid credit score
```

---

# Part 7: Business Scenario-Based Questions

Use this list for Q23 to Q27:

```python
loan_applications = [
    {"application_id": "APP001", "customer_id": "C001", "loan_amount": 500000, "credit_score": 760},
    {"application_id": "APP002", "customer_id": "C002", "loan_amount": -300000, "credit_score": 620},
    {"application_id": "APP003", "customer_id": "", "loan_amount": 750000, "credit_score": 710},
    {"application_id": "APP004", "customer_id": "C004", "loan_amount": 200000, "credit_score": 950},
    {"application_id": "APP005", "customer_id": "C005", "loan_amount": 1000000, "credit_score": 800}
]
```

---

## Q23. Validate loan amounts

Loop through the `loan_applications` list.

For each application:

* If `loan_amount` is greater than `0`, print:

```text
APP001 Valid loan amount
```

* If `loan_amount` is less than or equal to `0`, handle it using exception handling and print:

```text
APP002 Invalid loan amount
```

---

## Q24. Validate customer IDs

Loop through the `loan_applications` list.

For each application:

* If `customer_id` is not empty, print:

```text
APP001 Valid customer ID
```

* If `customer_id` is empty, raise and handle a `ValueError`, then print:

```text
APP003 Invalid customer ID
```

---

## Q25. Validate credit scores

Loop through the `loan_applications` list.

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

## Q26. Create a clean and rejected application list

Loop through the `loan_applications` list.

Create two empty lists:

```python
valid_applications = []
rejected_applications = []
```

Rules:

| Validation                               | Error Message        |
| ---------------------------------------- | -------------------- |
| loan_amount <= 0                         | Invalid loan amount  |
| customer_id is empty                     | Missing customer ID  |
| credit_score < 300 or credit_score > 900 | Invalid credit score |

If the application is valid, add it to `valid_applications`.

If the application has an error, add a dictionary to `rejected_applications` in this format:

```python
{
    "application_id": "APP002",
    "error": "Invalid loan amount"
}
```

Expected final output:

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

## Q27. Create a validation summary report

Using the result from Q26, print:

```text
Total Applications: 5
Valid Applications: 2
Rejected Applications: 3
```

---

# Bonus Questions

## Q28. Create a reusable application validation function

Create a function:

```python
def validate_application(application):
    # your code here
```

Rules:

| Condition                            | Error                |
| ------------------------------------ | -------------------- |
| loan_amount <= 0                     | Invalid loan amount  |
| customer_id is empty                 | Missing customer ID  |
| credit_score not between 300 and 900 | Invalid credit score |

If the application is valid, return:

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

## Q29. Use `validate_application()` on all applications

Use the function from Q28 and create:

```python
valid_applications = []
rejected_applications = []
```

Expected output should be the same as Q26.

---

## Q30. Explain in comments: why do we use exception handling?

Write 4–5 lines as comments explaining why exception handling is useful in real-world data engineering projects.

Hint points:

* bad data can come from files/APIs
* code should not crash completely
* errors should be handled gracefully
* invalid records can be rejected or logged
* valid records should continue processing

---

# Important Notes

1. Use `try-except` wherever the question asks you to handle errors.
2. Use specific exceptions like `ZeroDivisionError`, `ValueError`, `KeyError`, `IndexError` wherever possible.
3. Use `finally` where the question specifically asks for it.
4. Do not only print errors. Understand why the error happened.
5. Keep your code clean and readable.
6. Add comments before each question.

---

# Evaluation Criteria

| Area                                | Marks |
| ----------------------------------- | ----: |
| Basic try-except usage              |    15 |
| Specific exception handling         |    15 |
| Multiple except blocks              |    10 |
| finally block usage                 |    10 |
| raise usage                         |    15 |
| Exception handling inside functions |    15 |
| Business scenario validation        |    15 |
| Clean code and comments             |     5 |

**Total: 100 marks**
