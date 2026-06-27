---

# 📘 Python Assignment – Reading Data from Files (JSON, CSV, TXT)

## 🎯 Objective

The goal of this assignment is to understand how to **read data from different file formats** and convert them into **Pandas DataFrames**.

You will work with:

* JSON files
* CSV files
* Text (TXT) files

---

## 📁 Mandatory Folder Structure

Create the following folder structure **exactly as shown**:

```
file_reading_assignment/
│
├── data/
│   ├── customers.json
│   ├── loan_applications.csv
│   └── target_roles.txt
│
└── read_files.py
```

---

## 📄 Data Files

### 1️⃣ `data/customers.json`

```json
[
  {"customer_id": "C001", "customer_name": "Gaurang", "city": "Delhi", "employment_type": "Salaried"},
  {"customer_id": "C002", "customer_name": "Raman", "city": "Mumbai", "employment_type": "Self-Employed"},
  {"customer_id": "C003", "customer_name": "Amit", "city": "Bangalore", "employment_type": "Salaried"},
  {"customer_id": "C004", "customer_name": "Neha", "city": "Pune", "employment_type": "Salaried"},
  {"customer_id": "C005", "customer_name": "Sneha", "city": "Delhi", "employment_type": "Self-Employed"},
  {"customer_id": "C006", "customer_name": "Rohit", "city": "Chennai", "employment_type": "Salaried"},
  {"customer_id": "C007", "customer_name": "Ananya", "city": "Hyderabad", "employment_type": "Self-Employed"}
]
```

---

### 2️⃣ `data/loan_applications.csv`

```csv
application_id,customer_id,loan_amount,loan_status,credit_score
APP001,C001,500000,Approved,760
APP002,C002,300000,Rejected,620
APP003,C001,750000,Approved,710
APP004,C003,200000,Pending,580
APP005,C004,1000000,Approved,800
APP006,C005,400000,Rejected,650
APP007,C002,900000,Approved,740
APP008,C006,250000,Pending,600
APP009,C007,850000,Approved,780
```

---

### 3️⃣ `data/target_roles.txt`

```
Data Engineer
Analytics Engineer
AI Engineer
Machine Learning Engineer
Cloud Data Engineer
Backend Engineer
```

---

## 🧠 Tasks to Perform

### ✅ Task 1: Read JSON File

* Read `customers.json`
* Convert it into a Pandas DataFrame
* Print the DataFrame
* Print the shape of the DataFrame

---

### ✅ Task 2: Read CSV File

* Read `loan_applications.csv`
* Convert it into a Pandas DataFrame
* Print the DataFrame
* Print the column names

---

### ✅ Task 3: Read TXT File

* Read `target_roles.txt`
* Convert it into a Pandas DataFrame
* Column name must be: `target_role`
* Print the DataFrame

---

### ✅ Task 4: Basic Validation Checks

Print the following:

1. Total number of customers
2. Total number of loan applications
3. Total number of target roles


## 🎓 Expected Learning Outcomes

By completing this assignment, you will learn:

* How file paths work in Python
* How to read **JSON, CSV, and TXT** files
* How to convert raw file data into Pandas DataFrames
* Why DataFrames are the foundation of data engineering workflows

---

## 📤 Submission Instructions

Submit:

* `read_files.ipynb`
* Screenshot of program output

Guidelines:

* Code must run without errors
* Do not hardcode data inside Python
* Use meaningful variable names

---