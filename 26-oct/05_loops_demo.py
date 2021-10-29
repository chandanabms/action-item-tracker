#Generate a multiplication or a division table based on user input
m = input("enter the multiplication number:")
for i in range(1,11):
	r=int(m)*int(i)
	print(m,"*",i,"=",r)
	i+=i

