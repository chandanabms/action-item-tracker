#use of functions in py

a = 15
b = 30

def hello():
	return ("hello")

def add(a,b):
	print(a,",", b)
	return a+b

print(add(12,13))
print(add("abc", "xyz"))
print(add(a,b))

print(a,",", b)
#print("this is from a", hello(),"() function")
