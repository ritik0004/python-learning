# Part 1: Basic Try-Except
## Q1. Handle division by zero
#Create two variables:

from ast import If

from sqlalchemy import Result
from sympy import python
from tomlkit import value


try:
    result = a/b
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
    
## Q2. Handle file not found
a = 20
b = 5

try:
      result = a/b
      print(result)
except ZeroDivisionError:
      print("Error: Cannot divide by zero")

 ## Q3. Handle invalid number conversion

 #value = "abc"

try:
    number = int(value)
    print(number)
except ValueError:
     print("Error: Invalid number conversion")

## Q4. Handle valid number conversion
value = "100"

try:
     number = int(value)
     print(number)
except ValueError:
     print("Error: Invalid number conversion")

# Part 2: Handling Specific Exceptions
## Q5. Handle `ZeroDivisionError`

#Write a program where:
x = 10 / 0

try:
     x = 10 / 0
     print(x)
except ZeroDivisionError:
     print("Error: Cannot divide by zero")

## Q6. Handle `ValueError`
#Write a program where:
number = int("Python")

try:
     number = int("Python")
     print(number)
except ValueError:
     print("ValueError occured")
    
## Q7. Handle `IndexError`
#Use this list:

#python
numbers = [10, 20, 30]

try:
     print(numbers[5])
except IndexError:
     print("IndexError occurred: List index is out of range")
    
## Q8. Handle `KeyError`
#python
student = {
   # "name": "Gaurang",
   # "role": "Product Analyst"
   }
try:
     print(student["salary"])
except KeyError:
     print("KeyError occurred: Key not found in dictionary")

## Q9. Handle `TypeError`
result = "10" + 5

try:
     result = "10" + 5
     print(result)
except TypeError:
     print("TypeError occurred: Unsupported operation between string and number")

# Part 3: Multiple Except Blocks
## Q10. Handle multiple possible errors

#python
values = [10, 20, 30]
index = 5
divisor = 0

try:
     print(values[index])
     result = value / divisor
     print(result)
except IndexError:
     print("IndexError occurred")
except ZeroDivisionError:
     print("ZeroDivisionError occurred")

## Q11. Change the index and test division error
#python
values = [10, 20, 30]
index = 1
divisor = 0

try:
     value = values[index]
     result = value / divisor
     print(result)
except IndexError:
     print("IndexError occured")
except ZeroDivisionError:
     print("ZeroDivisionError occured")

## Q12. Handle general exception
#python
data = {"amount": "abc"}
result = int(data["amount"]) / 2

try:
     result = int(data["amount"]) / 2
     print(result)
except Exception as e:
     print("Error occurred:",e)

# Part 4: Finally Block
## Q13. Use `finally` with division
a = 10
b = 0

try:
     result = a / b
     print(result)
except ZeroDivisionError:
     print("Error:Cannot divide by zero")
finally:
     print("Execution completed")

## Q14. Finally should run even when there is no error

a = 20
b = 5

try:
     result = a / b
     print(result)
except ZeroDivisionError:
     print("Error:Cannot divide by zero")
finally:
          print("Execution completed")

## Q15. File closing simulation using finally
#python
file_open = True

try:
     print("Processing file")
finally:
     print("Closing file")

# Part 5: Raise Custom Errors
#python
loan_amount = -50000

try:
     if loan_amount < 0:
          raise ValueError("Loan amount cannot be negative")
except ValueError as e:
     print("Error:",e)

## Q17. Raise error for invalid credit score
credit_score = 950
#Valid credit score should be between `300` and `900`.
#If credit score is less than `300` or greater than `900`, raise a `ValueError`.

try:
     if credit_score < 300 or credit_score > 900:
          raise ValueError("Invalid credit score")
except ValueError as e:
     print("Error:",e)

## Q18. Raise error for missing customer ID
customer_id = ""
#If `customer_id` is empty, raise a `ValueError`.

try:
     if customer_id == "":
          raise ValueError("Customer ID is required")
except ValueError as e:
     print("Error:",e)


# Part 6: Exception Handling Inside Functions
## Q19. Create a safe division function

#Create a function:

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

print(safe_divide(10, 2))
print(safe_divide(10, 0))

## Q20. Create a safe integer conversion function
def safe_int_conversion(value):
 try:
        return int(value)
 except ValueError:
        print("Invalid number")

print(safe_int_conversion("10"))
print(safe_int_conversion("Python"))

## Q21. Create a function to validate loan amount
def validate_loan_amount(loan_amount):
   try:
     if loan_amount <= 0:
        raise ValueError("Valid loan amount greater than 0")
        return "Valid loan amount"
   except ValueError as e:
    print("Error:", e)

print(validate_loan_amount(500000))
print(validate_loan_amount(-10000))

## Q22. Create a function to validate credit score
def validate_credit_score(credit_score):
    try:
        if credit_score < 300 or credit_score > 900:
            raise ValueError("Invalid credit score")
        return "Valid credit score"
    except ValueError as e:
        print("Error:", e)

print(validate_credit_score(750))
print(validate_credit_score(1000))

# Part 7: Business Scenario-Based Questions
## Q23. Validate loan amounts
loan_applications = [
    {"application_id": "APP001", "customer_id": "C001", "loan_amount": 500000, "credit_score": 760},
    {"application_id": "APP002", "customer_id": "C002", "loan_amount": -300000, "credit_score": 620},
    {"application_id": "APP003", "customer_id": "", "loan_amount": 750000, "credit_score": 710},
    {"application_id": "APP004", "customer_id": "C004", "loan_amount": 200000, "credit_score": 950},
    {"application_id": "APP005", "customer_id": "C005", "loan_amount": 1000000, "credit_score": 800}
]
for application in loan_applications:
     try:
           if application["loan_amount"] <=0:
                raise ValueError("Invalid loan amount")
     except ValueError as e:
          print("Error:", e)

## Q24. Validate customer IDs
for application in loan_applications:
     try:
           if application["customer_id"] == "":
                raise ValueError("Valid customer ID is required")
     except ValueError as e:
          print("Error:", e)

## Q25. Validate credit scores
for application in loan_applications:
     try:
           if application["credit_score"] < 300 or application["credit_score"] > 900:
                raise ValueError("Invalid credit score")
     except ValueError as e:
          print("Error:", e)

## Q26. Create a clean and rejected application list
valid_applications = []
rejected_applications = []

for application in loan_applications:
     #try:
           if application["loan_amount"] <=0:
                raise ValueError("Invalid loan amount")
           if application["customer_id"] == "":
                raise ValueError("Missing customer ID")
           if application["credit_score"] < 300 or application["credit_score"] > 900:
                raise ValueError("Invalid credit score")
     #except ValueError as e:

## Q28. Create a reusable application validation function
def validate_application(application):
        try:
            if application["loan_amount"] <=0:
                    raise ValueError("Invalid loan amount")
            if application["customer_id"] == "":
                    raise ValueError("Missing customer ID")
            if application["credit_score"] < 300 or application["credit_score"] > 900:
                    raise ValueError("Invalid credit score")
            return "Valid application"
        except ValueError as e:
            print("Error:", e)

## Q30. Explain in comments: why do we use exception handling?
# It is imortant in real world engineering projects because data can contain invalid or missing values. Without exception handling a single error can stop the entire program.
#This improves reliability, debugging & oveall system stability.