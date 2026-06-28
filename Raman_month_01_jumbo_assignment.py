# Part 1: Data Types

## Q1. Create variables and print their data types
#Create the following variables:

#Print the type of each variable.

#print(type(student_name)) #string
#print(type(age))    #int
#print(type(monthly_salary)) # float
#print(type(is_working)) #boolean
#print(type(skills)) #list
#print(type(profile)) #dictionary
#print(type(coordinates)) #tuple
#print(type(unique_cities)) #set

## Q2. Create a student profile dictionary

student_profile = {"name": 'Ramandeep', 'age': 26, 'target_role': "Data and AI Engineer",'skills': ['SQL','Python','Excel','Power BI'], 'monthly_salary':15}

# Part 2: Indexing and Access

skills = ["SQL", "Python", "Excel", "Power BI", "GA4"]

## Q3. Print the first skill
print(skills[0])

## Q4. Print the third skill
print(skills [2])

## Q5. Print the last skill using positive indexing
print(skills[4])

## Q6. Print the last skill using negative indexing
print(skills[-1])

employee = {
    "name": "Gaurang",
    "role": "Product Analyst",
    "salary": 35000,
    "skills": ["SQL", "Python", "GA4"]
}

## Q7. Print the employee name
print(employee["name"])

## Q8. Print the employee role
print(employee["role"])

## Q9. Print the second skill from the skills list inside the dictionary
print(employee["skills"] [1])

## Q10. Print the total number of skills
print(len(employee["skills"]))

# Part 3: Mutability

numbers = [10, 20, 30, 40]

numbers[1]= 200
print(numbers)

## Q12. Update a dictionary
profile = {
    "name": "Gaurang",
    "role": "Product Analyst"
}

profile["role"] = "Data Engineer"
print(profile)

## Q13. Try changing a tuple
numbers_tuple = (10, 20, 30)
numbers[1] = 200
print(numbers_tuple)

#Traceback (most recent call last):
  #File "c:\Users\Ramandeep kaur\Desktop\python-learning\44.py", line 4, in <module>
    #numbers[1] = 200

    ## Q14. Try changing a string
name = "Gaurang"
#name [0] = "S"
# TyperError: 'str' object does not support item assignment

# Part 4: Sets
cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Bangalore"]

## Q15. Convert the list into a set to remove duplicates
unique_cities = set(cities)
print(unique_cities)

## Q16. Check whether `"Delhi"` exists in the set
print("Delhi" in cities)

## Q17. Add `"Chennai"` to the set
cities.add("chennai")
print(cities)

# Part 5: Big O Basics
## Q18. What is Big O notation?
#Big o notation tells us how fast or slow a programs runs as the data increases. It is used to measure the performance and efficiency of code.

## Q19. What is the time complexity of accessing a list item by index?
#```python
numbers = [10, 20, 30]
print(numbers[1])
#```

0(1) 
#constant time comlexity.
# execution time remains constant regardless of the size of the list.

## Q20. What is the time complexity of searching for a value in a list?
#```python
numbers = [10, 20, 30, 40]
print(30 in numbers)
#```

#o(n) 
# LINEAR TIME COMPLEXITY
#Data is increased, checking each item in the list takes more time, seaching was slower as the list grows. 

## Q21. What is the average time complexity of searching for a key in a dictionary?
#Example:

#```python
profile = {"name": "Gaurang", "role": "Product Analyst"}
print("name" in profile)
#```

#O(1)
#CONSTANT TIME COMPLEXITY
#Key searching in a dictionary is very fast, regardless of the size of the dictionary. It uses a hash table to store key value.

# Part 6: Conditions
## Q22. Check loan eligibility using credit score
credit_score = 720

if credit_score >= 700:
    print("Eligible for loan")
else:
    print("Not eligble for loan")

## Q23. Create credit score bands
credit_score = 760

if credit_score>= 750:
    print("Excellent")
elif credit_score<=749 and credit_score>=700:
    print("good")
elif credit_score<=650 and credit_score>=699: 
    print("average")
else:
    print("poor")

## Q24. Check high-value loan
loan_amount = 800000

if loan_amount >= 500000:
    print("high value loan")
elif loan_amount <=500000:
    print("normal loan")
    
## Q25. Check employment type

employment_type = "Salaried"

if employment_type == "Salaried":
    print("stable income profile")
elif employment_type == "Self-Employed":
    print("Business income profile")
else:
    print("Other income profile")

# Part 7: Logical Operators
## Q26. Loan eligibility using credit score and salary
credit_score = 720
monthly_salary = 40000

if credit_score >= 700 and monthly_salary >= 30000:
    print("Eligible")
else:
    print("Not Eligble")

## Q27. Metro city check
city = "Delhi"

if city == "Delhi" or city == "Mumbai" or city == "Banglore":
    print("Metro city")
else:
    print("Non-metro city")

## Q28. Risk profile check
if credit_score < 650 and loan_amount > 500000:
    print("High risk application")
else:
    print("Normal risk application")

## Q29. Rejection check using `not`
loan_status = "Pending"

if not loan_status == "Approved":
    print("Application not approved yet")
else:
    print("Application approved")

# Part 8: For Loops
skills = ["SQL", "Python", "Excel", "Power BI"]

## Q30. Print all skills

for skill in skills:
    print(skill)

## Q31. Print high-value loans from a list
loan_amounts = [200000, 500000, 750000, 1000000, 300000]
#Print only amounts greater than or equal to `500000`.

for amount in loan_amounts:
    if amount >= 500000:
        print(amount)

## Q32. Count approved applications
loan_statuses = ["Approved", "Rejected", "Approved", "Pending", "Approved"]

for status in loan_statuses:
    if status == "Approved":
        count+=1
        print("Approved Applications", count)
    
## Q33. Count rejected and pending applications
loan_statuses = ["Approved", "Rejected", "Approved", "Pending", "Rejected", "Pending"]

rejected = 0
pending = 0

for status in loan_statuses:
    if status == "Rejected":
        rejected += 1
    elif status == "Pending":
        pending +=1
    
    print("Rejected Application", rejected)
    print("Pending Application", pending)

    # Part 9: Break, Continue, and While Loop

## Q34. Stop loop when loan amount is greater than 700000
loan_amounts = [200000, 400000, 600000, 800000, 1000000]
#Print amounts one by one, but stop when amount is greater than `700000`.

for amount in loan_amounts:
    if amount > 70000:
        break
    print(amount)

## Q35. Skip pending applications
loan_statuses = ["Approved", "Pending", "Rejected", "Pending", "Approved"]
#Print all statuses except `"Pending"`.

for status in loan_statuses:
    if status == "Pending":
        continue
    print(status)

## Q36. Print numbers from 1 to 5 using a while loop

num = 1
while num <=5:
    print(num)
    num += 1

## Q37. Keep reducing loan balance
loan_balance = 500000
monthly_payment = 100000

#Using a while loop, reduce the loan balance by `monthly_payment` until the balance becomes `0`.

while loan_balance > 0:
    loan_balance -= monthly_payment
    print("Remaining Balance", loan_balance)
    print("Loan fully paid")

# Part 10: Functions
## Q38. Create a function to print your name

def print_name():
    print("Raman")
print_name()

## Q39. Create a function to calculate square
def square(number):
    return number * number
print(square(5))

## Q40. Create a function to calculate cube
def cube(num):
    return num*num*num
print(cube(3))

## Q41. Create a function to add two numbers

def add (a , b):
    return a+b
print(add(10,20))

## Q42. Create a function to divide two numbers
#divide(a, b)

def divide(a,b):
    return a / b
print(divide(20,4))

## Q43. Create a greeting function with default value
#greet_user(name, greeting="Hello")

def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}"
print(greet_user("Gaurang"))
print(greet_user("Gaurang", "Hi"))

## Q44. Create a function to calculate approval rate
#calculate_approval_rate(total_applications, approved_applications)

def calculate_approval_rate(total_applications, approved_applications):
    return approved_applications / total_applications * 100
print(calculate_approval_rate(10, 6))

## Q45. Create a function to check loan eligibility
#check_loan_eligibility(credit_score)

def check_loan_eligibility(credit_score):
    if credit_score >= 700:
        return "Eligible"
    else:
        return "Not Eligible"
print(check_loan_eligibility(720))

## Q46. Create a function to return credit score band
def get_credit_score_band(credit_score):
    if credit_score >=750:
        return "Excellent"
    elif credit_score == 700 or credit_score == 749:
        return "good"
    elif credit_score == 650 or credit_score == 699:
        return "Average"
    else:
        return "Poor"
    print(get_credit_score_band(760))

# Part 11: Scope and Local Variables
## Q47. Local variable example
def show_message():
    message = "This is a local variable"
#print(message)

show_message()
#print(message)

## Q48. Calculate bonus
#calculate_bonus(salary)

def calculate_bonus(salary):
    bonus = salary * 0.10
    return bonus
print(calculate_bonus(50000))

# Part 12: Exception Handling
## Q49. Handle division by zero
a = 10
b = 0

try:
   print (a/b)
except ZeroDivisionError:
  print("Error:", "Cannot divide by zero")

  ## Q50. Handle invalid number conversion
value = "abc"
try: 
    print(int(value))
except ValueError:
    print("Error:", "Invalid number conversion")

## Q51. Handle list index error
numbers = [10, 20, 30]
try:
    print(numbers[5])
except IndexError:
    print("IndexError occurred")

## Q52. Handle dictionary key error
student = {
    "name": "Gaurang",
    "role": "Product Analyst"
}

try:
    print(student["salary"])
except KeyError:
    print("KeyError occurred")

## Q53. Use finally block
a = 10
b = 0

try:
    print(a/b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
finally:
    print("Execution completed")

## Q54. Raise custom error for negative loan amount

loan_amount = -50000

try:
    if loan_amount <0 :
        raise ValueError("Error: Loan amount cannot be negative")
except ValueError as e:
    print ("Error")

## Q55. Create a safe division function
#safe_divide(a, b)

#def safe_divide(a, b):

# Part 13: List of Dictionaries

loan_applications = [
    {"application_id": "APP001", "customer_id": "C001", "loan_amount": 500000, "credit_score": 760, "loan_status": "Approved", "city": "Delhi"},
    {"application_id": "APP002", "customer_id": "C002", "loan_amount": 300000, "credit_score": 620, "loan_status": "Rejected", "city": "Mumbai"},
    {"application_id": "APP003", "customer_id": "C003", "loan_amount": 750000, "credit_score": 710, "loan_status": "Approved", "city": "Delhi"},
    {"application_id": "APP004", "customer_id": "C004", "loan_amount": 200000, "credit_score": 580, "loan_status": "Pending", "city": "Bangalore"},
    {"application_id": "APP005", "customer_id": "C005", "loan_amount": 1000000, "credit_score": 800, "loan_status": "Approved", "city": "Pune"}
]
## Q56. Print application ID and loan status for each application

for application in loan_applications:
    print(application["application_id"], application["loan_status"])

## Q57. Print eligible or not eligible for each application
for application in loan_applications:
    if application ["credit_score"] >= 700:
        print(application["application_id"], "Eligble")
    else:
        print(application["application_id"], "Not Eligble")

    ## Q58. Count total applications
print("Total Applications:", len (loan_applications))

## Q59. Count total approved applications
approved_count = 0
for applications in loan_applications:
    if application[loan_status] == "Approved":
        approved_count +=1
    
print("Approved Applications:", approved_count)

## Q60. Calculate total loan amount requested
 
total_loan_amount = 0
for application in loan_applications:
    total_loan_amount += application["loan_amount"]
print("Total Loan Amount Requested:", total_loan_amount)

## Q61. Calculate total approved loan amount
#Only include applications where loan status is `"Approved"`.

approved_loan_amount = 0
for application in loan_applications:
 if application ["loan_status"] == "Approved":
     approved_loan_amount += application["loan_amount"]

print("Total Approved Loan Amount:", approved_loan_amount)

## Q62. Calculate average loan amount
total_loan_amount = 0
for application in loan_applications:
    total_loan_amount += application["loan_amount"]

average_loan_amount = total_loan_amount/ loan_amount

print("Average Loan Amount:", average_loan_amount)

## Q63. Count applications by city manually

delhi = 0
mumbai = 0
banglore = 0
pune = 0

for application in loan_applications:
    if application[city] == "Delhi":
        delhi +=1
    elif application[city] == "Mumbai":
        mumbai +=1
    elif application[city] == "Banglore":
        banglore +=1
    elif application[city] == "Pune":
        pune +=1
print("Delhi:", delhi)
print("Mumbai:",mumbai)
print("Banglore:", banglore)
print("Pune:", pune)

## Q64. Create a new list of high-value approved applications
high_value_approved = 0

for application in loan_applications:
    if application["loan_status"] == "Approved" and application["loan_amount"] >=70000:

       print(high_value_approved)

## Q65. Create a summary dictionary
approved_count =0
total_loan_amount = 0
approved_loan_amount = 0
 

 # Part 14: Functions With List of Dictionaries

## Q66. Create a function to count total applications
def count_total_applications(applications):
    return len(applications)
print(count_total_applications(loan_applications))

## Q67. Create a function to count approved applications
def count_approved_applications(applications):
    count = 0
    for application in loan_applications:
        if application["loan_status"] == "Approved":
            count +=1
    print("count_approved_applications(loan_applications)")

 ## Q68. Create a function to calculate total approved loan amount

def calculate_total_approved_amount(applications):
    total = 0
    for application in loan_applications:
        if application["loan status"] == "Approved":
            total += application["loan_amount"]
        print(calculate_total_approved_amount(loan_applications))

## Q69. Create a function to return high-value approved applications

def get_high_value_approved_applications(applications):
    high_value = 0
    for application in loan_applications:
        if application ["loan_status"] == "Approved" and application ["loan_amount"] >= 70000:
          print(get_high_value_approved_applications(loan_applications))

## Q70. Create a function to generate full loan summary


# Part 15: Business Validation Mini Task

raw_loan_applications = [
    {"application_id": "APP001", "customer_id": "C001", "loan_amount": 500000, "credit_score": 760},
    {"application_id": "APP002", "customer_id": "C002", "loan_amount": -300000, "credit_score": 620},
    {"application_id": "APP003", "customer_id": "", "loan_amount": 750000, "credit_score": 710},
    {"application_id": "APP004", "customer_id": "C004", "loan_amount": 200000, "credit_score": 950},
    {"application_id": "APP005", "customer_id": "C005", "loan_amount": 1000000, "credit_score": 800}
]

## Q71. Validate loan amount

for application in raw_loan_applications:
    if application["loan_amount"] > 0:
        print(application["application_id"],"Valid loan amount")
    else:
        print(application["application_id"], "Invalid loan amount")

## Q72. Validate customer ID

for application in raw_loan_applications:
    if application["application_id"] != "":
        print(application["application_id"],"Valid customer ID")
    else:
        print(application["application_id"],"Invalid customer ID")

## Q73. Validate credit score
for application in raw_loan_applications:
    if 300 <= application["credit_score"] <=900:
        print(application["application_id"],"Valid credit score")
    else:
        print(application["application_id"],"Invalid credit score")

## Q74. Create valid and rejected application lists
valid_applications = []
rejected_applications = []

for application in raw_loan_applications:
    if application["loan_amount"] <= 0:
        print("Invalid loan amount")
    elif application["customer_id"] == "":
        print("Missing customer ID")
    elif application["credit_score"]<300 or application["credit_score"] > 900:
        print("Invalid credit score")
    
print(valid_applications)
print(rejected_applications)

## Q75. Create a validation summary

# Bonus Section

## Q78. Explain `print()` vs `return`
# print() - It displays the output on the screen.
# return - It sends a value back from a function

## Q79. Explain why exception handling is useful
#It prevents the program from crashing when an error occured.
# It makes real world applications more relible & user friendly .
#It allows us to handle errors gracefully using try & except.

## Q80. Explain why list of dictionaries is important
# It makes searching , filtering & updating data much easier.
# A list of dictionaries stores multiple records in a structured format.































    




          










