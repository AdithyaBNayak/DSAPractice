# Wave Print a Matrix
arr = [[1,2,3],[4,5,6],[7,8,9]]
nCol = len(arr[0])
nRow = len(arr)
for col in range(nCol):
    # When row number is even go down
    if col & 1 == 0:
        for i in range(nRow):
            print(arr[i][col], end=" ")

    # When row number is odd go up
    else:
        for j in range(nRow-1,-1,-1):
            print(arr[j][col], end=" ")
