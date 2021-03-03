class AdjList:
    def __init__(self, cities):
        self.adj = [[] for i in range(len(cities))]
        self.v = len(cities)
        self.initialize()

    def addEdge(self, source, target):
        self.adj[source].append(target)
        self.adj[target].append(source)

    def initialize(self):
        self.addEdge(0, 1)
        self.addEdge(0, 2)
        self.addEdge(0, 3)
        self.addEdge(0, 5)
        self.addEdge(0, 7)
        self.addEdge(0, 8)
        self.addEdge(1, 2)
        self.addEdge(1, 3)
        self.addEdge(1, 4)
        self.addEdge(2, 3)
        self.addEdge(3, 4)
        self.addEdge(4, 5)
        self.addEdge(4, 6)
        self.addEdge(4, 7)
        self.addEdge(4, 8)
        self.addEdge(4, 10)
        self.addEdge(6, 10)
        self.addEdge(7, 8)
        self.addEdge(7, 9)
