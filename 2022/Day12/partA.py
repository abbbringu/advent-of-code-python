"""
We will use a path finding algorithm, the one I'm implementing
is the dijkstra algorithm. 
"""
from collections import defaultdict, deque
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
        
def findVertex(matrix, pos, visited, cost):
    toVisit = []
    xBound, yBound = len(matrix[0]), len(matrix)
    x, y = pos[0], pos[1]
    ogX, ogY = x,y
    #print("we are in ", matrix[y][x])
    for xChange, yChange in [(-1,0),(0,1),(1,0),(0,-1)]:
        x = ogX + xChange
        y = ogY + yChange
        if ( 0<= x < xBound) and (0<=y<yBound):
                
            #if (x,y) in visited:
            #    continue
            vertex = matrix[y][x]
            origin = matrix[ogY][ogX]
            if vertex == 'E' and origin != 'z':
                continue
            if origin == 'S':
                origin = 'a'
            if (ord(vertex) <= ord(origin)) + 1:
                toVisit.append(((x,y), cost + 1))
    return toVisit

def dijkstra(matrix, startPos):
    visited = []
    toVisit = deque()
    toVisit += [(startPos, 0)]
    while toVisit:
        (x,y),d = toVisit.popleft()
        if (x,y) in visited:
            continue
        visited.append((x,y))
        if matrix[y][x] == 'E'  :
            print(x, y)
            return f"Found the end in {d} steps"

        toVisit += findVertex(matrix, (x,y), visited, d)
    print("Did not find the end",d)
    return "could not find a path"


def main():
    with open('./Day12/input.txt') as f:
        # Every row into array
        lines = f.readlines()
        # Part A
        matrix = createMatrix(lines)
        start = findStart(matrix)
        print(dijkstra(matrix, start))
        # Part B
        #print(drawing(lines))

main()