#2
#Creating an empty dictionary called dog & Adding name, color, breed, legs, age to the dog dictionary
dog = {"name":"Lyca", "color":"Black", "breed":"Rottwiller","age":2,"legs":4}
#Creating a student dictionary & Adding first_name, last_name, gender, age, marital status, skills, Country, City, address
student = { "first_name":"Bharath", "Last_name":"Reddy", "gender":"male", "age":23, "marital_status":"Unmarried", "skills":["Java","SQL","Python"], "Country":"India", "city":"Hyderabad","adress":"kukatpully"}
print(dog)
print(student)
print(len(student)) #finding the length of the student
print(student["skills"],type(student["skills"])) #finding the data_type 
student["skills"].append("Reading")
student["skills"].append("Cooking") #adding the skills
print(student.keys()) #Getting the dictionary keys as a list
print(student.values()) #Getting the dictionary values as a list