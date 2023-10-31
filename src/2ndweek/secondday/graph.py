class Graph(object):
    def __init__(self) -> None:
        self.graph={}
    
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    
    def add_edge(self,vertex1,vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)
    
    def get_vertices(self):
        return list(self.graph.keys())
    
    def getEdges(self):
        edges=[]
        for vertex in self.graph:
            for neighbours in self.graph[vertex]:
                edges.append((vertex,neighbours))
        return edges

g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_edge("A","B")
g.add_edge("B", "C")
g.add_edge("A","C")
print(g.get_vertices())
print(g.getEdges())