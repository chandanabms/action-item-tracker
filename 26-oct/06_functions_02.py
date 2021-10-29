#program to choose operator

def check_input():
	print("Do you want a simple calculation or a table? ")
	in_check = input("Press \'c\' for calulator\nPress \'t\' for tables\n: ")
	if in_check == 'c':
		print("We will be doing simple calulations..")
		n1 = int(input("enter the value: "))
		n2 = int(input("enter the value: "))
		print("Choose \'+\', \'-\', \'*\', \'/\'")
		op = input("select an operator from above: ")
		if op == '+':
			print(add(n1, n2))
			#print(n1+n2)
		elif op =='-':
			print(sub(n1,n2))
		elif op =='*':
			print(mul(n1,n2))
		elif op =='/':
			print(div(n1,n2))
		else:
			print("we will do something else...")

	elif in_check == 't':
		#print("you are generating a table")
		#add_table()
		num = input("enter the number to generate table: ")
		steps = input("how many steps do you need? \n: ")
		print("Choose your operation..")
		oper = input("\'M\' for Multiplication\n\'D\' for Division\n\'A\' for Addition\n\'S\' for Subtraction\n: ")
		if oper == 'M' or oper == 'm':
			mul_table(num, steps)
		elif oper == 'D' or oper == 'd':
			div_table(num, steps)
		elif oper =='A' or oper == 'a':
			add_table(num,steps)
		elif oper == 'S' or oper == 's':
			sub_table(num,steps)
		else:
			print("will do something here...")
	else:
		print("there is nothing...")

def add(a,b):
	return (a+b)

def add_table(a,b):
	print("Welcome to print tables..")
	#loop to generate the table here and print the output
	#for i in (1,10):
		#print(i*n1+n2,"\n")
		#check = input("press\'yes\'for continue \press\'no\' to quit: \n: ") 
def sub(a,b):
	return (a-b)


def sub_table(a,b):
	print("this has a subtraction table...")

def mul(a,b):
	return (a*b)

def mul_table(a,b):
	print("print a multiplication table")

def div(a,b):
	return(a/b)

def diuv_table(a,b):
	print("Print a division table")

#in_check = input("Press \'c\' for simple calulation \nPress \'t\' to generate a table: \n: ")


check_input()



'''
if op == '+':
	print(add())
elif op == '-':
	print(sub())

else:
	print("nothing..")

'''
