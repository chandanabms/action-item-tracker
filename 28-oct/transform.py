#python program to transpose the matrix
row = int(input("enter the row num: "))
col = int(input("enter the number of column: "))
print("enter the elements for matrix 1: ")
matrix1 = [[int(input()) for i in range(col)] for j in range (row)]
print("matrix1: ")
for i in range(row):
        for j in range(col):
                print("|",matrix1[i][j],"|")
for k in matrix1:
        print("|",k,"|")

print("matrix before transpose")
for row in matrix1:
    print(row)
result = [[matrix1[j][i] for j in range(len(matrix1))] for i in range(len(matrix1))]
#result = [[matrix[j][i] for j in range(matrix)] for i in range(matrix)]
print("matrix after transpose")
for row in result:
    print(row)
