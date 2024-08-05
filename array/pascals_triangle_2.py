# Pascal's Triangle II (119, array, easy)

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
    #    1
    #   1 1
    #  1 2 1
    # 1 3 3 1
    # 1 4 6 4 1

 # Example 1:

 # Input: rowIndex = 3
 # Output: [1,3,3,1]

def getRow(rowIndex ):

    triangle = []

    for i in range(0, rowIndex + 1):

        row = []

        if i > 0:
            prevRow = triangle[len(triangle) -1]
        else:
            prevRow = []

        for j in range(0, i + 1):

            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(prevRow[j - 1] + prevRow[j])

        triangle.append(row)

    return triangle[rowIndex]
