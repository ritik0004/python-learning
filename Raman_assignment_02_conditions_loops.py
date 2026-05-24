# Part 1: Conditions

## Q1. Check loan eligibility using credit score
credit_score = 720

if credit_score >=700:
 print("Eligble for loan")
else:
 print("Not eligble for loan")

 ## Q2. Create credit score bands
credit_score = 760

if credit_score >=750:
 print("Excellent")
elif credit_score >=700:
 print("Good")
elif credit_score >=650:
 print("Fair")
else:
 print("Poor")

 ## Q3. Check high-value loan
# Create a variable:
loan_amount = 800000

if loan_amount > 500000:
 print("High-value loan")
else:
 print("standard loan")


 ## Q4. Check employment type

#Create a variable:
employment_type = "Salaried"

if employment_type == "Salaried":
 print("Stable income profile")
elif employment_type == "self-employed":
 print("Business income profile")
else:
 print("other income profile")


# Part 2: Logical Operators
## Q5. Loan eligibility using credit score and salary

credit_score = 720
monthly_salary = 40000

if credit_score >=700 and monthly_salary >=30000:
 print("Eligble")
else:
 print("Not eligble")

 ## Q6. Metro city check
city = "Delhi"

if city == "Delhi" or city == "Mumbai" or city == "Bangalore":
 print("Metro city")
else:
 print("Non-metro city")

## Q7. Risk profile check
credit_score = 620
loan_amount = 900000

if credit_score < 650 and loan_amount > 500000:
 print("High risk application")
else:
 print("Normal risk application")

 ## Q8. Rejection check using `not`

loan_status = "Pending"

if loan_status != "Approved":
 print("Application not approved yet")
else:
 print("Application approved")

 # Part 3: For Loops
## Q9. Print all skills

skills = ["SQL", "Python", "Excel", "Power BI"]

for skills in skills:
 print(skills)

 ## Q10. Print high-value loans from a list
loan_amounts = [200000, 500000, 750000, 1000000, 300000]

#Print only loan amounts greater than or equal to `500000`.

for loan_amount in loan_amounts:
 if loan_amount >=500000:
  print(loan_amount)

  ## Q11. Count approved applications
loan_statuses = ["Approved", "Rejected", "Approved", "Pending", "Approved"]

#Count how many applications are approved.

count = 0
for status in loan_statuses:
 if status == "Approved":
  count += 1
  print(count)

  ## Q12. Count rejected and pending applications
loan_statuses = ["Approved", "Rejected", "Approved", "Pending", "Rejected", "Pending"]

count_rejected = 0
count_pending = 0
for status in loan_statuses:
 if status == "Rejected":
  count_rejected += 1
  print("count_rejected")
 elif status == "Pending": 
  count +=1
  print("count_pending")

  # Part 4: List of Dictionaries

loan_applications = [
    {"application_id": "APP001", "customer_id": "C001", "loan_amount": 500000, "credit_score": 760, "loan_status": "Approved", "city": "Delhi"},
    {"application_id": "APP002", "customer_id": "C002", "loan_amount": 300000, "credit_score": 620, "loan_status": "Rejected", "city": "Mumbai"},
    {"application_id": "APP003", "customer_id": "C003", "loan_amount": 750000, "credit_score": 710, "loan_status": "Approved", "city": "Delhi"},
    {"application_id": "APP004", "customer_id": "C004", "loan_amount": 200000, "credit_score": 580, "loan_status": "Pending", "city": "Bangalore"},
    {"application_id": "APP005", "customer_id": "C005", "loan_amount": 1000000, "credit_score": 800, "loan_status": "Approved", "city": "Pune"}
]

## Q13. Print application ID and loan status for each application
for application in loan_applications:
  print(application ["application_id"], application["loan_status"])

  ## Q14. Print eligible or not eligible for each application

for application in loan_applications:
 if application["credit_score"] >= 700:
  print(application["application_id"], "eligible")
 else:
  print(application["application_id"], "not eligible")

## Q15. Count total approved applications
count_approved = 0
for application in loan_applications:
 if application["loan_status"] == "Approved":
  count_approved += 1
  print(count_approved)

  ## Q16. Calculate total approved loan amount
  #Only include applications where loan status is `"Approved"`.

count_approved_loan_amount = 0
for application in loan_applications:
 if application["loan_status"] == "Approved":
  count_approved_loan_amount += application["loan_amount"]
  print(count_approved_loan_amount)

## Q17. Count applications by city manually
city_count = {}
for application in loan_applications:
 
 ## Q18. Create a new list of high-value approved applications
 #loan_status is `"Approved"` and loan_amount >= 700000 

#for application in loan_applications:
#if application["loan_status"] == "Approved" and application["loan_amount"] >= 700000:
#print(loan_applications)                    #Incomplete

# Part 5: `break` and `continue`

## Q19. Stop loop when loan amount is greater than 700000
 loan_amounts = [200000, 400000, 600000, 800000, 1000000]
#Print amounts one by one, but stop the loop when amount is greater than `700000`

for amount in loan_amounts:
    if amount > 700000:
         break
    print(amount)

 ## Q20. Skip pending applications
loan_statuses = ["Approved", "Pending", "Rejected", "Pending", "Approved"]
#Print all statuses except `"Pending"`.

for status in loan_statuses:
 if status == "Pending":
  continue
 print(status)

 # Part 6: While Loop

## Q21. Print numbers from 1 to 5 using a while loop

num = 1
while num <=5:
 print(num)
 num +=1

 ## Q22. Keep reducing loan balance
#Create a variable:

loan_balance = 500000
monthly_payment = 100000

#Using a while loop, reduce the loan balance by `monthly_payment` until the balance becomes `0`.

while loan_balance > 0:
 loan_amount = loan_balance - monthly_payment
 print("Remaining balance:", loan_amount)
 print("loan fully paid")

 # Part 7: Mini Practical Task
## Q23. Loan Application Summary Report

#Create a summary report and print:

#1. Total applications
#2. Approved applications
#3. Rejected applications
#4. Pending applications
#5. Total loan amount requested
#6. Total approved loan amount
#7. Average loan amount
#8. High-value applications count
#9. Applications from Delhi


1#
print("Loan_applications", len(loan_applications))

2#
count_approved = 0
for application in loan_applications:
 if application["loan_status"] == "Approved":
  count_approved += 1
  print("Approved applications:", count_approved)

  3#
  count_approved = 0
for application in loan_applications:
 if application["loan_status"] == "Rejected":
  count_approved += 1
  print("Rejected applications:", count_approved)

  4#
count_approved = 0
for application in loan_applications:
 if application["loan_status"] == "Pending":
  count_approved += 1
  print("Pending applications:", count_approved)

  5#
total_loan_amount = 0
for application in loan_applications:
    total_loan_amount += application["loan_amount"]
    print("Total loan amount requested:", total_loan_amount)
    
    6#
total_approved_amount = 0
for application in loan_applications:
    if application["loan_status"] == "Approved":
        total_approved_amount += application["loan_amount"]
print("Total approved loan amount:", total_approved_amount)

9#
count_delhi = 0
for application in loan_applications:
    if application["city"] == "Delhi":
     count_delhi += 1
    print("Applications from Delhi:", count_delhi)

