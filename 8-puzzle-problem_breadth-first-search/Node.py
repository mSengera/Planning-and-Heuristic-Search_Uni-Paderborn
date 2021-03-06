import copy

"""
Node class with basic functions and data structure
"""
class Node:
    boardConfiguration = []
    nullPosition = []
    backpointer = ""
    depth = -1

    def __init__(self, boardConfiguration, nullPointer, depth):
        self.setBoardConfiguration(boardConfiguration)
        self.setNullPosition(nullPointer)
        self.setDepth(depth)

    def successors(self):
        successors = []

        node = self.getBoardConfiguration()
        zero_point = self.getNullPosition()
        depth = self.getDepth() + 1

        # Up
        successor_node = copy.deepcopy(node)
        changed_zero_y = zero_point[0] - 1

        if 0 <= changed_zero_y <= 2:
            successor_node[zero_point[0]][zero_point[1]] = node[changed_zero_y][zero_point[1]]
            successor_node[changed_zero_y][zero_point[1]] = 0

            new_node = Node(successor_node, [changed_zero_y, zero_point[1]], depth)
            new_node.setBackpointer(self)

            successors.append(new_node)

        # Down
        successor_node = copy.deepcopy(node)
        changed_zero_y = zero_point[0] + 1

        if 0 <= changed_zero_y <= 2:
            successor_node[zero_point[0]][zero_point[1]] = node[changed_zero_y][zero_point[1]]
            successor_node[changed_zero_y][zero_point[1]] = 0

            new_node = Node(successor_node, [changed_zero_y, zero_point[1]], depth)
            new_node.setBackpointer(self)

            successors.append(new_node)

        # Left
        successor_node = copy.deepcopy(node)
        changed_zero_x = zero_point[1] - 1

        if 0 <= changed_zero_x <= 2:
            successor_node[zero_point[0]][zero_point[1]] = node[zero_point[0]][changed_zero_x]
            successor_node[zero_point[0]][changed_zero_x] = 0

            new_node = Node(successor_node, [zero_point[0], changed_zero_x], depth)
            new_node.setBackpointer(self)

            successors.append(new_node)

        # Right
        successor_node = copy.deepcopy(node)
        changed_zero_x = zero_point[1] + 1

        if 0 <= changed_zero_x <= 2:
            successor_node[zero_point[0]][zero_point[1]] = node[zero_point[0]][changed_zero_x]
            successor_node[zero_point[0]][changed_zero_x] = 0

            new_node = Node(successor_node, [zero_point[0], changed_zero_x], depth)
            new_node.setBackpointer(self)

            successors.append(new_node)

        return successors

    """
    Getter and Setter Methods
    """
    def setBoardConfiguration(self, boardConfiguration):
        self.boardConfiguration = boardConfiguration

    def getBoardConfiguration(self):
        return self.boardConfiguration

    def setNullPosition(self, nullPosition):
        self.nullPosition = nullPosition

    def getNullPosition(self):
        return self.nullPosition

    def setBackpointer(self, backpointer):
        self.backpointer = backpointer

    def getBackpointer(self):
        return self.backpointer

    def setDepth(self, depth):
        self.depth = depth

    def getDepth(self):
        return self.depth