#program to add two matrices
'''a = input("enter the dimension")
print(a)
b =int (input("enter the first matrxi"))
print(b)
c = int(input("enter the second matrix"))
print(c)
d = input("enter resulted matrix")'''
a = [[1,3,4],[6,7,8]]
b = [[4,5,6],[1,0,9]]
re = [[0,0,0],[0,0,0]]
for i in range(len(a)):

   for j in range(len(a[0])):
       re[i][j] = a[i][j] + b[i][j]
for r in re:
   print(r)

