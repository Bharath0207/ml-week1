#4
it_companies= {"Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"}
print(len(it_companies)) #Finding the length of the set it_companies
it_companies.add("Twitter") #Adding Twitter to it_companies
print(it_companies)
multiple_IT_companies = {"TCS","Wipro","Infosys"} #Adding multiple_IT_companies
print(multiple_IT_companies)
multiple_IT_companies.update(multiple_IT_companies) #Inserting the multiple_IT_companies to multiple_IT_companies
print(it_companies)
it_companies.remove("Wipro") #Removing the it_companies
print(it_companies)
#remove()- It will delete an item in a set and print from a SET[-11
#discard()-It will delete an item in a set and print from a SET[O]
A = {19,22, 24, 20, 25, 26}
print(A)
B= {19, 22, 20, 25, 26, 24, 28, 27}
print(B)
C=A.union(B) #Joining A and B
print(C)
A.intersection_update(B) #Finding A intersection B
print(A)
D=A.issubset(B) #Finding wheather A is subset to B or not
print(D)
E=A.isdisjoint(B) #Finding wheather A is disjoint to B or not
print(E)
print(A.union(B))
print(B.union(A) )
print(A.symmetric_difference(B))
#Delete the sets completely
age =[22, 19, 24, 25, 26, 24, 25, 24]
print(age)
#Convert the ages to a set and compare the length of the list and the set.
