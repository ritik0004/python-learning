**SQL Assignment for Class 1**.

The goal is to test his basics and make him start thinking in terms of **business metrics**, not just syntax.

---

# SQL Assignment 1 — Loan Application Analysis

## Objective

You are given loan application data. Write SQL queries to analyze application volume, approval trends, customer behavior, and loan performance.

---

# Table: `loan_applications`

```sql
CREATE TABLE loan_applications
(
      application_id      VARCHAR(20)
    , customer_id         VARCHAR(20)
    , application_date    DATE
    , loan_amount         DECIMAL(12,2)
    , loan_status         VARCHAR(20)
    , city                VARCHAR(50)
    , employment_type     VARCHAR(30)
    , credit_score        INT
)
;
```

---

# Sample Data

```sql
INSERT INTO loan_applications
(
      application_id
    , customer_id
    , application_date
    , loan_amount
    , loan_status
    , city
    , employment_type
    , credit_score
)
VALUES
      ('APP001', 'CUST001', '2024-01-05', 500000,  'Approved', 'Delhi',     'Salaried',      760)
    , ('APP002', 'CUST002', '2024-01-07', 300000,  'Rejected', 'Mumbai',    'Self-Employed', 620)
    , ('APP003', 'CUST003', '2024-01-10', 750000,  'Approved', 'Delhi',     'Salaried',      810)
    , ('APP004', 'CUST004', '2024-01-12', 200000,  'Pending',  'Bangalore', 'Student',       580)
    , ('APP005', 'CUST005', '2024-01-15', 1000000, 'Approved', 'Mumbai',    'Self-Employed', 700)
    , ('APP006', 'CUST006', '2024-01-18', 450000,  'Rejected', 'Delhi',     'Salaried',      650)
    , ('APP007', 'CUST007', '2024-01-20', 600000,  'Approved', 'Pune',      'Salaried',      730)
    , ('APP008', 'CUST008', '2024-01-22', 250000,  'Pending',  'Chennai',   'Self-Employed', 610)
    , ('APP009', 'CUST009', '2024-01-25', 900000,  'Approved', 'Bangalore', 'Salaried',      790)
    , ('APP010', 'CUST010', '2024-01-28', 150000,  'Rejected', 'Pune',      'Student',       560)
    , ('APP011', 'CUST001', '2024-02-02', 400000,  'Approved', 'Delhi',     'Salaried',      760)
    , ('APP012', 'CUST002', '2024-02-05', 350000,  'Pending',  'Mumbai',    'Self-Employed', 620)
    , ('APP013', 'CUST011', '2024-02-08', 800000,  'Approved', 'Hyderabad', 'Salaried',      840)
    , ('APP014', 'CUST012', '2024-02-10', 50000,   'Rejected', 'Chennai',   'Student',       520)
    , ('APP015', 'CUST013', '2024-02-12', 1200000, 'Approved', 'Delhi',     'Self-Employed', 720)
;
```

---

# Questions

## Basic SQL

### 1. Show all records from the table.

Expected columns: all columns.

---

### 2. Show only approved loan applications.

Expected columns:

```text
application_id, customer_id, loan_amount, loan_status
```

---

### 3. Show applications where loan amount is greater than `500000`.

Expected columns:

```text
application_id, customer_id, loan_amount, city
```

---

### 4. Show applications from Delhi and Mumbai only.

Expected columns:

```text
application_id, customer_id, city, loan_status
```

---

### 5. Show applications where credit score is less than `650`.

Expected columns:

```text
application_id, customer_id, credit_score, loan_status
```

---

## Aggregation

### 6. Count total number of applications.

Expected output:

```text
total_applications
```

---

### 7. Count applications by loan status.

Expected output:

```text
loan_status | total_applications
```

---

### 8. Calculate total approved loan amount.

Expected output:

```text
total_approved_loan_amount
```

---

### 9. Calculate average loan amount by employment type.

Expected output:

```text
employment_type | avg_loan_amount
```

---

### 10. Find city-wise number of applications.

Expected output:

```text
city | total_applications
```

---

## Business Metrics

### 11. Calculate approval rate.

Formula:

```text
approved applications / total applications * 100
```

Expected output:

```text
approval_rate
```

---

### 12. Calculate rejection rate.

Formula:

```text
rejected applications / total applications * 100
```

Expected output:

```text
rejection_rate
```

---

### 13. Calculate approval rate by city.

Expected output:

```text
city | total_applications | approved_applications | approval_rate
```

---

### 14. Calculate approval rate by employment type.

Expected output:

```text
employment_type | total_applications | approved_applications | approval_rate
```

---

### 15. Find total approved loan amount by city.

Expected output:

```text
city | total_approved_loan_amount
```

---

## Filtering With Aggregation

### 16. Find cities having more than 2 applications.

Expected output:

```text
city | total_applications
```

---

### 17. Find employment types where average loan amount is greater than `400000`.

Expected output:

```text
employment_type | avg_loan_amount
```

---

### 18. Find cities where total approved loan amount is greater than `1000000`.

Expected output:

```text
city | total_approved_loan_amount
```

---

## Sorting

### 19. Show top 5 highest loan applications.

Expected columns:

```text
application_id, customer_id, loan_amount
```

---

### 20. Show cities sorted by highest number of applications.

Expected output:

```text
city | total_applications
```

---

## Date-Based Questions

### 21. Count applications by month.

Expected output:

```text
application_month | total_applications
```

Hint:

Use date formatting based on the database.

For PostgreSQL:

```sql
TO_CHAR(application_date, 'YYYY-MM')
```

---

### 22. Find total approved loan amount by month.

Expected output:

```text
application_month | total_approved_loan_amount
```

---

## Duplicate / Customer Behavior

### 23. Find customers who applied more than once.

Expected output:

```text
customer_id | total_applications
```

---

### 24. Find total loan amount requested by each customer.

Expected output:

```text
customer_id | total_requested_amount
```

---

### 25. Find the latest application date for each customer.

Expected output:

```text
customer_id | latest_application_date
```

---

# Bonus Questions

## 26. Create a credit score band.

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

## 27. Count applications by credit score band.

Expected output:

```text
credit_score_band | total_applications
```

---

## 28. Calculate approval rate by credit score band.

Expected output:

```text
credit_score_band | total_applications | approved_applications | approval_rate
```

---

## 29. Find customers whose latest application was approved.

Expected output:

```text
customer_id | application_id | application_date | loan_status
```

Hint:

Use a CTE or subquery.

---

## 30. Create a final summary report with these metrics:

Expected output:

```text
total_applications
approved_applications
rejected_applications
pending_applications
approval_rate
rejection_rate
total_approved_loan_amount
average_loan_amount
```

---

# Submission Instructions

Ask him to submit:

| Item       | Requirement                        |
| ---------- | ---------------------------------- |
| SQL file   | `assignment_01_loan_analysis.sql`  |
| Screenshot | Query outputs for any 10 questions |
| Notes      | Any questions he could not solve   |
| GitHub     | Push the file to Month 1 repo      |

---

# Evaluation Criteria

| Area                            | Marks |
| ------------------------------- | ----: |
| Correct SQL syntax              |    30 |
| Correct business logic          |    30 |
| Proper use of GROUP BY / HAVING |    15 |
| Clean formatting                |    10 |
| Attempts bonus questions        |    10 |
| GitHub submission               |     5 |

Total: **100 marks**.
