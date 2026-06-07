# Feedback: Python Assignment 3 — Functions

Hi Gaurang,

Good attempt on the functions assignment. I can see that you have understood the basic idea of creating functions using `def`, passing inputs, and calling functions. You have also attempted most of the questions, which is a good sign.

However, this assignment also shows that we need to strengthen a few important fundamentals before moving ahead, especially:

* calling functions correctly
* using `return` properly
* difference between `print()` and `return`
* function parameters and arguments
* conditions inside functions
* loops inside functions
* working with lists and list of dictionaries

Overall, the effort is good, but the implementation needs correction and more practice.

---

## What You Did Well

### 1. You understood basic function syntax

You were able to define functions like:

```python
def square(num):
    print(num**2)
```

This shows that you understand the basic structure:

```python
def function_name(parameter):
    # logic
```

That is a good start.

---

### 2. You attempted parameters and arguments

You used parameters in multiple functions:

```python
def add(a, b):
    print(a+b)
```

```python
def calculate_approval_rate(total_applications, approved_applications):
    print(approved_applications / total_applications * 100)
```

This shows that you are starting to understand how inputs are passed into functions.

---

### 3. You attempted business-related logic

You tried to create functions for:

* loan eligibility
* credit score band
* loan amount category
* approval rate
* rejection rate
* total loan amount
* approved applications

This is good because we are not learning Python just for syntax. We are learning Python for data and business logic.

---

### 4. You correctly attempted list filtering in Q26

This was one of your better answers:

```python
def get_high_value_loans(loan_amounts):
    greater = []
    for amount in loan_amounts:
        if amount >= 500000:
            greater.append(amount)
    return greater
```

This shows that you are beginning to understand how to loop through a list, apply a condition, and create a new list.

Good work here.

---

## Major Corrections Needed

## 1. Function must be called using parentheses

In Q1, you wrote:

```python
my_name
```

This does not call the function.

Correct version:

```python
my_name()
```

Whenever you want to execute a function, you must use parentheses.

---

## 2. Be careful with loop update logic

In Q2, you wrote:

```python
i+1=i
```

This is invalid Python syntax.

Correct version:

```python
i = i + 1
```

or

```python
i += 1
```

Correct solution:

```python
def print_multiples(n):
    i = 0
    while i < 10:
        print(n * i)
        i += 1

print_multiples(5)
```

Also, if the question asks for first 10 multiples from `0` to `9`, use:

```python
while i < 10
```

not:

```python
while i < 11
```

---

## 3. Use `return` when the function is expected to give back a value

Many of your functions use `print()` instead of `return`.

Example:

```python
def square(num):
    print(num**2)
```

This prints the answer, but it does not return it.

Better version:

```python
def square(num):
    return num ** 2

print(square(5))
```

Why this matters:

```python
result = square(5)
```

If your function only prints and does not return, then `result` will store `None`.

For functions like `square`, `cube`, `add`, `subtract`, `multiply`, `divide`, `calculate_approval_rate`, etc., you should usually use `return`.

---

## 4. Function names must match the requirement

In Q9, the required function was:

```python
divide(a, b)
```

But you wrote:

```python
def dvide(a,b):
```

Spelling matters in programming. If the question asks for `divide`, the function name should be exactly `divide`.

Also, you called it like this:

```python
dvide(20/5)
```

But the function expects two inputs:

```python
def dvide(a, b):
```

Correct version:

```python
def divide(a, b):
    return a / b

print(divide(20, 5))
```

---

## 5. Default arguments were missed in some questions

For Q19, the function should have had a default discount percentage:

```python
def calculate_final_price(price, discount_percentage=10):
    return price - price * discount_percentage / 100
```

Your function works only when both values are passed:

```python
def calculate_final_price(price, discount_percentage):
```

But the assignment required that if discount is not passed, it should automatically take `10`.

Correct:

```python
def calculate_final_price(price, discount_percentage=10):
    return price - price * discount_percentage / 100

print(calculate_final_price(1000))
print(calculate_final_price(1000, 20))
```

---

## 6. Conditions need boundary correction

In Q15, you wrote:

```python
elif credit_score < 750 and credit_score > 700:
```

This skips `700`.

For example, if credit score is exactly `700`, it will not go into this condition.

Better version:

```python
def get_credit_score_band(credit_score):
    if credit_score >= 750:
        return "Excellent"
    elif credit_score >= 700:
        return "Good"
    elif credit_score >= 650:
        return "Average"
    else:
        return "Poor"
```

This is cleaner and avoids boundary mistakes.

---

## 7. Loan amount category output does not match the assignment

In Q16, the expected categories were:

|   Loan Amount | Category  |
| ------------: | --------- |
|    >= 1000000 | Very High |
| 500000–999999 | High      |
| 200000–499999 | Medium    |
|      < 200000 | Low       |

But your output uses:

```python
high
Good
Average
Poor
```

The logic should match the business requirement exactly.

Correct version:

```python
def get_loan_amount_category(loan_amount):
    if loan_amount >= 1000000:
        return "Very High"
    elif loan_amount >= 500000:
        return "High"
    elif loan_amount >= 200000:
        return "Medium"
    else:
        return "Low"
```

---

## 8. Syntax issue in `calculate_bonus`

You wrote:

```python
def calculate_bonus(salary):
    return bonus = salary * 0.10
```

This is invalid syntax.

You cannot assign a variable directly inside `return`.

Correct version:

```python
def calculate_bonus(salary):
    bonus = salary * 0.10
    return bonus

print(calculate_bonus(50000))
```

or simply:

```python
def calculate_bonus(salary):
    return salary * 0.10
```

---

## 9. Q25 has a logic mistake

You wrote:

```python
def calculate_total_loan_amount(loan_amounts):
    total = 0
    for amount in loan_amounts:
        total += amount

    return amount
```

You are returning `amount`, which will only return the last value from the list.

You should return `total`.

Correct version:

```python
def calculate_total_loan_amount(loan_amounts):
    total = 0

    for amount in loan_amounts:
        total += amount

    return total
```

Expected output:

```text
2450000
```

---

## 10. List of dictionaries part is still weak

You correctly mentioned that this is your weak part. That is okay, but this is a very important area.

In real data engineering, data often looks like this:

```python
loan_applications = [
    {"application_id": "APP001", "loan_amount": 500000, "loan_status": "Approved"},
    {"application_id": "APP002", "loan_amount": 300000, "loan_status": "Rejected"}
]
```

You need to become comfortable with:

```python
for application in loan_applications:
    print(application["application_id"])
```

This is very important because list of dictionaries is very similar to records coming from APIs, JSON files, and databases.

---

## Important Missing Issue

For Q27 to Q29, you used:

```python
loan_applications
```

but in your submitted code, the `loan_applications` list was not defined before those function calls.

So this will give an error unless the data is defined above.

Always make sure the data exists before using it.

Example:

```python
loan_applications = [
    {"application_id": "APP001", "customer_id": "C001", "loan_amount": 500000, "credit_score": 760, "loan_status": "Approved"},
    {"application_id": "APP002", "customer_id": "C002", "loan_amount": 300000, "credit_score": 620, "loan_status": "Rejected"},
    {"application_id": "APP003", "customer_id": "C003", "loan_amount": 750000, "credit_score": 710, "loan_status": "Approved"},
    {"application_id": "APP004", "customer_id": "C004", "loan_amount": 200000, "credit_score": 580, "loan_status": "Pending"},
    {"application_id": "APP005", "customer_id": "C005", "loan_amount": 1000000, "credit_score": 800, "loan_status": "Approved"}
]
```

---

# Corrected Examples to Study

## Correct `square`

```python
def square(num):
    return num ** 2

print(square(5))
```

---

## Correct `add`

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

---

## Correct loan eligibility

```python
def check_loan_eligibility(credit_score):
    if credit_score >= 700:
        return "Eligible"
    else:
        return "Not Eligible"

print(check_loan_eligibility(720))
```

---

## Correct approval rate

```python
def calculate_approval_rate(total_applications, approved_applications):
    if total_applications == 0:
        return 0

    return approved_applications / total_applications * 100

print(calculate_approval_rate(10, 6))
```

---

## Correct total approved loan amount

```python
loan_applications = [
    {"application_id": "APP001", "customer_id": "C001", "loan_amount": 500000, "credit_score": 760, "loan_status": "Approved"},
    {"application_id": "APP002", "customer_id": "C002", "loan_amount": 300000, "credit_score": 620, "loan_status": "Rejected"},
    {"application_id": "APP003", "customer_id": "C003", "loan_amount": 750000, "credit_score": 710, "loan_status": "Approved"},
    {"application_id": "APP004", "customer_id": "C004", "loan_amount": 200000, "credit_score": 580, "loan_status": "Pending"},
    {"application_id": "APP005", "customer_id": "C005", "loan_amount": 1000000, "credit_score": 800, "loan_status": "Approved"}
]

def calculate_approved_loan_amount(applications):
    total = 0

    for application in applications:
        if application["loan_status"] == "Approved":
            total += application["loan_amount"]

    return total

print(calculate_approved_loan_amount(loan_applications))
```

---

# Score Estimate

| Area                              |  Score |
| --------------------------------- | -----: |
| Function definition and calling   | 8 / 15 |
| Parameters and arguments          | 9 / 15 |
| Return values                     | 5 / 15 |
| Conditions inside functions       | 8 / 15 |
| Default arguments                 | 4 / 10 |
| Local variables and scope         | 4 / 10 |
| Functions with lists/dictionaries | 7 / 15 |
| Clean code and comments           |  3 / 5 |

## Estimated Score: 48 / 100

This is not a bad score for the first functions assignment, but it clearly shows that functions need one more round of practice.

---

# What You Need to Focus on Next

Before moving forward, focus on these five things:

1. Always call functions using parentheses: `function_name()`
2. Use `return` when the function should give back a value
3. Match function names and outputs exactly with the question
4. Practice loops inside functions
5. Practice list of dictionaries again and again

---

# Practice Task Before Next Class

Please redo these questions:

| Question | Reason                           |
| -------- | -------------------------------- |
| Q2       | loop syntax issue                |
| Q9       | function name and argument issue |
| Q15      | condition boundary issue         |
| Q16      | category output mismatch         |
| Q21      | local variable and return issue  |
| Q24      | count approved applications      |
| Q25      | total loan amount logic          |
| Q27–Q30  | list of dictionaries practice    |

---

# Final Feedback

You are understanding the concept at a surface level, which is a good start. But now we need to move from “I can write a function” to “I can write a correct, reusable function that returns the expected result.”

The main correction is:

```text
Do not only print inside functions. Learn when to return.
```

Once this becomes clear, your Python logic will improve quickly.
