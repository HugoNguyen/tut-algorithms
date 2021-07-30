# Dijkstra algorithm

import sys;
import heapq;

class Node(object):

    def __init__(self, name: str) -> None:
        self.name = name;
        self.visited = False;
        self.predecessor: Node = None;
        self.adjacenciesList: list[Edge] = [];
        self.minDistance = sys.maxsize; # set init min is infinity

    def __cmp__(self, otherVertex):
        return self.__cmp__(self.minDistance, otherVertex.minDistance);

    def __lt__(self, otherVertex):
        selfPriority = self.minDistance;
        otherPriority = otherVertex.minDistance;
        return selfPriority < otherPriority;

class Edge(object):

    def __init__(self, weight: int, startVertex: Node, targetVertex: Node) -> None:
        self.weight = weight;
        self.startVertex = startVertex;
        self.targetVertex= targetVertex;

class Dijkstra(object):

    def calculateShortestPath(self, startVertex: Node):
        
        q: list[Node] = [];
        startVertex.minDistance = 0;
        heapq.heappush(q, startVertex);

        while q: # means while q not empty, or len(q) > 0
            actualVertex = heapq.heappop(q); # pop Node with minum distince

            for edge in actualVertex.adjacenciesList:
                u = edge.startVertex;
                v = edge.targetVertex;
                newDistance = u.minDistance + edge.weight;

                if newDistance < v.minDistance:
                    v.predecessor = u;
                    v.minDistance = newDistance;
                    heapq.heappush(q, v);

    def getShortestPathTo(self, targetVertex: Node):
        print("Shortest path to vertex is: ", targetVertex.minDistance);
        node = targetVertex;

        while node is not None:
            print("%s " % node.name);
            node = node.predecessor;

if __name__ == "__main__":
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

    nodeA.adjacenciesList.append(edgeAB);
    nodeA.adjacenciesList.append(edgeAH);
    nodeA.adjacenciesList.append(edgeAE);
    nodeB.adjacenciesList.append(edgeBD);
    nodeB.adjacenciesList.append(edgeBC);
    nodeB.adjacenciesList.append(edgeBH);
    nodeH.adjacenciesList.append(edgeHC);
    nodeH.adjacenciesList.append(edgeHF);
    nodeE.adjacenciesList.append(edgeEH);
    nodeE.adjacenciesList.append(edgeEF);
    nodeE.adjacenciesList.append(edgeEG);
    nodeF.adjacenciesList.append(edgeFC);
    nodeF.adjacenciesList.append(edgeFG);
    nodeC.adjacenciesList.append(edgeCD);
    nodeC.adjacenciesList.append(edgeCG);
    nodeD.adjacenciesList.append(edgeDG);

    # vertexList = (nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH);

    algorithm = Dijkstra();
    algorithm.calculateShortestPath(nodeA);
    algorithm.getShortestPathTo(nodeG);