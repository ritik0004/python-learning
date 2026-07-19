# Python Practice Assignment -- Functions & Data Processing

## Instructions

-   Do NOT use ChatGPT or any AI tools.
-   Every function must return a value.
-   Avoid using print() inside functions unless explicitly asked.
-   Test every function after writing it.
-   Follow proper naming conventions.
-   Write clean, readable code.

## Dataset

``` python
loan_applications = [
    {"application_id":"APP001","customer_id":"C001","loan_amount":500000,"credit_score":760,"loan_status":"Approved","city":"Delhi"},
    {"application_id":"APP002","customer_id":"C002","loan_amount":300000,"credit_score":620,"loan_status":"Rejected","city":"Mumbai"},
    {"application_id":"APP003","customer_id":"C003","loan_amount":750000,"credit_score":710,"loan_status":"Approved","city":"Delhi"},
    {"application_id":"APP004","customer_id":"C004","loan_amount":200000,"credit_score":580,"loan_status":"Pending","city":"Bangalore"},
    {"application_id":"APP005","customer_id":"C005","loan_amount":1000000,"credit_score":800,"loan_status":"Approved","city":"Pune"},
    {"application_id":"APP006","customer_id":"C006","loan_amount":650000,"credit_score":690,"loan_status":"Approved","city":"Delhi"},
    {"application_id":"APP007","customer_id":"C007","loan_amount":450000,"credit_score":640,"loan_status":"Rejected","city":"Mumbai"},
    {"application_id":"APP008","customer_id":"C008","loan_amount":850000,"credit_score":730,"loan_status":"Approved","city":"Chennai"}
]
```

## Questions

### Part 1 -- Basic Functions

1.  get_name()
2.  square(num)
3.  cube(num)
4.  Return larger of two numbers.
5.  Return "Even" or "Odd".

### Part 2 -- Function Parameters

6.  greet(name)
7.  greet(name, greeting="Hello")
8.  calculate_bonus(salary)
9.  calculate_final_salary(salary, bonus)
10. calculate_monthly_emi(loan_amount, months)

### Part 3 -- Conditions

11. Loan eligibility
12. Credit score band
13. Loan amount category
14. Return True if loan \> 500000
15. Return True if score \>700 and loan \>500000

### Part 4 -- Loops

16. Total loan amount
17. Average loan amount
18. Approved count
19. Rejected count
20. Pending count
21. Highest loan
22. Lowest loan

### Part 5 -- Lists

23. Return approved applications
24. Return rejected applications
25. Return Delhi applications
26. Return loan amounts \>=700000
27. Return customer IDs with approved loans

### Part 6 -- Dictionary Processing

28. City counts
29. Status counts
30. Credit score band counts

### Part 7 -- Function Composition

31. calculate_approval_rate()
32. calculate_average_credit_score()
33. calculate_total_approved_loan_amount()
34. calculate_total_rejected_loan_amount()
35. get_high_value_approved_applications()

### Part 8 -- Debugging

For each snippet: - Explain the mistake. - Correct it.

``` python
def square(num):
    print(num**2)
result = square(5)
print(result)
```

``` python
def total(numbers):
    total=0
    for n in numbers:
        total+=n
    return n
```

``` python
cities=[]
for app in loan_applications:
    if app["city"]=="Delhi":
        cities=app["city"]
return cities
```

``` python
approved=0
for app in loan_applications:
    if app["loan_status"]="Approved":
        approved+=1
```

``` python
def greet(name):
return "Hello "+name
```

### Part 9 -- Mini Project

Implement:

``` python
generate_summary_report(loan_applications)
```

Return: - total applications - approved - rejected - pending - total
requested amount - total approved amount - highest loan - lowest loan -
average loan amount - approval rate - city counts

## Submission

-   Submit one assignment.py file.
-   Use return instead of print.
-   Ensure the program runs without syntax errors.
-   Test every function before submission.
