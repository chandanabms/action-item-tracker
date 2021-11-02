#python program on lists
'''mylist = ['apple',3,'true','banana',0.3]
print(mylist)
mylist1 = ['black']
#j = mylist + mylist1
for i in mylist1:
	mylist.append(i)
print(mylist)
print(mylist[3:])
fruitsbasket = [['apple', 5],['orange', 4]]
#print(fruitsbasket[0:1])
a = input("enter the fruits u want: ")
if a == 'apple':
	print(fruitsbasket[0])
elif a == 'orange':
	print(fruitsbasket[1])
else:
	print("we dont have other fruits")
b = input("how many fruits u want? ")
for i in range(len(a)):
	print(i)'''
name = input("what is your name?" )
print("hello",name, "can you please provide the first action item")
deadline = input("what is the deadline of this activity: ")
forms = input("enter the date and time in mm/dd/yyyy format and time in hh/mm")
list1=[]
list1.append(forms)
print(list1)
print("what is the status of the current action item: ")
status = input("enter the status: ")
if status == 'inqueue':
	print("take this project as soon as possible")
elif status == 'inprogess':
	print("completed in estimated time")
elif status == 'done':
	print("your project is ready")
else:
	print("project cancelled")
list2=[]
list2.append(status)
print(list2)

