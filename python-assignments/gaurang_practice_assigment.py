def get_name(name):
    return name 

print(get_name("gaurang"))

def square(num):
    return num**2
print(square(2))    


def cube(num):
    return num**3
print(cube(2)) 

def compare(a,b):
    if a>b:
        return a
    else :
        return b
print(compare(3,5))            

def odd_even(num):
    if num%2==0:
        return "is_even"
    else :
       return "id_odd"
print(odd_even(2))          

def greet(name):
    return name
print(greet("Gaurang"))   


def reet(name, greeting="Hello"):
    return f"{greeting} {name}"    #please explain me this how to write this
print(reet("gaurang"))

def calculate_bonus(salary):
    bonus=salary*0.10
    return bonus
print(calculate_bonus(30000))

def calculate_final_salary(salary, bonus):
    final = salary + bonus
    return final
print(calculate_final_salary(35000, 2000))    

def calculate_monthly_emi(loan_amount, months):
    emi = loan_amount/months    
    return emi
print(calculate_monthly_emi(100000, 12))

def Loan_eligibility(credit_score):
    if credit_score>700:
        return "eligible"
    else  :
        return "not-eligible"
print(Loan_eligibility(699))

def Credit_score_band(credit_score):
    if 0<credit_score<500:
        return "low_band"
    elif 500<credit_score<700:
        return "avg_band"
    else:    
        return "High band"  
print(Credit_score_band(600))  

def Loan_amount_category(amount):
    if 0<amount<500000:
        return "low"
    elif 500000<amount<1000000:
        return "high"
    else:    
        return "very_high"
print(Loan_amount_category(700000))
  

 #Return True if loan \> 500000
 
loan_applications =    [  {"application_id":"APP001","customer_id":"C001","loan_amount":500000,"credit_score":760,"loan_status":"Approved","city":"Delhi"},
    {"application_id":"APP002","customer_id":"C002","loan_amount":300000,"credit_score":620,"loan_status":"Rejected","city":"Mumbai"},
    {"application_id":"APP003","customer_id":"C003","loan_amount":750000,"credit_score":710,"loan_status":"Approved","city":"Delhi"},
    {"application_id":"APP004","customer_id":"C004","loan_amount":200000,"credit_score":580,"loan_status":"Pending","city":"Bangalore"},
    {"application_id":"APP005","customer_id":"C005","loan_amount":1000000,"credit_score":800,"loan_status":"Approved","city":"Pune"},
    {"application_id":"APP006","customer_id":"C006","loan_amount":650000,"credit_score":690,"loan_status":"Approved","city":"Delhi"},
    {"application_id":"APP007","customer_id":"C007","loan_amount":450000,"credit_score":640,"loan_status":"Rejected","city":"Mumbai"},
    {"application_id":"APP008","customer_id":"C008","loan_amount":850000,"credit_score":730,"loan_status":"Approved","city":"Chennai"}
]



def has_large_loan(loan_applications):
    for i in loan_applications:
        if i["loan_amount"] > 500000:
            return True
    return False

print(has_large_loan(loan_applications))

     
#Return True if score \>700 and loan \>500000
def has_largeloan(loan_applications):
    for i in loan_applications:
        if  i["loan_amount"] > 500000 and i["credit_score"]>700:
            return True
    return False
print(has_largeloan(loan_applications))        

#Total loan amount

def Total_loan_amount(loan_applications):
    amount_t=0
    for  i in loan_applications:
        amount_t += i["loan_amount"]
    return amount_t
print(Total_loan_amount(loan_applications))

#Average loan amount
def Average_loan_amount(loan_applications):
    amount_t=0
    for  i in loan_applications:
        amount_t += i["loan_amount"]
    
    count_t=0
    for u in loan_applications:
        count_t += 1
    return amount_t/count_t   
print(Average_loan_amount(loan_applications))


#Approved count
def Approved_count(loan_applications):
    count_t=0
    for  i in loan_applications:
        if i["loan_status"]=="Approved":
            count_t +=1
    return count_t  
print(Approved_count(loan_applications)) 

#

def Rejected_count(loan_applications):
    count_t=0
    for  i in loan_applications:
        if i["loan_status"]=="Rejected":
            count_t +=1
    return count_t  
print(Rejected_count(loan_applications))

def Pending_count(loan_applications):
    count_t=0
    for  i in loan_applications:
        if i["loan_status"]=="Pending":
            count_t +=1
    return count_t  
print(Pending_count(loan_applications))



def Highest(loan_applications):
    max_loan_amount=loan_applications[0]["loan_amount"]

    for  i in loan_applications:
        if i["loan_amount"] >max_loan_amount:
            max_loan_amount=i["loan_amount"]
    return  max_loan_amount
print(Highest(loan_applications))


def lowest(loan_applications):
    lowest_amount=loan_applications[0]["loan_amount"]
    for i in loan_applications:
        if i["loan_amount"]<lowest_amount:
            lowest_amount=i["loan_amount"]
    return  lowest_amount
print(lowest(loan_applications))           


def square(num):
    return num**2
result = square(5)
print(result)

def total(numbers):
    total=0
    for n in numbers:
        total+=n
    return total
print(total([1,2,3]))    

#Return approved applications
def approved_app(loan_applications):
    all=[]
    for i in loan_applications:
        if i["loan_status"]=="Approved":
            all.append(i["application_id"])
    return all        
print(approved_app(loan_applications))            

def Rejected_app(loan_applications):
    all=[]
    for i in loan_applications:
        if i["loan_status"]=="Rejected":
            all.append(i["application_id"])
    return all        
print(Rejected_app(loan_applications))  


["city"]=="Delhi"

def delhi_app(loan_applications):
    all=[]
    for i in loan_applications:
        if i["city"]=="Delhi":
            all.append(i["application_id"])
    return all        
print(delhi_app(loan_applications))

def loan_amount(loan_applications):
    bigamount=[]
    for i in loan_applications:
        if i["loan_amount"]>=700000:
            bigamount.append(i["loan_amount"])
    return bigamount
print(loan_amount(loan_applications))   


def loan_apporved(loan_applications):
    customer=[]
    for i in loan_applications:
        if i["loan_status"]=="Approved":
            customer.append(i["customer_id"])
    return customer
print(loan_apporved(loan_applications)) 


def city_counts(loan_applications):
    counts = {}

    for app in loan_applications:
        city = app["city"]

        if city in counts:
            counts[city] += 1
        else:
            counts[city] = 1

    return counts

print(city_counts(loan_applications))  


#29 Status_counts
def Status_counts(loan_applications):
    status ={}
    for i in loan_applications :
        ss =i["loan_status"]

        if ss in status:
            status[ss]+=1

        else:
            status[ss]=1
    return status    
print(Status_counts(loan_applications))       

#30. Credit score band counts

def score_band(loan_applications):
    band={'good_credit_score':0,
'avg_credit_score':0,
'poor_credit_score':0}
    for i in loan_applications:
        credit=i["credit_score"]

        if credit>700 :
           band["good_credit_score"]+=1 
        elif 500<= credit <=700:
           band["avg_credit_score"]+=1 
        else:
            band["poor_credit_score"]+=1
    return band        
print(score_band(loan_applications))

#calculate_approval_rate()

def calculate_approval_rate(loan_applications):
    count=0
    approved_count=0
    for i in loan_applications:
        if i["loan_status"]=="Approved":
            approved_count+=1
            count+=1
        else:
            count+=1
    return(approved_count/count)  
print(calculate_approval_rate(loan_applications))    

#calculate_average_credit_score()
def calculate_average_credit_score(loan_applications):
    count=0
    credit_score=0
    for i in loan_applications:
        
        credit_score+=i["credit_score"]
        count+=1
    return(credit_score/count)   
print(calculate_average_credit_score(loan_applications))     

#calculate_total_approved_loan_amount()
def calculate_total_approved_loan_amount(loan_applications):
    approved_amount=0
    for i in loan_applications:
        if i["loan_status"]=="Approved":
            approved_amount+=i["loan_amount"]
    return  approved_amount
print(calculate_total_approved_loan_amount(loan_applications))      

def calculate_total_rejected_loan_amount(loan_applications):
    Rejected_amount=0
    for i in loan_applications:
        if i["loan_status"]=="Rejected":
            Rejected_amount+=i["loan_amount"]
    return  Rejected_amount
print(calculate_total_rejected_loan_amount(loan_applications)) 

def get_high_value_approved_applications(loan_applications):
    for i in loan_applications:
        if i["loan_amount"]>700000 and i["loan_status"]=="Approved":
            print(i)

print(get_high_value_approved_applications(loan_applications))

cities=0
for app in loan_applications:
    if app["city"]=="Delhi":
        cities+=1
    print(cities)


def approved(loan_applications):
    approved=0
    for app in loan_applications:
        if app["loan_status"]=="Approved":
            approved+=1
    return approved
print(approved(loan_applications))      

def greet(name):
    return "Hello " + name



  
