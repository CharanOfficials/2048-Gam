import random
def startGame():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat

def addNew2(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while (mat[r][c]) != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2

def getCurrentState(mat):
    # for the entire board to check whether 2048 is present
    for r in range(4):
        for c in range(4):
            if mat[r][c] == 2048:
                return 'WON'

    # for the rntire board to chrck whether the 0 is present 
    for r in range(4):
        for c in range(4):
            if mat[r][c] == 0:
                return 'GAME NOT OVER'
    
    # Every row and column except the last row and column    
    for r in range(3):
        for c in range(3):
            if mat[r][c] == mat[r][c+1] or mat[r][c] == mat[r+1][c]:
                return 'GAME NOT OVER'

    # for checking the last row
    for c in range:
        if mat[3][c] == mat[3][c+1]:
            return "GAME NOT OVER"

    # for checking the last column
    for r in range(3):
        if mat[r][3] == mat[r+1][3]:
            return "GAME NOT OVER"
        
    return "LOST"

# move all the non zeroes on one side and all of the rest on another side
def compression(mat):
    changed = False
    newMat = [[0]*4 for i in range(4)]
    for r in range(4):
        pos = 0
        for c in range(4):
            if mat[r][c] != 0:
                newMat[r][pos] = mat[r][c]
                if pos != j:
                    changed = True
                pos+=1
    return newMat, changed

# left move
def merge(mat): 
    changed = False
    for r in range(4):
        for c in range(3):
            if mat[r][c] == mat[r][c+1] and mat[r][c] != 0:
                mat[r][c] = mat[r][c]*2
                mat[r][c+1] = 0
                changed = True
                
    return mat, changed
                
def reverse(mat):
    newMat = []
    for i in range(4):
        newMat.append([])
        for j in range(4):
            newMat[i].append(mat[i][4-j-1])
    return newMat

def transposeMatrix(mat):
    newMat = []
    for i in range(4):
        newMat.append([])
        for j in range(4):
            newMat[i].append(mat[j][i])
    return newMat

def leftMove(grid):
    newGrid, change1 = compression(grid)
    newGrid, change2 = merge(newGrid)
    changed = change1 or change2
    newGrid, temp = compression(newGrid)
    return newGrid, changed

def rightMove(grid):
    newGrid = reverse(grid)
    newGrid, change1 = compression(grid)
    newGrid, change2 = merge(newGrid)
    changed = change1 or change2
    newGrid, temp = compression(newGrid)
    newGrid = reverse(newGrid)
    return newGrid, changed

def upMove(grid):
    newGrid = transposeMatrix(grid)
    newGrid, change1 = compression(newGrid)
    newGrid, change2 = merge(newGrid)
    changed = change1 or change2
    newGrid, temp = compression(newGrid)
    newGrid = transposeMatrix(newGrid)
    return newGrid, changed

def downMove(grid):
    newGrid = transposeMatrix(grid)
    newGrid = reverse(newGrid)
    newGrid, change1 = compression(newGrid)
    newGrid, change2 = merge(newGrid)
    changed = change1 or change2
    newGrid, temp = compression(newGrid)
    newGrid = reverse(newGrid)
    newGrid = transposeMatrix(newGrid)
    return newGrid, changed
