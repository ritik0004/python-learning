import json 
import pandas as pd

with open("data/customers.json","r") as file:
    customers_data=json.load(file)

customers_df=pd.DataFrame(customers_data)
print(customers_df)
print(customers_df.shape)
total_customers=len(customers_df)
print(total_customers)


loans_df=pd.read_csv("data/loan_applications.csv")
print("Loans DataFrame:")
print(loans_df)
print(loans_df.columns)
total_loan_applications=len(loans_df)
print(total_loan_applications)

with open("data/target_roles.txt","r") as file:
    roles=file.read().splitlines()
roles_df=pd.DataFrame(roles,columns=["target_role"])
print("Roles DataFrame:")
print(roles_df)
total_target_roles=len(roles_df)
print(total_target_roles)


