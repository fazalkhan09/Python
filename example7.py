# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
input_str=input("Enter the values for rows and cols separeted by comma in 2-D matrix")
dimensions=[int(i) for i in input_str.split(",")]
rows=dimensions[0]
cols=dimensions[1]
multilist=[[0 for col in range(cols)] for row in range(rows)]
for row in range(rows):
    for col in range(cols):
        multilist[row][col]=row*col
print(multilist)