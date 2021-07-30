# Bellnam-Ford algorithm, find shortest path + detect circle

import sys;

class Node(object):

    def __init__(self, name: str) -> None:
        self.name = name;
        self.visited = False;
        self.predecessor: Node = None;
        self.adjacenciesList: list[Edge] = [];
        self.minDistance = sys.maxsize; # set init min is infinity

class Edge(object):

    def __init__(self, weight: int, startVertex: Node, targetVertex: Node) -> None:
        self.weight = weight;
        self.startVertex = startVertex;
        self.targetVertex= targetVertex;

class BellmanFord(object):
    HAS_CYCLE = False;

    def calculateShortestPath(self, vertexList: list[Node], edgeList: list[Edge], startVertex: Node):
        startVertex.minDistance = 0;

        for i in range(0, len(vertexList)-1):
            for edge in edgeList:
                u = edge.startVertex;
                v = edge.targetVertex;

                newDistance = u.minDistance + edge.weight;

                if newDistance < v.minDistance:
                    v.minDistance = newDistance;
                    v.predecessor = u;
        
        for edge in edgeList:
            if self.hasCycle(edge):
                BellmanFord.HAS_CYCLE = True; # Negative cycle detected
                return;

    def hasCycle(self, edge: Edge):
        if (edge.startVertex.minDistance + edge.weight) < edge.targetVertex.minDistance:
            return True;
        else:
            return False;

    def getShortestPathTo(self, targetVertex: Node):
        if not BellmanFord.HAS_CYCLE:
            print("Shorted path exists with value: ", targetVertex.minDistance);

            node = targetVertex;

            while node is not None:
                print("%s " % node.name);
                node = node.predecessor;
        else:
            print("Negative cycle detected...");

def test_has_no_cycle():
    nodeA = Node("A");
    nodeB = Node("B");
    nodeC = Node("C");
    nodeD = Node("D");
    nodeE = Node("E");
    nodeF = Node("F");
    nodeG = Node("G");
    nodeH = Node("H");

    edgeAB = Edge(5, nodeA, nodeB);
    edgeAH = Edge(8,nodeA,nodeH);
    edgeAE = Edge(9,nodeA,nodeE);
    edgeBD = Edge(15,nodeB,nodeD);
    edgeBC = Edge(12,nodeB,nodeC);
    edgeBH = Edge(4,nodeB,nodeH);
    edgeHC = Edge(7,nodeH,nodeC);
    edgeHF = Edge(6,nodeH,nodeF);
    edgeEH = Edge(5,nodeE,nodeH);
    edgeEF = Edge(4,nodeE,nodeF);
    edgeEG = Edge(20,nodeE,nodeG);
    edgeFC = Edge(1,nodeF,nodeC);
    edgeFG = Edge(13,nodeF,nodeG);
    edgeCD = Edge(3,nodeC,nodeD);
    edgeCG = Edge(11,nodeC,nodeG);
    edgeDG = Edge(9,nodeD,nodeG);

    vertexList = (nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH);
    edgeList = (edgeAB,edgeAH,edgeAE,edgeBD,edgeBC,edgeBH,edgeHC,edgeHF,edgeEH,edgeEF,edgeEG,edgeFC,edgeFG,edgeCD,edgeCG,edgeDG);

    algorithm = BellmanFord();
    algorithm.calculateShortestPath(vertexList, edgeList, nodeA);
    algorithm.getShortestPathTo(nodeG);

def test_has_cycle():
    nodeA = Node("A");
    nodeB = Node("B");
    nodeC = Node("C");
    nodeD = Node("D");
    edgeAB = Edge(1,nodeA,nodeB);
    edgeBC = Edge(1,nodeB,nodeC);
    edgeCA = Edge(-3,nodeC,nodeA);
    edgeBD = Edge(3,nodeB,nodeD);
    edgeCD = Edge(1,nodeC,nodeD);

    vertexList = (nodeA, nodeB, nodeC, nodeD);
    edgeList = (edgeAB, edgeBC, edgeCA, edgeBD, edgeCD);

    algorithm = BellmanFord();
    algorithm.calculateShortestPath(vertexList, edgeList, nodeA);
    algorithm.getShortestPathTo(nodeD);

if __name__ == "__main__":
    # test_has_no_cycle();
    test_has_cycle();