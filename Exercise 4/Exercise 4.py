import numpy as np
matrix = []

row = int(input("Write the size of the row: "))
column = int(input("Write the size of the colums: "))
for i in range(row):
    a = []
    for j in range(column):
        a.append(int(input("Write the numbers that you want do add: ")))
    matrix.append(a)

array = np.array(matrix)
matrix_transpose = array.transpose()

print(matrix_transpose)
   
            