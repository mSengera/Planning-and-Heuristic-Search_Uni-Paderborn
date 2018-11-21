import sys

# Import Node class
from Node import Node

"""
Get most promising solution base from OPEN
"""
def _min(OPEN):
    bestnode = []
    val = sys.maxsize
    arr = False

    for index, node in enumerate(OPEN):
        if node.getFval() < val:
            bestnode = [[node, index]]
            val = node.getFval()
            arr = False
        elif node.getFval() == val:
            bestnode.append([node, index])
            arr = True

        # Check if more than one best solution base is available
        if arr:
            besth1 = sys.maxsize
            _bestnode = []

            for node in bestnode:
                if node[0].h1 <= besth1:
                    _bestnode = [node]
                    besth1 = node[0].h1

            bestnode = _bestnode

    return bestnode[0]


"""
Get a solution path from an starting board configuration s, to a goal node.
"""
def aStar(s, goal_node):
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

        if n.getBoardConfiguration() == goal_node:
            return n

        CLOSED.append(n)

        for successor in n.successors():
            successor.f(goal_node)  # TODO: Store g, h and f value as variables in Node
            OPEN.append(successor)

            # TODO: Add path discarding

    return False


"""
Main Program
"""

# Starting Point "s"
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


solution_node = aStar(s, g)

# Further computation from solution_path. With backpointer, reconstruct the solution path
print(solution_node.getBackpointer())
