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


