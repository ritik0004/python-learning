Yes — below is a **follow-up SQL assignment** at a tougher level than the first one. It focuses on the exact gaps he had earlier: `GROUP BY`, `HAVING`, conditional aggregation, CTEs, date logic, joins, window functions, and business metric thinking.

You can copy-paste this directly.

---

# SQL Assignment 2: Advanced Loan Analytics

## Objective

This assignment is designed to strengthen your SQL skills beyond basic filtering and aggregation.

You will practice:

| Concept                 | What You Should Learn                        |
| ----------------------- | -------------------------------------------- |
| Joins                   | Combining data from multiple tables          |
| GROUP BY                | Aggregating data at the correct grain        |
| HAVING                  | Filtering after aggregation                  |
| CASE WHEN               | Creating business logic                      |
| Conditional Aggregation | Calculating metrics like approval rate       |
| CTEs                    | Breaking complex queries into readable steps |
| Window Functions        | Ranking and latest-record logic              |
| Date Functions          | Monthly and daily reporting                  |
| Business Metrics        | Thinking like a Data Analyst / Data Engineer |

---

## Submission Instructions

Create one SQL file:

```sql
assignment_02_advanced_loan_analytics.sql
```

Add a comment before every question like this:

```sql
-- Q1. Find total applications by city
```

Submit:

1. SQL file
2. Screenshots/output for at least 15 questions
3. Mention any questions you could not solve
4. Push the SQL file to GitHub

---

# Database Setup

## Table 1: `customers`

```sql
CREATE TABLE customers
(
      customer_id        VARCHAR(20)
    , customer_name      VARCHAR(100)
    , city               VARCHAR(50)
    , age                INT
    , employment_type    VARCHAR(30)
    , monthly_income     DECIMAL(12,2)
    , signup_date        DATE
)
;
```

## Table 2: `loan_applications`

```sql
CREATE TABLE loan_applications
(
      application_id      VARCHAR(20)
    , customer_id         VARCHAR(20)
    , application_date    DATE
    , loan_amount         DECIMAL(12,2)
    , loan_status         VARCHAR(20)
    , loan_type           VARCHAR(30)
    , credit_score        INT
)
;
```

## Table 3: `loan_payments`

```sql
CREATE TABLE loan_payments
(
      payment_id          VARCHAR(20)
    , application_id      VARCHAR(20)
    , payment_date        DATE
    , payment_amount      DECIMAL(12,2)
    , payment_status      VARCHAR(20)
)
;
```

---

# Sample Data

## Insert into `customers`

```sql
INSERT INTO customers
(
      customer_id
    , customer_name
    , city
    , age
    , employment_type
    , monthly_income
    , signup_date
)
VALUES
      ('CUST001', 'Amit Sharma',    'Delhi',     29, 'Salaried',      65000,  '2023-11-10')
    , ('CUST002', 'Priya Mehta',    'Mumbai',    34, 'Self-Employed', 85000,  '2023-12-05')
    , ('CUST003', 'Rahul Verma',    'Delhi',     26, 'Salaried',      48000,  '2024-01-12')
    , ('CUST004', 'Sneha Rao',      'Bangalore', 22, 'Student',       15000,  '2024-01-20')
    , ('CUST005', 'Karan Malhotra', 'Mumbai',    41, 'Self-Employed', 120000, '2023-10-15')
    , ('CUST006', 'Neha Gupta',     'Delhi',     31, 'Salaried',      72000,  '2024-02-01')
    , ('CUST007', 'Rohit Singh',    'Pune',      28, 'Salaried',      55000,  '2024-02-08')
    , ('CUST008', 'Ananya Iyer',    'Chennai',   36, 'Self-Employed', 90000,  '2024-02-10')
    , ('CUST009', 'Vikram Joshi',   'Bangalore', 45, 'Salaried',      110000, '2023-09-25')
    , ('CUST010', 'Meera Nair',     'Pune',      24, 'Student',       18000,  '2024-03-01')
    , ('CUST011', 'Arjun Kapoor',   'Hyderabad', 39, 'Salaried',      95000,  '2024-03-05')
    , ('CUST012', 'Riya Sen',       'Chennai',   23, 'Student',       12000,  '2024-03-08')
    , ('CUST013', 'Manav Batra',    'Delhi',     37, 'Self-Employed', 100000, '2024-03-12')
    , ('CUST014', 'Simran Kaur',    'Jaipur',    30, 'Salaried',      52000,  '2024-03-15')
    , ('CUST015', 'Dev Patel',      'Ahmedabad', 33, 'Self-Employed', 78000,  '2024-03-18')
;
```

## Insert into `loan_applications`

```sql
INSERT INTO loan_applications
(
      application_id
    , customer_id
    , application_date
    , loan_amount
    , loan_status
    , loan_type
    , credit_score
)
VALUES
      ('APP001', 'CUST001', '2024-01-05', 500000,  'Approved', 'Personal', 760)
    , ('APP002', 'CUST002', '2024-01-07', 300000,  'Rejected', 'Personal', 620)
    , ('APP003', 'CUST003', '2024-01-10', 750000,  'Approved', 'Auto',     810)
    , ('APP004', 'CUST004', '2024-01-12', 200000,  'Pending',  'Personal', 580)
    , ('APP005', 'CUST005', '2024-01-15', 1000000, 'Approved', 'Business', 700)
    , ('APP006', 'CUST006', '2024-01-18', 450000,  'Rejected', 'Personal', 650)
    , ('APP007', 'CUST007', '2024-01-20', 600000,  'Approved', 'Auto',     730)
    , ('APP008', 'CUST008', '2024-01-22', 250000,  'Pending',  'Personal', 610)
    , ('APP009', 'CUST009', '2024-01-25', 900000,  'Approved', 'Business', 790)
    , ('APP010', 'CUST010', '2024-01-28', 150000,  'Rejected', 'Personal', 560)
    , ('APP011', 'CUST001', '2024-02-02', 400000,  'Approved', 'Personal', 760)
    , ('APP012', 'CUST002', '2024-02-05', 350000,  'Pending',  'Auto',     620)
    , ('APP013', 'CUST011', '2024-02-08', 800000,  'Approved', 'Business', 840)
    , ('APP014', 'CUST012', '2024-02-10', 50000,   'Rejected', 'Personal', 520)
    , ('APP015', 'CUST013', '2024-02-12', 1200000, 'Approved', 'Business', 720)
    , ('APP016', 'CUST014', '2024-02-15', 300000,  'Approved', 'Personal', 710)
    , ('APP017', 'CUST015', '2024-02-18', 650000,  'Rejected', 'Auto',     640)
    , ('APP018', 'CUST003', '2024-03-01', 850000,  'Approved', 'Business', 810)
    , ('APP019', 'CUST005', '2024-03-05', 500000,  'Pending',  'Personal', 700)
    , ('APP020', 'CUST009', '2024-03-10', 1100000, 'Approved', 'Business', 790)
;
```

## Insert into `loan_payments`

```sql
INSERT INTO loan_payments
(
      payment_id
    , application_id
    , payment_date
    , payment_amount
    , payment_status
)
VALUES
      ('PAY001', 'APP001', '2024-02-05', 50000,  'Paid')
    , ('PAY002', 'APP001', '2024-03-05', 50000,  'Paid')
    , ('PAY003', 'APP003', '2024-02-10', 75000,  'Paid')
    , ('PAY004', 'APP005', '2024-02-15', 100000, 'Paid')
    , ('PAY005', 'APP005', '2024-03-15', 100000, 'Missed')
    , ('PAY006', 'APP007', '2024-02-20', 60000,  'Paid')
    , ('PAY007', 'APP009', '2024-02-25', 90000,  'Paid')
    , ('PAY008', 'APP011', '2024-03-02', 40000,  'Paid')
    , ('PAY009', 'APP013', '2024-03-08', 80000,  'Paid')
    , ('PAY010', 'APP015', '2024-03-12', 120000, 'Missed')
    , ('PAY011', 'APP016', '2024-03-15', 30000,  'Paid')
    , ('PAY012', 'APP018', '2024-03-20', 85000,  'Paid')
    , ('PAY013', 'APP020', '2024-03-25', 110000, 'Paid')
;
```

---

# Part 1: Revision of Aggregation and Business Metrics

## Q1. Count total loan applications.

Expected output:

```text
total_applications
```

---

## Q2. Count applications by loan status.

Expected output:

```text
loan_status | total_applications
```

---

## Q3. Calculate total approved loan amount.

Expected output:

```text
total_approved_loan_amount
```

---

## Q4. Calculate approval rate.

Formula:

```text
approved applications / total applications * 100
```

Expected output:

```text
approval_rate
```

---

## Q5. Calculate loan status summary in one query.

Expected output:

```text
total_applications | approved_applications | rejected_applications | pending_applications
```

Hint: Use `CASE WHEN`.

---

# Part 2: Joins

## Q6. Show each loan application with customer details.

Expected output:

```text
application_id | customer_id | customer_name | city | employment_type | loan_amount | loan_status
```

---

## Q7. Show approved loan applications with customer name and city.

Expected output:

```text
application_id | customer_name | city | loan_amount | loan_type | credit_score
```

---

## Q8. Find city-wise total applications using `customers` and `loan_applications`.

Expected output:

```text
city | total_applications
```

---

## Q9. Find employment-type-wise approval rate.

Expected output:

```text
employment_type | total_applications | approved_applications | approval_rate
```

---

## Q10. Find customer-wise total loan amount requested.

Expected output:

```text
customer_id | customer_name | total_requested_amount
```

---

# Part 3: GROUP BY, HAVING, and Filtering After Aggregation

## Q11. Find cities with more than 2 loan applications.

Expected output:

```text
city | total_applications
```

---

## Q12. Find employment types where average loan amount is greater than `500000`.

Expected output:

```text
employment_type | avg_loan_amount
```

---

## Q13. Find customers who applied more than once.

Expected output:

```text
customer_id | customer_name | total_applications
```

---

## Q14. Find loan types where total approved loan amount is greater than `1500000`.

Expected output:

```text
loan_type | total_approved_loan_amount
```

---

# Part 4: CASE WHEN

## Q15. Create credit score bands.

Rules:

| Credit Score | Band      |
| -----------: | --------- |
|       >= 750 | Excellent |
|      700–749 | Good      |
|      650–699 | Average   |
|        < 650 | Poor      |

Expected output:

```text
application_id | customer_id | credit_score | credit_score_band
```

---

## Q16. Count applications by credit score band.

Expected output:

```text
credit_score_band | total_applications
```

---

## Q17. Calculate approval rate by credit score band.

Expected output:

```text
credit_score_band | total_applications | approved_applications | approval_rate
```

---

## Q18. Create loan amount bands.

Rules:

|   Loan Amount | Band      |
| ------------: | --------- |
|    >= 1000000 | Very High |
| 500000–999999 | High      |
| 200000–499999 | Medium    |
|      < 200000 | Low       |

Expected output:

```text
application_id | loan_amount | loan_amount_band
```

---

## Q19. Calculate total applications and approved applications by loan amount band.

Expected output:

```text
loan_amount_band | total_applications | approved_applications
```

---

# Part 5: Date-Based Reporting

## Q20. Count applications by month.

Expected output:

```text
application_month | total_applications
```

For PostgreSQL, use:

```sql
TO_CHAR(application_date, 'YYYY-MM')
```

---

## Q21. Calculate monthly approval rate.

Expected output:

```text
application_month | total_applications | approved_applications | approval_rate
```

---

## Q22. Calculate monthly total approved loan amount.

Expected output:

```text
application_month | total_approved_loan_amount
```

---

## Q23. Find the first application date for each customer.

Expected output:

```text
customer_id | customer_name | first_application_date
```

---

## Q24. Find the latest application date for each customer.

Expected output:

```text
customer_id | customer_name | latest_application_date
```

---

# Part 6: CTEs

## Q25. Using a CTE, find cities with approval rate greater than 60%.

Expected output:

```text
city | total_applications | approved_applications | approval_rate
```

---

## Q26. Using a CTE, find customers whose total requested loan amount is greater than `800000`.

Expected output:

```text
customer_id | customer_name | total_requested_amount
```

---

## Q27. Using a CTE, calculate credit score band and then count applications by band.

Expected output:

```text
credit_score_band | total_applications
```

---

## Q28. Using a CTE, calculate loan amount band and then calculate total approved loan amount by band.

Expected output:

```text
loan_amount_band | total_approved_loan_amount
```

---

# Part 7: Window Functions

## Q29. Rank loan applications by loan amount from highest to lowest.

Expected output:

```text
application_id | customer_id | loan_amount | loan_rank
```

Hint:

Use `RANK()` or `DENSE_RANK()`.

---

## Q30. Find the highest loan application for each city.

Expected output:

```text
city | application_id | customer_id | loan_amount
```

Hint:

Use `ROW_NUMBER()` with `PARTITION BY city`.

---

## Q31. Find the latest loan application for each customer.

Expected output:

```text
customer_id | customer_name | application_id | application_date | loan_status
```

Hint:

Use `ROW_NUMBER()` with `PARTITION BY customer_id ORDER BY application_date DESC`.

---

## Q32. Find customers whose latest application was approved.

Expected output:

```text
customer_id | customer_name | application_id | application_date | loan_status
```

---

# Part 8: Payment Analysis

## Q33. Show approved loan applications with total payment received.

Expected output:

```text
application_id | customer_id | loan_amount | total_payment_received
```

---

## Q34. Find applications where payment status has at least one missed payment.

Expected output:

```text
application_id | customer_id | loan_amount | missed_payment_count
```

---

## Q35. Calculate payment recovery percentage for each approved application.

Formula:

```text
total paid amount / loan amount * 100
```

Expected output:

```text
application_id | customer_id | loan_amount | total_paid_amount | recovery_percentage
```

Only include approved applications.

---

## Q36. Find customers with missed payments.

Expected output:

```text
customer_id | customer_name | application_id | missed_payment_count
```

---

# Part 9: Final Business Reports

## Q37. Create a city-level loan performance report.

Expected output:

```text
city
total_applications
approved_applications
rejected_applications
pending_applications
approval_rate
total_approved_loan_amount
avg_credit_score
```

---

## Q38. Create an employment-type-level performance report.

Expected output:

```text
employment_type
total_applications
approved_applications
rejected_applications
pending_applications
approval_rate
avg_loan_amount
total_approved_loan_amount
```

---

## Q39. Create a loan-type-level performance report.

Expected output:

```text
loan_type
total_applications
approved_applications
approval_rate
total_requested_amount
total_approved_amount
avg_credit_score
```

---

## Q40. Create a customer-level loan summary.

Expected output:

```text
customer_id
customer_name
city
employment_type
total_applications
approved_applications
rejected_applications
pending_applications
total_requested_amount
latest_application_date
```

---

# Bonus Questions

## Q41. Find the top 3 customers by total requested loan amount.

Expected output:

```text
customer_id | customer_name | total_requested_amount | customer_rank
```

---

## Q42. Find the top customer by total requested loan amount in each city.

Expected output:

```text
city | customer_id | customer_name | total_requested_amount
```

---

## Q43. Find customers who have applied more than once and have at least one approved application.

Expected output:

```text
customer_id | customer_name | total_applications | approved_applications
```

---

## Q44. Find customers whose approved loan amount is more than 10 times their monthly income.

Expected output:

```text
customer_id | customer_name | monthly_income | total_approved_loan_amount | income_multiple
```

---

## Q45. Create a final portfolio-style report combining customer, application, and payment data.

Expected output:

```text
customer_id
customer_name
city
employment_type
total_applications
approved_applications
total_approved_loan_amount
total_paid_amount
missed_payment_count
latest_application_date
customer_risk_category
```

Risk category rules:

| Rule                       | Risk Category |
| -------------------------- | ------------- |
| missed_payment_count >= 1  | High Risk     |
| average credit_score < 650 | Medium Risk   |
| otherwise                  | Low Risk      |


# Evaluation Criteria

| Area                                  | Marks |
| ------------------------------------- | ----: |
| Correct SQL syntax                    |    20 |
| Correct joins                         |    15 |
| Correct aggregation logic             |    20 |
| CASE WHEN and conditional aggregation |    15 |
| CTE usage                             |    10 |
| Window functions                      |    10 |
| Business report quality               |     5 |
| Clean formatting                      |     5 |

**Total: 100 marks**
