import math
class maths:
	def add(x, y):
		return x + y
	def subtract(x, y):
		return x - y
	def multiply(x, y):
		return x * y
	def divide(x, y):
		return x / y
	def mod(x,y):
                return x % y
	def pow(x,y):
		return x**2
		return y**2
	def floor(x,y):
		return x // y
	def sqr(x,y):
		return math.sqrt(x)
		return math.sqrt(y)
	def fact(x,y):
		return math.factorial(x)
		return math.factorial(y)
	def log(x,y):
		return math.log(x)
		return math.log(y)
	print("Select operation.")
	print("1.Add")
	print("2.Subtract")
	print("3.Multiply")
	print("4.Divide")
	print("5.modules")
	print("6.power")
	print("7.floor division")
	print("8.square root")
	print("9.factorial")
	print("10.logs")
	while True:
		choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")
		if choice in ('1', '2', '3', '4','5','6','7','8','9','10'):
			num1 = int(input("Enter first number: "))
			num2 = int(input("Enter second number: "))
		if choice == '1':
			print("addition of",num1,"and",num2,"is", add(num1, num2))
		elif choice == '2':
			print("subtraction of",num1,"and",num2,"is", subtract(num1, num2))
		elif choice == '3':
			print("multiplication of",num1,"and",num2,"is", multiply(num1, num2))
		elif choice == '4':
			print("division of",num1,"and",num2,"is", divide(num1, num2))
		elif choice == '5':
			print("modulus of ",num1,"and",num2,"is", mod(num1, num2))
		elif choice == '6':
			print("power of",num1,"and",num2,"is", pow(num1, num2))
		elif choice == '7':
			print("floor division of",num1,"and",num2,"is", floor(num1, num2))
		elif choice == '8':
                        print("square root of",num1,"and",num2,"is", sqr(num1,num2))
		elif choice == '9':
                        print("factorial of",num1, "and",num2,"is", fact(num1, num2))
		elif choice == '10':
                        print("logs of ",num1,"and",num2,"is", log(num1,num2))
		else:
                        print("Invalid choice")

		check = input("Do you want to continue  ? (yes/no): ")
		if check == "no":
			break
		else:
			print("Invalid Input")
