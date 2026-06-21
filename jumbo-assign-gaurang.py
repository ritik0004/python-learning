print(type(student_name))   #string
print(type(age))   #int
print(type(monthly_salary))  #float
print(type(is_working))    #boolean
print(type(skills))  #list
print(type(profile))  #dictionary
print(type(coordinates))  #  tuple
print(type(unique_cities)) #set



student_profile ={name:"Gaurang" , age:26 , current_role:"Product Analyst" , target_role:"Data and AI Engineer" , skills:["SQL", "Python", "Excel", "GA4"],
monthly_salary:"Dal Roti chal ri ha Malik"}

skills = ["SQL", "Python", "Excel", "Power BI", "GA4"]
skills[0]
skills[2]
skills[-1]

print(employee["name"])
print(employee["role"])
print(employee["skills"][1])
print(len(employee["skills"]))

numbers = [10, 20, 30, 40]
numbers[1]=200
print(numbers)

profile = {
    "name": "Gaurang",
    "role": "Product Analyst"
}

profile["role"]="DE"

print(profile)

numbers_tuple = (10, 20, 30)
numbers_tuple[1]=34
print(numbers_tuple)
  ERROR!
Traceback (most recent call last):
  File "<main.py>", line 2, in <module>
TypeError: 'tuple' object does not support item assignment


ERROR!
Traceback (most recent call last):
  File "<main.py>", line 2, in <module>
TypeError: 'str' object does not support item assignment


cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Bangalore"]

unique_cities = set(cities)

print(unique_cities)


cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Bangalore"]

for i in cities :
    if i =="Delhi":
        print("True")

    else:
        pass  

#17
cities.append("chennai") 
print(cities)     


# Q19 / Q21
#we can directly get the data it is not size depenndent because location is defined O(1)


#20 
#we can-not directly get the data it is  size depenndent because location is not  defined O(n) , interpreter has to check each and every position


#22
credit_score = 720
if credit_score>=720:
    print("Eligible for loan ")

else:
   print("Not eligible for loan")


#23

credit_score = 760

if credit_score>=750:
    print("Excellent")
elif credit_score<=749 and credit_score>=700:
    print("Good")    
elif credit_score<=699 and credit_score>=650:
    print("AVG")   

else:
   print("poor")

#24
loan_amount = 800000
if loan_amount >= 500000 :
    print("high value ")

elif loan_amount <= 500000:
   print("Normal value")

#25


if employment_type =="Salaried" :
    print("Stable income profil")

elif employment_type =="Self-Employed":
   print("Buz income profile")

else :
    print("Other income profile")   


#26
credit_score = 720
monthly_salary = 40000    

if credit_score >= 700 and monthly_salary >= 30000:
    print("Eligible")

else:
    print("not Eligible")   

#27
city = "Delhi"
if city  in ['delhi','mumbai','banglore']   :
    print('metro')      

else:
    print('non-metro city')                  

#28
credit_score = 620
loan_amount = 900000

if credit_score < 650 and loan_amount > 500000:
    print("High risk application ")

else:
    print('Normal risk application')


#29

loan_status = "Pending"
if loan_status=="Approved":
    print('Application approved')

else:
    print('Application not approved yet')  

#30
skills = ["SQL", "Python", "Excel", "Power BI"]

for i in skills:
    print(i)

#31
loan_amounts = [200000, 500000, 750000, 1000000, 300000]
for i in loan_amounts:
    if i >=500000 :
        print(i)

    else:
        pass 


#32
loan_statuses = ["Approved", "Rejected", "Approved", "Pending", "Approved"]
lst=[]
for i in loan_statuses:
    if i=='Approved':
        lst.append(i)
    else:
        pass
print(len(lst))  

#33
loan_statuses = ["Approved", "Rejected", "Approved", "Pending", "Approved"]
lst=[]
mst=[]
for i in loan_statuses:
    if i=='Approved':
        lst.append(i)

    elif i=='Rejected':
        mst.append(i)   
    else:
        pass
print("approved", len(lst))  
print("Rejected" , len(mst))

#34
loan_amounts = [200000, 400000, 600000, 800000, 1000000]
for i in loan_amounts:
    if i >700000:
        break
    else:
        print(i)


#35
loan_statuses = ["Approved", "Pending", "Rejected", "Pending", "Approved"]
   for i in loan_statuses:
    if i =="Pending"  :
        pass
    else:
        print(i)    

#36
i=0
while i<6 :
    print(i)
    i+=1    

#37
loan_balance = 500000
monthly_payment = 100000

while loan_balance>0:
    loan_balance -=monthly_payment
    print("Remaining Balance:", loan_balance)

print("Loan fully paid")    


#38
def name(n):
    print(n)
name('Gaurang') 

#39
def square(num):
    print(num**2)
square(5) 

#40
def cube(num):
    print(num**3)
cube(3) 

#41
def add(a, b):
    return a+b

print(add(10, 20)) 

#42
def divide(a, b):
    return a/b

print(divide(20, 4))

#43
## Q43. Create a greeting function with default value - i don't understand this


#44
def calculate_approval_rate(total_applications, approved_applications):
    return approved_applications / total_applications * 100

print(calculate_approval_rate(10, 6))

#45
def check_loan_eligibility(credit_score):
    if credit_score>=720:
       print("Eligible for loan ")

    else:
       print("Not eligible for loan")

check_loan_eligibility(720)     


#46
def  get_credit_score_band(credit_score)  :
        if credit_score>=750:
            return Excellent
        elif credit_score<=749 and credit_score>=700:
             return Good 
        elif credit_score<=699 and credit_score>=650:
            return AVG  
        
        else:
            return poor 
           
print(get_credit_score_band(760))  


#47
def calculate_bonus(salary):

      bonus = salary * 0.10
      return bonus
print(calculate_bonus(50000)) 


#48

a = 10
b = 0

try:
    result = a / b
    print(result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

#49
value = "abc"
try :
    print(int(value))

except    ValueError:
        print("Invalid number conversion")

#50      
numbers = [10, 20, 30]
try:
     print(numbers[5])


Expect IndexError:
     print("IndexError occurred")

#51
student = {
    "name": "Gaurang",
    "role": "Product Analyst"
}

try:
    print(student["salary"])

except KeyError :
    print("KeyError occurred")   

#52
a = 10
b = 0

try:
    result = a / b
    print(result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

finally:
    print("Execution completed")     


#53
loan_amount = -50000
try :
    if loan_amount<0:
       raise ValueError("Loan amount cannot be negative")

except ValueError as e:
    print("Error:", e)


#54
def safe_divide(a, b):

        try :
            return (a/b) 
        
        except ZeroDivisionError:
           return "Cannot divide by zero"
                      

print(safe_divide(10, 2))
print(safe_divide(10, 0))          

#56
loan_applications = [
    {"application_id": "APP001", "customer_id": "C001", "loan_amount": 500000, "credit_score": 760, "loan_status": "Approved", "city": "Delhi"},
    {"application_id": "APP002", "customer_id": "C002", "loan_amount": 300000, "credit_score": 620, "loan_status": "Rejected", "city": "Mumbai"},
    {"application_id": "APP003", "customer_id": "C003", "loan_amount": 750000, "credit_score": 710, "loan_status": "Approved", "city": "Delhi"},
    {"application_id": "APP004", "customer_id": "C004", "loan_amount": 200000, "credit_score": 580, "loan_status": "Pending", "city": "Bangalore"},
    {"application_id": "APP005", "customer_id": "C005", "loan_amount": 1000000, "credit_score": 800, "loan_status": "Approved", "city": "Pune"}
]


for i in loan_applications:
    print(i["application_id"],i["loan_status"])
#57
for i  in    loan_applications:
    if i["credit_score"] >=700:
        print(i["application_id"],"eligible")
    else:
         print(i["application_id"],"not-eligible")   

#58
Total_Applications=0
for i in loan_applications:
    Total_Applications+=1
print(Total_Applications)

#59
Total_Applications=0
for i in loan_applications:
    if i["loan_status"]=="Approved":
         Total_Applications+=1
print(Total_Applications)   


#60 - used chtgpt
Total_Applications=0
for i in loan_applications:
    Total_Applications+=i["loan_amount"]
         
print(Total_Applications)

#61
Total_Applications=0
for i in loan_applications:
    if i["loan_status"]=="Approved":
            Total_Applications+=i["loan_amount"]
         
print(Total_Applications)

#62
Total_Applications=0
no=0
for i in loan_applications:
    Total_Applications+=i["loan_amount"]
    no+=1
         
x=Total_Applications
y=no
print(x/y)

#63 not able to  solve


#64

for i in loan_applications:
    if i["loan_status"]=="Approved" and i["loan_amount"] >= 700000 :
       print(i["application_id"])

#65 - taken help of chtgpt
summary = {
    "total_applications": len(loan_applications),
    "approved_applications": 0,
    "rejected_applications": 0,
    "pending_applications": 0,
    "total_requested_amount": 0,
    "total_approved_amount": 0
}

for i in  loan_applications :
    summary["total_requested_amount"] += i["loan_amount"]
    if i["loan_status"]=="Approved" :
        summary["approved_applications"]+=1
        summary["total_approved_amount"] += i["loan_amount"]

    elif  i["loan_status"]=="Rejected" :
        summary["rejected_applications"]+=1  
    elif    i["loan_status"]=="Pending":
         summary["pending_applications"]+=1

summary["average_loan_amount"] = (
    summary["total_requested_amount"] /
    summary["total_applications"]
)
print(summary)

#66
def count_total_applications(applications):
    return len(applications)

print(count_total_applications(loan_applications))

#67

def count_approved_applications(applications):
    count = 0

    for application in applications:
        if application["loan_status"] == "Approved":
            count += 1

    return count

print(count_approved_applications(loan_applications))


#68
def count_approved_applications(applications):
    count = 0

    for application in applications:
        if application["loan_status"]=="Approved":
            count  += application["loan_amount"]
            

    return count

print(count_approved_applications(loan_applications))

#69
def get_high_value_approved_applications(loan_applications):
    
        for application in loan_applications: 
            if application["loan_status"]=="Approved" and application["loan_amount"] >= 700000:
                return application["application_id"]
print(get_high_value_approved_applications(loan_applications))   

#70
def generate_loan_summary(applications):
    summary = {
        "total_applications": len(applications),
        "approved_applications": 0,
        "rejected_applications": 0,
        "pending_applications": 0,
        "total_requested_amount": 0,
        "total_approved_amount": 0
    }

    for app in applications:
        
        summary["total_requested_amount"] += app["loan_amount"]

        
        if app["loan_status"] == "Approved":
            summary["approved_applications"] += 1
            summary["total_approved_amount"] += app["loan_amount"]

        elif app["loan_status"] == "Rejected":
            summary["rejected_applications"] += 1

        elif app["loan_status"] == "Pending":
            summary["pending_applications"] += 1

    
    summary["average_loan_amount"] = (
        summary["total_requested_amount"] /
        summary["total_applications"]
    )

    summary["approval_rate"] = (
        summary["approved_applications"] /
        summary["total_applications"] * 100
    )

    return summary


print(generate_loan_summary(loan_applications))

#71
raw_loan_applications = [
    {"application_id": "APP001", "customer_id": "C001", "loan_amount": 500000, "credit_score": 760},
    {"application_id": "APP002", "customer_id": "C002", "loan_amount": -300000, "credit_score": 620},
    {"application_id": "APP003", "customer_id": "", "loan_amount": 750000, "credit_score": 710},
    {"application_id": "APP004", "customer_id": "C004", "loan_amount": 200000, "credit_score": 950},
    {"application_id": "APP005", "customer_id": "C005", "loan_amount": 1000000, "credit_score": 800}
]

for i in raw_loan_applications:
    if i["loan_amount"]>0:
        print(i["application_id"],"valid loan_amount")
    else:    
        print(i["application_id"],"not-valid loan_amount")

#72
for i in raw_loan_applications:
    if i["customer_id"] != "":
        print(i["application_id"], "Valid customer ID")
    else:
        print(i["application_id"], "Invalid customer ID")  


#73
for i in raw_loan_applications:
    if 300 <= i["credit_score"] <= 900:
        print(i["credit_score"], "Valid credit score")
    else:
        print(i["credit_score"], "Invalid credit score")               


## Q78. Explain `print()` vs `return`  - print gives us ouptut directly and return sends back the value from function 

## Q79. Explain why exception handling is useful - it helps on data validation and gives us expected error 

## Q80. Explain why list of dictionaries is important - we can see all the values are entered by customer with reference to particular details 
