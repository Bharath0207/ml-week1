#3
#Creating a tuple & adding names of sisters and brothers

Brothers = ("Ram", "Laxman")
print (Brothers)
Sisters = ("Sita", "Latha")
print(Sisters)
#Joining brothers and sisters tuples 
Siblings = Sisters + Brothers
print (Siblings)
print(len(Siblings)) #length of the Siblings
family_members= ("Krishna", "Geetha") + Siblings #adding the name of my father and mother
print(family_members) #assigning it to the family_members tuple