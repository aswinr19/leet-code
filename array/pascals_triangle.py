# Pascal's Triangle (118, array, easy)

# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

    #    1
    #   1 1
    #  1 2 1
    # 1 3 3 1
    # 1 4 6 4 1

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

def generate(numRows ):

    triangle = []

    for i in range(0, numRows):

        row = []
        if i > 0:
            prevRow = triangle[len(triangle) -1]
        else:
            prevRow = []

        for j in range(0, i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(prevRow[j -1] + prevRow[j])

        triangle.append(row)

    return triangle

print(generate(5))
