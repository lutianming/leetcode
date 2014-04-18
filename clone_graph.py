# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        queue = []
        nodeMap = {}
        queue.append(node)

        startNode = None
        while len(queue) > 0:
            node = queue.pop()
            if node not in nodeMap:
                newNode = UndirectedGraphNode(node.label)
                nodeMap[node] = newNode
            else:
                newNode = nodeMap[node]

            if not startNode:
                startNode = newNode

            if len(node.neighbors) == len(newNode.neighbors):
                continue

            for neighbor in node.neighbors:
                if neighbor in nodeMap:
                    newNeighbor = nodeMap[neighbor]
                else:
                    newNeighbor = UndirectedGraphNode(neighbor.label)
                    nodeMap[neighbor] = newNeighbor

                newNode.neighbors.append(newNeighbor)
                queue.append(neighbor)

        return startNode
