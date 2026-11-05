matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(len(matrix))

print(len(matrix[0]))

print(matrix[1][2])

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end="")
    print("\n")

