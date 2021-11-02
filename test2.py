'''title = input("enter the title of the project: ")
print(f"title of the poject is: {title}")
descrption = input("give some information about the project: ")
print("descrption: ",descrption)
dead = input("what is the dead line for " + title + "?")
date = input("please provide tha date and time for in mm-dd-yyyy and hh:mm: "+ title)
lst = []
count = 0
for i in range(count):
	count = count+1'''
a = int(input("length of list"))
lst = []
#a = a+1
for x in range(a):
	title = input("enter the title of the project: ")
	print(f"title of the poject is: {title}")
	descrption = input("give some information about the project: ")
	print("descrption: ",descrption)
	dead = input("what is the dead line for " + title + "?")
	date = input("please provide tha date and time for in mm-dd-yyyy and hh:mm : " + title + "?")
	#a = a+1
	lst.append(a)
	lst.append(title)
	lst.append(dead)
	a = a+1
print(lst)
