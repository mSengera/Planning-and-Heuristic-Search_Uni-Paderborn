# Import Node class
from Node import Node

"""
Get a solution path from an starting board configuration s, to a goal node.
"""
def DFS(s, goal_node, k):
    OPEN = []
    CLOSED = []

    # Append S (Starting Node) top OPEN
    OPEN.append(s)

    if not OPEN:
        return False

    while OPEN:
        n = OPEN.pop()

        CLOSED.append(n)

        for successor in n.successors():
            if successor.getBoardConfiguration() == goal_node:
                return successor

            if n.getDepth() <= k:
                OPEN.append(successor)

    return False

"""
Main Programm
"""

# Startng Point "s"
starting_board_configuration = \
        [
            [1, 2, 3],
            [0, 8, 4],
            [7, 6, 5]
        ]

s = Node(starting_board_configuration, [1, 0], 0)

# target board configuration
target_board_configuration = \
        [
            [1, 2, 3],
            [8, 0, 4],
            [7, 6, 5]
        ]

g = target_board_configuration


solution_node = DFS(s, g, 5)

# Further computation from solution_path. With backpointer, reconstruct the solution path
print(solution_node.getBackpointer())