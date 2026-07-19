# Feedback: Python Assignment 2 — Gaurang

## Overall Feedback

Good attempt, Gaurang. You solved several condition and loop-based questions correctly, especially the early questions on eligibility, credit score banding, high-value loans, logical operators, and simple loops.

However, this assignment also shows that you need more practice with list-of-dictionaries logic, counters using loops, `while` loop syntax, and completing all questions. It is good that you clearly mentioned where you used ChatGPT and where you did not understand the logic. That honesty is useful because now we know exactly what to revise.

---

## What You Did Well

| Area | Feedback |
|---|---|
| Basic conditions | You correctly used `if`, `elif`, and `else` for many beginner-level problems. |
| Credit score logic | You understood the broad idea of credit score bands. |
| High-value loan check | Correct logic for checking loan amount. |
| Logical operators | You correctly used `and` in eligibility and risk checks. |
| For loop basics | You correctly looped through skills and loan amounts. |
| Filtering values | You correctly printed loan amounts greater than or equal to 500000. |
| List of dictionaries basics | You were able to access `application_id` and `loan_status` from dictionaries. |
| Skipping pending statuses | You solved this using `pass` and `else`; it works logically, though `continue` would be better for this question. |

---

## Mistakes and Corrections

## 1. Credit Score Band Labels

You wrote:

```python
elif credit_score<= 699 and credit_score>= 650:
    print("Good")
else:
    print("bad")
```

Expected labels were:

| Credit Score | Band |
|---:|---|
| >= 750 | Excellent |
| 700–749 | Good |
| 650–699 | Average |
| < 650 | Poor |

Correct version:

```python
credit_score = 760

if credit_score >= 750:
    print("Excellent")
elif credit_score >= 700:
    print("Good")
elif credit_score >= 650:
    print("Average")
else:
    print("Poor")
```

You do not need to write both sides like `<= 749 and >= 700` because earlier conditions already handle the upper range.

---

## 2. Employment Type Case Sensitivity

You wrote:

```python
elif employment_type=="self-Employed":
```

But expected value was:

```python
"Self-Employed"
```

Python is case-sensitive.

Correct version:

```python
elif employment_type == "Self-Employed":
    print("Business income profile")
```

---

## 3. Metro City Check Is Incomplete

You wrote:

```python
if city in
```

This is incomplete and will give a syntax error.

Correct version:

```python
city = "Delhi"

if city in ["Delhi", "Mumbai", "Bangalore"]:
    print("Metro city")
else:
    print("Non-metro city")
```

---

## 4. Rejection Check Logic Is Incorrect

You wrote:

```python
loan_status = "Pending"
if loan_status < 650:
    print("Application not approved yet")
else:
    print("Application approved")
```

Here, `loan_status` is a string, but you are comparing it with a number `650`. That is incorrect.

Correct version:

```python
loan_status = "Pending"

if loan_status != "Approved":
    print("Application not approved yet")
else:
    print("Application approved")
```

---

## 5. Counting Approved Applications Using Loop

You used:

```python
approved = loan_statuses.count("Approved")
```

This gives the correct answer, but the purpose of the assignment was to practice loop-based counting.

Expected loop-based version:

```python
loan_statuses = ["Approved", "Rejected", "Approved", "Pending", "Approved"]

approved_count = 0

for status in loan_statuses:
    if status == "Approved":
        approved_count += 1

print("Approved Applications:", approved_count)
```

This pattern is very important for data processing.

---

## 6. List of Dictionaries Needs More Practice

You completed Q13 with help, but Q14 to Q18 were mostly missing.

This is an important area because real data often looks like a list of dictionaries.

Example pattern:

```python
for application in loan_applications:
    print(application["application_id"], application["loan_status"])
```

For approved count:

```python
approved_count = 0

for application in loan_applications:
    if application["loan_status"] == "Approved":
        approved_count += 1

print("Total Approved Applications:", approved_count)
```

For total approved loan amount:

```python
total_approved_amount = 0

for application in loan_applications:
    if application["loan_status"] == "Approved":
        total_approved_amount += application["loan_amount"]

print("Total Approved Loan Amount:", total_approved_amount)
```

---

## 7. Break Logic Is Partially Correct But Should Use `break`

You wrote:

```python
for i in loan_amounts:
    if i <700000:
        print(i)
```

This prints the correct values for the given data, but it does not use `break`.

Expected version:

```python
loan_amounts = [200000, 400000, 600000, 800000, 1000000]

for amount in loan_amounts:
    if amount > 700000:
        break
    print(amount)
```

Why this matters:

`break` stops the loop completely when the condition is met.

---

## 8. Continue Question Should Use `continue`

You wrote:

```python
for i in loan_statuses:
    if i=="Pending":
        pass
    else:
        print(i)
```

This works, but the assignment was meant to practice `continue`.

Better version:

```python
for status in loan_statuses:
    if status == "Pending":
        continue
    print(status)
```

---

## 9. While Loop Syntax Is Incorrect

You wrote:

```python
while loan_balance =0 :
    print(loan_balance-monthly_payment)
```

Problems:

- `=` is assignment, not comparison.
- In conditions, use `==`, `>`, `<`, etc.
- The loop should continue while loan balance is greater than 0.
- You need to update `loan_balance` inside the loop.

Correct version:

```python
loan_balance = 500000
monthly_payment = 100000

while loan_balance > 0:
    loan_balance = loan_balance - monthly_payment
    print("Remaining Balance:", loan_balance)

print("Loan fully paid")
```

---

## 10. Mini Practical Task Was Not Attempted

The final summary report was not completed. This is an important question because it combines all concepts:

- loops
- conditions
- counters
- totals
- average calculation
- dictionary access

You should reattempt this after revising list-of-dictionaries.

---

## Important Concepts to Revise

| Concept | Priority |
|---|---|
| `if city in [...]` syntax | High |
| String comparison vs number comparison | High |
| Counting using loops | Very High |
| List of dictionaries | Very High |
| `break` and `continue` | High |
| `while` loop syntax | High |
| Completing all questions | High |

---

## Suggested Practice Before Next Class

Use this data:

```python
loan_applications = [
    {"application_id": "APP001", "loan_amount": 500000, "loan_status": "Approved", "city": "Delhi"},
    {"application_id": "APP002", "loan_amount": 300000, "loan_status": "Rejected", "city": "Mumbai"},
    {"application_id": "APP003", "loan_amount": 750000, "loan_status": "Approved", "city": "Delhi"}
]
```

Write code to calculate:

1. Total applications  
2. Approved applications  
3. Rejected applications  
4. Total loan amount  
5. Total approved loan amount  
6. Applications from Delhi  

Do not use `.count()` for this practice. Use loops.

---

## Estimated Score

| Section | Score |
|---|---:|
| Conditions | 13 / 20 |
| Logical operators | 10 / 15 |
| For loops | 14 / 20 |
| List of dictionaries | 6 / 25 |
| Break / continue | 5 / 10 |
| While loop | 0 / 5 |
| Clean code and comments | 3 / 5 |

**Total: 51 / 100**

---

## Final Note

You have started well, but this assignment shows that the next focus should be loops with dictionaries. Do not worry about this score; the important thing is that we now know where the gap is. Once you understand how to loop through a list of dictionaries and update counters/totals, a lot of Python data-processing logic will become easier.
