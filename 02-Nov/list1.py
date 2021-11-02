#python program using dynamic list
def getinputs():
	title = input("enter the title of the project: ")
	print(f"title of the poject is: {title}")
	descrption = input("give some information about the project: ")
	print("descrption: ",descrption)
	dead = input("what is the dead line for " + title + "?")
	date = input("please provide tha date and time for in mm-dd-yyyy and hh:mm: "+ title)
	count = 0
	for i in range(0,10):
        	count += 1
	list = []
	list.append(count)
	list.append(title)
	for j in list:
		print(j,list)
	check_status()
def check_status():
	status = input("what is the current status: ")
	if status == 'inqueue':
        	print("take this project as soon as possible")
	elif status == 'inprogress':
        	print("complete the project in estimated time")
	elif status == 'testing':
		print("in testing")
	elif status == 'done':
        	print("your project is ready")
	else:
       		print("project cancelled")
getinputs()

