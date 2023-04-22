import copy

def is_valid(arr, x, y, num):
    arr[x][y] = num
    
    column_list = [arr[i][y] for i in range(9)] 
    zeroes = column_list.count(0)
    if zeroes != 0: zeroes -= 1
    if len(set(column_list)) + zeroes != 9: 
        return False

    row_list = [arr[x][j] for j in range(9)]
    zeroes = row_list.count(0)
    if zeroes != 0: zeroes -= 1
    if len(set(row_list)) + zeroes != 9:
        return False

    row_no = (x//3)*3 
    col_no = (y//3)*3 
    box_list = [arr[i][j] for i in range(row_no, row_no+3) for j in range(col_no, col_no+3)]
    zeroes = box_list.count(0)
    if zeroes != 0: zeroes -= 1
    if len(set(box_list)) + zeroes != 9:
        return False

    return True
     
def empty_cell(arr):
    for x, i in enumerate(arr):
        for y, j in enumerate(i):
            if j == 0:
                return (x, y)
    return None

def solve(arr, steps):
    cell = empty_cell(arr)
    if cell == None:
        return (True, steps, arr)

    x, y = cell
    for i in range(1, 10):
        if is_valid(copy.deepcopy(arr), x, y, i):
            arr[x][y] = i
            steps.append([f"{x}x{y}",  i])
            a, steps, arr = solve(arr, steps)
            if a:
                return True, steps, arr
            
            arr[x][y] = 0
            steps.append([f"{x}x{y}",  " "])


    return False, steps, arr