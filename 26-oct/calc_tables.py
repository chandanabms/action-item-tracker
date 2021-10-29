#generate tables according to operators
print("tables to generate")
print("select any operator")
op = input("enter the operator")
n1 = int(input("enter the 1st num"))
steps = 10
if op=="+":
	for i in range(1,steps):
		r=i+n1
		print(i,"*",n1,"=",r)
elif op=="-":
	for i  in range(1,steps):
		r=i-n1
		print(i,"*",n1,"=",r)
elif op=="*":
	for i in range(1,steps):
		r=i*n1
		print(i,"*",n1,"=",r)
elif op=="/":
	for i in range(1,steps):
		r=i/n1
		print(r)
else:
	print("opertor doesnt match")
