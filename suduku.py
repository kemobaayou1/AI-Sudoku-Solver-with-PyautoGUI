board = [
    [5,0,8,2,1,0,0,1,3],
    [9,1,5,0,0,0,6,0,7],
    [0,8,3,0,1,0,0,0,0],
    [0,6,0,1,2,9,0,3,0],
    [0,3,2,8,0,5,4,7,0],
    [5,0,8,4,0,4,0,0,0],
    [0,0,1,2,0,0,0,0,5],
    [0,0,0,0,8,1,0,2,6],
    [0,0,0,7,4,0,8,0,0]
]
#backtracking
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(bo,i,(row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            bo[row][col]=0
    return False
def valid(bo, num, pos):
#check row
     for i in range(len(bo[0])):
         if bo[pos[0]][i] == num and pos[1] != i:
             return False

#check column
     for i in range(len(bo)):
         if bo[i][pos[1]] == num and pos[0] != i:
             return False
#check box
     box_x = pos[1] // 3
     box_y = pos[0] // 3

     for i in range(box_y*3, box_y*3 + 3):
         for j in range(box_x *3, box_x*3 + 3):
             if bo[i][j] == num and (i,j ) != pos:
                 return False
     return True




#print border after each 3 rows
def print_bored(border):

    for i in range(len(border)):
        if i % 3  == 0 and i != 0:
            print("----------------------------")

#to divied with lettel border in colummn
        for j in range(len(border[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(border[i][j])
            else:
                print(str(border[i][j]) + " ", end="")

# func to find the empty space
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row ,col
    return None

print_bored(board)
solve(board)
print("ـــــــــــــــــــــــــــــــــــــــ")
print_bored(board)