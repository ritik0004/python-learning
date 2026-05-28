# Feedback: Python Assignment 2 — Raman

## Overall Feedback

Good effort, Raman. You attempted most parts of the assignment and showed understanding of conditions, logical operators, loops, `break`, `continue`, and basic processing of lists and dictionaries.

However, the main issue is that several outputs are printed inside the loop instead of after the loop is complete. This causes intermediate values to print multiple times instead of final results. There are also some incomplete sections and indentation issues.

The most important focus area now is: **write the logic inside the loop, but print the final result after the loop finishes.**

---

## What You Did Well

| Area | Feedback |
|---|---|
| Conditions | You used `if`, `elif`, and `else` correctly in many questions. |
| Logical operators | You correctly used `and`, `or`, and `!=` in most cases. |
| For loops | You were able to loop through lists and print values. |
| Filtering values | You correctly printed high-value loans from a list. |
| List of dictionaries | You accessed dictionary values like `application["application_id"]` and `application["loan_status"]`. |
| `break` | You correctly stopped the loop when amount became greater than 700000. |
| `continue` | You correctly skipped `Pending` statuses. |
| While loop basics | You attempted the while loop and understood repeated execution partially. |

---

## Mistakes and Corrections

## 1. Printing Count Inside the Loop

You wrote:

```python
count = 0
for status in loan_statuses:
 if status == "Approved":
  count += 1
  print(count)
```

This prints the count every time an approved status is found.

Better version:

```python
count = 0
for status in loan_statuses:
    if status == "Approved":
        count += 1

print("Approved Applications:", count)
```

Rule:

```text
Update the count inside the loop.
Print the final count outside the loop.
```

---

## 2. Wrong Variable Used in Pending Count

You wrote:

```python
elif status == "Pending": 
  count +=1
  print("count_pending")
```

Here, you should update `count_pending`, not `count`.

Correct version:

```python
count_rejected = 0
count_pending = 0

for status in loan_statuses:
    if status == "Rejected":
        count_rejected += 1
    elif status == "Pending":
        count_pending += 1

print("Rejected Applications:", count_rejected)
print("Pending Applications:", count_pending)
```

---

## 3. Printing Text Instead of Variable Value

You wrote:

```python
print("count_rejected")
```

This prints the text `count_rejected`, not the value of the variable.

Correct:

```python
print(count_rejected)
```

or better:

```python
print("Rejected Applications:", count_rejected)
```

---

## 4. City Count Question Is Incomplete

You started:

```python
city_count = {}
for application in loan_applications:
```

but did not complete the logic.

Correct version:

```python
city_count = {}

for application in loan_applications:
    city = application["city"]

    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

print(city_count)
```

Expected output:

```text
{'Delhi': 2, 'Mumbai': 1, 'Bangalore': 1, 'Pune': 1}
```

---

## 5. High-Value Approved Applications Is Incomplete

The requirement was to create a new list of applications where:

```text
loan_status is Approved and loan_amount >= 700000
```

Correct version:

```python
high_value_approved = []

for application in loan_applications:
    if application["loan_status"] == "Approved" and application["loan_amount"] >= 700000:
        high_value_approved.append(application)

print(high_value_approved)
```

---

## 6. While Loop for Loan Balance

You wrote:

```python
while loan_balance > 0:
 loan_amount = loan_balance - monthly_payment
 print("Remaining balance:", loan_amount)
 print("loan fully paid")
```

Problem:

- `loan_balance` is never updated.
- This can lead to an infinite loop.
- `Loan fully paid` should print after the loop, not inside the loop.

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

## 7. Mini Practical Task Needs Cleaner Output

For the summary report, you are printing values inside loops, so outputs come multiple times.

Example:

```python
for application in loan_applications:
 if application["loan_status"] == "Approved":
  count_approved += 1
  print("Approved applications:", count_approved)
```

Correct approach:

```python
count_approved = 0

for application in loan_applications:
    if application["loan_status"] == "Approved":
        count_approved += 1

print("Approved Applications:", count_approved)
```

---

## Important Concepts to Revise

| Concept | Priority |
|---|---|
| Printing outside the loop | Very High |
| Counter variables | Very High |
| Dictionary-based counting | High |
| Appending records to a new list | High |
| While loop update condition | High |
| Clean indentation | Medium |

---

## Correct Pattern to Remember

For counting:

```python
count = 0

for item in items:
    if condition:
        count += 1

print(count)
```

For summing:

```python
total = 0

for item in items:
    total += item

print(total)
```

For filtering into a new list:

```python
new_list = []

for item in items:
    if condition:
        new_list.append(item)

print(new_list)
```

---

## Estimated Score

| Section | Score |
|---|---:|
| Conditions | 17 / 20 |
| Logical operators | 14 / 15 |
| For loops | 14 / 20 |
| List of dictionaries | 12 / 25 |
| Break / continue | 9 / 10 |
| While loop | 2 / 5 |
| Clean code and comments | 3 / 5 |

**Total: 71 / 100**

---

## Final Note

Good progress compared to the first assignment. You are starting to understand how loops and conditions work together. The biggest improvement needed is to avoid printing intermediate values inside the loop unless specifically required. First complete the calculation, then print the final result.
