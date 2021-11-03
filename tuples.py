'''T1 = (101, "Peter", 22)
T2 = ("Apple", "Banana", "Orange")
T3 = 10,20,30,40,50
print(type(T1))
print(type(T2))
print(type(T3))
tuple1 = tuple(input("Enter the tuple elements ..."))
print(tuple1)
count = 0
for i in tuple1:
	print("tuple1[%d] = %s"%(count, i))
	count = count+1
tup = (1,2,3,4,5,6,7)
print(tup[0])
print(tup[1])
print(tup[2])
# It will give the IndexError
print(tup[9])
tup = tuple(input("enter the title...: "))
print(tup)
tup2 = tuple(input("enter the project description: "))
print(tup2)
for i in tup2:
	print(tuple(tup+tup2))
print(len(tup2))
print(tup[:1])'''
Employee = {1:{"Name": "John", "Age": "29", "Salary":"25000","Company":"GOOGLE"}, 2:{"id":"2", "Name":"Chandana", "Age":"11", "Salary":"20000", "Company":"Bluemindz"}}
print(type(Employee))
print(Employee)
'''print("printing Employee data .... ")
print("Name : %s" %Employee["Name"])
print("Age : %d" %Employee["Age"])
print("Salary : %d" %Employee["salary"])
print("Company : %s" %Employee["Company"])
Employee[4] = {"address":"mysore"}
print(Employee[4])
Employee[3] = 'tcs'
print(Employee)
del(Employee["Name"])
print(Employee)
Employee["lastname"]='alex'
print(Employee)
Employee["salary"]='50000'
print(Employee)'''
user = input("enter the dictionary value you want to search: ")
if user == '1':
	print(Employee[1]['Name'])
	print(Employee[1]['Age'])
	print(Employee[1]['Salary'])
	print(Employee[1]['Company'])
	print(Employee[1])
elif user == '2':
	print(Employee[2]['Name'])
	print(Employee[2]['Age'])
	print(Employee[2]['Salary'])
	print(Employee[2]['Company'])
	print(Employee[2])
else:
	print("nothing to display")
