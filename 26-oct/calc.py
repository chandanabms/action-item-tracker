#Get the math operatior from user

#user selects between +, -, *, /, % and ^

'''
user provides input values 
ex: 
operator = +
val1 = 12
val2 = 13

result = 12+13 = 25

'''
print("This is a simple calculator with python")
print("Choose +, -, *, \, % or ^ to do the calculations")
op = input("enter the operator: ")
n1 = int(input("enter the value for 1st num: "))
n2 = int(input("enter the value for 2nd num: "))

#print(int(n1)+int(n2))

if op=="+":
	print("sum of",n1, "and",n2, "is",n1+n2)
elif op=="-":
	print(f"Subtracting {n1} from {n2} is {n1-n2}")
else:
	print("you did not choose the right operator")
