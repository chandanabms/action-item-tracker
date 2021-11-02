prj_name = input("Enter project name: ")
print(f"Let's start working {prj_name}")
who_is =  input(f"Who is working on {prj_name}? ")
print(f"Welcome to {prj_name} {who_is}")
how_many = int(input(f"How many people are working on {prj_name}? "))
print("Project Summary:")
print(f"{prj_name} will be woked out with {how_many} people with {who_is}...")

if how_many <= 0:
	print("No body likes this project...")
if (how_many >= 5 and how_many<=10):
	print("It's a small sized project!!")
	if(who_is == "Puneeth"):
		print("Project",prj_name,"deals with Python programming")
	if(who_is == "Chandana"):
		print(f"Project {prj_name} deals with Python Testing and Auomation..")
	else:
		print("Dont know what's the project scope..")
elif (how_many>=10 and how_many <=50):
	print("It's a mid sized project")
else:
	print("It's a big big project...")

'''
x = int(input("enter the number: "))
y = int(input("enter the number: "))

if x!=y:
	if x>y:
		print("x is greater")
	else:
		print("y is greaterr")
else:
	print("both are equal")
'''

'''
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")



x = "34$"
y = x.rstrip('$')
int(y)

#compliation error on line 52
'''
