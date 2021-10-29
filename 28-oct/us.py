a = input("enter the dimension: ")
matrix_a= [[int(input()) for i in range(a)] for i in range(a)]
print("First Matrix is: ")
for n in matrix_a:
    print(n)

c = int(input("enter the second matrix"))
print(c)
re = [[0,0],[0,0]]
for i in range(len(a)):
	for j in range(len(a[0])):
		re[i][j] = a[i][j] + b[i][j]
for r in re:
	print(r)


