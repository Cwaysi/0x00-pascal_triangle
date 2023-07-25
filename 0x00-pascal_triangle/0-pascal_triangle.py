#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    pascal = [[1]]  # The first row is always [1]

    for i in range(1, n):
        row = [1]  # The first element of each row is always 1
        for j in range(1, i):
            row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        row.append(1)  # The last element of each row is always 1
        pascal.append(row)

    return pascal

# Test the function
# n = 5
# result = pascal_triangle(n)
# for row in result:
#    print(row)

