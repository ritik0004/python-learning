# Online Python compiler (interpreter) to run Python online.

print(type(25)) #int
print(type("Gaurang")) # str
print(type(35000.50)) #float
print(type(True)) #- boolean
print(type(["SQL", "Python", "Excel"])) #- list
print(type({"role": "Product Analyst", "experience": 2}))#- dictionary
print(type({"Delhi", "Mumbai", "Pune"}))# - set


# Part 2: Indexing Practice

skills = ["SQL", "Python", "Excel", "Power BI", "Google Analytics"]


## Q2. Print the first skill.
print(skills[0])



## Q3. Print the third skill.
print(skills[2])



## Q4. Print the last skill using positive indexing.


print(skills[4])


## Q5. Print the last skill using negative indexing.


print(skills[-1])

# Part 3: Dictionary Access


employee = {
    "name": "Gaurang",
    "role": "Product Analyst",
    "salary": 35000,
    "skills": ["SQL", "Python", "GA4"]
}



print(employee["name"])


## Q7. Print the employee role.


print(employee["role"])


## Q8. Print the second skill from the `skills` list inside the dictionary.


print(employee["skills"][1])




# Part 4: Mutability Practice

## Q9. Create a list and change its second value.


numbers = [10, 20, 30, 40]


numbers[1]=200
print(numbers)



## Q10. Create a dictionary and update the value of `role`.




profile = {
    "name": "Gaurang",
    "role": "Product Analyst"
}

profile["role"]="Data Engineer"
print(profile)



## Q11. Try changing a tuple value.


numbers_tuple = (10, 20, 30)


#Try to change `20` to `200`.

##Write the error message as a comment.

##ERROR!
#Traceback (most recent call last):
 #@ File "<main.py>", line 12, in <module>
#TypeError: 'tuple' object does not support item assignment

#Expected learning:

#```text
#Tuple is immutable.



## Q12. Try changing a string value.

#Use this string:

#```python
#name = "Gaurang"
#```

#Try to change the first character from `G` to `S`.

#Write the error message as a comment.
#ERROR!
#Traceback (most recent call last):
#  File "<main.py>", line 11, in <module>
#TypeError: 'str' object does not support item assignment
#Expected learning:

#```text
#String is immutable.
#```

#---

# Part 5: Set Practice


cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Bangalore"]


## Q13. Convert the list into a set to remove duplicates.

#used chatgpt to  understand
unique=list(set(cities))
print(unique)

#Expected output:

#```text
#{'Delhi', 'Mumbai', 'Pune', 'Bangalore'}
#```
#print()
#Note: The order may be different. That is okay.

## Q14. Check whether `"Delhi"` exists in the set.

 
cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Bangalore"] 
print("Delhi"  in cities)

#Expected output:
#print("Delhi" exists in cities)
#```text
#True
#```

## Q15. Add `"Chennai"` to the set.

cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Bangalore"]

cities.append("Chennai")
print(cities)
#Expected output should include:

#```text
#Chennai
#```

#---

# Part 6: Big O Understanding

#Answer these questions in plain English.
#big O works for time complexity and space compleaxity , as i am able to understand sometimes we have a fixed value to check time taken will
#be less , but for not unique value and we have million values it takes very time taking

## Q16. What is Big O notation?

#Write the answer in 2–3 lines.
#O(n) # when interprator has to check all the details one by one 
#O(1) # when we have defined path 

#---

## Q17. What is the time complexity of accessing a list item by index?

#Example:

#```python
#numbers = [10, 20, 30]
#print(numbers[1])
#```

#Expected answer:

#```text
#O(1)
#``` time complexity will be low becuase position is  defined

#---

## Q18. What is the time complexity of searching for a value in a list?

#Example:

#```python
#numbers = [10, 20, 30, 40]
#print(30 in numbers)
#```

#Expected answer:
#in this time complexity will be high becuase position is not defined , each and every position is checked and verified
#```text
#O(n)
#```
#
#---

## Q19. What is the average time complexity of searching for a key in a dictionary?

#Example:

#```python
profile = {"name": "Gaurang", "role": "Product Analyst"}
print("name" in profile)
#```
#time complexity will be low becuase position is  defined
#Expected answer:

#```text
#O(1)
#```

#---

## Q20. What is the average time complexity of searching for a value in a set?

#Example:

#```python
#cities = {"Delhi", "Mumbai", "Pune"}
#print("Delhi" in cities)
#```
# time complexity will be high becuase position is not defined , each and every position is checked and verified
#Expected answer:

#```text
#O(n)
#```

#---

# Part 7: Mini Practical Task

## Q21. Create a student profile using a dictionary.

#The dictionary should contain the following keys:


student_profile = {
    "name": "Gaurang",
    "age": 25,
    "current_role": "Product Analyst",
    "target_role": "Data and AI Engineer",
    "skills": ["SQL", "Python", "Excel", "GA4"],
    "monthly_salary": 35000
}


#Now print the following:

#1. Name
#2. Current role
#3. Target role
#4. First skill
#5. Total number of skills

#---
student_profile={"name":"gaurang sharma","age":26,"current role":"product analyst","target role":"AI Engineer","skills":["sql","excel","python"]}
print(student_profile["name"])
print(student_profile["current role"])
print(student_profile["target role"])
print(student_profile["skills"][0])
print(len(student_profile["skills"])) # - used chatgpt
# Evaluation Criteria

