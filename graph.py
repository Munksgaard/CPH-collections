##
## Authors: Kim Lundsteen Juncher and Brian Soborg Mathiasen
## Insitute of Computer Science, Copenhagen University, Denmark
##
## Date: 28-05-2010
##
## graph.py
##
## LICENSED UNDER: GNU General Public License v2
##

import random as r

class Graph(object):
    """Very dynamic graph data structure, implementing basic graph functionality
    as well as methods for visualisations."""
    def __init__ (self):
        """ Constructor. """
        self.vertices = {}
        self.edges = {}
        self._edgeidcount = 0
#        self.__subconstruct__(visual)

    def addVertex(self, vertex_id):
        """ Adds a vertex with id vertex_id to the graph """
        self.vertices[vertex_id] = self.Vertex(vertex_id)

    def removeVertex(self, vertex_id):
        """ removes a vertex with id vertex_id from the graph """
        if self.vertexExists(vertex_id):
            self.removeEdges(self.getAdjEdges(vertex_id))
            del self.vertices[vertex_id]

    def addEdge(self, (vertex_id_1, vertex_id_2), weight=0): 
        """ Adds an edge with id (vertex_id_1,vertex_id_2) to the graph """
        if not self.vertexExists(vertex_id_1): self.addVertex(vertex_id_1)
        if not self.vertexExists(vertex_id_2): self.addVertex(vertex_id_2)
        edge_id = self._edgeidcount
        self._edgeidcount += 1
        self.edges[(vertex_id_1, vertex_id_2)] = self.Edge(edge_id, (vertex_id_1,
                                                         vertex_id_2), weight)

    def removeEdge(self, (vertex_id_1, vertex_id_2)):
        """ Removes an edge with id (vertex_id_1, vertex_id_2) from the graph """
        if self.edgeExists((vertex_id_1, vertex_id_2)):
            del self.edges[(vertex_id_1, vertex_id_2)]

    def vertexExists(self, vertex_id):
        """ Checks if vertex with vertex_id exists in the graph """
        return vertex_id in self.vertices

    def edgeExists(self, (vertex_id_1, vertex_id_2)):
        """ Checks if edge with (vertex_id_1,vertex_id_2) exists in the graph """
        return (vertex_id_1, vertex_id_2) in self.edges

    def removeEdges(self, edge_list):
        """ Removes a list of edges from the graph """
        for edge in edge_list:
            self.removeEdge(edge)

    def getVertices(self):
        """ Function to return the list of vertex objects """
        return [self.getVertex(vertex) for vertex in self.vertices]
    
    def getEdges(self): 
        """ Function to return the list of edge objects """
        return [self.getEdge(edge) for edge in self.edges]

#    def degreeList(self): 
#        return
    
    def getAdjEdges(self, vertex_id):
        """ returns a list of sets denoting edges adjacent to the vertex with
        id vertex_id """
        return [(edge.start_vertex, edge.end_vertex) for edge in self.getEdges() if edge.start_vertex == vertex_id or edge.end_vertex == vertex_id]

    def getAdjVertices(self, vertex_id):
        """ returns a list of ids denoting vertices adjacent to the vertex with
        id vertex_id """
        # this function needs rewriting
        buf = []
        for edge in self.getAdjEdges(self, vertex_id):
            if edge.start_vertex == vertex_id:
                buf.append(edge.end_vertex)
            elif edge.end_vertex == vertex_id:
                buf.append(edge.start_vertex)
        return buf
    
    def getVertex(self, vertex_id): 
        """ returns the vertex object with id vertex_id  """
        if self.vertexExists(vertex_id):
            return self.vertices[vertex_id]
            
    def getEdge(self, (vert_id_1, vert_id_2)):
        """ returns the edge object with id (vertex_id_1, vertex_id_2)  """
        if self.edgeExists((vert_id_1, vert_id_2)):
            return self.edges[(vert_id_1, vert_id_2)]

    def clear(self): 
        """ Clears and empties the graph """
        self.vertices = {}
        self.edges = {}
        self._edgeidcount = 0
        
    def generateRandomGraph(self, numberofvertices=0, numberofedges=0):
        """ Generates and occupies the structure with random number of vertices
        and edges. Will by default construct an MST graph."""
        if numberofvertices == 0:
            numberofvertices = r.randint(5,10)
        self.clear()
        vertexId = 0
        self.addVertex(vertexId)
        for i in range(1,numberofvertices):
            neighbor = r.randint(0,len(self.getVertices())-1)
            vertexId += 1
            self.addVertex(i)
            self.addEdge((i, neighbor))
        if numberofedges:
            for i in range(0,numberofedges):
                added = False
                while not added:
                    neighbour1 = r.randint(0,len(self.getVertices())-1)
                    neighbour2 = r.randint(0,len(self.getVertices())-1)
                    if not self.edgeExists((neighbour1, neighbour2)):
                        self.addEdge((neighbour1, neighbour2))
                        added = True

    class Vertex:
        """ Object used by the parent Graph class for storing vertex information
        """
        def __init__(self, vertex_id, label=None):
            self._id = vertex_id
            self.label = label
            
        def getId(self):
            return self._id
            
        def getLabel(self):
            if not self.label:
                return self.getId()
            return self.label
        
    class Edge:
        """ Object used by the parent Graph class for storing edge information
        """
        def __init__(self, edge_id, (start_vertex_id, end_vertex_id), weight):
            self._id = edge_id
            self.weight = weight
            self.start_vertex = start_vertex_id
            self.end_vertex = end_vertex_id
                
        def getId(self):
            return self._id
        def getWeight(self):
            return self.weight
        
        
