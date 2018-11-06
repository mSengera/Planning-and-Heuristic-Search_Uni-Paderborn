# Import Node class
from Node import Node

"""
Get a solution path from an starting board configuration s, to a goal node.
"""
def BF(s, goal_node):
    OPEN = []
    CLOSED = []

    # Append S (Starting Node) top OPEN
    OPEN.append(s)

    if not OPEN:
        return False

    while OPEN:
        n = _min(OPEN)

        CLOSED.append(n)

        for successor in n.successors():
            if successor.getBoardConfiguration() == goal_node:
                return successor

            OPEN.append(successor)

    return False

"""
Get most promising solution base from OPEN
"""
def _min(OPEN):
    bestnode = ""
    val = 9999999999

    for node in OPEN:
        if node.getFval() < val:
            bestnode = node
            val = node.getFval()

    return bestnode

"""
Main Programm
"""

# Startng Point "s"
starting_board_configuration = \
        [
            [1, 2, 3],
            [7, 0, 4],
            [6, 8, 5]
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


solution_node = BF(s, g)

# Further computation from solution_path. With backpointer, reconstruct the solution path
print(solution_node.getBackpointer())