import heapq

# Defining the class Node, which we will use within the heap queue
# Each node will contain the position, cost, parent node, and heuristic value
class Node:
    def __init__(self, position, cost, parent, heuristic):
        self.position = position
        self.cost = cost
        self.parent = parent
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic

def heuristic_a(point, end):
    # This heuristic uses the Manhattan distance
    return abs(end[0] - point[0]) + abs(end[1] - point[1])

def heuristic_b(point, end):
    # This heuristic uses the Euclidean distance
    import math
    return math.sqrt((end[0] - point[0])**2 + (end[1] - point[1])**2)

# Implement greedy best-first search inside the 'greedy' function

def greedy(maze, start, finish, heuristic):

    # Create empty heap queue and visited list
    heap_queue = []
    heapq.heappush(heap_queue, Node(start, 0, None, heuristic(start, finish)))
    visited = []

    while heap_queue:
        current_node = heapq.heappop(heap_queue)

        if current_node.position in visited:
            continue

        visited.append(current_node.position)

        if current_node.position == finish:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return len(path), visited

        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for neighbor in neighbors:
                next_pos = (current_node.position[0] + neighbor[0], current_node.position[1] + neighbor[1])

                if (next_pos[0] >= 0 and next_pos[0] < len(maze)) and (next_pos[1] >= 0 and next_pos[1] < len(maze[0])) and maze[next_pos[0]][next_pos[1]] == 0:
                    heapq.heappush(heap_queue, Node(next_pos, current_node.cost + 1, current_node, heuristic(next_pos, finish)))

    return -1, visited

# Implement the 'visualize' function which displays the solution process

def visualize(viz):
    # Print a step-by-step visualization to the console
    for i in range(len(viz)):
        for j in range(len(viz[i])):
            if (i, j) in viz:
                print(f' {i, j}: Visited')
            else:
                print(' . ', end='')
        print()

maze_samples = {
    'sample1': {
        'maze': [[0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0],
                 [0, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0]],
        'start': (0, 0),
        'end': (5, 4)
    },
    'sample2': {
        'maze': [[0, 0, 0, 1, 0],
                 [1, 1, 0, 1, 0],
                 [0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0]],
        'start': (0, 0),
        'end': (4, 4)
    }
}

heuristics = [heuristic_a, heuristic_b]

for sample, values in maze_samples.items():
    print(f'Running {sample}\n--------------------')
    for heur in heuristics:
        print(f'Greedy result for {heur.__name__}:')
        result, visited = greedy(values['maze'], values['start'], values['end'], heur)
        print(f'Path count: {result}')
        print(f'Visited points:')
        visualize(visited)
        print('\n')
