"""
Node class with basic functions and data structure
"""
class Node:
    backpointer = ""
    depth = -1
    boardConfiguration = 0

    def __init__(self, depth, boardConfiguration):
        self.setDepth(depth)
        self.setBoardConfiguration(boardConfiguration)

    def nextSuccessors(self):
        return ""

    def expanded(self):
        if not self.boardConfiguration:
            return True
        else:
            return False

    """
    Getter and Setter Methods
    """
    def setBackpointer(self, backpointer):
        self.backpointer = backpointer

    def getBackpointer(self):
        return self.backpointer

    def setDepth(self, depth):
        self.depth = depth

    def getDepth(self):
        return self.depth

    def setBoardConfiguration(self, boardConfiguration):
        self.boardConfiguration = boardConfiguration