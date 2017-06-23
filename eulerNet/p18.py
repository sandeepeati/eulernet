
# maximum sum following a path in the given triangle

# reading the triangle from the triangle19.txt

triangle = []

with open('triangle18.txt') as f:
    for line in f:
        triangle.append([int(i) for i in line.rstrip('\n').split(" ")])


def recSumAtRow(rowData, rowNum):
    # iterate over the given row
    for i in range(len(rowData[rowNum])):
        # add the largest of the values below-left or below-right
        rowData[rowNum][i] += max([rowData[rowNum+1][i],rowData[rowNum+1][i+1]])
    # base case
    if len(rowData[rowNum])==1:
        return rowData[rowNum][0]
    # recursive case
    else:
        return recSumAtRow(rowData, rowNum-1)



ans = recSumAtRow(triangle, len(triangle)-2)
print(ans)
print(len(triangle)-2)

