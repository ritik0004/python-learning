a=10
b=0

try:
  result=(a/b)
  print(result)

except ZeroDivisionError:
  print("Error: Cannot divide by zero")


#2
a = 20
b = 5
try:
  result=(a/b)
  print(result)

except ZeroDivisionError:
  print("Error: Cannot divide by zero")

#3
value = "abc"

try:
  number= int(value)
  print(number)

except ValueError:
    print("Error: Invalid number conversion")

#4
value=100
try:
  xx=int(value)
  print("converted value":xx)    

except ValueError:
    print("Error: Invalid number conversion")

#5
x = 10 / 0
try:
  result=(a/b)

except ZeroDivisionError:
  print("ZeroDivisionError occurred")  


#6

try:
  number = int("Python") 

except ValueError:
    print("ValueError occurred")


## Q7. Handle `IndexError`

numbers = [10, 20, 30]
try :
  print(numbers[5])

except IndexError:
    print("IndexError occurred: List index is out of range")

    

#8
student = {
    "name": "Gaurang",
    "role": "Product Analyst"
}


try:
  student["salary"]

except KeyError:
  print("KeyError occurred: Key does not exist")  


#9


try :
  result = "10" + 5
  print(result)


except  TypeError:
  print("TypeError occurred: Unsupported operation between string and number")


#10
values = [10, 20, 30]
index = 5
divisor = 0

try:
    value = values[index]
    result = value / divisor
    print(result)

except IndexError:
    print("IndexError occurred")

except ZeroDivisionError:
    print("ZeroDivisionError occurred")  

#11
values = [10, 20, 30]
index = 1
divisor = 0

try:
  value=values[index]
  result=value/divisor

except IndexError:
      print("IndexError occurred")
except ZeroDivisionError:
      print("ZeroDivisionError occurred")   


#12 NOT ABLE TO UNDERSTAND this statement

data = {"amount": "abc"}

try:
  result = int(data["amount"]) / 2      
  print(result)
   
except Exception as e:
    print("Error occurred:", e)   

#13
a = 10
b = 0

try :
  xx1=a/b
  print(xx1)

except  ZeroDivisionError:
  print("cannot divide by zero")


finally:
    print("Execution completed")


#14
a = 20
b = 5
try :
  xx1=a/b
  print(xx1)

except  ZeroDivisionError:
  print("cannot divide by zero")


finally:
    print("Execution completed") 


#15
file_open = True

try:
    print("Processing file")

finally:
    print("Closing file")


#16 (used Chatgpt)
loan_amount = -50000

try :
  if loan_amount<0:
    raise ValueError ("Loan amount cannot be negative")

except ValueError as e:
    print("Error:", e)   


#17
credit_score = 950
try:
  if credit_score>900 and credit_score<300 :
    raise ValueError ("Invalid credit score")

except ValueError as e:
    print("Error:", e)


#18
customer_id = ""   
try:
  if customer_id=="":
    raise ValueError ("Customer ID is required")

except ValueError as e:
    print("Error:", e) 

#19
def safe_divide(a, b):

      try:
        return a/b
        

      except ZeroDivisionError:
        return "Cannot divide by zero"

print(safe_divide(10, 2))
print(safe_divide(10, 0))  

#20
def safe_int_conversion(value):

      try:
        xx2=int(value)
        return xx2


      except ValueError:
        return "Invalid number"

print(safe_int_conversion("100"))
print(safe_int_conversion("abc"))


#21
def validate_loan_amount(loan_amount):
       try:
        if loan_amount > 0:
          return "Valid loan amount"

        else:
          ValueError("Loan amount must be greater than 0")  

       
       except ValueError as e:
        return str(e)

print(validate_loan_amount(500000))
print(validate_loan_amount(-10000))

#22    i am not able to do value error as e 
def validate_credit_score(credit_score):
    try :
      if 300 <= credit_score <= 900:
         return "Valid credit score"

      else:
        return ValueError("Invalid credit score")

    except ValueError as e:
        return str(e)

print(validate_credit_score(720))
print(validate_credit_score(950))  

#23
loan_applications = [
    {"application_id": "APP001", "customer_id": "C001", "loan_amount": 500000, "credit_score": 760},
    {"application_id": "APP002", "customer_id": "C002", "loan_amount": -300000, "credit_score": 620},
    {"application_id": "APP003", "customer_id": "", "loan_amount": 750000, "credit_score": 710},
    {"application_id": "APP004", "customer_id": "C004", "loan_amount": 200000, "credit_score": 950},
    {"application_id": "APP005", "customer_id": "C005", "loan_amount": 1000000, "credit_score": 800}
]
for i in  loan_applications:
    try :
      
          if i["loan_amount"]>0:
            print("Valid amount")

          else:
            raise ValueError

    except ValueError:
            print(i["application_id"], "Invalid loan amount")     


#24 riase and return error doubt
for i in  loan_applications:
    try :
      
          if i["customer_id"]=="":
            raise  ValueError

          else:
            print(i["customer_id"],"is valid")
            

    except ValueError:
            print(i["customer_id"], "Invalid")


#25

for i in  loan_applications:
    try :
      
          if not (300<=i["credit_score"] <=900):
            raise  ValueError

          else:
            print(i["application_id"],"is valid")
            

    except ValueError:
            print(i["application_id"], "Invalid")



#26            

  

