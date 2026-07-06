# Step 1: Import required libraries
import json
import pandas as pd

# -----------------------------------------
# Step 2: Read JSON file
# -----------------------------------------

# Open and load JSON file
with open("data/customers.json", "r") as file:
    customers_data = json.load(file)

# Convert JSON (list of dicts) into DataFrame
customers_df = pd.DataFrame(customers_data)

print("Customers DataFrame:")
print(customers_df)
print("-" * 50)

# # -----------------------------------------
# # Step 3: Read CSV file
# # -----------------------------------------

loans_df = pd.read_csv("data/loans.csv")

print("Loans DataFrame:")
print(loans_df)
print("-" * 50)

# # -----------------------------------------
# # Step 4: Read TXT file
# # -----------------------------------------

with open("data/notes.txt", "r") as file:
    roles = file.read().splitlines()

# Convert text data into DataFrame
roles_df = pd.DataFrame(roles, columns=["target_roles"])

print("Roles DataFrame:")
print(roles_df)
print("-" * 50)

# # -----------------------------------------
# # Step 5: Merge JSON and CSV data
# # -----------------------------------------

# # Merge loans with customers on customer_id
# merged_df = pd.merge(loans_df, customers_df, on="customer_id", how="left")

# print("Merged Loan + Customer Data:")
# print(merged_df)
# print("-" * 50)

# # -----------------------------------------
# # Step 6: Add TXT data to final DataFrame
# # -----------------------------------------

# # Add roles as a new column (repeated values)
# merged_df["suggested_role"] = roles_df["target_roles"][0]

# print("Final Combined DataFrame:")
# print(merged_df)