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
        bestnode = _min(OPEN)
        n = bestnode[0]
        del OPEN[bestnode[1]]

        CLOSED.append(n)

        for successor in n.successors():
            if successor.getBoardConfiguration() == goal_node:
                return successor

            successor.f(goal_node)
            OPEN.append(successor)

    return False

"""
Get most promising solution base from OPEN
"""
def _min(OPEN):
    bestnode = []
    val = 9999999999

    for index, node in enumerate(OPEN):
        if node.getFval() < val:
            bestnode = [[node, index]]
            val = node.getFval()
            arr = False
        elif node.getFval() == val:
            bestnode.append([node, index])
            arr = True

        if arr:
            besth1 = 9999999999
            _bestnode = []

            for node in bestnode:
                if node[0].h1 <= besth1:
                    _bestnode = [node]
                    besth1 = node[0].h1

            bestnode = _bestnode

    return bestnode[0]

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

s = Node(starting_board_configuration, [1, 1], 0)

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