import Node from Node

def backtracking(s, k):
    OPEN = []
    OPEN.append(s)

    if not OPEN:
        return False

    while OPEN:
        n = OPEN[-1]

        if n.expanded() or n.getDepth() > k:
            OPEN.pop()
        else:
            successor = n.nextSuccessor()

    exit()
    return Node()

"""
Main programm
"""

# Starting Node
"""
8 3 6 7
6 5 9 8
5 3 7 8
1 2 4 6
"""
starting_config = [
    [8, 6, 5, 1],
    [3, 5, 3, 2],
    [6, 9, 7, 4],
    [7, 8, 8, 6]
]

s = Node(0, starting_config)

solution_node = backtracking(s, 4)

if solution_node:
    print(solution_node.getBackpointer())