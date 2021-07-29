# Depth-first search

class Node(object):

    def __init__(self, name) -> None:
        self.name = name;
        self.adjacencyList = [];
        self.visited = False;
        self.predecessor = None;

class DepthFirstSearch(object):

    def dfs(self, node: Node):
        node.visited = True;
        print("%s" % node.name);

        for n in node.adjacencyList:
            if not n.visited:
                self.dfs(n);

nodeA = Node("A");
nodeB = Node("B");
nodeC = Node("C");
nodeD = Node("D");
nodeE = Node("E");

nodeA.adjacencyList.append(nodeB);
nodeB.adjacencyList.append(nodeC);
nodeB.adjacencyList.append(nodeD);
nodeD.adjacencyList.append(nodeE);

dfs = DepthFirstSearch();
dfs.dfs(nodeA);