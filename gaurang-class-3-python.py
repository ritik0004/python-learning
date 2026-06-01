gaurang-class-3-python

#1
def my_name():
   print ("gaurang")

my_name


#2
def print_multiples(n):
    i=0
    while i < 11 :
        print (n*i)
        i+1=i


print_multiples(5)

#3
def square(num):
    print(num**2)

square(5)    

#4
def cube(num):
    print(num**3)

cube(5) 

#5
def greet(name):
    print("hello", name,"!")

greet("gaurang")    

#6
def add(a,b):
    print(a+b)

add(10,20)    


#7
def subtract(a,b):
    print(a-b)

subtract(20,5)    


#8
def multiply(a,b):
    print(a*b)

multiply(20,5) 

#9
def dvide(a,b):
    print(a/b)

dvide(20/5) 

#10
def calculate_total_salary(base_salary, bonus):
       print(base_salary+bonus)


calculate_total_salary(35000, 5000)


#11
def calculate_monthly_payment(loan_amount, months):
      print(loan_amount/months)

calculate_monthly_payment(120000, 12)


#12
def calculate_approval_rate(total_applications, approved_applications):
    print(approved_applications / total_applications * 100)

calculate_approval_rate(10, 6)

#13
def calculate_rejection_rate(total_applications, rejected_applications):
    print(rejected_applications / total_applications * 100)


calculate_rejection_rate(10, 3)   

#14
def check_loan_eligibility(credit_score):
    if credit_score >= 700:
        print("eligible")
    else :
        print("no_eligible")

check_loan_eligibility(720)        


#15
def get_credit_score_band(credit_score):
    if credit_score >= 750:
        print("Excellent")
    elif credit_score < 750 and credit_score>700:
        print("Good")
    elif credit_score < 699 and credit_score>650:
        print("Average")    
    else :
        print("Poor")

get_credit_score_band(741)     


#16
def get_loan_amount_category(loan_amount):

    if loan_amount >= 1000000:
        print("high")
    elif loan_amount > 500000 and loan_amount <999999 :
        print("Good")
    elif loan_amount < 499999 and loan_amount>200000:
        print("Average")    
    else :
        print("Poor")

get_loan_amount_category(5600000)


#17
def greet_user(name, greeting="Hello"):
    return f"{greeting},{name}!"

print(greet_user("Gaurang"))    

#18
def greet_user1(name, greting):
    return f"{greting},{name}!"

print(greet_user1("Gaurang", "Hi"))

#19
def user_location(name, city, country):
    return f"{name} lives in {city},{country}"

print(user_location("gaurang","gurugram","india") )

print(user_location("John", "New York", "USA"))

#20
def calculate_final_price(price, discount_percentage):
    return price-price*(discount_percentage/100)

print(calculate_final_price(100, 10))
print(calculate_final_price(1000, 20))

#21

def xxx(n):
    print("n")

xxx(9)


def  calculate_bonus(salary):
    return bonus = salary * 0.10

print(calculate_bonus(50000)    

#ERROR!
#Traceback (most recent call last):
#  File "<main.py>", line 2
#    return bonus = salary * 0.10
                 ^
#SyntaxError: invalid syntax

# no we cannot access bonus from outside

def outer_function():
    
    def inner_function():

        print("I am inside inner function")

    inner_function()

outer_function()
    

#23
def loan_summary(loan_amount, credit_score):
    if credit_score >= 750:
        print("Excellent")
    elif credit_score < 750 and credit_score>700:
        print("Good")
    elif credit_score < 699 and credit_score>650:
        print("Average")    
    else :
        print("Poor")

    if loan_amount >= 1000000:
        print("high")
    elif loan_amount > 500000 and loan_amount <999999 :
        print("Good")
    elif loan_amount < 499999 and loan_amount>200000:
        print("Average")    
    else :
        print("Poor")


print(loan_summary(750000, 720))    

#24  --- THIS IS MY WEAK PART

loan_statuses = ["Approved", "Rejected", "Approved", "Pending", "Approved"]

def calculate_total_loan_amount(loan_statuses):
    count = 0

    for i in loan_statuses:
        if i == "Approved":
            count += 1

    return count

print(calculate_total_loan_amount(loan_statuses))


#25 --- THIS IS MY WEAK PART
loan_amounts = [200000, 500000, 750000, 1000000]


def calculate_total_loan_amount(loan_amounts):
    total=0
    for amount in loan_amounts:
        total+=amount

    return amount

print(calculate_total_loan_amount(loan_amounts))

#26  -- weak part
loan_amounts = [200000, 500000, 750000, 1000000, 300000]
def get_high_value_loans(loan_amounts):
    greater= []
    for amount in loan_amounts:
        if amount >=500000:
             greater.append(amount)
        else :
           pass 
    return    greater

print(get_high_value_loans(loan_amounts))


#27
def count_total_applications(loan_applications):
    total=0
    for application in loan_applications:
        total +=1
        
    return total
    
print(count_total_applications(loan_applications)) 


#28

def count_approved_from_applications(loan_applications):
    total=0
    for application in loan_applications:
        if application["loan_status"]=="Approved":
              total +=1
        
    return total
    
print(count_approved_from_applications(loan_applications)) 

#29
def calculate_approved_loan_amount(applications):
    total=0
    for application in applications:
        if application["loan_status"]=="Approved":
              total +=application["loan_amount"]
        
    return total
    
print(calculate_approved_loan_amount(loan_applications))  

#30pyth