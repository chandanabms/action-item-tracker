#learning if, elif, else in python

a = input("Enter a number")

check_even = int(a)%2

if(check_even == 0):
	print(a,"is an even number")
elif(check_even == 1):
	print(a,"is an odd number")
else:
	print("Its not a number")
