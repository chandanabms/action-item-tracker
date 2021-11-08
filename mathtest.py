'''import math
class mathtest:
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def add(self):
		print("sum of ",a + b)
	def sub(self):
		print("subtraction of",a - b)
	def mul(self):
        	print("multiplication of",a * b)
	def div(self):
		print("division of ",a / b)
	def mod(Self):
		print("modules od ",a % b)
	def pow(self):
		print("power of ",a**2)
		print("power ob",b**2)
	def floor(Self):
		print("floor division of",a // b)
	def sqr(self):
		print("square root of a",math.sqrt(a))
		print("square root b".math.sqrt(b))
	def fact(self):
		print("factorial of a",math.factorial(a))
		print("factorial of b",math.factorial(b))
	def log(self):
		print("log of a",math.log(a))
		print("log of b",math.log(b))
	# 3def main(self):
		a = int(input("Enter first number:"))
		b = int(input("Enter second number:"))
		obj = mathtest(a,b)
		print("select operation")
		print("1.Addition")
		print("2.Subtraction")
		print("3.multiplication")
		print("4.division")
		print("5.modules")
		print("6.power")
		print("7.floor division")
		print("8.square root")
		print("9.factorial")
		print("10.logs")
		choice = int(input("Enter your choice:"))
		if choice == 1:
			print(obj.add())
		elif choice == 2:
			print(obj.sub())
		elif choice == 3:
			print(obj.mul())
		elif choice == 4:
			print(obj.div())
		elif choice == 5:
			print(obj.mod())
		elif choice == 6:
			print(obj.pow())
		elif choice == 7:
			print(obj.floor())
		elif choice == 8:
			print(obj.sqr())
		elif choice == 9:
			print(obj.fact())
		elif choice == 10:
			print(obj.log())
		else:
			print("Invalid choice")
		print("do you want to continue press y for yes and no for exit")
		reply = ("enter your choice")
		if reply == "y" or "Y" :
			for i in choice:
				print(i)
		elif reply == "n" or "N":
			print("thank you")'''
def continue():
    resp = input("Continue ? Y/N ")
    if resp == "n" or resp == "N":
        return False
    return True
while True:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = input("Enter choice(1/2/3/4):")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
       print(num1,"+",num2,"=", (num1 + num2))

    elif choice == '2':
       print(num1,"-",num2,"=", (num1 - num2))

    elif choice == '3':
       print(num1,"*",num2,"=", (num1 * num2))

    elif choice == '4':
       print(num1,"/",num2,"=", (num1 / num2))

    else:
       print("Invalid input")
    if not continue() :
