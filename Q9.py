#9.
#number of students
n = int(input("Enter number of students : "))
#this line read inputs from user using map() function
x = list(map(int,input("/nEnter weights of students :").strip().split()))[:n]
print("\nL1 : ",x)
y = [i/2.2048364154 for i in x]
y = ['%2f' % elem for elem in y]
print(y)