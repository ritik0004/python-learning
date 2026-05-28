Here is a **directly shareable assignment** based on the function concepts you taught: function definition, calling, parameters, arguments, return values, local scope, nested functions, and default arguments.

---

# Python Assignment 3: Functions

## Objective

This assignment is designed to check your understanding of Python functions.

You will practice:

| Concept             | What You Should Understand                    |
| ------------------- | --------------------------------------------- |
| Function Definition | How to create a function using `def`          |
| Function Calling    | How to execute a function                     |
| Parameters          | Inputs accepted by a function                 |
| Arguments           | Actual values passed while calling a function |
| Return Values       | Sending output back from a function           |
| Local Variables     | Variables created inside a function           |
| Nested Functions    | Function inside another function              |
| Default Arguments   | Parameters with default values                |

---

## Submission Instructions

Create one Python file with the following name:

```python
assignment_03_functions.py
```

Add a comment before every question like this:

```python
# Q1. Create a function to calculate square of a number
```

Do not write all logic directly outside functions.
Each question must be solved using a function.

---

# Part 1: Function Definition and Calling

## Q1. Create a function to print your name

Create a function called `print_name()`.

The function should print your name.

Expected output:

```text
Gaurang
```

---

## Q2. Create a function to print multiples of a number

Create a function called `print_multiples(n)`.

The function should print the first 10 multiples of `n`.

Example function call:

```python
print_multiples(5)
```

Expected output:

```text
0
5
10
15
20
25
30
35
40
45
```

---

## Q3. Create a function to calculate square

Create a function called `square(num)`.

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

## Q4. Create a function to calculate cube

Create a function called `cube(num)`.

The function should return the cube of the number.

Example:

```python
print(cube(3))
```

Expected output:

```text
27
```

---

# Part 2: Parameters and Arguments

## Q5. Create a greeting function

Create a function called `greet(name)`.

The function should return:

```text
Hello, <name>!
```

Example:

```python
print(greet("Gaurang"))
```

Expected output:

```text
Hello, Gaurang!
```

---

## Q6. Create a function to add two numbers

Create a function called `add(a, b)`.

The function should return the sum of two numbers.

Example:

```python
result = add(10, 20)
print(result)
```

Expected output:

```text
30
```

---

## Q7. Create a function to subtract two numbers

Create a function called `subtract(a, b)`.

The function should return `a - b`.

Example:

```python
print(subtract(20, 5))
```

Expected output:

```text
15
```

---

## Q8. Create a function to multiply two numbers

Create a function called `multiply(a, b)`.

The function should return the multiplication of two numbers.

Example:

```python
print(multiply(4, 5))
```

Expected output:

```text
20
```

---

## Q9. Create a function to divide two numbers

Create a function called `divide(a, b)`.

The function should return `a / b`.

Example:

```python
print(divide(20, 4))
```

Expected output:

```text
5.0
```

---

# Part 3: Return Values

## Q10. Create a function to calculate total salary

Create a function called `calculate_total_salary(base_salary, bonus)`.

The function should return:

```text
base_salary + bonus
```

Example:

```python
print(calculate_total_salary(35000, 5000))
```

Expected output:

```text
40000
```

---

## Q11. Create a function to calculate loan EMI-like monthly amount

Create a function called `calculate_monthly_payment(loan_amount, months)`.

The function should return:

```text
loan_amount / months
```

Example:

```python
print(calculate_monthly_payment(120000, 12))
```

Expected output:

```text
10000.0
```

---

## Q12. Create a function to calculate approval rate

Create a function called `calculate_approval_rate(total_applications, approved_applications)`.

Formula:

```text
approved_applications / total_applications * 100
```

Example:

```python
print(calculate_approval_rate(10, 6))
```

Expected output:

```text
60.0
```

---

## Q13. Create a function to calculate rejection rate

Create a function called `calculate_rejection_rate(total_applications, rejected_applications)`.

Formula:

```text
rejected_applications / total_applications * 100
```

Example:

```python
print(calculate_rejection_rate(10, 3))
```

Expected output:

```text
30.0
```

---

# Part 4: Conditions Inside Functions

## Q14. Create a function to check loan eligibility

Create a function called `check_loan_eligibility(credit_score)`.

Rules:

| Credit Score | Output       |
| -----------: | ------------ |
|       >= 700 | Eligible     |
|        < 700 | Not Eligible |

Example:

```python
print(check_loan_eligibility(720))
```

Expected output:

```text
Eligible
```

---

## Q15. Create a function to return credit score band

Create a function called `get_credit_score_band(credit_score)`.

Rules:

| Credit Score | Band      |
| -----------: | --------- |
|       >= 750 | Excellent |
|      700–749 | Good      |
|      650–699 | Average   |
|        < 650 | Poor      |

Example:

```python
print(get_credit_score_band(760))
```

Expected output:

```text
Excellent
```

---

## Q16. Create a function to return loan amount category

Create a function called `get_loan_amount_category(loan_amount)`.

Rules:

|   Loan Amount | Category  |
| ------------: | --------- |
|    >= 1000000 | Very High |
| 500000–999999 | High      |
| 200000–499999 | Medium    |
|      < 200000 | Low       |

Example:

```python
print(get_loan_amount_category(750000))
```

Expected output:

```text
High
```

---

# Part 5: Default Arguments

## Q17. Create a greeting function with default value

Create a function called `greet_user(name, greeting="Hello")`.

Example 1:

```python
print(greet_user("Gaurang"))
```

Expected output:

```text
Hello, Gaurang!
```

Example 2:

```python
print(greet_user("Gaurang", "Hi"))
```

Expected output:

```text
Hi, Gaurang!
```

---

## Q18. Create a function with default country

Create a function called `user_location(name, city, country="India")`.

Example:

```python
print(user_location("Gaurang", "Gurugram"))
```

Expected output:

```text
Gaurang lives in Gurugram, India
```

Example:

```python
print(user_location("John", "New York", "USA"))
```

Expected output:

```text
John lives in New York, USA
```

---

## Q19. Create a function to calculate final price after discount

Create a function called `calculate_final_price(price, discount_percentage=10)`.

Formula:

```text
price - price * discount_percentage / 100
```

Example 1:

```python
print(calculate_final_price(1000))
```

Expected output:

```text
900.0
```

Example 2:

```python
print(calculate_final_price(1000, 20))
```

Expected output:

```text
800.0
```

---

# Part 6: Local Variables and Scope

## Q20. Create a function with a local variable

Create a function called `show_message()`.

Inside the function, create a variable:

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

## Q21. Create a function to calculate bonus

Create a function called `calculate_bonus(salary)`.

Inside the function:

```text
bonus = salary * 0.10
```

Return the bonus.

Example:

```python
print(calculate_bonus(50000))
```

Expected output:

```text
5000.0
```

Question:

Can you access the variable `bonus` outside the function?

Write your answer as a comment.

---

# Part 7: Nested Functions

## Q22. Create a nested function

Create a function called `outer_function()`.

Inside it, create another function called `inner_function()`.

`inner_function()` should print:

```text
I am inside inner function
```

`outer_function()` should call `inner_function()`.

Example:

```python
outer_function()
```

Expected output:

```text
I am inside inner function
```

---

## Q23. Create a nested function for loan summary

Create a function called `loan_summary(loan_amount, credit_score)`.

Inside this function, create two nested functions:

1. `get_loan_category()`
2. `get_credit_band()`

Rules for loan category:

|   Loan Amount | Category  |
| ------------: | --------- |
|    >= 1000000 | Very High |
| 500000–999999 | High      |
| 200000–499999 | Medium    |
|      < 200000 | Low       |

Rules for credit band:

| Credit Score | Band      |
| -----------: | --------- |
|       >= 750 | Excellent |
|      700–749 | Good      |
|      650–699 | Average   |
|        < 650 | Poor      |

The final function should return:

```text
Loan Category: High, Credit Band: Good
```

Example:

```python
print(loan_summary(750000, 720))
```

Expected output:

```text
Loan Category: High, Credit Band: Good
```

---

# Part 8: Functions With Lists

## Q24. Create a function to count approved applications

Use this list:

```python
loan_statuses = ["Approved", "Rejected", "Approved", "Pending", "Approved"]
```

Create a function called `count_approved_applications(statuses)`.

The function should return the number of approved applications.

Expected output:

```text
3
```

---

## Q25. Create a function to calculate total loan amount

Use this list:

```python
loan_amounts = [200000, 500000, 750000, 1000000]
```

Create a function called `calculate_total_loan_amount(amounts)`.

The function should return the total loan amount.

Expected output:

```text
2450000
```

---

## Q26. Create a function to find high-value loans

Use this list:

```python
loan_amounts = [200000, 500000, 750000, 1000000, 300000]
```

Create a function called `get_high_value_loans(amounts)`.

The function should return a new list containing loan amounts greater than or equal to `500000`.

Expected output:

```text
[500000, 750000, 1000000]
```

---

# Part 9: Functions With List of Dictionaries

Use this data for Q27 to Q30:

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

## Q27. Create a function to count total applications

Create a function called `count_total_applications(applications)`.

Expected output:

```text
5
```

---

## Q28. Create a function to count approved applications

Create a function called `count_approved_from_applications(applications)`.

Expected output:

```text
3
```

---

## Q29. Create a function to calculate total approved loan amount

Create a function called `calculate_approved_loan_amount(applications)`.

Expected output:

```text
2250000
```

---

## Q30. Create a function to generate loan summary report

Create a function called `generate_loan_summary(applications)`.

The function should return a dictionary with the following keys:

```python
{
    "total_applications": 5,
    "approved_applications": 3,
    "rejected_applications": 1,
    "pending_applications": 1,
    "total_requested_amount": 2750000,
    "total_approved_amount": 2250000,
    "approval_rate": 60.0
}
```

Expected output:

```text
{'total_applications': 5, 'approved_applications': 3, 'rejected_applications': 1, 'pending_applications': 1, 'total_requested_amount': 2750000, 'total_approved_amount': 2250000, 'approval_rate': 60.0}
```

---

# Bonus Questions

## Q31. Handle division by zero

Update the `calculate_approval_rate(total_applications, approved_applications)` function.

If `total_applications` is `0`, return `0`.

Example:

```python
print(calculate_approval_rate(0, 0))
```

Expected output:

```text
0
```

---

## Q32. Create a reusable percentage function

Create a function called `calculate_percentage(part, total)`.

Formula:

```text
part / total * 100
```

If `total` is `0`, return `0`.

Example:

```python
print(calculate_percentage(3, 5))
```

Expected output:

```text
60.0
```

---

## Q33. Use one function inside another function

Create a function called `generate_summary_with_percentage(applications)`.

Inside this function, use the `calculate_percentage(part, total)` function to calculate approval rate.

Expected output:

```python
{
    "total_applications": 5,
    "approved_applications": 3,
    "approval_rate": 60.0
}
```

---

# Important Notes

1. Use `return` when the function needs to send a value back.
2. Use `print()` only when you want to display output.
3. Variables created inside a function are local variables.
4. Default arguments are used when no value is passed for that parameter.
5. Each question should be solved using a function.
6. Keep your code clean and readable.

---

# Evaluation Criteria

| Area                              | Marks |
| --------------------------------- | ----: |
| Function definition and calling   |    15 |
| Parameters and arguments          |    15 |
| Return values                     |    15 |
| Conditions inside functions       |    15 |
| Default arguments                 |    10 |
| Local variables and scope         |    10 |
| Functions with lists/dictionaries |    15 |
| Clean code and comments           |     5 |

**Total: 100 marks**
