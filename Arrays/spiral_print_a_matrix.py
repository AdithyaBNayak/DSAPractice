# Spriral Print a Matrix - spiral moving clockwise

array = [[1,2,3,4],[5,6,7,8], [9,10,11,12],[13,14,15,16]]
"""
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16
"""
startingRow = 0
startingCol = 0
m = len(array[0])
n = len(array)
endingRow = n-1
endingCol = m-1

count = 0
output = []
total_elements = m * n
while count < total_elements:
    # Printing Starting row
    for i in range(startingCol,endingCol+1):
        if count >= total_elements:
            break
        output.append(array[startingRow][i])
        count += 1        
    startingRow += 1

    # Printing Ending Column
    for i in range(startingRow,endingRow+1):
        if count >= total_elements:
            break
        output.append(array[i][endingCol])
        count += 1        
    endingCol -= 1

    # Printing Ending Row
    for i in range(endingCol,startingCol-1, -1):
        if count >= total_elements:
            break
        output.append(array[endingRow][i])
        count += 1        
    endingRow -= 1

    # Printing Starting Column
    for i in range(endingRow,startingRow-1, -1):
        if count >= total_elements:
            break
        output.append(array[i][startingCol])
        count += 1        
    startingCol += 1    

print(output)