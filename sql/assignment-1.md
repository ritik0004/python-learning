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
select * from  loan_applications

---

### 2. Show only approved loan applications.

Expected columns:

```text
application_id, customer_id, loan_amount, loan_status
```
select application_id, customer_id, loan_amount, loan_status from  loan_applications

---

### 3. Show applications where loan amount is greater than `500000`.

Expected columns:

```text
application_id, customer_id, loan_amount, city
```
select application_id, customer_id, loan_amount, city from  loan_applications where loan_amount >500000
---

### 4. Show applications from Delhi and Mumbai only.

Expected columns:

```text
application_id, customer_id, city, loan_status
```
### 4. Show applications from Delhi and Mumbai only.
select application_id, customer_id, loan_status, city from  loan_applications where city in ('Delhi','Mumbai')
---

### 5. Show applications where credit score is less than `650`.

Expected columns:

```text
application_id, customer_id, credit_score, loan_status
```
select application_id, customer_id, loan_status, credit_score from  loan_applications where credit_score<'650'
---

## Aggregation

### 6. Count total number of applications.

Expected output:

```text
total_applications
```
select count( distinct application_id) from loan_applications
---

### 7. Count applications by loan status.

Expected output:

```text
loan_status | total_applications
```
select total_applications, count(application_id) from loan_applications
group by loan_status
---

### 8. Calculate total approved loan amount.

Expected output:

```text
total_approved_loan_amount
```
select loan_status, sum(loan_amount) as total_approved_loan_amount from loan_applications
group by loan_status having  loan_status ='approved'
---

### 9. Calculate average loan amount by employment type.

Expected output:

```text
employment_type | avg_loan_amount
```
 select  employment_type, avg(loan_amount) as avg_loan_amount from loan_applications group by  employment_type
---

### 10. Find city-wise number of applications.

Expected output:

```text
city | total_applications
```
select city , count(application_id) from loan_applications group by city

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
select sum((select count(application_id) from loan_applications where loan_status='approved' )/(select count(application_id) from loan_applications)*100) 
as  approval_rate from loan_applications
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
select sum((select count(application_id) from loan_applications where loan_status='rejected' )/(select count(application_id) from loan_applications)*100)
as  rejection_rate from loan_applications
---

### 13. Calculate approval rate by city.

Expected output:

```text
city | total_applications | approved_applications | approval_rate
```
select city , sum(application_id) , (select count(application_id) from loan_applications where loan_status='approved') , 
sum ((select count(application_id) from loan_applications where loan_status='approved')/(select count(application_id) from loan_applications))*100
 from loan_applications group by city
---

### 14. Calculate approval rate by employment type.

Expected output:

```text
employment_type | total_applications | approved_applications | approval_rate
```
select employment_type , sum(application_id) , (select count(application_id) from loan_applications where loan_status='approved') , 
sum ((select count(application_id) from loan_applications where loan_status='approved')/(select count(application_id) from loan_applications))*100
as approval_rate from loan_applications
group by employment_type
---

### 15. Find total approved loan amount by city.

Expected output:

```text
city | total_approved_loan_amount
```
select city , sum(loan_amount) from loan_applications
grouup by city having loan_status='approved'
---

## Filtering With Aggregation

### 16. Find cities having more than 2 applications.

Expected output:

```text
city | total_applications
```
with cte as(select city,sum(application_id) as total_applications from  loan_applications group by city) , select city from cte where total_applications>2
---

### 17. Find employment types where average loan amount is greater than `400000`.

Expected output:

```text
employment_type | avg_loan_amount
```
with cte as(select employment_type,avg(loan_amount) as avg_loan_amount from  loan_applications group by employment_type) , select employment_type from cte where avg_loan_amount>400000
---

### 18. Find cities where total approved loan amount is greater than `1000000`.

Expected output:

```text
city | total_approved_loan_amount
```
with cte as(select (distinct city), sum(loan_amount) as total_approved_loan_amount from loan_applications where loan_status='approved' group by city),
select city , total_approved_loan_amount  from cte where total_approved_loan_amount>1000000
---

## Sorting

### 19. Show top 5 highest loan applications.

Expected columns:

```text
application_id, customer_id, loan_amount
```
select application_id, customer_id, loan_amount from loan_applications order by loan_amount desc limit 5
---

### 20. Show cities sorted by highest number of applications.

Expected output:

```text
city | total_applications
```
select city , sum(application_id) as xx from loan_applications group by city order by sum(application_id) desc
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
with cte as 
( select TO_CHAR(application_date, 'YYYY-MM') , application_id from loan_applications ) ,
select 
---

### 22. Find total approved loan amount by month.

Expected output:

```text
application_month | total_approved_loan_amount
```  with cte as ( 
select TO_CHAR(application_date, 'YYYY-MM') ,loan_amount from loan_applications where loan_status='approved')
select as xx , sum(loan_amount) from cte group  by xx
---

## Duplicate / Customer Behavior

### 23. Find customers who applied more than once.

Expected output:

```text
customer_id | total_applications
```
select customer_id,countapplication_id)
 from loan_applications group by customer_id having count(application_id)>2
---

### 24. Find total loan amount requested by each customer.

Expected output:

```text
customer_id | total_requested_amount
```
select customer_id,count(loan_amount)
from loan_applications group by customer_id having count(loan_amount)
---

### 25. Find the latest application date for each customer.

Expected output:

```text
customer_id | latest_application_date
```
select max(application_date)  over (partition by user_id) as latest_application_date
from loan_applications 
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
select application_id ,customer_id ,credit_score , case when credit_score > 750 then 'Excellent' 
when credit_scorebetween 700 and 749 then 'Good' 
when credit_score between 650nd 699then 'AVG'
else 'poor' end as credit_score_band from loan_applications
---

## 27. Count applications by credit score band.

Expected output:

```text
credit_score_band | total_applications
```
with cte as (select application_id ,customer_id ,credit_score , case when credit_score > 750 then 'Excellent' 
when credit_scorebetween 700 and 749 then 'Good' 
when credit_score between 650nd 699then 'AVG'
else 'poor' end as credit_score_band from loan_applications) , select credit_score_band , count(total_applications)
 group by credit_score_band
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
