# Breadth first search

class Node(object):
    def __init__(self, name) -> None:
        self.name = name; # name of every single Node, likes, A, B, C, etc
        self.adjacencyList = [];
        self.visited = False;
        self.predecessor = None;

class BreadthFirstSearch(object):
    
    def bfs(self, startNode: Node):
        queue = [];
        queue.append(startNode);
        startNode.visited = True;

        # bfs->queue    dfs-> stack but ususaly we implemnt it with recursion !!!
        while queue:
            actualNode: Node = queue.pop(0);
            print("%s " % actualNode.name);

            for n in actualNode.adjacencyList:
                if not n.visited:
                    n.visited = True;
                    queue.append(n);

# matrix = [
#     ['a', 'b', 'c', 'd', 'e'],
#     [0, 1, 1, 0, 0],
#     [1, 0, 0, 1, 0],
#     [1, 0, 0, 0, 0],
#     [0, 1, 0, 0, 1],
#     [0, 0, 0, 1, 0],
# ]

nodeA = Node("A");
nodeB = Node("B");
nodeC = Node("C");
nodeD = Node("D");
nodeE = Node("E");

nodeA.adjacencyList.append(nodeB);
nodeB.adjacencyList.append(nodeC);
nodeB.adjacencyList.append(nodeD);
nodeD.adjacencyList.append(nodeE);

bfs = BreadthFirstSearch();
bfs.bfs(nodeA);
