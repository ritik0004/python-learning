credit_score = 720 
if credit_score>= 700:
    print("eligible for loan")
else:


    print("not eligible for loan")

#ans 2
credit_score = 760 
if credit_score>= 750:
    print("Excellent")


elif credit_score<= 749 and credit_score>= 700  :
    print("Good")

elif credit_score<= 699 and credit_score>= 650  :
    print("Good")
else   :


    print("bad")

#ans 3 
loan_amount = 800000

if  loan_amount >= 500000  :
    print("High value loan")
else: 
    print("Normal loan")

#ans4
employment_type = "Salaried"
if employment_type=="Salaried":
  print("Stable income profile")
elif employment_type=="self-Employed":
    print("Business income profile")
else:
    print("Other income profile")

#ans5
credit_score = 720
monthly_salary = 40000
if credit_score>= 700 and monthly_salary>=30000:
    print("eligible")
else:
    print("Not eligible")

#ans6
city = "Delhi"
if city in




#ans7 
credit_score = 620
loan_amount = 900000
if credit_score< 650 and loan_amount>500000:
    print("High risk application")
else:
    print("Normal risk application")

#ans 8 
loan_status = "Pending"
if loan_status< 650 :
    print("Application not approved yet")
else:
    print("Application approved") 

#ans 9 
skills = ["SQL", "Python", "Excel", "Power BI"]
for i in skills:
    print(i)   

#ans 10
loan_amounts = [200000, 500000, 750000, 1000000, 300000]
for i in     loan_amounts:
    if i>=500000:
        print(i)

#ans 11  ( I used chatgpt not able to build the logic for this)
mujhe ye smjhna ha
loan_statuses = ["Approved", "Rejected", "Approved", "Pending", "Approved"]
approved=loan_statuses.count("Approved")
print("approved:",approved)

#ans 12
loan_statuses = ["Approved", "Rejected", "Approved", "Pending", "Rejected", "Pending"]
Rejected =loan_statuses.count("Rejected")
print ("Rejected:",Rejected)
pndig=loan_statuses.count("Pending")
print ("pending:",pndig)

#ans 13 ( I used chatgpt not able to build the logic for this)
mujhe ye smjhna ha
loan_applications = [
    {"application_id": "APP001", "customer_id": "C001", "loan_amount": 500000, "credit_score": 760, "loan_status": "Approved", "city": "Delhi"},
    {"application_id": "APP002", "customer_id": "C002", "loan_amount": 300000, "credit_score": 620, "loan_status": "Rejected", "city": "Mumbai"},
    {"application_id": "APP003", "customer_id": "C003", "loan_amount": 750000, "credit_score": 710, "loan_status": "Approved", "city": "Delhi"},
    {"application_id": "APP004", "customer_id": "C004", "loan_amount": 200000, "credit_score": 580, "loan_status": "Pending", "city": "Bangalore"},
    {"application_id": "APP005", "customer_id": "C005", "loan_amount": 1000000, "credit_score": 800, "loan_status": "Approved", "city": "Pune"}
]

for i in loan_applications:
 print(i["application_id"],i["loan_status"])


# ans 19
loan_amounts = [200000, 400000, 600000, 800000, 1000000]
for  i in loan_amounts:
    if  i <700000:
        print(i)

#ans 20
loan_statuses = ["Approved", "Pending", "Rejected", "Pending", "Approved"]
for i in loan_statuses:
    if i=="Pending":
        pass
    else :
        print(i)


#ans 21
loan_balance = 500000
monthly_payment = 100000
while loan_balance =0 :
    print(loan_balance-monthly_payment)


 




