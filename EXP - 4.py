import heapq

class Node:
    def __init__(self, row, col, cost=0, heuristic=0, parent=None):
        self.row = row
        self.col = col
        self.cost = cost  
        self.heuristic = heuristic  
        self.parent = parent

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def a_star_search(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])

    open_set = [start_node] 
    closed_set = set()

    came_from = {}  

    g_score = {start: 0}

    f_score = {start: heuristic(start, goal)}

    while open_set:
        current_node = heapq.heappop(open_set)

        if (current_node.row, current_node.col) == goal:
            return reconstruct_path(came_from, goal)

        closed_set.add((current_node.row, current_node.col))

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]: 
            neighbor_row, neighbor_col = current_node.row + dr, current_node.col + dc

            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols and grid[neighbor_row][neighbor_col] != 1: 
                neighbor = (neighbor_row, neighbor_col)
                tentative_g_score = g_score[(current_node.row, current_node.col)] + 1 

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = (current_node.row, current_node.col)
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, Node(neighbor_row, neighbor_col, tentative_g_score, heuristic(neighbor, goal)))

    return None  

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def reconstruct_path(came_from, goal):
    current = goal
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

start_point = (0, 0)
goal_point = (9, 9)

path = a_star_search(grid, start_point, goal_point)

if path:
    print("Path found:")
    for row, col in path:
        print(f"({row}, {col})")
else:
    print("No path found.")

if path:
    path_set = set(path)
    for r in range(len(grid)):
        row_str = ""
        for c in range(len(grid[0])):
            if (r, c) == start_point:
                row_str += "S "
            elif (r, c) == goal_point:
                row_str += "G "
            elif (r, c) in path_set:
                row_str += "* "
            elif grid[r][c] == 1:
                row_str += "# "
            else:
                row_str += ". "
        print(row_str)
