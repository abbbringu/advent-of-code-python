
"""
Idea:
Save positions of head and tail in a tupel
* Move head to designated direction
* See relation of head and tail to see what
  to do next
* Put the new tail position in the visited list
* Continue untill out of orders
"""
# ------------------- Part A -------------------
def visited(lines):
    visited = [[0,0]]
    # Positions:
    # Following x, y
    head = [0,0]
    tail = [0,0]

    for order in lines:
        order = order.split(" ")
        order[1] = int(order[1])

        # Check whhich direction to move head
        while order[1] > 0:
            if order[0] == "R":
                head[0] += 1
            elif order[0] == "L":
                head[0] -= 1
            elif order[0] == "U":
                head[1] += 1
            elif order[0] == "D":
                head[1] -= 1
            order[1] -= 1
            # Update tail position based on head
            tail = updateTail(head, tail)
            # Check if it's a new position and append
            # if new
            inList = False
            for i in visited:
                if i[0] == tail[0] and i[1] == tail[1]:
                    inList = True
                    break
            if not inList:
                visited.append([tail[0], tail[1]])

    result = len(visited)
    return result


# ------------------- Part B -------------------
def visitedTen(lines):
    visited = [[0,0]]
    # Positions:
    # Following x, y
    rope = [[0,0] for _ in range(10)]

    for order in lines:
        order = order.split(" ")
        order[1] = int(order[1])

        # Check whhich direction to move head
        while order[1] > 0:
            if order[0] == "R":
                rope[0][0] += 1
            elif order[0] == "L":
                rope[0][0] -= 1
            elif order[0] == "U":
                rope[0][1] += 1
            elif order[0] == "D":
                rope[0][1] -= 1
            order[1] -= 1
            # Update rope positinos based on head
            for i in range(10):
                if i == 0: continue
                rope[i] = updateTail(rope[i-1], rope[i])

            # Check if it's a new position and append
            # if new
            inList = False
            for i in visited:
                if i[0] == rope[-1][0] and i[1] == rope[-1][1]:
                    inList = True
                    break
            if not inList:
                visited.append([rope[-1][0], rope[-1][1]])

    result = len(visited)
    return result
# function for calculating new tail position 
def updateTail(head, tail):
    # there are some cases
    # Either directly to the horizontly, or vertically. 
    # Or 2 steps and 1 step in either axis. 
    x = head[0] - tail[0]
    y = head[1] - tail[1]

    if abs(x) + abs(y) >= 3:  # Sign of diaganol
        # Add one to both x and y in the respective direction
        if abs(x) == 1:
            tail[0] += x
        else:                       # If abs(x) == 2
            if x < 0:
                tail[0] += x + 1
            else:
                tail[0] += x - 1
                
        if abs(y) == 1:
            tail[1] += y
        else:
            if y < 0:
                tail[1] += y + 1
            else:
                tail[1] += y - 1
        return tail 
        
    if abs(x) > 1:
        if x < 0:
            tail[0] += x + 1
        else:
            tail[0] += x - 1
    elif abs(y) > 1:
        if y < 0:
                tail[1] += y + 1
        else:
            tail[1] += y - 1
    return tail





def main():
    with open('./Day9/input.txt') as f:
        # Every row into array
        lines = f.readlines()
        # Part A
        print(visited(lines))
        # Part B
        print(visitedTen(lines))


main()