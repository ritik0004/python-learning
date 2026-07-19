# Python Assignment 2: Conditions, Loops, and Business Logic

## Objective

This assignment is designed to check your understanding of:

| Concept              | What You Should Understand                 |
| -------------------- | ------------------------------------------ |
| `if / elif / else`   | Applying business rules                    |
| Comparison operators | `==`, `!=`, `>`, `<`, `>=`, `<=`           |
| Logical operators    | `and`, `or`, `not`                         |
| `for` loops          | Iterating through lists                    |
| `while` loops        | Repeating code until a condition changes   |
| `break`              | Stopping a loop                            |
| `continue`           | Skipping one loop iteration                |
| List of dictionaries | Processing multiple records like real data |

---

## Submission Instructions

Create one Python file with the following name:

```python
assignment_02_conditions_loops.py
```

Add a comment before every question like this:

```python
# Q1. Check loan eligibility using credit score
```

---

# Part 1: Conditions

## Q1. Check loan eligibility using credit score

Create a variable:

```python
credit_score = 720
```

Write a condition:

| Condition           | Output                |
| ------------------- | --------------------- |
| credit score >= 700 | Eligible for loan     |
| credit score < 700  | Not eligible for loan |

Expected output:

```text
Eligible for loan
```

---

## Q2. Create credit score bands

Create a variable:

```python
credit_score = 760
```

Print the credit score band based on these rules:

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

## Q3. Check high-value loan

Create a variable:

```python
loan_amount = 800000
```

Print:

| Condition             | Output          |
| --------------------- | --------------- |
| loan amount >= 500000 | High value loan |
| loan amount < 500000  | Normal loan     |

Expected output:

```text
High value loan
```

---

## Q4. Check employment type

Create a variable:

```python
employment_type = "Salaried"
```

Print:

| Condition                            | Output                  |
| ------------------------------------ | ----------------------- |
| employment type is `"Salaried"`      | Stable income profile   |
| employment type is `"Self-Employed"` | Business income profile |
| any other value                      | Other income profile    |

Expected output:

```text
Stable income profile
```

---

# Part 2: Logical Operators

## Q5. Loan eligibility using credit score and salary

Create these variables:

```python
credit_score = 720
monthly_salary = 40000
```

Print:

| Condition                                       | Output       |
| ----------------------------------------------- | ------------ |
| credit_score >= 700 and monthly_salary >= 30000 | Eligible     |
| otherwise                                       | Not eligible |

Expected output:

```text
Eligible
```

---

## Q6. Metro city check

Create a variable:

```python
city = "Delhi"
```

Print:

| Condition                            | Output         |
| ------------------------------------ | -------------- |
| city is Delhi or Mumbai or Bangalore | Metro city     |
| otherwise                            | Non-metro city |

Expected output:

```text
Metro city
```

---

## Q7. Risk profile check

Create these variables:

```python
credit_score = 620
loan_amount = 900000
```

Print:

| Condition                                   | Output                  |
| ------------------------------------------- | ----------------------- |
| credit_score < 650 and loan_amount > 500000 | High risk application   |
| otherwise                                   | Normal risk application |

Expected output:

```text
High risk application
```

---

## Q8. Rejection check using `not`

Create a variable:

```python
loan_status = "Pending"
```

Print:

| Condition                   | Output                       |
| --------------------------- | ---------------------------- |
| loan_status is not Approved | Application not approved yet |
| loan_status is Approved     | Application approved         |

Expected output:

```text
Application not approved yet
```

---

# Part 3: For Loops

## Q9. Print all skills

Use this list:

```python
skills = ["SQL", "Python", "Excel", "Power BI"]
```

Print each skill one by one.

Expected output:

```text
SQL
Python
Excel
Power BI
```

---

## Q10. Print high-value loans from a list

Use this list:

```python
loan_amounts = [200000, 500000, 750000, 1000000, 300000]
```

Print only loan amounts greater than or equal to `500000`.

Expected output:

```text
500000
750000
1000000
```

---

## Q11. Count approved applications

Use this list:

```python
loan_statuses = ["Approved", "Rejected", "Approved", "Pending", "Approved"]
```

Count how many applications are approved.

Expected output:

```text
Approved Applications: 3
```

---

## Q12. Count rejected and pending applications

Use this list:

```python
loan_statuses = ["Approved", "Rejected", "Approved", "Pending", "Rejected", "Pending"]
```

Print:

```text
Rejected Applications: 2
Pending Applications: 2
```

---

# Part 4: List of Dictionaries

Use this data for Q13 to Q18:

```python
loan_applications = [
    {"application_id": "APP001", "customer_id": "C001", "loan_amount": 500000, "credit_score": 760, "loan_status": "Approved", "city": "Delhi"},
    {"application_id": "APP002", "customer_id": "C002", "loan_amount": 300000, "credit_score": 620, "loan_status": "Rejected", "city": "Mumbai"},
    {"application_id": "APP003", "customer_id": "C003", "loan_amount": 750000, "credit_score": 710, "loan_status": "Approved", "city": "Delhi"},
    {"application_id": "APP004", "customer_id": "C004", "loan_amount": 200000, "credit_score": 580, "loan_status": "Pending", "city": "Bangalore"},
    {"application_id": "APP005", "customer_id": "C005", "loan_amount": 1000000, "credit_score": 800, "loan_status": "Approved", "city": "Pune"}
]
```

---

## Q13. Print application ID and loan status for each application

Expected output:

```text
APP001 Approved
APP002 Rejected
APP003 Approved
APP004 Pending
APP005 Approved
```

---

## Q14. Print eligible or not eligible for each application

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

## Q15. Count total approved applications

Expected output:

```text
Total Approved Applications: 3
```

---

## Q16. Calculate total approved loan amount

Only include applications where loan status is `"Approved"`.

Expected output:

```text
Total Approved Loan Amount: 2250000
```

---

## Q17. Count applications by city manually

Do not use any external library.

Expected output:

```text
Delhi: 2
Mumbai: 1
Bangalore: 1
Pune: 1
```

Hint:

Use an empty dictionary:

```python
city_count = {}
```

---

## Q18. Create a new list of high-value approved applications

Rule:

| Condition                                             |
| ----------------------------------------------------- |
| loan_status is `"Approved"` and loan_amount >= 700000 |

Expected output:

```python
[
    {"application_id": "APP003", "customer_id": "C003", "loan_amount": 750000, "credit_score": 710, "loan_status": "Approved", "city": "Delhi"},
    {"application_id": "APP005", "customer_id": "C005", "loan_amount": 1000000, "credit_score": 800, "loan_status": "Approved", "city": "Pune"}
]
```

---

# Part 5: `break` and `continue`

## Q19. Stop loop when loan amount is greater than 700000

Use this list:

```python
loan_amounts = [200000, 400000, 600000, 800000, 1000000]
```

Print amounts one by one, but stop the loop when amount is greater than `700000`.

Expected output:

```text
200000
400000
600000
```

---

## Q20. Skip pending applications

Use this list:

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

# Part 6: While Loop

## Q21. Print numbers from 1 to 5 using a while loop

Expected output:

```text
1
2
3
4
5
```

---

## Q22. Keep reducing loan balance

Create a variable:

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

# Part 7: Mini Practical Task

## Q23. Loan Application Summary Report

Use this data:

```python
loan_applications = [
    {"application_id": "APP001", "customer_id": "C001", "loan_amount": 500000, "credit_score": 760, "loan_status": "Approved", "city": "Delhi"},
    {"application_id": "APP002", "customer_id": "C002", "loan_amount": 300000, "credit_score": 620, "loan_status": "Rejected", "city": "Mumbai"},
    {"application_id": "APP003", "customer_id": "C003", "loan_amount": 750000, "credit_score": 710, "loan_status": "Approved", "city": "Delhi"},
    {"application_id": "APP004", "customer_id": "C004", "loan_amount": 200000, "credit_score": 580, "loan_status": "Pending", "city": "Bangalore"},
    {"application_id": "APP005", "customer_id": "C005", "loan_amount": 1000000, "credit_score": 800, "loan_status": "Approved", "city": "Pune"}
]
```

Create a summary report and print:

1. Total applications
2. Approved applications
3. Rejected applications
4. Pending applications
5. Total loan amount requested
6. Total approved loan amount
7. Average loan amount
8. High-value applications count
9. Applications from Delhi

Expected output:

```text
Total Applications: 5
Approved Applications: 3
Rejected Applications: 1
Pending Applications: 1
Total Loan Amount Requested: 2750000
Total Approved Loan Amount: 2250000
Average Loan Amount: 550000.0
High Value Applications Count: 3
Applications from Delhi: 2
```

---

# Evaluation Criteria

| Area                    | Marks |
| ----------------------- | ----: |
| Conditions              |    20 |
| Logical operators       |    15 |
| For loops               |    20 |
| List of dictionaries    |    25 |
| Break / continue        |    10 |
| While loop              |     5 |
| Clean code and comments |     5 |

**Total: 100 marks**
