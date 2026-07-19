# Part 1: Function Definition and Calling

## Q1. Create a function to print your name
from numpy import square
from scipy import stats


def print_name():
    print("Ramandeep Kaur")
print_name()

## Q2. Create a function to print multiples of a number
def print_multiples(n):
    for i in range(1, 11):
        print(n * i)
print_multiples(5)

## Q3. Create a function to calculate square

def calculate_square(num):
    return num * num

print(calculate_square(5))

## Q4. Create a function to calculate cube
#Create a function called `cube(num)`.

#The function should return the cube of the number.

def cube(num):
    return num * num * num
print (cube(3))

# Part 2: Parameters and Arguments
## Q5. Create a greeting function

def greet (name):
    print (f"Hello, {name}")
greet ("Raman")

## Q6. Create a function to add two numbers
#Create a function called `add(a, b)`.

def add (a , b):
    return (a+b)
result = add(10, 20)
print(result)

## Q7. Create a function to subtract two numbers
#Create a function called `subtract(a, b)`.

def subtract (a , b):
    return (a-b)
result = subtract(20,5)
print(result)

## Q8. Create a function to multiply two numbers
#Create a function called `multiply(a, b)`.

def multiply (a,b):
    return (a*b)
result = multiply(4,5)
print(result)

## Q9. Create a function to divide two numbers
#Create a function called `divide(a, b)`.

def divide (a,b):
    return (a/b)
result = divide(20,4)
print(result)

# Part 3: Return Values
## Q10. Create a function to calculate total salary

def calculate_total_salary(base_salary, bonus):
    return base_salary + bonus
result = calculate_total_salary(35000, 5000)
print(result)

## Q11. Create a function to calculate loan EMI-like monthly amount
#Create a function called `calculate_monthly_payment(loan_amount, months)`.

def calculate_monthly_payment(loan_amount, months):
    return loan_amount / months
result = calculate_monthly_payment(120000, 12)
print (result)

## Q12. Create a function to calculate approval rate
#Create a function called `calculate_approval_rate(total_applications, approved_applications)`.

def calculate_approval_rate(total_applications, approved_applications):
    return approved_applications / total_applications *100

result = calculate_approval_rate(10, 6)
print(result)

## Q13. Create a function to calculate rejection rate
#Create a function called `calculate_rejection_rate(total_applications, rejected_applications)`.

def calculate_rejection_rate(total_applications, rejected_applications):
    return rejected_applications / total_applications *100

result = calculate_rejection_rate(10, 3)
print(result)

# Part 4: Conditions Inside Functions
## Q14. Create a function to check loan eligibility
#Create a function called `check_loan_eligibility(credit_score)`.

def check_loan_eligibility(credit_score):
    if credit_score >=700:
        return "Eligble for loan"
    else:
        return "Not eligible for loan"
print(check_loan_eligibility(720))

## Q15. Create a function to return credit score band
#Create a function called `get_credit_score_band(credit_score)`.

def get_credit_score_band(credit_score):
    if credit_score >=750:
        return "Excellent"
    elif credit_score > 700:
        return "Good"
    elif credit_score > 650:
        return "Fair"
    else:
        return "Poor"
print(get_credit_score_band(760))

## Q16. Create a function to return loan amount category
#Create a function called `get_loan_amount_category(loan_amount)`.

#Rules

def get_loan_amount_category(loan_amount):
    if loan_amount >= 1000000:
        return "Very high"
    elif loan_amount >= 500000:
        return "High"
    elif loan_amount >=200000:
        return "Medium"
    else:
        return 'Low'
print(get_loan_amount_category(750000))

# Part 5: Default Arguments
## Q17. Create a greeting function with default value
#Create a function called `greet_user(name, greeting="Hello")`.

def greet_user(name, greeting = "Hello"):
    return f"{greeting}, {name}"
print(greet_user("Raman"))

## Q18. Create a function with default country

#Create a function called `user_location(name, city, country="India")`.

def user_location(name, city, country = "India"):
    return f"{name} lives in {city}, {country}"
print(user_location("Raman", "Delhi"))
print(user_location("John", "New York", "USA"))

## Q19. Create a function to calculate final price after discount
#Create a function called `calculate_final_price(price, discount_percentage=10)`.

def calculate_final_price(price, discount_percentage=10):
    return price - price * discount_percentage / 100
print(calculate_final_price(1000))
print(calculate_final_price(1000, 20))

# Part 6: Local Variables and Scope
## Q20. Create a function with a local variable
#Create a function called `show_message()`.

def show_message():
    message = "This is a local variable"
    print(message)

    ## Q21. Create a function to calculate bonus
#Create a function called `calculate_bonus(salary)`.

def calculate_bonus(salary):
    bonus = salary * 0.10
    return bonus
print(calculate_bonus(50000))

#Can you access the variable `bonus` outside the function?
# YES , because of return statement 

# Part 7: Nested Functions
## Q22. Create a nested function
#Create a function called `outer_function()`.

#Inside it, create another function called `inner_function()`.

#`inner_function()` should print:

def outer_function():
    def inner_function():
        print("I am inside inner function")
    inner_function()
outer_function()

## Q23. Create a nested function for loan summary
#Create a function called `loan_summary(loan_amount, credit_score)`.

#Inside this function, create two nested functions:

#1. `get_loan_category()`
#2. `get_credit_band()`

def loan_summary(loan_amount, credit_score):
    def get_loan_category():
        if loan_amount >= 1000000:
            return "very high"
        elif loan_amount >=500000:
            return "high"
        elif loan_amount >=200000:
            return "medium"
        else:
            return "low"
        
        def get_credit_histroy():
            if credit_score >=750:
                return "Excellent"
            elif credit_score > 700:
                return "Good"
            elif credit_score > 650:
                return "Average"
            else:
                return "Poor"
            print(loan_summary(750000, 720))


# Part 8: Functions With Lists
## Q24. Create a function to count approved applications
#Create a function called `count_approved_applications(statuses)`.

def count_approved_applications(statuses):
    return statuses.count("Approved")
loan_statuses = ["Approved", "Rejected", "Approved", "Pending", "Approved"]
print(count_approved_applications(loan_statuses))

## Q25. Create a function to calculate total loan amount
#Create a function called `calculate_total_loan_amount(amounts)`.

def calculate_total_loan_amount(amounts):
    return sum(amounts)
loan_amounts = [200000, 500000, 750000, 1000000]
print(calculate_total_loan_amount(loan_amounts))

## Q26. Create a function to find high-value loans
#Create a function called `get_high_value_loans(amounts)`.

def get_high_value_loans(amounts):
    for amounts in amounts:
        if amounts >=500000:
            print(amounts)

loan_amounts = [200000, 500000, 750000, 1000000, 300000]                  #error
print(get_high_value_loans(loan_amounts))

# Part 9: Functions With List of Dictionaries
## Q27. Create a function to count total applications
def count_total_applications(applications):
    return len(applications)
print(count_total_applications(loan_statuses))

## Q28. Create a function to count approved applications
def count_approved_applications(statuses):
    count = 0
    for status in statuses:
        if status == "Approved":
            count += 1
    return count

print(count_approved_applications(loan_statuses))

## Q29. Create a function to calculate total approved loan amount

#Create a function called `calculate_approved_loan_amount(applications)`.

def calculate_approved_loan_amount(applications):
    total_amount = 0
    for application in applications:
        if application["status"] == "Approved":
            total_amount += application["loan_amount"]

print(calculate_approved_loan_amount(loan_statuses))

## Q30. Create a function to generate loan summary report
#Create a function called `generate_loan_summary(applications)`.

## Q31. Handle division by zero
#Update the `calculate_approval_rate(total_applications, approved_applications)` function.
#doubt

   