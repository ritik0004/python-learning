#Task 1: Read JSON File

from asyncio import Task
import json
import pandas as pd

# Read JSON file
with open("data/customers.json", "r") as file:
    customers = json.load(file)

# Convert it into a Pandas DataFrame
customers_df = pd.DataFrame(customers)

#Print the DataFrame
print(customers_df)

#Print the shape of the DataFrame
print(customers_df.shape)

#Task 2: Read CSV File

#Read loan_applications.csv
loan_df = pd.read_csv("data/loan_applications.csv")

#Convert it into a Pandas DataFrame
loan_df = pd.read_csv("data/loan_applications.csv")

#Print the DataFrame
print(loan_df)

#Print the column names
print(loan_df.columns)

#Task 3: Read TXT File

with open("data/target_roles.txt", "r") as file:
    target_roles_txt = file.read()

    #Convert it into a Pandas DataFrame
    target_roles_df = pd.DataFrame([target_roles_txt], columns=["Target Roles"])

    #Print the DataFrame
    print(target_roles_df)


#Task 4: Basic Validation Checks
#Total number of customers
print("Total number of customers:", len(customers_df))

#Total number of loan applications
print("Total number of loan applications:", len(loan_df))

#Total number of target roles
print("Total number of target roles:", len(target_roles_df))
