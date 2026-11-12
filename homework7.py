# 方法二：使用嵌套循环动态创建
rows, cols = 3, 3
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        # 填充 1 到 9 的数字作为示例
        row.append(i * cols + j + 1)
    matrix.append(row)

# 逐行显示
print("--- 动态创建的 3x3 矩阵 ---")
for row in matrix:
    print(row)