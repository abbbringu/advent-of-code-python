"""
We will use a path finding algorithm, the one I'm implementing
is the dijkstra algorithm. 
"""
def createMatrix(lines):
    matrix = []
    for row in lines:
        matrix.append(row.strip('\n'))
    return matrix


def findStart(matrix):
    y = 0
    for row in matrix:
        if 'S' in row:
            print(row.index('S'),y)
            return (row.index('S'), y)
        y += 1
        
def findVertex(matrix, pos, visited):
    toVisit = []
    xBound, yBound = len(matrix[0]), len(matrix)
    x, y = pos[0], pos[1]
    ogX, ogY = x,y
    xChange = [1, -1, 0, 0]
    yChange = [0, 0, 1, -1]
    for i in range(4):
        x +=  xChange[i]
        y +=  yChange[i]
        if x < 0 or y < 0 or x >= xBound or y >= yBound:
            continue
        elif (x,y) in visited:
            continue

        vertex = matrix[y][x]
        origin = matrix[ogY][ogX]
        if vertex == 'E' and origin != 'z':
            continue

        if vertex == 'S':
            vertex = 'a'
        
        if (ord(vertex) - ord(origin)) <= 1:
            toVisit.append((x,y))
    return toVisit
        


def dijkstra(matrix, startPos):
    print("not defined")
    










def main():
    with open('./Day12/test.txt') as f:
        # Every row into array
        lines = f.readlines()
        # Part A
        matrix = createMatrix(lines)
        start = findStart(matrix)
        # Part B
        #print(drawing(lines))

main()