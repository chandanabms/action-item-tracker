#learning variables in python
myname = input("Enter your name: ")
age = input("Enter your age: ")
edu = input("What is your educational qualification? ")

#print(myname)

age = int(age)

if age > 18 and age < 25:
	print("Hello", myname, "you are", age,"years old and your highest education is",edu)

elif age >= 25 and age <= 100:
	print("Hello", myname,"You are over qualified")

elif age == 15 or age == 101:
	print("Hi", myname,"hope you are doing great..." )

else:
	print("Hello", myname,"you are not qualified..")

